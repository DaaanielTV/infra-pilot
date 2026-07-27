"""Region & federation — multi-datacenter support.

Tracks physical datacenter regions and allows instances, networks, and
storage to be placed in specific locations. The federation layer enables
cross-region management from a single control plane.

This addresses Proxmox's lack of native multi-datacenter support and
avoids OpenStack's complexity of cells and availability zones.
"""

from .region import Region, Datacenter, RegionStatus
from .federation import Federation, FederationPeer

__all__ = [
    "Region",
    "Datacenter",
    "RegionStatus",
    "Federation",
    "FederationPeer",
]
