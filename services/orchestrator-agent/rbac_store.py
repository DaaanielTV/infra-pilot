"""Best-effort persistence of RBAC state to PostgreSQL.

The RBAC engine is in-memory; these helpers sync organizations, custom
roles and role assignments into the tables created by
``integration.init_database_tables`` so state survives restarts.

Every function fails soft: when the database is unavailable the change
is logged and the in-memory state still applies.
"""

import json
import logging

import db

logger = logging.getLogger(__name__)


async def persist_org(org) -> None:
    """Upsert an organization row (best-effort)."""
    try:
        pool = await db.get_pool()
        await pool.execute(
            """
            INSERT INTO organizations
                (id, name, owner_user_id, settings, is_active, created_at, updated_at)
            VALUES ($1, $2, $3, $4, $5, $6, $7)
            ON CONFLICT (id) DO UPDATE SET
                name = EXCLUDED.name,
                owner_user_id = EXCLUDED.owner_user_id,
                settings = EXCLUDED.settings,
                is_active = EXCLUDED.is_active,
                updated_at = EXCLUDED.updated_at
            """,
            org.id,
            org.name,
            org.owner_user_id,
            json.dumps(org.settings) if org.settings else None,
            org.is_active,
            org.created_at,
            org.updated_at,
        )
    except Exception as exc:
        logger.warning("Failed to persist org %s: %s", org.id, exc)


async def persist_role(role) -> None:
    """Upsert a custom role row (built-ins are re-seeded on start)."""
    if role.is_builtin:
        return
    try:
        pool = await db.get_pool()
        await pool.execute(
            """
            INSERT INTO roles (name, permissions, is_builtin, description)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (name) DO UPDATE SET
                permissions = EXCLUDED.permissions,
                description = EXCLUDED.description
            """,
            role.name,
            json.dumps(sorted(p.value for p in role.permissions)),
            False,
            role.description,
        )
    except Exception as exc:
        logger.warning("Failed to persist role %s: %s", role.name, exc)


async def persist_membership(membership) -> None:
    """Insert a role assignment row (best-effort)."""
    try:
        pool = await db.get_pool()
        await pool.execute(
            """
            INSERT INTO role_assignments
                (user_id, org_id, project_id, role_name, granted_by, granted_at, expires_at)
            VALUES ($1, $2, NULLIF($3, ''), $4, NULLIF($5, ''), $6, $7)
            ON CONFLICT (user_id, org_id, project_id) DO UPDATE SET
                role_name = EXCLUDED.role_name,
                granted_by = EXCLUDED.granted_by,
                granted_at = EXCLUDED.granted_at,
                expires_at = EXCLUDED.expires_at
            """,
            membership.user_id,
            membership.org_id,
            membership.project_id,
            membership.role_name,
            membership.granted_by,
            membership.granted_at,
            membership.expires_at,
        )
    except Exception as exc:
        logger.warning(
            "Failed to persist membership %s@%s: %s",
            membership.user_id,
            membership.org_id,
            exc,
        )


async def delete_org(org_id: str) -> None:
    """Delete an organization row and its cascade (best-effort)."""
    try:
        pool = await db.get_pool()
        await pool.execute("DELETE FROM organizations WHERE id = $1", org_id)
    except Exception as exc:
        logger.warning("Failed to delete org %s: %s", org_id, exc)


async def delete_role(name: str) -> None:
    """Delete a custom role row (best-effort)."""
    try:
        pool = await db.get_pool()
        await pool.execute("DELETE FROM roles WHERE name = $1", name)
    except Exception as exc:
        logger.warning("Failed to delete role %s: %s", name, exc)


async def delete_membership(user_id: str, org_id: str, project_id: str = "") -> None:
    """Delete a role assignment row (best-effort)."""
    try:
        pool = await db.get_pool()
        await pool.execute(
            """
            DELETE FROM role_assignments
            WHERE user_id = $1 AND org_id = $2 AND project_id IS NOT DISTINCT FROM $3
            """,
            user_id,
            org_id,
            None if not project_id else project_id,
        )
    except Exception as exc:
        logger.warning(
            "Failed to delete membership %s@%s: %s", user_id, org_id, exc
        )


async def load_rbac_state(engine) -> None:
    """Load persisted orgs/roles/assignments into the engine (best-effort).

    Intended to run once at startup against a fresh engine. When the
    database is unavailable the engine keeps its built-in roles only.
    """
    try:
        pool = await db.get_pool()
        org_rows = await pool.fetch("SELECT * FROM organizations")
        role_rows = await pool.fetch("SELECT * FROM roles")
        member_rows = await pool.fetch("SELECT * FROM role_assignments")
    except Exception as exc:
        logger.warning("Failed to load RBAC state: %s", exc)
        return

    orgs = []
    for row in org_rows:
        orgs.append(
            {
                "id": row["id"],
                "name": row["name"],
                "owner_user_id": row["owner_user_id"],
                "settings": row["settings"] or {},
                "is_active": row["is_active"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
            }
        )

    roles = []
    for row in role_rows:
        try:
            permissions = json.loads(row["permissions"]) if row["permissions"] else []
        except (TypeError, ValueError):
            permissions = []
        roles.append(
            {
                "name": row["name"],
                "permissions": permissions,
                "is_builtin": row["is_builtin"],
                "description": row["description"] or "",
            }
        )

    memberships = []
    for row in member_rows:
        memberships.append(
            {
                "user_id": row["user_id"],
                "org_id": row["org_id"],
                "project_id": row["project_id"] or "",
                "role_name": row["role_name"],
                "granted_by": row["granted_by"] or "",
                "granted_at": row["granted_at"],
                "expires_at": row["expires_at"],
            }
        )

    engine.restore({"orgs": orgs, "roles": roles, "memberships": memberships})
    logger.info(
        "RBAC state loaded: %d orgs, %d custom roles, %d memberships",
        len(orgs),
        len(roles),
        len(memberships),
    )
