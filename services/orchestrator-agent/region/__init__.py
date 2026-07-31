"""Region & federation — multi-datacenter support.

Tracks physical datacenter regions and allows instances, networks, and
storage to be placed in specific locations. The federation layer enables
cross-region management from a single control plane.

This addresses Proxmox's lack of native multi-datacenter support and
avoids OpenStack's complexity of cells and availability zones.
"""

from .federation import Federation, FederationPeer
from .region import Datacenter, Region, RegionStatus

__all__ = [
    "Region",
    "Datacenter",
    "RegionStatus",
    "Federation",
    "FederationPeer",
]
