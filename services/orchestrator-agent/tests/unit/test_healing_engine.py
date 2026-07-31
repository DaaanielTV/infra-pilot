"""Tests for the self-healing and auto-remediation engine."""

from datetime import datetime, timezone

import pytest

from healing.engine import (
    HealingEngine,
    HealthStatus,
    RemediationAction,
    RemediationPolicy,
)


@pytest.fixture
def engine():
    return HealingEngine()


class TestPolicyManagement:
    def test_set_and_get_policy(self, engine):
        policy = RemediationPolicy(instance_id="i-1")
        engine.set_policy(policy)
        assert engine.get_policy("i-1") is policy

    def test_remove_policy(self, engine):
        policy = RemediationPolicy(instance_id="i-2")
        engine.set_policy(policy)
        engine.remove_policy("i-2")
        assert engine.get_policy("i-2") is None


class TestHealthChecks:
    @pytest.mark.asyncio
    async def test_check_unknown_instance(self, engine):
        status = await engine.check_instance("nonexistent")
        assert status == HealthStatus.UNKNOWN

    @pytest.mark.asyncio
    async def test_check_all_empty(self, engine):
        results = await engine.check_all()
        assert results == {}


class TestRemediation:
    @pytest.mark.asyncio
    async def test_remediate_no_policy(self, engine):
        result = await engine.remediate("nonexistent")
        assert result is None

    @pytest.mark.asyncio
    async def test_default_restart_handler(self, engine):
        # Should not crash for nonexistent instance
        result = await engine._default_restart("i-1", RemediationAction.RESTART)
        # Will fail because docker provider not registered, but should not raise
        assert result is False

    def test_default_notify(self, engine):
        assert engine._default_notify("i-1", RemediationAction.NOTIFY) is True

    def test_default_escalate(self, engine):
        assert engine._default_escalate("i-1", RemediationAction.ESCALATE) is True

    def test_custom_handler(self, engine):
        called = []

        def my_handler(instance_id, action):
            called.append((instance_id, action))
            return True

        engine.register_handler(RemediationAction.RESTART, my_handler)
        assert engine._handlers[RemediationAction.RESTART] is my_handler

    @pytest.mark.asyncio
    async def test_remediate_rate_limited(self, engine):
        policy = RemediationPolicy(instance_id="i-rate", max_restarts_per_hour=0)
        engine.set_policy(policy)

        # Add many recent restarts
        for _ in range(10):
            from healing.engine import RemediationResult
            engine._recent_actions.append(
                RemediationResult(
                    instance_id="i-rate",
                    action=RemediationAction.RESTART,
                    success=True,
                )
            )

        result = await engine.remediate("i-rate")
        assert result is not None
        assert result.action == RemediationAction.ESCALATE


class TestHealthStatus:
    def test_enum_values(self):
        assert HealthStatus.HEALTHY == "healthy"
        assert HealthStatus.UNHEALTHY == "unhealthy"
        assert HealthStatus.DEGRADED == "degraded"
        assert HealthStatus.UNKNOWN == "unknown"

    def test_remediation_action_values(self):
        assert RemediationAction.RESTART == "restart"
        assert RemediationAction.RECREATE == "recreate"
        assert RemediationAction.MIGRATE == "migrate"
        assert RemediationAction.SCALE_UP == "scale_up"
        assert RemediationAction.NOTIFY == "notify"
        assert RemediationAction.ESCALATE == "escalate"
