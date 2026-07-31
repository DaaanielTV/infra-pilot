"""Region and datacenter models for multi-datacenter awareness.

A Region is a logical grouping of datacenters (e.g. ``us-east``).
A Datacenter is a physical location within a region (e.g. ``us-east-1a``).
Instances and volumes specify their region for placement.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional


class RegionStatus(str, Enum):
    ACTIVE = "active"
    DEGRADED = "degraded"
    DOWN = "down"
    MAINTENANCE = "maintenance"


@dataclass
class Datacenter:
    """A physical or logical datacenter / availability zone."""

    id: str
    name: str
    region_id: str
    location: str = ""
    provider: str = "docker"
    status: RegionStatus = RegionStatus.ACTIVE
    total_cpu_cores: float = 0
    total_memory_mb: int = 0
    total_storage_gb: int = 0
    used_cpu_cores: float = 0
    used_memory_mb: int = 0
    used_storage_gb: int = 0
    labels: Dict[str, str] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def cpu_available(self) -> float:
        return self.total_cpu_cores - self.used_cpu_cores

    @property
    def memory_available(self) -> int:
        return self.total_memory_mb - self.used_memory_mb

    @property
    def storage_available(self) -> int:
        return self.total_storage_gb - self.used_storage_gb

    def utilization(self) -> Dict[str, float]:
        """Return resource utilization as percentages."""
        return {
            "cpu_percent": round(
                (
                    (self.used_cpu_cores / self.total_cpu_cores * 100)
                    if self.total_cpu_cores > 0
                    else 0
                ),
                1,
            ),
            "memory_percent": round(
                (
                    (self.used_memory_mb / self.total_memory_mb * 100)
                    if self.total_memory_mb > 0
                    else 0
                ),
                1,
            ),
            "storage_percent": round(
                (
                    (self.used_storage_gb / self.total_storage_gb * 100)
                    if self.total_storage_gb > 0
                    else 0
                ),
                1,
            ),
        }


@dataclass
class Region:
    """A logical region that groups datacenters."""

    id: str
    name: str
    display_name: str = ""
    status: RegionStatus = RegionStatus.ACTIVE
    datacenters: List[Datacenter] = field(default_factory=list)
    labels: Dict[str, str] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)

    def add_datacenter(self, dc: Datacenter) -> None:
        self.datacenters.append(dc)

    def remove_datacenter(self, dc_id: str) -> bool:
        before = len(self.datacenters)
        self.datacenters = [dc for dc in self.datacenters if dc.id != dc_id]
        return len(self.datacenters) < before

    def get_datacenter(self, dc_id: str) -> Optional[Datacenter]:
        for dc in self.datacenters:
            if dc.id == dc_id:
                return dc
        return None

    @property
    def total_cpu(self) -> float:
        return sum(dc.total_cpu_cores for dc in self.datacenters)

    @property
    def total_memory(self) -> int:
        return sum(dc.total_memory_mb for dc in self.datacenters)

    @property
    def total_storage(self) -> int:
        return sum(dc.total_storage_gb for dc in self.datacenters)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "display_name": self.display_name,
            "status": self.status.value,
            "datacenters": [
                {
                    "id": dc.id,
                    "name": dc.name,
                    "status": dc.status.value,
                    "utilization": dc.utilization(),
                }
                for dc in self.datacenters
            ],
            "labels": self.labels,
            "created_at": self.created_at.isoformat(),
        }
