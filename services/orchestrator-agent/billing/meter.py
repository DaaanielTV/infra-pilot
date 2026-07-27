"""Usage metering — tracks resource consumption per tenant.

Reads live stats from compute providers and aggregates into
hourly/daily usage records tagged by org/project/instance.
"""

import asyncio
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

from compute.base import ComputeProvider, InstanceInfo, InstanceStats
from compute.registry import ProviderRegistry

logger = logging.getLogger(__name__)


class UsageMetric(str, Enum):
    CPU_CORES = "cpu_cores"
    MEMORY_MB = "memory_mb"
    STORAGE_GB = "storage_gb"
    NETWORK_RX_GB = "network_rx_gb"
    NETWORK_TX_GB = "network_tx_gb"
    SNAPSHOT_COUNT = "snapshot_count"
    BACKUP_COUNT = "backup_count"


@dataclass
class ResourceUsage:
    """Snapshot of resource usage at a point in time."""
    instance_id: str
    instance_name: str
    org_id: str
    project_id: str
    provider: str
    cpu_cores: float
    memory_mb: int
    storage_gb: int
    network_rx_bytes: int = 0
    network_tx_bytes: int = 0
    snapshot_count: int = 0
    backup_count: int = 0
    collected_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class UsageRecord:
    """Aggregated usage for a time window."""
    org_id: str
    project_id: str
    instance_id: str
    metric: UsageMetric
    value: float
    window_start: datetime
    window_end: datetime
    provider: str = "docker"


class UsageMeter:
    """Collects and aggregates usage data from compute providers.

    Designed to be called periodically (e.g. every 60s) from the
    existing resource monitoring loop.
    """

    def __init__(self):
        self._buffer: List[ResourceUsage] = []

    async def collect(self) -> List[ResourceUsage]:
        """Poll all providers and collect current usage snapshots."""
        snapshots: List[ResourceUsage] = []
        provider_names = ProviderRegistry.list_providers()

        for provider_name in provider_names:
            prov = ProviderRegistry.get(provider_name)
            if not prov:
                continue
            try:
                instances = await prov.list()
                for inst in instances:
                    usage = await self._snapshot(provider_name, prov, inst)
                    if usage:
                        snapshots.append(usage)
            except Exception as exc:
                logger.warning("Failed to collect usage from %s: %s", provider_name, exc)

        self._buffer.extend(snapshots)
        return snapshots

    async def _snapshot(
        self, provider_name: str, prov: ComputeProvider, inst: InstanceInfo
    ) -> Optional[ResourceUsage]:
        stats = await prov.stats(inst.id)
        if stats is None:
            return None

        org_id = inst.spec.metadata.get("org_id", "")
        project_id = inst.spec.metadata.get("project_id", "")

        return ResourceUsage(
            instance_id=inst.id,
            instance_name=inst.name,
            org_id=org_id,
            project_id=project_id,
            provider=provider_name,
            cpu_cores=inst.spec.cpu_cores,
            memory_mb=inst.spec.memory_mb,
            storage_gb=inst.spec.storage_gb,
            network_rx_bytes=stats.network_rx_bytes,
            network_tx_bytes=stats.network_tx_bytes,
        )

    def get_usage_for_org(
        self, org_id: str, since: Optional[datetime] = None
    ) -> List[ResourceUsage]:
        """Return all buffered usage records for an organization."""
        results = [r for r in self._buffer if r.org_id == org_id]
        if since:
            results = [r for r in results if r.collected_at >= since]
        return results

    def clear_buffer(self) -> int:
        """Clear the in-memory buffer (after persisting)."""
        count = len(self._buffer)
        self._buffer.clear()
        return count

    async def run_loop(self, interval_seconds: int = 60) -> None:
        """Background loop that collects usage on an interval."""
        logger.info("Usage meter started (interval: %ds)", interval_seconds)
        while True:
            try:
                snapshots = await self.collect()
                logger.debug("Collected %d usage snapshots", len(snapshots))
            except Exception as exc:
                logger.error("Usage collection error: %s", exc)
            await asyncio.sleep(interval_seconds)
