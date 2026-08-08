"""aiohttp webhook server for GitOps, health and metrics endpoints.

Extracted from main.py so the webhook surface can be tested and
extended without importing the Discord bot entry point.
"""

import dataclasses
import hashlib
import hmac
import logging
import os
import sys
import uuid
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Optional

import psutil
from aiohttp import web
from discord.ext import commands

from rbac import Organization, Permission, RBACEngine, Role

logger = logging.getLogger(__name__)

# The federation API token holder acts as platform administrator for the
# RBAC management API. Tenant users are represented by memberships inside
# the engine and never authenticate over the wire.
rbac_engine = RBACEngine()


def _serialize_rbac(obj: Any) -> Any:
    """Serialize RBAC dataclasses and enums into JSON-safe primitives."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, (set, frozenset)):
        return sorted(_serialize_rbac(v) for v in obj)
    if isinstance(obj, dict):
        return {k: _serialize_rbac(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serialize_rbac(v) for v in obj]
    if isinstance(obj, Enum):
        return obj.value
    if dataclasses.is_dataclass(obj):
        return {k: _serialize_rbac(v) for k, v in dataclasses.asdict(obj).items()}
    return obj


async def rbac_roles_list(request: web.Request) -> web.Response:
    """List all roles with their permissions."""
    return web.json_response(
        {"roles": [_serialize_rbac(r) for r in rbac_engine.list_roles()]}
    )


async def rbac_role_create(request: web.Request) -> web.Response:
    """Create a custom role from {name, permissions, description?}."""
    try:
        body = await request.json()
    except Exception:
        return web.json_response({"error": "invalid JSON body"}, status=400)
    name = body.get("name")
    permission_names = body.get("permissions")
    if not isinstance(name, str) or not name or not isinstance(permission_names, list):
        return web.json_response(
            {"error": "name and permissions list are required"}, status=400
        )
    try:
        permissions = {Permission(p) for p in permission_names}
    except ValueError:
        valid = ", ".join(sorted(p.value for p in Permission))
        return web.json_response(
            {"error": "unknown permission; valid values: " + valid}, status=400
        )
    role = Role(
        name=name, permissions=permissions, description=str(body.get("description", ""))
    )
    return web.json_response(_serialize_rbac(rbac_engine.create_role(role)), status=201)


async def rbac_org_create(request: web.Request) -> web.Response:
    """Create an organization and auto-assign the owner role."""
    try:
        body = await request.json()
    except Exception:
        return web.json_response({"error": "invalid JSON body"}, status=400)
    name = body.get("name")
    owner_user_id = body.get("owner_user_id")
    if (
        not isinstance(name, str)
        or not name
        or not isinstance(owner_user_id, str)
        or not owner_user_id
    ):
        return web.json_response(
            {"error": "name and owner_user_id are required"}, status=400
        )
    org = Organization(
        id=str(body.get("id") or f"org-{uuid.uuid4().hex[:12]}"),
        name=name,
        owner_user_id=owner_user_id,
    )
    return web.json_response(_serialize_rbac(rbac_engine.create_org(org)), status=201)


async def rbac_orgs_for_user(request: web.Request) -> web.Response:
    """List organizations the given user is a member of (?user_id=...)."""
    user_id = request.query.get("user_id", "")
    if not user_id:
        return web.json_response(
            {"error": "user_id query parameter is required"}, status=400
        )
    orgs = rbac_engine.list_orgs_for_user(user_id)
    return web.json_response({"orgs": [_serialize_rbac(o) for o in orgs]})


async def rbac_role_assign(request: web.Request) -> web.Response:
    """Assign a role to a user within an organization (optionally scoped to a project)."""
    try:
        body = await request.json()
    except Exception:
        return web.json_response({"error": "invalid JSON body"}, status=400)
    user_id = body.get("user_id")
    org_id = body.get("org_id")
    role_name = body.get("role_name")
    if not all(isinstance(v, str) and v for v in (user_id, org_id, role_name)):
        return web.json_response(
            {"error": "user_id, org_id and role_name are required"}, status=400
        )
    if rbac_engine.get_role(role_name) is None:
        return web.json_response({"error": f"unknown role: {role_name}"}, status=400)
    if rbac_engine.get_org(org_id) is None:
        return web.json_response({"error": f"unknown org: {org_id}"}, status=404)
    membership = rbac_engine.assign_role(
        user_id=user_id,
        org_id=org_id,
        role_name=role_name,
        project_id=str(body.get("project_id", "")),
        granted_by=str(body.get("granted_by", "api")),
    )
    return web.json_response(_serialize_rbac(membership), status=201)


async def rbac_org_permissions(request: web.Request) -> web.Response:
    """Return the resolved permission list for a user within an org (?user_id=...)."""
    user_id = request.query.get("user_id", "")
    org_id = request.match_info["org_id"]
    if not user_id:
        return web.json_response(
            {"error": "user_id query parameter is required"}, status=400
        )
    if rbac_engine.get_org(org_id) is None:
        return web.json_response({"error": f"unknown org: {org_id}"}, status=404)
    resolved = [
        p for p in Permission if rbac_engine.has_permission(user_id, p, org_id=org_id)
    ]
    return web.json_response(
        {
            "user_id": user_id,
            "org_id": org_id,
            "permissions": sorted(p.value for p in resolved),
        }
    )


async def rbac_org_members(request: web.Request) -> web.Response:
    """List memberships of an organization (optionally ?project_id=...)."""
    org_id = request.match_info["org_id"]
    if rbac_engine.get_org(org_id) is None:
        return web.json_response({"error": f"unknown org: {org_id}"}, status=404)
    members = rbac_engine.list_members(org_id, request.query.get("project_id", ""))
    return web.json_response({"members": [_serialize_rbac(m) for m in members]})


async def verify_github_signature(
    request: web.Request, handler: Callable[[web.Request], object]
) -> web.Response:
    """Verify GitHub webhook HMAC-SHA256 signature (X-Hub-Signature-256).

    Fails closed: without a configured GITHUB_WEBHOOK_SECRET the route
    refuses all traffic instead of accepting unsigned requests.
    """
    secret = os.getenv("GITHUB_WEBHOOK_SECRET", "")
    if not secret:
        return web.json_response({"error": "webhook auth not configured"}, status=503)
    body = await request.read()
    signature = request.headers.get("X-Hub-Signature-256", "")
    expected = "sha256=" + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(signature, expected):
        logger.warning(
            "Rejected webhook with invalid signature from %s", request.remote
        )
        return web.json_response({"error": "invalid webhook signature"}, status=401)
    return await handler(request)


async def verify_gitops_token(
    request: web.Request, handler: Callable[[web.Request], object]
) -> web.Response:
    """Verify GitOps webhook Bearer token.

    Fails closed: without a configured GITOPS_WEBHOOK_TOKEN the route
    refuses all traffic instead of accepting unauthenticated requests.
    """
    token = os.getenv("GITOPS_WEBHOOK_TOKEN", "")
    if not token:
        return web.json_response({"error": "webhook auth not configured"}, status=503)
    auth = request.headers.get("Authorization", "")
    if not (auth.startswith("Bearer ") and hmac.compare_digest(auth[7:], token)):
        logger.warning("Rejected webhook with invalid token from %s", request.remote)
        return web.json_response({"error": "unauthorized"}, status=401)
    return await handler(request)


async def start_webhook_server(bot_instance: commands.Bot):
    """Start the aiohttp webhook server for GitOps and health endpoints.

    Args:
        bot_instance: The Discord bot instance to attach webhook routes from.
    """
    app = build_webhook_app(bot_instance)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("GITOPS_WEBHOOK_PORT", "8500"))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info("Webhook server listening on port %d", port)


async def build_webhook_app(bot_instance: commands.Bot) -> web.Application:
    """Build the aiohttp application with all webhook and API routes.

    Extracted from start_webhook_server so the route table can be tested
    with aiohttp's TestClient without binding a real port.
    """
    app = web.Application()

    async def verify_federation_token(request: web.Request) -> Optional[web.Response]:
        """Check Bearer token on federation API routes.

        Fails closed in production: without a configured
        ``FEDERATION_API_TOKEN`` every ``/api/`` route refuses traffic.
        In other environments a missing token logs a warning and allows
        requests so local development stays usable.

        Returns ``None`` if the token is valid (or auth is explicitly
        disabled in a non-production environment), otherwise a 503/401.
        """
        api_token = os.getenv("FEDERATION_API_TOKEN", "")
        if not api_token:
            environment = os.getenv(
                "NODE_ENV", os.getenv("ENVIRONMENT", "development")
            )
            if environment == "production":
                return web.json_response(
                    {
                        "error": "auth not configured",
                        "message": "FEDERATION_API_TOKEN is required in production",
                    },
                    status=503,
                )
            logger.warning(
                "FEDERATION_API_TOKEN is not set; /api/ routes are unauthenticated "
                "in %s environment. Set a token before deploying to production.",
                environment,
            )
            return None
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Bearer ") and hmac.compare_digest(auth[7:], api_token):
            return None
        return web.json_response(
            {
                "error": "unauthorized",
                "message": "Invalid or missing federation API token",
            },
            status=401,
        )

    @web.middleware
    async def federation_auth_middleware(request: web.Request, handler):
        """Apply token verification to /api/ paths."""
        if request.path.startswith("/api/"):
            response = await verify_federation_token(request)
            if response:
                return response
        return await handler(request)

    app.middlewares.append(federation_auth_middleware)

    async def health(request: web.Request) -> web.Response:
        from db import get_pool as _get_pool

        db_ok = False
        try:
            pool = await _get_pool()
            conn = await pool.acquire()
            await conn.execute("SELECT 1")
            await pool.release(conn)
            db_ok = True
        except Exception:
            pass

        return web.json_response(
            {
                "status": "ok" if db_ok else "degraded",
                "service": "orchestrator-agent",
                "postgresql": "up" if db_ok else "down",
            }
        )

    async def metrics(request: web.Request) -> web.Response:
        """Prometheus /metrics endpoint."""
        pyver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        lines = [
            "# HELP orchestrator_agent_info Static info about the agent",
            "# TYPE orchestrator_agent_info gauge",
            f'orchestrator_agent_info{{service="orchestrator-agent"}} 1',
            "",
            "# HELP python_info Python runtime info",
            "# TYPE python_info gauge",
            f'python_info{{version="{pyver}"}} 1',
            "",
        ]

        # Process metrics
        proc = psutil.Process()
        with proc.oneshot():
            mem = proc.memory_info()
            lines.append(
                "# HELP process_virtual_memory_bytes Virtual memory size in bytes"
            )
            lines.append("# TYPE process_virtual_memory_bytes gauge")
            lines.append(f"process_virtual_memory_bytes {mem.vss}")
            lines.append(
                "# HELP process_resident_memory_bytes Resident memory size in bytes"
            )
            lines.append("# TYPE process_resident_memory_bytes gauge")
            lines.append(f"process_resident_memory_bytes {mem.rss}")
            cpu_percent = proc.cpu_percent(interval=0)
            lines.append("# HELP process_cpu_percent CPU usage percentage")
            lines.append("# TYPE process_cpu_percent gauge")
            lines.append(f"process_cpu_percent {cpu_percent}")
            lines.append("")

        # VPS instance metrics (from bot if available)
        vps_cog = bot_instance.get_cog("VPSCommands")
        if vps_cog and hasattr(vps_cog, "vps_manager"):
            vm = vps_cog.vps_manager
            instances = getattr(vm, "vps_instances", {})
            total = len(instances)
            running = sum(1 for i in instances.values() if i.get("status") == "running")
            stopped = sum(1 for i in instances.values() if i.get("status") == "stopped")
            lines.append("# HELP orchestrator_vps_instances_total Total VPS instances")
            lines.append("# TYPE orchestrator_vps_instances_total gauge")
            lines.append(f"orchestrator_vps_instances_total {total}")
            lines.append(
                "# HELP orchestrator_vps_instances_running Running VPS instances"
            )
            lines.append("# TYPE orchestrator_vps_instances_running gauge")
            lines.append(f"orchestrator_vps_instances_running {running}")
            lines.append(
                "# HELP orchestrator_vps_instances_stopped Stopped VPS instances"
            )
            lines.append("# TYPE orchestrator_vps_instances_stopped gauge")
            lines.append(f"orchestrator_vps_instances_stopped {stopped}")
            lines.append("")

        return web.Response(
            text="\n".join(lines),
            content_type="text/plain; charset=utf-8",
        )

    async def federation_status(request: web.Request) -> web.Response:
        """Federation peer status endpoint (requires valid token)."""
        return web.json_response(
            {
                "status": "ok",
                "service": "orchestrator-agent",
                "federation": {"enabled": bool(os.getenv("FEDERATION_API_TOKEN", ""))},
                "version": "1.0.0",
            }
        )

    app.router.add_get("/health", health)
    app.router.add_get("/api/health", health)
    app.router.add_get("/metrics", metrics)
    app.router.add_get("/api/v1/federation/status", federation_status)
    app.router.add_get("/api/v1/rbac/roles", rbac_roles_list)
    app.router.add_post("/api/v1/rbac/roles", rbac_role_create)
    app.router.add_post("/api/v1/rbac/orgs", rbac_org_create)
    app.router.add_get("/api/v1/rbac/orgs", rbac_orgs_for_user)
    app.router.add_post("/api/v1/rbac/assign", rbac_role_assign)
    app.router.add_get("/api/v1/rbac/orgs/{org_id}/permissions", rbac_org_permissions)
    app.router.add_get("/api/v1/rbac/orgs/{org_id}/members", rbac_org_members)

    cog = bot_instance.get_cog("GitDeployer")
    if cog:

        async def github_webhook(request: web.Request) -> web.Response:
            return await verify_github_signature(request, cog.handle_webhook)

        app.router.add_post("/webhook/github/{deploy_id}", github_webhook)
        app.router.add_post("/webhook/github", github_webhook)

    gitops_cog = bot_instance.get_cog("GitOpsSync")
    if gitops_cog:

        async def gitops_webhook(request: web.Request) -> web.Response:
            return await verify_gitops_token(request, gitops_cog.handle_webhook)

        app.router.add_post("/webhook/gitops", gitops_webhook)

    return app
