"""Auto-scaling engine — monitors resource usage and adjusts capacity.

Evaluates scaling rules from the ``scaling_rules`` database table,
queries live stats from VPSManager, and triggers scale actions
(CPU/memory changes via Docker's ``container.update()``).
"""

from .engine import ScalingAction, ScalingEngine, ScalingEvent, ScalingRule

__all__ = ["ScalingEngine", "ScalingAction", "ScalingRule", "ScalingEvent"]
