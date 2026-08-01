"""Orchestrator Agent entry point - Discord bot with webhook server."""

import asyncio
import hashlib
import hmac
import logging
import os
import sys
from typing import Callable, Optional

import discord
from aiohttp import web
from config import config
from discord.ext import commands
from integration import init_database_tables

logger = logging.getLogger(__name__)

BOT_PREFIX = "/"
FEDERATION_API_TOKEN: str = os.getenv("FEDERATION_API_TOKEN", "")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)
bot.config = config

# Auto-scaling engine (initialised after cog load completes)
scaling_engine = None

CORE_COGS = [
    "cogs.vps_commands",
    "cogs.vps_pricing",
    "cogs.vps_billing",
    "cogs.prepaid_billing",
    "cogs.monitoring",
    "cogs.bot_commands",
    "cogs.health_checks",
    "cogs.backup_manager",
    "cogs.resource_manager",
    "cogs.template_manager",
    "cogs.task_scheduler",
    "cogs.alert_manager",
    "cogs.auto_scaler",
    "cogs.cleanup",
    "cogs.database_manager",
    "cogs.modpack_installer",
    "cogs.update_manager",
]


async def load_cogs():
    """Load all core Discord cogs."""
    for cog in CORE_COGS:
        try:
            await bot.load_extension(cog)
            logger.info("Loaded cog: %s", cog)
        except commands.errors.ExtensionAlreadyLoaded:
            logger.warning("Cog already loaded: %s", cog)
        except Exception as exc:
            logger.error("Failed to load cog %s: %s", cog, exc)


@bot.event
async def on_ready():
    """Handle the bot ready event - initialise DB and sync commands."""
    logger.info("Bot ready. Logged in as %s", bot.user)
    try:
        await init_database_tables()
        logger.info("Database tables initialised")
    except Exception as exc:
        logger.warning("Database initialisation skipped: %s", exc)

    await bot.tree.sync()
    logger.info("Commands synced")

    # Wire auto-scaling engine (only once)
    if not hasattr(bot, "scaling_engine") or bot.scaling_engine is None:
        vps_cog = bot.get_cog("VPSCommands")
        if vps_cog and hasattr(vps_cog, "vps_manager"):
            from scaling import ScalingEngine

            engine = ScalingEngine(vps_cog.vps_manager)
            bot.scaling_engine = engine
            # Set engine on AutoScaler cog if loaded
            asc = bot.get_cog("AutoScaler")
            if asc:
                asc.engine = engine
            # Connect to healing engine if available
            healing = bot.get_cog("HealingCog")
            if healing and hasattr(healing, "engine"):
                healing.engine.set_scaling_engine(engine)
                logger.info("Scaling engine connected to healing engine")
            asyncio.create_task(engine.start())
            logger.info("Auto-scaling engine started")

    asyncio.create_task(start_webhook_server(bot))


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
    app = web.Application()

    async def verify_federation_token(request: web.Request) -> Optional[web.Response]:
        """Check Bearer token on federation API routes.

        Returns ``None`` if the token is valid (or auth is disabled),
        otherwise a 401 response.
        """
        if not FEDERATION_API_TOKEN:
            return None
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Bearer ") and auth[7:] == FEDERATION_API_TOKEN:
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

    async def github_webhook_wrapper(
        request: web.Request, handler: Callable[[web.Request], object]
    ) -> web.Response:
        return await verify_github_signature(request, handler)

    async def gitops_webhook_wrapper(
        request: web.Request, handler: Callable[[web.Request], object]
    ) -> web.Response:
        return await verify_gitops_token(request, handler)

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
        import os
        import sys

        import psutil

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
                "federation": {"enabled": bool(FEDERATION_API_TOKEN)},
                "version": "1.0.0",
            }
        )

    app.router.add_get("/health", health)
    app.router.add_get("/api/health", health)
    app.router.add_get("/metrics", metrics)
    app.router.add_get("/api/v1/federation/status", federation_status)

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

    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("GITOPS_WEBHOOK_PORT", "8500"))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info("Webhook server listening on port %d", port)


async def run_health_only():
    """Run only the health/webhook server without the Discord bot."""
    await start_webhook_server(bot)
    await asyncio.Event().wait()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )

    token_missing = (
        not config.DISCORD_BOT_TOKEN
        or config.DISCORD_BOT_TOKEN == "your_discord_bot_token_here"
    )
    disabled = os.getenv("ORCHESTRATOR_AGENT_DISABLED", "true").lower() == "true"

    if token_missing or disabled:
        logger.warning("Discord bot disabled; starting health/webhook server only")
        try:
            asyncio.run(run_health_only())
        except KeyboardInterrupt:
            logger.info("Server shutting down")
        sys.exit(0)

    asyncio_loop = None
    try:
        asyncio_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(asyncio_loop)
        asyncio_loop.run_until_complete(load_cogs())
        bot.run(config.DISCORD_BOT_TOKEN)
    except KeyboardInterrupt:
        logger.info("Bot shutting down")
    finally:
        if asyncio_loop:
            asyncio_loop.close()
