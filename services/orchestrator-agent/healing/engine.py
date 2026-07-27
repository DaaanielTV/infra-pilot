"""Healing engine — watches health status and triggers remediation.

Designed to integrate with the existing health check infrastructure
(VPSManager.run_health_check) and auto-remediation config.
"""

import asyncio
import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Any, Awaitable, Callable, Dict, List, Optional, Set

from compute.base import ComputeProvider, InstancePowerState
from compute.registry import ProviderRegistry

logger = logging.getLogger(__name__)


class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"


class RemediationAction(str, Enum):
    RESTART = "restart"
    RECREATE = "recreate"
    MIGRATE = "migrate"
    SCALE_UP = "scale_up"
    EXEC_COMMAND = "exec_command"
    NOTIFY = "notify"
    ESCALATE = "escalate"


@dataclass
class RemediationResult:
    """Outcome of a remediation attempt."""
    instance_id: str
    action: RemediationAction
    success: bool
    message: str = ""
    duration_ms: int = 0
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class HealthCheck:
    """A single health check configuration."""
    instance_id: str
    check_type: str  # ping, port, process, http
    target: str = ""
    interval_seconds: int = 30
    timeout_seconds: int = 10
    retries: int = 3
    failure_count: int = 0
    last_status: HealthStatus = HealthStatus.UNKNOWN
    last_checked: Optional[datetime] = None


@dataclass
class RemediationPolicy:
    """Rules for when and how to remediate an instance."""
    instance_id: str
    max_restarts_per_hour: int = 3
    restart_cooldown_seconds: int = 30
    enable_auto_restart: bool = True
    enable_auto_recreate: bool = False
    enable_auto_migrate: bool = False
    health_check_type: str = "http"
    health_check_target: str = "http://localhost:80/health"
    notify_on_failure: bool = True
    escalate_after_minutes: int = 10


REMEDIATION_HANDLER = Callable[[str, RemediationAction], bool]
REMEDIATION_HANDLER_CORO = Callable[[str, RemediationAction], Awaitable[bool]]


