"""Self-healing & auto-remediation engine.

Monitors health check results and automatically executes remediation
playbooks when failures are detected. Avoids the Proxmox problem of
basic HA and the OpenStack problem of requiring external monitoring
stack for automated recovery.
"""

from .engine import HealingEngine, HealthStatus, RemediationAction, RemediationResult

__all__ = [
    "HealingEngine",
    "RemediationAction",
    "RemediationResult",
    "HealthStatus",
]
