"""Federation — cross-region control plane.

Allows one infra-pilot instance to manage resources in remote regions
via peer-to-peer federation. Each peer exposes a REST API that the
federation layer proxies to provide a unified management interface.
"""

import asyncio
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

import aiohttp
from region.region import Region, RegionStatus

logger = logging.getLogger(__name__)


class PeerStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    DEGRADED = "degraded"
    UNKNOWN = "unknown"


@dataclass
class FederationPeer:
    """A remote infra-pilot instance."""

    id: str
    name: str
    api_url: str
    api_token: str = ""
    status: PeerStatus = PeerStatus.UNKNOWN
    region_ids: List[str] = field(default_factory=list)
    last_seen: Optional[datetime] = None
    version: str = ""
    labels: Dict[str, str] = field(default_factory=dict)
    timeout_seconds: int = 10


class Federation:
    """Manages connections to remote peers for cross-region orchestration.

    Proxies instance lifecycle, health checks, and monitoring to remote
    regions while presenting a unified API to the user.
    """

    def __init__(self):
        self._peers: Dict[str, FederationPeer] = {}
        self._session: Optional[aiohttp.ClientSession] = None
        self._running = False

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    # ------------------------------------------------------------------
    # Peer management
    # ------------------------------------------------------------------
    def register_peer(self, peer: FederationPeer) -> None:
        self._peers[peer.id] = peer
        logger.info("Registered federation peer: %s (%s)", peer.name, peer.api_url)

    def unregister_peer(self, peer_id: str) -> bool:
        return self._peers.pop(peer_id, None) is not None

    def get_peer(self, peer_id: str) -> Optional[FederationPeer]:
        return self._peers.get(peer_id)

    def list_peers(self) -> List[FederationPeer]:
        return list(self._peers.values())

    # ------------------------------------------------------------------
    # Health / heartbeats
    # ------------------------------------------------------------------
    async def ping_peer(self, peer: FederationPeer) -> bool:
        """Check if a peer is reachable."""
        session = await self._get_session()
        try:
            async with session.get(
                f"{peer.api_url}/health",
                timeout=aiohttp.ClientTimeout(total=peer.timeout_seconds),
            ) as resp:
                if resp.status == 200:
                    peer.status = PeerStatus.ONLINE
                    peer.last_seen = datetime.now(timezone.utc)
                    return True
                peer.status = PeerStatus.DEGRADED
                return False
        except Exception as exc:
            logger.warning("Peer %s unreachable: %s", peer.name, exc)
            peer.status = PeerStatus.OFFLINE
            return False

    async def ping_all(self) -> Dict[str, bool]:
        """Ping all registered peers concurrently."""
        results: Dict[str, bool] = {}
        tasks = {pid: self.ping_peer(peer) for pid, peer in self._peers.items()}
        for pid, task in tasks.items():
            try:
                results[pid] = await task
            except Exception:
                results[pid] = False
        return results

    # ------------------------------------------------------------------
    # Remote operations (proxied)
    # ------------------------------------------------------------------
    async def remote_list_instances(self, peer: FederationPeer) -> List[Dict[str, Any]]:
        """List instances on a remote peer."""
        session = await self._get_session()
        headers = {"Authorization": f"Bearer {peer.api_token}"}
        try:
            async with session.get(
                f"{peer.api_url}/api/v1/servers",
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=peer.timeout_seconds),
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data if isinstance(data, list) else data.get("servers", [])
                logger.warning("Remote list failed on %s: %d", peer.name, resp.status)
                return []
        except Exception as exc:
            logger.error("Error listing instances on %s: %s", peer.name, exc)
            return []

    async def remote_create_instance(
        self, peer: FederationPeer, spec: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """Provision an instance on a remote peer."""
        session = await self._get_session()
        headers = {
            "Authorization": f"Bearer {peer.api_token}",
            "Content-Type": "application/json",
        }
        try:
            async with session.post(
                f"{peer.api_url}/api/v1/servers",
                json=spec,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=peer.timeout_seconds),
            ) as resp:
                if resp.status in (200, 201):
                    return await resp.json()
                logger.warning("Remote create failed on %s: %d", peer.name, resp.status)
                return None
        except Exception as exc:
            logger.error("Error creating instance on %s: %s", peer.name, exc)
            return None

    # ------------------------------------------------------------------
    # Background health monitoring
    # ------------------------------------------------------------------
    async def start_heartbeat(self, interval_seconds: int = 30) -> None:
        """Start a background loop that pings all peers."""
        if self._running:
            return
        self._running = True
        logger.info("Federation heartbeat started (interval: %ds)", interval_seconds)
        while self._running:
            await self.ping_all()
            await asyncio.sleep(interval_seconds)

    async def stop(self) -> None:
        self._running = False
        if self._session and not self._session.closed:
            await self._session.close()

    async def close(self) -> None:
        await self.stop()
