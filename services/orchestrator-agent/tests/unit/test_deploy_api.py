"""Integration tests for the deployment API on the webhook server."""

import os
import time
import unittest
import importlib
from datetime import datetime
from types import SimpleNamespace

from aiohttp.test_utils import TestClient, TestServer

os.environ["FEDERATION_API_TOKEN"] = "test-federation-token"
os.environ["GITOPS_WEBHOOK_TOKEN"] = "test-gitops-token"

from compute.base import (  # noqa: E402
    ComputeProvider,
    InstanceInfo,
    InstancePowerState,
    InstanceSpec,
    InstanceStats,
    ProviderCapabilities,
    ProviderError,
)
from compute.registry import ProviderRegistry  # noqa: E402
from webhook_server import build_webhook_app  # noqa: E402

BOT = SimpleNamespace(get_cog=lambda name: None)
AUTH = {"Authorization": "Bearer test-federation-token"}


class FakeProvider(ComputeProvider):
    """In-memory provider that records the operations it performs."""

    name = "fake"

    def __init__(self):
        self.instances: dict = {}

    @property
    def capabilities(self) -> ProviderCapabilities:
        return ProviderCapabilities(max_instances=10, regions=["default"])

    async def create(self, spec: InstanceSpec) -> InstanceInfo:
        if "boom" in spec.image:
            raise ProviderError("simulated create failure")
        info = InstanceInfo(
            id=spec.name,
            name=spec.name,
            provider="fake",
            status=InstancePowerState.RUNNING,
            spec=spec,
            created_at=datetime.now(),
            host="fake-host",
        )
        self.instances[spec.name] = info
        return info

    async def get(self, instance_id: str) -> InstanceInfo:
        if instance_id not in self.instances:
            raise ProviderError("missing")
        return self.instances[instance_id]

    async def list(self):
        return list(self.instances.values())

    async def start(self, instance_id: str) -> bool:
        return True

    async def stop(self, instance_id: str) -> bool:
        return True

    async def restart(self, instance_id: str) -> bool:
        return True

    async def delete(self, instance_id: str) -> bool:
        self.instances.pop(instance_id, None)
        return True

    async def update(self, instance_id: str, spec: InstanceSpec) -> bool:
        return True

    async def stats(self, instance_id: str) -> InstanceStats:
        return None


ProviderRegistry.register(FakeProvider)


def make_manifest(name: str, image: str = "nginx:1.25") -> dict:
    return {
        "api_version": "v1",
        "kind": "InfraFile",
        "metadata": {"name": name, "environment": "production"},
        "spec": {
            "instances": [
                {
                    "name": name,
                    "provider": "fake",
                    "image": image,
                    "cpu": 1.0,
                    "memory_mb": 512,
                    "storage_gb": 10,
                }
            ]
        },
    }


class DeployApiTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # Other test modules call ProviderRegistry.clear(), so re-register
        # the built-in provider (import re-run) and the fake one per test.
        import compute.docker_provider  # noqa: F401

        importlib.reload(compute.docker_provider)
        ProviderRegistry.register(FakeProvider)
        self.app = await build_webhook_app(BOT)
        self.client = TestClient(TestServer(self.app))
        await self.client.start_server()
        self.addAsyncCleanup(self.client.close)

    async def asyncTearDown(self):
        ProviderRegistry._providers.pop("fake", None)
        ProviderRegistry._instances.pop("fake", None)

    async def test_deploy_route_requires_federation_token(self):
        resp = await self.client.post(
            "/api/v1/deployments", json={"manifest": make_manifest("m1")}
        )
        self.assertEqual(resp.status, 401)

    async def test_manifest_is_required(self):
        for body in ({}, {"dry_run": True}, {"manifest": "not-a-dict"}):
            resp = await self.client.post(
                "/api/v1/deployments", json=body, headers=AUTH
            )
            self.assertEqual(resp.status, 400, body)

    async def test_invalid_manifest_is_rejected(self):
        bad = {"spec": {"instances": "not-a-list"}}
        resp = await self.client.post(
            "/api/v1/deployments", json={"manifest": bad}, headers=AUTH
        )
        self.assertEqual(resp.status, 400)

    async def test_dry_run_reconcile_returns_counts(self):
        resp = await self.client.post(
            "/api/v1/deployments",
            json={"manifest": make_manifest("m-dry"), "dry_run": True},
            headers=AUTH,
        )
        self.assertEqual(resp.status, 200)
        body = await resp.json()
        self.assertEqual(body["manifest_name"], "m-dry")
        self.assertTrue(body["dry_run"])
        self.assertEqual(body["instances_created"], 1)
        self.assertEqual(body["errors"], [])

    async def test_apply_reconcile_creates_instance(self):
        resp = await self.client.post(
            "/api/v1/deployments",
            json={"manifest": make_manifest("m-apply")},
            headers=AUTH,
        )
        self.assertEqual(resp.status, 200)
        body = await resp.json()
        self.assertFalse(body["dry_run"])
        self.assertEqual(body["instances_created"], 1)

    async def test_provider_failure_reports_207(self):
        resp = await self.client.post(
            "/api/v1/deployments",
            json={"manifest": make_manifest("m-boom", image="nginx:boom")},
            headers=AUTH,
        )
        self.assertEqual(resp.status, 207)
        body = await resp.json()
        self.assertIn("simulated create failure", body["errors"][0])

    async def test_user_without_deploy_permission_is_denied(self):
        resp = await self.client.post(
            "/api/v1/rbac/orgs",
            json={"name": "Acme", "owner_user_id": "u-owner"},
            headers=AUTH,
        )
        self.assertEqual(resp.status, 201)
        org_id = (await resp.json())["id"]

        resp = await self.client.post(
            "/api/v1/deployments",
            json={
                "manifest": make_manifest("m-denied"),
                "user_id": "u-outsider",
                "org_id": org_id,
            },
            headers=AUTH,
        )
        self.assertEqual(resp.status, 403)

    async def test_org_owner_can_deploy(self):
        resp = await self.client.post(
            "/api/v1/rbac/orgs",
            json={"name": "BossCorp", "owner_user_id": "u-boss"},
            headers=AUTH,
        )
        self.assertEqual(resp.status, 201)
        org_id = (await resp.json())["id"]

        resp = await self.client.post(
            "/api/v1/deployments",
            json={
                "manifest": make_manifest("m-owned"),
                "user_id": "u-boss",
                "org_id": org_id,
            },
            headers=AUTH,
        )
        self.assertEqual(resp.status, 200)

    async def test_providers_list_includes_builtin_and_fake(self):
        resp = await self.client.get("/api/v1/providers", headers=AUTH)
        self.assertEqual(resp.status, 200)
        body = await resp.json()
        self.assertIn("docker", body["providers"])
        self.assertIn("fake", body["providers"])

    async def test_gitops_webhook_requires_valid_token(self):
        resp = await self.client.post(
            "/webhook/gitops", json={"manifest": make_manifest("m-gh")}
        )
        self.assertEqual(resp.status, 401)

        resp = await self.client.post(
            "/webhook/gitops",
            json={"manifest": make_manifest("m-gh")},
            headers={
                "Authorization": "Bearer wrong-token",
                "X-Timestamp": str(int(time.time())),
            },
        )
        self.assertEqual(resp.status, 401)

    async def test_gitops_webhook_runs_reconcile(self):
        resp = await self.client.post(
            "/webhook/gitops",
            json={"manifest": make_manifest("m-gitops")},
            headers={
                "Authorization": "Bearer test-gitops-token",
                "X-Timestamp": str(int(time.time())),
            },
        )
        self.assertEqual(resp.status, 200)
        body = await resp.json()
        self.assertEqual(body["manifest_name"], "m-gitops")
