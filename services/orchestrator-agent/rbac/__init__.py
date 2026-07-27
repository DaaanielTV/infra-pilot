"""Multi-tenant RBAC — organizations, projects, teams, and fine-grained permissions.

Avoids the Proxmox problem of flat user management and the OpenStack
problem of overly complex role hierarchies by offering a clean
org → project → team model with scoped permissions.
"""

from .models import (
    Organization,
    Project,
    Team,
    Role,
    Permission,
    Membership,
    ALL_PERMISSIONS,
)
from .engine import RBACEngine, AccessDeniedError

__all__ = [
    "Organization",
    "Project",
    "Team",
    "Role",
    "Permission",
    "Membership",
    "ALL_PERMISSIONS",
    "RBACEngine",
    "AccessDeniedError",
]