class HealingEngine:
    """Monitors health and triggers remediation automatically.

    Designed to run as a background asyncio task alongside the
    existing resource monitor and health check infrastructure.
    """

    def __init__(self):
        self._policies: Dict[str, RemediationPolicy] = {}
        self._health_checks: Dict[str, HealthCheck] = {}
        self._recent_actions: List[RemediationResult] = []
        self._handlers: Dict[RemediationAction, REMEDIATION_HANDLER] = {}
        self._running = False
        self._task: Optional[asyncio.Task] = None
        self._pending_tasks: Set[asyncio.Task] = set()
        self._scaling_engine: Optional[Any] = None

        self._register_default_handlers()

    def _register_default_handlers(self) -> None:
        """Wire up built-in remediation actions."""
        self._handlers[RemediationAction.RESTART] = self._default_restart
        self._handlers[RemediationAction.NOTIFY] = self._default_notify
        self._handlers[RemediationAction.ESCALATE] = self._default_escalate
        # SCALE_UP is handled by the ScalingEngine when registered externally

    def set_scaling_engine(self, engine) -> None:
        """Connect a ScalingEngine to handle SCALE_UP actions."""
        self._scaling_engine = engine
        self._handlers[RemediationAction.SCALE_UP] = self._default_scale_up

    def register_handler(
        self, action: RemediationAction, handler: REMEDIATION_HANDLER
    ) -> None:
        """Override or add a remediation handler."""
        self._handlers[action] = handler

    # ------------------------------------------------------------------
    # Policy management
    # ------------------------------------------------------------------
    def set_policy(self, policy: RemediationPolicy) -> None:
        self._policies[policy.instance_id] = policy
        self._health_checks[policy.instance_id] = HealthCheck(
            instance_id=policy.instance_id,
            check_type=policy.health_check_type,
            target=policy.health_check_target,
        )

    def remove_policy(self, instance_id: str) -> None:
        self._policies.pop(instance_id, None)
        self._health_checks.pop(instance_id, None)

    def get_policy(self, instance_id: str) -> Optional[RemediationPolicy]:
        return self._policies.get(instance_id)

    # ------------------------------------------------------------------
    # Health checks
    # ------------------------------------------------------------------
    async def check_instance(self, instance_id: str) -> HealthStatus:
        """Run a health check for an instance via its compute provider."""
        hc = self._health_checks.get(instance_id)
        if not hc:
            return HealthStatus.UNKNOWN

        # Find the provider that owns this instance
        for prov_name in ProviderRegistry.list_providers():
            prov = ProviderRegistry.get(prov_name)
            if not prov:
                continue
            try:
                info = await prov.get(instance_id)
                if info.status == InstancePowerState.RUNNING:
                    hc.last_status = HealthStatus.HEALTHY
                else:
                    hc.last_status = HealthStatus.UNHEALTHY
                hc.last_checked = datetime.now(timezone.utc)
                return hc.last_status
            except Exception:
                continue

        hc.last_status = HealthStatus.UNKNOWN
        hc.last_checked = datetime.now(timezone.utc)
        return hc.last_status

    async def check_all(self) -> Dict[str, HealthStatus]:
        """Check all managed instances."""
        results: Dict[str, HealthStatus] = {}
        for instance_id in list(self._health_checks.keys()):
            results[instance_id] = await self.check_instance(instance_id)
        return results

    # ------------------------------------------------------------------
    # Remediation
    # ------------------------------------------------------------------
    async def remediate(self, instance_id: str) -> Optional[RemediationResult]:
        """Attempt to remediate an unhealthy instance."""
        policy = self._policies.get(instance_id)
        if not policy:
            logger.info("No remediation policy for %s", instance_id)
            return None

        # Check rate limits
        recent_restarts = [
            r for r in self._recent_actions[-60:]
            if r.instance_id == instance_id and r.action == RemediationAction.RESTART
        ]
        if len(recent_restarts) >= policy.max_restarts_per_hour:
            logger.warning("Rate limit hit for %s (%d restarts/hour)", instance_id, len(recent_restarts))
            return await self._escalate(instance_id, "Rate limit exceeded")

        actions = [
            (RemediationAction.RESTART, policy.enable_auto_restart),
            (RemediationAction.RECREATE, policy.enable_auto_recreate),
            (RemediationAction.MIGRATE, policy.enable_auto_migrate),
        ]

        for action, enabled in actions:
            if not enabled:
                continue

            handler = self._handlers.get(action)
            if not handler:
                continue

            start = datetime.now(timezone.utc)
            try:
                if asyncio.iscoroutinefunction(handler):
                    success = await handler(instance_id, action)
                else:
                    success = handler(instance_id, action)
            except Exception as exc:
                success = False
                logger.error("Remediation handler failed for %s: %s", instance_id, exc)
            duration = int((datetime.now(timezone.utc) - start).total_seconds() * 1000)

            result = RemediationResult(
                instance_id=instance_id,
                action=action,
                success=success,
                message=f"{action.value} {'succeeded' if success else 'failed'}",
                duration_ms=duration,
            )
            self._recent_actions.append(result)

            if success:
                logger.info("Remediation succeeded for %s: %s", instance_id, action.value)
                return result

        return await self._escalate(instance_id, "All remediation actions failed")

    async def _escalate(self, instance_id: str, reason: str) -> Optional[RemediationResult]:
        """Escalate to a human operator."""
        handler = self._handlers.get(RemediationAction.ESCALATE)
        if handler:
            if asyncio.iscoroutinefunction(handler):
                await handler(instance_id, RemediationAction.ESCALATE)
            else:
                handler(instance_id, RemediationAction.ESCALATE)
        return RemediationResult(
            instance_id=instance_id,
            action=RemediationAction.ESCALATE,
            success=True,
            message=f"Escalated: {reason}",
        )

    # ------------------------------------------------------------------
    # Default handlers (can be overridden)
    # ------------------------------------------------------------------
    async def _default_restart(self, instance_id: str, action: RemediationAction) -> bool:
        """Default: restart via Docker provider."""
        prov = ProviderRegistry.get("docker")
        if not prov:
            return False
        try:
            await prov.restart(instance_id)
            return True
        except Exception as exc:
            logger.error("Restart failed for %s: %s", instance_id, exc)
            return False

    def _default_scale_up(self, instance_id: str, action: RemediationAction) -> bool:
        """Delegate SCALE_UP to the connected ScalingEngine."""
        if not self._scaling_engine:
            logger.warning("No scaling engine connected for SCALE_UP on %s", instance_id)
            return False
        try:
            # Trigger an immediate evaluate for all rules on this instance
            import asyncio
            task = asyncio.ensure_future(self._scaling_engine.evaluate_all())
            self._pending_tasks.add(task)
            task.add_done_callback(self._pending_tasks.discard)
            return True
        except Exception as exc:
            logger.error("SCALE_UP delegation failed for %s: %s", instance_id, exc)
            return False

    def _default_notify(self, instance_id: str, action: RemediationAction) -> bool:
        logger.warning("Health alert for instance %s", instance_id)
        return True

    def _default_escalate(self, instance_id: str, action: RemediationAction) -> bool:
        logger.error("ESCALATION: instance %s requires human intervention", instance_id)
        return True

    # ------------------------------------------------------------------
    # Background loop
    # ------------------------------------------------------------------
    async def start(self, interval_seconds: int = 30) -> None:
        """Start the background healing loop."""
        if self._running:
            return
        self._running = True
        self._task = asyncio.create_task(self._loop(interval_seconds))
        logger.info("Healing engine started (interval: %ds)", interval_seconds)

    async def stop(self) -> None:
        self._running = False
        if self._task:
            self._task.cancel()
            self._task = None
        logger.info("Healing engine stopped")

    async def _loop(self, interval_seconds: int) -> None:
        while self._running:
            try:
                statuses = await self.check_all()
                for instance_id, status in statuses.items():
                    if status == HealthStatus.UNHEALTHY:
                        logger.info("Unhealthy instance detected: %s", instance_id)
                        await self.remediate(instance_id)
            except Exception as exc:
                logger.error("Healing loop error: %s", exc)
            await asyncio.sleep(interval_seconds)
