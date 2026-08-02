"""Comprehensive CLI tests for automation & orchestration commands (features 71-80)."""

import pytest
import json
import argparse
from unittest.mock import patch, MagicMock, PropertyMock


class TestCLIQuotaCommands:
    def test_quota_list_command(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.quota_list.return_value = [
                {"quota_id": "q1", "entity_type": "org"}
            ]
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_quota_list

            args = argparse.Namespace(output="json")
            cmd_quota_list(args)
            mock_client.quota_list.assert_called_once()

    def test_quota_check_command(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.quota_check.return_value = {"allowed": True, "violations": []}
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_quota_check

            args = argparse.Namespace(
                entity_type="org", entity_id="org-1", cpu=4, memory=8, output="json"
            )
            cmd_quota_check(args)
            mock_client.quota_check.assert_called_once_with(
                "org", "org-1", {"cpu": 4, "memory": 8}
            )

    def test_quota_check_exceeded(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.quota_check.return_value = {
                "allowed": False,
                "violations": ["cpu limit exceeded"],
            }
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_quota_check

            args = argparse.Namespace(
                entity_type="org", entity_id="org-1", cpu=32, memory=128, output="json"
            )
            cmd_quota_check(args)
            assert mock_client.quota_check.return_value["allowed"] is False

    def test_quota_check_no_resources(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.quota_check.return_value = {"allowed": True, "violations": []}
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_quota_check

            args = argparse.Namespace(
                entity_type="org", entity_id="org-1", cpu=0, memory=0, output="json"
            )
            cmd_quota_check(args)
            assert mock_client.quota_check.return_value["allowed"] is True

    def test_quota_list_multiple(self):
        mock_quotas = [{"quota_id": "q1"}, {"quota_id": "q2"}]
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.quota_list.return_value = mock_quotas
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_quota_list

            args = argparse.Namespace(output="json")
            cmd_quota_list(args)
            assert len(mock_client.quota_list.return_value) == 2

    def test_quota_check_missing_entity(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.quota_check.return_value = {"error": "entity not found"}
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_quota_check

            args = argparse.Namespace(
                entity_type="org",
                entity_id="nonexistent",
                cpu=1,
                memory=1,
                output="json",
            )
            cmd_quota_check(args)
            assert "error" in mock_client.quota_check.return_value


class TestCLIMaintenanceCommands:
    def test_maintenance_list_command(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.maintenance_list_windows.return_value = [
                {"window_id": "w1", "name": "DB Upgrade"}
            ]
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_maintenance_list

            args = argparse.Namespace(output="json")
            cmd_maintenance_list(args)
            mock_client.maintenance_list_windows.assert_called_once()

    def test_maintenance_schedule_command(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.maintenance_schedule.return_value = {
                "window_id": "w1",
                "status": "scheduled",
            }
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_maintenance_schedule

            args = argparse.Namespace(
                name="Upgrade",
                start="2026-06-01T02:00:00Z",
                end="2026-06-01T04:00:00Z",
                systems="db-01,db-02",
                output="json",
            )
            cmd_maintenance_schedule(args)
            mock_client.maintenance_schedule.assert_called_once_with(
                "Upgrade",
                "2026-06-01T02:00:00Z",
                "2026-06-01T04:00:00Z",
                ["db-01", "db-02"],
            )

    def test_maintenance_list_multiple(self):
        mock_windows = [{"window_id": "w1"}, {"window_id": "w2"}, {"window_id": "w3"}]
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.maintenance_list_windows.return_value = mock_windows
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_maintenance_list

            args = argparse.Namespace(output="json")
            cmd_maintenance_list(args)
            assert len(mock_client.maintenance_list_windows.return_value) == 3

    def test_maintenance_schedule_custom_systems(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.maintenance_schedule.return_value = {
                "window_id": "w1",
                "affected_systems": ["web-01", "web-02", "db-01"],
            }
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_maintenance_schedule

            systems = "web-01,web-02,db-01"
            args = argparse.Namespace(
                name="Deploy",
                start="2026-06-01T02:00:00Z",
                end="2026-06-01T04:00:00Z",
                systems=systems,
                output="json",
            )
            cmd_maintenance_schedule(args)
            expected_systems = [s.strip() for s in systems.split(",")]
            assert mock_client.maintenance_schedule.call_args[0][3] == expected_systems

    def test_maintenance_schedule_error(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.maintenance_schedule.return_value = {
                "error": "overlapping window"
            }
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_maintenance_schedule

            args = argparse.Namespace(
                name="Upgrade",
                start="2026-06-01T02:00:00Z",
                end="2026-06-01T04:00:00Z",
                systems="srv1",
                output="json",
            )
            cmd_maintenance_schedule(args)
            assert "error" in mock_client.maintenance_schedule.return_value
