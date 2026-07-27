"""Integration layer: database schema, MySQL helpers, and notification proxying."""

import logging
from typing import Any, Dict, Optional

import mysql.connector
import requests

from config import config

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT = 5
DEFAULT_PORT = 3306


def _send_request(
    method: str, endpoint: str, data: Optional[Dict[str, Any]] = None
) -> tuple:
    """Send an HTTP request to the integration service.

    Args:
        method: HTTP method (GET or POST).
        endpoint: API endpoint path.
        data: Optional JSON payload for POST requests.

    Returns:
        A tuple of ``(success, response_data)``.
    """
    url = f"{config.INTEGRATION_SERVICE_URL}{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=REQUEST_TIMEOUT)
        else:
            logger.warning("Unsupported HTTP method: %s", method)
            return False, None

        if response.status_code in (200, 201):
            return True, response.json()
        logger.warning(
            "Request failed with status %s: %s", response.status_code, response.text
        )
        return False, None
    except requests.Timeout:
        logger.warning("Request timeout for %s", endpoint)
        return False, None
    except requests.RequestException as exc:
        logger.warning("Request error for %s: %s", endpoint, exc)
        return False, None
    except ValueError as exc:
        logger.warning("Failed to parse response JSON: %s", exc)
        return False, None


def get_db_connection():
    """Create and return a new MySQL database connection.

    Returns:
        A ``mysql.connector.connection`` instance.
    """
    return mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
        port=getattr(config, "DB_PORT", DEFAULT_PORT),
    )


