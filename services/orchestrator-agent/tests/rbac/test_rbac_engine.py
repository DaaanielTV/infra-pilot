"""Unit tests for the RBAC engine (rbac package)."""

from datetime import datetime

import pytest

from rbac import (
    AccessDeniedError,
    Organization,
    Permission,
    Project,
    RBACEngine,
    Role,
    Team,
)


@pytest.fixture
def engine() -> RBACEngine:
    return RBACEngine()


@pytest.fixture
def org(engine: RBACEngine) -> Organization:
    return engine.create_org(
        Organization(id="org-1", name="Acme", owner_user_id="user-owner")
    )


def test_create_org_grants_owner_membership(engine: RBACEngine):
    engine.create_org(Organization(id="org-x", name="X", owner_user_id="alice"))
    assert engine.has_permission("alice", Permission.INSTANCE_CREATE, org_id="org-x")
    assert engine.has_permission("alice", Permission.ORG_DELETE, org_id="org-x")


def test_viewer_has_only_read_permissions(engine: RBACEngine, org: Organization):
    engine.assign_role("bob", org.id, "viewer")
    assert engine.has_permission("bob", Permission.INSTANCE_READ, org_id=org.id)
    assert not engine.has_permission("bob", Permission.INSTANCE_CREATE, org_id=org.id)
    assert not engine.has_permission("bob", Permission.ORG_MANAGE, org_id=org.id)


def test_operator_cannot_delete_org(engine: RBACEngine, org: Organization):
    engine.assign_role("carol", org.id, "operator")
    assert engine.has_permission("carol", Permission.INSTANCE_CREATE, org_id=org.id)
    assert not engine.has_permission("carol", Permission.ORG_DELETE, org_id=org.id)


def test_require_permission_passes_and_raises(engine: RBACEngine, org: Organization):
    engine.assign_role("dave", org.id, "operator")
    engine.require_permission("dave", Permission.BACKUP_CREATE, org_id=org.id)
    with pytest.raises(AccessDeniedError):
        engine.require_permission("dave", Permission.ORG_MANAGE, org_id=org.id)


def test_permissions_are_org_scoped(engine: RBACEngine, org: Organization):
    engine.assign_role("erin", org.id, "admin")
    other = engine.create_org(
        Organization(id="org-2", name="Other", owner_user_id="someone")
    )
    assert engine.has_permission("erin", Permission.INSTANCE_READ, org_id=org.id)
    assert not engine.has_permission("erin", Permission.INSTANCE_READ, org_id=other.id)


def test_project_scoped_permissions(engine: RBACEngine, org: Organization):
    engine.create_project(Project(id="proj-1", org_id=org.id, name="Web"))
    engine.assign_role("frank", org.id, "viewer", project_id="proj-1")
    assert engine.has_permission(
        "frank", Permission.INSTANCE_READ, org_id=org.id, project_id="proj-1"
    )
    assert not engine.has_permission("frank", Permission.INSTANCE_READ, org_id=org.id)


def test_assign_and_remove_membership(engine: RBACEngine, org: Organization):
    engine.assign_role("grace", org.id, "billing")
    assert engine.has_permission("grace", Permission.BILLING_MANAGE, org_id=org.id)
    assert engine.remove_membership("grace", org.id)
    assert not engine.has_permission("grace", Permission.BILLING_MANAGE, org_id=org.id)
    assert not engine.remove_membership("grace", org.id)


def test_list_orgs_for_user(engine: RBACEngine, org: Organization):
    engine.assign_role("henry", org.id, "viewer")
    engine.assign_role("henry", "org-unrelated", "viewer")
    listed = engine.list_orgs_for_user("henry")
    assert [o.id for o in listed] == ["org-1"]


def test_delete_org_cascades_memberships(engine: RBACEngine, org: Organization):
    engine.assign_role("ida", org.id, "viewer")
    engine.create_project(Project(id="proj-2", org_id=org.id, name="API"))
    assert engine.delete_org(org.id)
    assert engine.get_org(org.id) is None
    assert engine.get_project("proj-2") is None
    assert engine.list_members(org.id) == []


def test_teams_add_and_remove_members(engine: RBACEngine, org: Organization):
    engine.create_project(Project(id="proj-3", org_id=org.id, name="TeamX"))
    team = engine.create_team(
        Team(id="team-1", org_id=org.id, project_id="proj-3", name="WebTeam")
    )
    assert engine.add_user_to_team(team.id, "jim")
    assert "jim" in team.member_ids
    assert engine.has_permission(
        "jim", Permission.INSTANCE_READ, org_id=org.id, project_id="proj-3"
    )
    assert engine.remove_user_from_team(team.id, "jim")
    assert not engine.has_permission(
        "jim", Permission.INSTANCE_READ, org_id=org.id, project_id="proj-3"
    )


def test_custom_roles(engine: RBACEngine):
    role = Role(
        name="deployer",
        permissions={Permission.MANIFEST_DEPLOY, Permission.MANIFEST_READ},
    )
    engine.create_role(role)
    assert engine.get_role("deployer") is role
    assert engine.delete_role("deployer")
    assert engine.get_role("deployer") is None


def test_builtin_roles_cannot_be_deleted(engine: RBACEngine):
    assert not engine.delete_role("owner")
    assert not engine.delete_role("viewer")


def test_list_members_filters_by_project(engine: RBACEngine, org: Organization):
    engine.create_project(Project(id="proj-4", org_id=org.id, name="A"))
    engine.create_project(Project(id="proj-5", org_id=org.id, name="B"))
    engine.assign_role("kim", org.id, "viewer", project_id="proj-4")
    engine.assign_role("leo", org.id, "viewer", project_id="proj-5")
    assert {m.user_id for m in engine.list_members(org.id)} == {"user-owner", "kim", "leo"}
    assert {m.user_id for m in engine.list_members(org.id, "proj-4")} == {"kim"}


def test_to_dict_serializes_state(engine: RBACEngine, org: Organization):
    state = engine.to_dict()
    assert "org-1" in state["orgs"]
    assert any(
        m["user_id"] == "user-owner" and m["role_name"] == "owner"
        for m in state["memberships"]
    )
