"""Tests for the auto-scaling engine."""

from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, MagicMock, PropertyMock

import pytest
from scaling import ScalingAction, ScalingEngine, ScalingEvent, ScalingRule


@pytest.fixture
def mock_vps_manager():
    mgr = MagicMock()
    mgr.vps_instances = {
        "abc123": {
            "container_id": "abc123",
            "config": {
                "cpu_limit": 2.0,
                "memory_limit": 2048,
                "storage_limit": 50,
                "image": "ubuntu:22.04",
                "ports": {},
                "env_vars": {},
            },
        }
    }
    mgr.get_vps_stats = AsyncMock(
        return_value={
            "status": "running",
            "cpu_usage": 95.0,
            "memory_usage": 80.0,
        }
    )
    mgr.update_vps_config = AsyncMock(return_value=True)
    return mgr


@pytest.fixture
def engine(mock_vps_manager):
    return ScalingEngine(mock_vps_manager)


class TestScalingRule:
    def test_create_rule(self):
        rule = ScalingRule(
            id=1,
            container_id="abc123",
            metric="cpu_usage",
            threshold=80.0,
            duration_minutes=5,
            action="scale_up",
        )
        assert rule.id == 1
        assert rule.metric == "cpu_usage"
        assert rule.enabled is True

    def test_rule_disabled(self):
        rule = ScalingRule(
            id=2,
            container_id="def456",
            metric="memory_usage",
            threshold=90.0,
            duration_minutes=3,
            action="scale_down",
            enabled=False,
        )
        assert rule.enabled is False


class TestScalingEngine:
    @pytest.mark.asyncio
    async def test_evaluate_no_breach(self, engine):
        rule = ScalingRule(
            id=1,
            container_id="abc123",
            metric="cpu_usage",
            threshold=95.0,
            duration_minutes=2,
            action="scale_up",
        )
        stats = {"cpu_usage": 50.0}
        event = await engine.evaluate(rule, stats)
        assert event is None

    @pytest.mark.asyncio
    async def test_evaluate_breach_insufficient_duration(self, engine):
        rule = ScalingRule(
            id=2,
            container_id="abc123",
            metric="cpu_usage",
            threshold=80.0,
            duration_minutes=5,
            action="scale_up",
        )
        stats = {"cpu_usage": 95.0}
        # First call, consecutive count is 1, needs 5
        event = await engine.evaluate(rule, stats)
        assert event is None

    @pytest.mark.asyncio
    async def test_evaluate_triggers_scale_up(self, engine, mock_vps_manager):
        engine._consecutive["abc123_3"] = 4  # Pre-seed 4 breaches
        rule = ScalingRule(
            id=3,
            container_id="abc123",
            metric="cpu_usage",
            threshold=80.0,
            duration_minutes=5,
            action="scale_up",
        )
        stats = {"cpu_usage": 95.0}
        event = await engine.evaluate(rule, stats)
        assert event is not None
        assert event.action == ScalingAction.SCALE_UP
        assert event.previous_cores == 2.0
        assert event.new_cores == 3.0  # 2.0 + 1.0
        assert event.success is True
        mock_vps_manager.update_vps_config.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_cooldown_respects_delay(self, engine):
        rule = ScalingRule(
            id=4,
            container_id="abc123",
            metric="cpu_usage",
            threshold=80.0,
            duration_minutes=1,
            action="scale_up",
            cooldown_until=datetime.now(timezone.utc) + timedelta(hours=1),
        )
        engine._consecutive["abc123_4"] = 5
        stats = {"cpu_usage": 95.0}
        event = await engine.evaluate(rule, stats)
        assert event is None  # Blocked by cooldown

    def test_get_scale_step(self, engine):
        new_cores, new_memory = engine._get_scale_step(
            1.0, 1024, ScalingAction.SCALE_UP
        )
        assert new_cores == 2.0
        assert new_memory == 2048

        new_cores, new_memory = engine._get_scale_step(
            4.0, 8192, ScalingAction.SCALE_DOWN
        )
        assert new_cores == 3.5
        assert new_memory == 7680

    def test_get_scale_step_capped(self, engine):
        new_cores, new_memory = engine._get_scale_step(
            100.0, 999999, ScalingAction.SCALE_UP
        )
        assert new_cores == 4.0  # max_cpu
        assert new_memory == 8192  # max_memory_mb

    @pytest.mark.asyncio
    async def test_evaluate_all_empty(self, engine):
        events = await engine.evaluate_all()
        assert events == []

    @pytest.mark.asyncio
    async def test_add_and_list_rules(self, engine):
        rule = ScalingRule(
            id=10,
            container_id="abc123",
            metric="cpu_usage",
            threshold=80.0,
            duration_minutes=5,
            action="scale_up",
        )
        engine.add_rule(rule)
        assert len(engine.list_rules()) == 1
        assert engine.get_rule(10) is rule

    @pytest.mark.asyncio
    async def test_remove_rule(self, engine):
        engine.add_rule(
            ScalingRule(
                id=20,
                container_id="abc123",
                metric="cpu_usage",
                threshold=80.0,
                duration_minutes=5,
                action="scale_up",
            )
        )
        assert engine.remove_rule(20) is True
        assert engine.remove_rule(99) is False

    def test_engine_defaults(self, engine):
        assert engine._running is False
        assert engine._task is None
        assert engine._recent_events == []


class TestScalingEvent:
    def test_create_event(self):
        event = ScalingEvent(
            container_id="abc123",
            rule_id=1,
            action=ScalingAction.SCALE_UP,
            metric="cpu_usage",
            value=95.0,
            threshold=80.0,
            previous_cores=2.0,
            new_cores=3.0,
            previous_memory_mb=2048,
            new_memory_mb=3072,
            success=True,
        )
        assert event.success is True
        assert event.message == ""
        assert event.timestamp is not None