def init_database_tables():
    """Create all required database tables if they don't already exist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    tables = [
        """
        CREATE TABLE IF NOT EXISTS player_economy (
            uuid VARCHAR(255) PRIMARY KEY,
            balance DOUBLE DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS economy_transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            uuid VARCHAR(255) NOT NULL,
            amount DOUBLE NOT NULL,
            type VARCHAR(50) NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS vps_statistics (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            container_id VARCHAR(255) NOT NULL,
            cpu_usage DOUBLE,
            memory_usage DOUBLE,
            memory_used BIGINT,
            memory_total BIGINT,
            network_rx BIGINT,
            network_tx BIGINT,
            disk_usage DOUBLE,
            status VARCHAR(50),
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_container_id (container_id),
            INDEX idx_timestamp (timestamp)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS vps_peak_statistics (
            container_id VARCHAR(255) PRIMARY KEY,
            peak_cpu DOUBLE DEFAULT 0,
            peak_memory DOUBLE DEFAULT 0,
            peak_network BIGINT DEFAULT 0,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS vps_containers (
            container_id VARCHAR(255) PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            container_name VARCHAR(255),
            ssh_command TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_user_id (user_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS health_checks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            container_id VARCHAR(255) NOT NULL,
            check_type VARCHAR(50) NOT NULL,
            target VARCHAR(255),
            interval_seconds INT DEFAULT 60,
            last_check TIMESTAMP,
            last_status VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_container (container_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS health_check_results (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            check_id INT NOT NULL,
            status VARCHAR(50) NOT NULL,
            response_time_ms INT,
            error_message TEXT,
            checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_check_id (check_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS backup_rotation (
            id INT AUTO_INCREMENT PRIMARY KEY,
            container_id VARCHAR(255) NOT NULL,
            image_id VARCHAR(255),
            name VARCHAR(255),
            retention_type VARCHAR(20),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_container (container_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS snapshots (
            id INT AUTO_INCREMENT PRIMARY KEY,
            container_id VARCHAR(255) NOT NULL,
            name VARCHAR(255),
            image_id VARCHAR(255),
            snapshot_type VARCHAR(20) DEFAULT 'manual',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_container (container_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS dns_records (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            type VARCHAR(10) DEFAULT 'A',
            value VARCHAR(255) NOT NULL,
            ttl INT DEFAULT 300,
            zone VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_name (name)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS ssl_certificates (
            id INT AUTO_INCREMENT PRIMARY KEY,
            domain VARCHAR(255) NOT NULL,
            status VARCHAR(50) DEFAULT 'pending',
            expires_at TIMESTAMP,
            issued_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_domain (domain)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS scaling_rules (
            id INT AUTO_INCREMENT PRIMARY KEY,
            container_id VARCHAR(255) NOT NULL,
            metric VARCHAR(50) NOT NULL,
            threshold DOUBLE NOT NULL,
            duration_minutes INT DEFAULT 5,
            action VARCHAR(50) NOT NULL,
            cooldown_until TIMESTAMP,
            enabled TINYINT(1) DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_container (container_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS resource_quotas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            resource_type VARCHAR(50) NOT NULL,
            soft_limit BIGINT,
            hard_limit BIGINT,
            usage BIGINT DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY uk_user_resource (user_id, resource_type)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS load_balancer_pools (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            algorithm VARCHAR(50) DEFAULT 'round_robin',
            health_check_type VARCHAR(50) DEFAULT 'tcp',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY uk_name (name)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS lb_pool_members (
            id INT AUTO_INCREMENT PRIMARY KEY,
            pool_id INT NOT NULL,
            container_id VARCHAR(255) NOT NULL,
            host VARCHAR(255),
            port INT,
            weight INT DEFAULT 1,
            enabled TINYINT(1) DEFAULT 1,
            UNIQUE KEY uk_pool_member (pool_id, container_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS recovery_playbooks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            steps JSON,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY uk_name (name)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS recovery_executions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            playbook_id INT NOT NULL,
            container_id VARCHAR(255) NOT NULL,
            status VARCHAR(50) DEFAULT 'pending',
            current_step INT DEFAULT 0,
            error_message TEXT,
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP,
            INDEX idx_container (container_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS templates (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            version INT DEFAULT 1,
            config JSON,
            created_by VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY uk_name_version (name, version)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS scheduled_tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            task_type VARCHAR(50) NOT NULL,
            target_app_id VARCHAR(255),
            target_container_id VARCHAR(255),
            cron_expression VARCHAR(100) NOT NULL,
            command TEXT,
            enabled BOOLEAN DEFAULT TRUE,
            created_by VARCHAR(255),
            last_run_at TIMESTAMP NULL,
            last_run_status VARCHAR(50),
            next_run_at TIMESTAMP NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS dr_plans (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            plan_type VARCHAR(50) NOT NULL,
            status VARCHAR(50) DEFAULT 'ready',
            config JSON,
            rto_actual_seconds INT,
            rpo_actual_seconds INT,
            last_drill TIMESTAMP NULL,
            last_drill_status VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            UNIQUE KEY uk_name (name)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS dr_drills (
            id INT AUTO_INCREMENT PRIMARY KEY,
            plan_id INT NOT NULL,
            status VARCHAR(50) DEFAULT 'pending',
            steps JSON,
            current_step INT DEFAULT 0,
            rto_achieved INT,
            rpo_achieved INT,
            error_message TEXT,
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP NULL,
            INDEX idx_plan_id (plan_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS runbooks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            steps JSON,
            gates JSON,
            rollback JSON,
            trigger_type VARCHAR(50) DEFAULT 'manual',
            trigger_config JSON,
            enabled TINYINT(1) DEFAULT 1,
            created_by VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            UNIQUE KEY uk_name (name)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS runbook_executions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            runbook_id INT NOT NULL,
            status VARCHAR(50) DEFAULT 'pending',
            current_step INT DEFAULT 0,
            step_results JSON,
            triggered_by VARCHAR(255),
            error_message TEXT,
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP NULL,
            INDEX idx_runbook_id (runbook_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS synthetic_checks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            check_type VARCHAR(20) NOT NULL,
            target VARCHAR(500) NOT NULL,
            interval_minutes INT DEFAULT 5,
            probe_location VARCHAR(100),
            config JSON,
            enabled TINYINT(1) DEFAULT 1,
            last_status VARCHAR(50),
            last_checked_at TIMESTAMP NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_type (check_type),
            INDEX idx_enabled (enabled)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS synthetic_check_results (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            check_id INT NOT NULL,
            probe_location VARCHAR(100),
            status VARCHAR(50) NOT NULL,
            response_time_ms INT,
            status_code INT,
            error_message TEXT,
            checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_check_id (check_id),
            INDEX idx_checked_at (checked_at)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS scan_results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            image_name VARCHAR(500) NOT NULL,
            scanner VARCHAR(50) DEFAULT 'trivy',
            status VARCHAR(50) DEFAULT 'pending',
            summary JSON,
            vulnerabilities JSON,
            auto_remediation_pr VARCHAR(500),
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP NULL,
            INDEX idx_image (image_name),
            INDEX idx_status (status)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS scan_policies (
            id INT AUTO_INCREMENT PRIMARY KEY,
            severity VARCHAR(50) NOT NULL,
            action VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY uk_severity (severity)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS scan_allowlist (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cve_id VARCHAR(50) NOT NULL,
            reason TEXT,
            added_by VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY uk_cve (cve_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS alerts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            container_id VARCHAR(255),
            alert_type VARCHAR(50) NOT NULL,
            threshold DOUBLE,
            channel VARCHAR(50) DEFAULT 'dm',
            enabled TINYINT(1) DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_user (user_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS k8s_clusters (
            name VARCHAR(255) PRIMARY KEY,
            status VARCHAR(50) DEFAULT 'starting',
            node_count INT DEFAULT 1,
            type VARCHAR(50) DEFAULT 'k3s',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS edge_nodes (
            name VARCHAR(255) PRIMARY KEY,
            location VARCHAR(255) NOT NULL,
            status VARCHAR(50) DEFAULT 'registered',
            last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS faas_functions (
            name VARCHAR(255) PRIMARY KEY,
            repo VARCHAR(512) NOT NULL,
            status VARCHAR(50) DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS cloud_pricing_cache (
            id INT AUTO_INCREMENT PRIMARY KEY,
            provider VARCHAR(50) NOT NULL,
            instance_type VARCHAR(100) NOT NULL,
            price_monthly DECIMAL(10,2) NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            UNIQUE KEY uk_provider_instance (provider, instance_type)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS optimization_recommendations (
            id VARCHAR(50) PRIMARY KEY,
            vps_id VARCHAR(255) NOT NULL,
            analysis JSON,
            status VARCHAR(20) DEFAULT 'pending',
            applied_by VARCHAR(255),
            applied_at TIMESTAMP NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_vps_id (vps_id),
            INDEX idx_status (status)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS threat_incidents (
            id VARCHAR(50) PRIMARY KEY,
            vps_id VARCHAR(255) NOT NULL,
            anomaly_score DOUBLE DEFAULT 0,
            alerts JSON,
            stats JSON,
            status VARCHAR(20) DEFAULT 'open',
            detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_vps_id (vps_id),
            INDEX idx_status (status)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS capacity_forecasts (
            id VARCHAR(50) PRIMARY KEY,
            vps_id VARCHAR(255) NOT NULL,
            forecast JSON,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_vps_id (vps_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS gitops_sync_state (
            id VARCHAR(50) PRIMARY KEY,
            vps_id VARCHAR(255) NOT NULL,
            config_snapshot JSON,
            version_id VARCHAR(50),
            sync_type VARCHAR(20) DEFAULT 'sync',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_vps_id (vps_id)
        )
        """,
    ]

    # RBAC tables (multi-tenant organizations, projects, teams, roles)
    rbac_tables = [
        """
        CREATE TABLE IF NOT EXISTS organizations (
            id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            owner_user_id VARCHAR(255) NOT NULL,
            settings JSON,
            is_active TINYINT(1) DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            INDEX idx_owner (owner_user_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS projects (
            id VARCHAR(36) PRIMARY KEY,
            org_id VARCHAR(36) NOT NULL,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            labels JSON,
            is_active TINYINT(1) DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            INDEX idx_org (org_id),
            FOREIGN KEY (org_id) REFERENCES organizations(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS teams (
            id VARCHAR(36) PRIMARY KEY,
            org_id VARCHAR(36) NOT NULL,
            project_id VARCHAR(36) NOT NULL,
            name VARCHAR(255) NOT NULL,
            role_name VARCHAR(50) DEFAULT 'viewer',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_project (project_id),
            FOREIGN KEY (org_id) REFERENCES organizations(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS team_members (
            team_id VARCHAR(36) NOT NULL,
            user_id VARCHAR(255) NOT NULL,
            PRIMARY KEY (team_id, user_id),
            FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS role_assignments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            org_id VARCHAR(36) NOT NULL,
            project_id VARCHAR(36),
            role_name VARCHAR(50) NOT NULL,
            granted_by VARCHAR(255),
            expires_at TIMESTAMP NULL,
            granted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_user (user_id),
            INDEX idx_org (org_id),
            FOREIGN KEY (org_id) REFERENCES organizations(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS roles (
            name VARCHAR(50) PRIMARY KEY,
            permissions JSON NOT NULL,
            is_builtin TINYINT(1) DEFAULT 0,
            description TEXT
        )
        """,
    ]
    # Billing tables (usage metering and invoicing)
    billing_tables = [
        """
        CREATE TABLE IF NOT EXISTS usage_records (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            org_id VARCHAR(36) NOT NULL,
            project_id VARCHAR(36),
            instance_id VARCHAR(255) NOT NULL,
            instance_name VARCHAR(255),
            provider VARCHAR(50) DEFAULT 'docker',
            cpu_cores DECIMAL(6,2) DEFAULT 0,
            memory_mb INT DEFAULT 0,
            storage_gb INT DEFAULT 0,
            network_rx_bytes BIGINT DEFAULT 0,
            network_tx_bytes BIGINT DEFAULT 0,
            collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_org (org_id),
            INDEX idx_collected (collected_at)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS invoices (
            id VARCHAR(36) PRIMARY KEY,
            org_id VARCHAR(36) NOT NULL,
            org_name VARCHAR(255) NOT NULL,
            period_start TIMESTAMP NOT NULL,
            period_end TIMESTAMP NOT NULL,
            subtotal DECIMAL(12,2) DEFAULT 0,
            discount DECIMAL(12,2) DEFAULT 0,
            tax_rate DECIMAL(5,4) DEFAULT 0,
            tax_amount DECIMAL(12,2) DEFAULT 0,
            total DECIMAL(12,2) DEFAULT 0,
            currency VARCHAR(3) DEFAULT 'USD',
            status VARCHAR(20) DEFAULT 'draft',
            paid_at TIMESTAMP NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_org_status (org_id, status)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS invoice_line_items (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            invoice_id VARCHAR(36) NOT NULL,
            description VARCHAR(255) NOT NULL,
            quantity DECIMAL(14,4) DEFAULT 0,
            unit VARCHAR(50) DEFAULT '',
            unit_price DECIMAL(12,6) DEFAULT 0,
            total DECIMAL(12,2) DEFAULT 0,
            metric VARCHAR(50) DEFAULT '',
            FOREIGN KEY (invoice_id) REFERENCES invoices(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS pricing_tiers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            org_id VARCHAR(36),
            metric VARCHAR(50) NOT NULL,
            unit_price DECIMAL(12,6) NOT NULL,
            effective_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY uk_org_metric (org_id, metric)
        )
        """,
    ]
    # Region / federation tables (multi-datacenter support)
    region_tables = [
        """
        CREATE TABLE IF NOT EXISTS regions (
            id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            display_name VARCHAR(255),
            status VARCHAR(20) DEFAULT 'active',
            labels JSON,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS datacenters (
            id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            region_id VARCHAR(36) NOT NULL,
            location VARCHAR(255),
            provider VARCHAR(50) DEFAULT 'docker',
            status VARCHAR(20) DEFAULT 'active',
            total_cpu_cores DECIMAL(8,2) DEFAULT 0,
            total_memory_mb BIGINT DEFAULT 0,
            total_storage_gb BIGINT DEFAULT 0,
            used_cpu_cores DECIMAL(8,2) DEFAULT 0,
            used_memory_mb BIGINT DEFAULT 0,
            used_storage_gb BIGINT DEFAULT 0,
            labels JSON,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (region_id) REFERENCES regions(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS federation_peers (
            id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            api_url VARCHAR(512) NOT NULL,
            api_token VARCHAR(512),
            status VARCHAR(20) DEFAULT 'unknown',
            version VARCHAR(50),
            labels JSON,
            last_seen TIMESTAMP NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
    ]
    tables.extend(rbac_tables)
    tables.extend(billing_tables)
    tables.extend(region_tables)

    for table in tables:
        try:
            cursor.execute(table)
        except Exception as exc:
            logger.error("Error creating table: %s", exc)

    conn.commit()
    cursor.close()
    conn.close()


async def notify_integration(event_type: str, data: Dict[str, Any]) -> bool:
    """Send a server event notification to the integration service.

    Args:
        event_type: The type of event (e.g. ``server_created``).
        data: Event payload data.

    Returns:
        ``True`` if the notification was sent successfully.
    """
    payload = {
        "event_type": event_type,
        "server_name": data.get("server_name"),
        "details": data,
    }
    success, _ = _send_request(
        "POST", "/api/notifications/server-event", payload
    )
    return success


async def notify_server_created(server_id: str, server_name: str) -> bool:
    """Notify that a server was created."""
    data = {
        "server_id": server_id,
        "server_name": server_name,
        "service": "orchestrator",
    }
    return await notify_integration("server_created", data)


async def notify_server_started(server_id: str, server_name: str) -> bool:
    """Notify that a server was started."""
    data = {
        "server_id": server_id,
        "server_name": server_name,
        "service": "orchestrator",
    }
    return await notify_integration("server_started", data)


async def notify_server_stopped(server_id: str, server_name: str) -> bool:
    """Notify that a server was stopped."""
    data = {
        "server_id": server_id,
        "server_name": server_name,
        "service": "orchestrator",
    }
    return await notify_integration("server_stopped", data)


async def notify_server_deleted(server_id: str, server_name: str) -> bool:
    """Notify that a server was deleted."""
    data = {
        "server_id": server_id,
        "server_name": server_name,
        "service": "orchestrator",
    }
    return await notify_integration("server_deleted", data)


async def sync_user_to_integration(
    user_id: str, email: str, username: str
) -> Dict[str, Any]:
    """Synchronise a user record to the integration service.

    Args:
        user_id: The Discord user ID.
        email: The user's email address.
        username: The user's display name.

    Returns:
        The API response dict, or an empty dict on failure.
    """
    payload = {"email": email, "username": username, "discord_id": user_id}
    success, response = _send_request("POST", "/api/users", payload)
    return response or {}


async def get_unified_metrics() -> Dict[str, Any]:
    """Fetch unified dashboard metrics from the integration service.

    Returns:
        The metrics response dict, or an empty dict on failure.
    """
    success, response = _send_request("GET", "/api/metrics/dashboard")
    return response or {}


async def broadcast_notification(
    message: str, title: str = "Notification"
) -> bool:
    """Broadcast a notification through the integration service.

    Args:
        message: The notification body.
        title: The notification title.

    Returns:
        ``True`` if broadcast was successful.
    """
    payload = {"content": message, "title": title}
    success, _ = _send_request("POST", "/api/notifications", payload)
    return success
