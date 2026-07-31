"""Auto-scaling engine — monitors resource usage and adjusts capacity."""

import asyncio
import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

from config import config

logger = logging.getLogger(__name__)


class ScalingAction(str, Enum):
    SCALE_UP = "scale_up"
    SCALE_DOWN = "scale_down"


@dataclass
class ScalingRule:
    """A single auto-scaling rule loaded from the database."""

    id: int
    container_id: str
    metric: str  # cpu_usage, memory_usage
    threshold: float  # trigger percentage (e.g. 80.0)
    duration_minutes: int  # how long metric must exceed threshold before acting
    action: str  # scale_up, scale_down
    cooldown_until: Optional[datetime] = None
    enabled: bool = True


@dataclass
class ScalingEvent:
    """Record of a scaling action that was taken."""

    container_id: str
    rule_id: int
    action: ScalingAction
    metric: str
    value: float
    threshold: float
    previous_cores: float
    new_cores: float
    previous_memory_mb: int
    new_memory_mb: int
    success: bool
    message: str = ""
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ScalingEngine:
    """Monitors VPS resource usage and applies scaling rules.

    Usage::

        engine = ScalingEngine(vps_manager)
        await engine.start()
        # ... runs in background ...
        await engine.stop()
    """

    def __init__(self, vps_manager):
        self._vps_manager = vps_manager
        self._rules: Dict[int, ScalingRule] = {}
        self._consecutive: Dict[str, int] = {}  # container_id -> breach count
        self._running = False
        self._task: Optional[asyncio.Task] = None
        self._recent_events: List[ScalingEvent] = []
        self._db = None  # Set via set_db_pool(db_pool) if using asyncpg

    def set_db_pool(self, db_pool) -> None:
        """Inject an async database pool (optional, falls back to no persistence)."""
        self._db = db_pool

    # ------------------------------------------------------------------
    # Rule management
    # ------------------------------------------------------------------
    def add_rule(self, rule: ScalingRule) -> None:
        self._rules[rule.id] = rule

    def remove_rule(self, rule_id: int) -> bool:
        return self._rules.pop(rule_id, None) is not None

    def get_rule(self, rule_id: int) -> Optional[ScalingRule]:
        return self._rules.get(rule_id)

    def list_rules(self, container_id: Optional[str] = None) -> List[ScalingRule]:
        if container_id:
            return [r for r in self._rules.values() if r.container_id == container_id]
        return list(self._rules.values())

    async def load_rules_from_db(self) -> int:
        """Load enabled scaling rules from the database."""
        if not self._db:
            return 0
        try:
            rows = await self._db.fetch(
                "SELECT id, container_id, metric, threshold, "
                "duration_minutes, action, cooldown_until, enabled "
                "FROM scaling_rules WHERE enabled = TRUE"
            )
            count = 0
            for row in rows:
                self._rules[row["id"]] = ScalingRule(
                    id=row["id"],
                    container_id=row["container_id"],
                    metric=row["metric"],
                    threshold=row["threshold"],
                    duration_minutes=row["duration_minutes"],
                    action=row["action"],
                    cooldown_until=row.get("cooldown_until"),
                    enabled=row["enabled"],
                )
                count += 1
            logger.info("Loaded %d scaling rules from database", count)
            return count
        except Exception as exc:
            logger.error("Failed to load scaling rules: %s", exc)
            return 0

    # ------------------------------------------------------------------
    # Scaling logic
    # ------------------------------------------------------------------
    def _get_scale_step(
        self, current_cores: float, current_memory_mb: int, action: ScalingAction
    ):
        """Compute the new resource limits for a scale action.

        Scale up:   +1 CPU core, +1 GB RAM   (capped at max limits)
        Scale down: -0.5 CPU core, -512 MB RAM  (floored at min limits)
        """
        limits = config.RESOURCE_LIMITS
        min_cpu = limits["min_cpu"]
        max_cpu = limits["max_cpu"]
        min_mem = limits["min_memory_mb"]
        max_mem = limits["max_memory_mb"]

        if action == ScalingAction.SCALE_UP:
            new_cores = min(current_cores + 1.0, max_cpu)
            new_memory = min(current_memory_mb + 1024, max_mem)
        else:
            new_cores = max(current_cores - 0.5, min_cpu)
            new_memory = max(current_memory_mb - 512, min_mem)

        return new_cores, new_memory

    async def evaluate(
        self, rule: ScalingRule, stats: Dict[str, Any]
    ) -> Optional[ScalingEvent]:
        """Check if a rule's threshold is breached and scale if needed."""
        metric_value = stats.get(rule.metric, 0.0)
        container_id = rule.container_id
        breach_key = f"{container_id}_{rule.id}"

        if metric_value >= rule.threshold:
            self._consecutive[breach_key] = self._consecutive.get(breach_key, 0) + 1
        else:
            self._consecutive[breach_key] = 0
            return None

        # Check if we've breached long enough
        if self._consecutive[breach_key] < rule.duration_minutes:
            return None

        # Check cooldown
        now = datetime.now(timezone.utc)
        if rule.cooldown_until and now < rule.cooldown_until:
            return None

        # Determine action direction
        action = ScalingAction(rule.action)

        # Get current resources
        instance_info = self._vps_manager.vps_instances.get(container_id)
        if not instance_info:
            logger.warning("Instance %s not found for scaling", container_id)
            return None

        cfg = instance_info.get("config", {})
        current_cores = float(cfg.get("cpu_limit", 1))
        current_memory_mb = int(cfg.get("memory_limit", 1024))

        new_cores, new_memory = self._get_scale_step(
            current_cores, current_memory_mb, action
        )

        # Skip if no change
        if new_cores == current_cores and new_memory == current_memory_mb:
            return None

        # Apply via VPSManager
        from vps_manager import VPSConfig

        new_cfg = VPSConfig(
            cpu_limit=new_cores,
            memory_limit=new_memory,
            storage_limit=int(cfg.get("storage_limit", 10)),
            image=cfg.get("image", "ubuntu:22.04"),
            ports=cfg.get("ports", {}),
            env_vars=cfg.get("env_vars", {}),
        )

        logger.info(
            "Scaling %s %s: cpu %.1f->%.1f, mem %d->%d",
            action.value,
            container_id[:12],
            current_cores,
            new_cores,
            current_memory_mb,
            new_memory,
        )

        try:
            success = await self._vps_manager.update_vps_config(container_id, new_cfg)
        except Exception as exc:
            success = False
            logger.error("Scale action failed for %s: %s", container_id, exc)

        event = ScalingEvent(
            container_id=container_id,
            rule_id=rule.id,
            action=action,
            metric=rule.metric,
            value=metric_value,
            threshold=rule.threshold,
            previous_cores=current_cores,
            new_cores=new_cores,
            previous_memory_mb=current_memory_mb,
            new_memory_mb=new_memory,
            success=success,
            message=f"{action.value}: {metric_value:.1f}% >= {rule.threshold}%",
        )
        self._recent_events.append(event)
        self._recent_events = self._recent_events[-200:]

        # Update cooldown in rule
        rule.cooldown_until = now + timedelta(
            minutes=config.AUTO_SCALE_COOLDOWN_MINUTES
        )

        # Reset consecutive counter
        self._consecutive[breach_key] = 0

        return event

    async def evaluate_all(self) -> List[ScalingEvent]:
        """Check all rules against current stats."""
        events: List[ScalingEvent] = []
        for rule in list(self._rules.values()):
            if not rule.enabled:
                continue
            stats = await self._vps_manager.get_vps_stats(rule.container_id)
            if stats is None:
                continue
            event = await self.evaluate(rule, stats)
            if event:
                events.append(event)
        return events

    # ------------------------------------------------------------------
    # Background loop
    # ------------------------------------------------------------------
    async def start(self, interval_seconds: int = 60) -> None:
        if self._running:
            return
        self._running = True
        self._task = asyncio.create_task(self._loop(interval_seconds))
        logger.info("Scaling engine started (interval: %ds)", interval_seconds)

    async def stop(self) -> None:
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None
        logger.info("Scaling engine stopped")

    async def _loop(self, interval_seconds: int) -> None:
        await self.load_rules_from_db()
        while self._running:
            try:
                events = await self.evaluate_all()
                if events:
                    logger.info("Scaling engine: %d event(s) triggered", len(events))
            except Exception as exc:
                logger.error("Scaling loop error: %s", exc)
            await asyncio.sleep(interval_seconds)
