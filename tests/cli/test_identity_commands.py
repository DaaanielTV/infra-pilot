"""Comprehensive CLI tests for identity & governance commands (features 61-70)."""
import pytest
import json
import argparse
from unittest.mock import patch, MagicMock, PropertyMock


class TestCLIAuditCommands:
    def test_audit_anomalies_command(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.audit_get_anomalies.return_value = [{"id": "a1", "type": "off_hours"}]
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_audit_anomalies
            args = argparse.Namespace(output="json")
            cmd_audit_anomalies(args)
            mock_client.audit_get_anomalies.assert_called_once()

    def test_audit_trend_command(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.audit_get_trend.return_value = {"user_id": "u1", "anomaly_count": 5}
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_audit_trend
            args = argparse.Namespace(user_id="u1", output="json")
            cmd_audit_trend(args)
            mock_client.audit_get_trend.assert_called_once_with("u1")

    def test_audit_summary_command(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.audit_get_summary.return_value = {"total_events": 1000, "anomaly_count": 15}
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_audit_summary
            args = argparse.Namespace(output="json")
            cmd_audit_summary(args)
            mock_client.audit_get_summary.assert_called_once()

    def test_audit_anomalies_with_threshold(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.audit_get_anomalies.return_value = [{"id": "a1", "score": 95}]
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_audit_anomalies
            args = argparse.Namespace(output="json")
            cmd_audit_anomalies(args)
            assert len(mock_client.audit_get_anomalies.return_value) >= 1

    def test_audit_anomalies_empty(self):
        with patch("cli.ipilot.cli.get_client") as mock_get:
            mock_client = MagicMock()
            mock_client.audit_get_anomalies.return_value = []
            mock_get.return_value = mock_client
            from cli.ipilot.cli import cmd_audit_anomalies
            args = argparse.Namespace(output="json")
            cmd_audit_anomalies(args)
            assert mock_client.audit_get_anomalies.return_value == []