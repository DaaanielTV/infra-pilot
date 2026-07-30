"""HTTP API client for the Infra Pilot backend.

Provides the ``ApiClient`` class with full coverage of all API endpoints.
"""

import json
import logging
from typing import Any, Dict, List, Optional

import requests

from .core.exceptions import APIError, AuthenticationError, ConnectionError

logger = logging.getLogger(__name__)

API_PREFIX = "/api/v1"
DEFAULT_TIMEOUT = 30


class ApiClient:
    """HTTP API client for Infra Pilot backend.

    Maintains full backward compatibility with existing ``cmd_*`` functions
    while adding session management and better error handling.

    Args:
        base_url: The base URL of the API server.
        token: Optional bearer token for authenticated requests.
    """

    def __init__(self, base_url: str, token: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def _headers(self) -> Dict[str, str]:
        """Return a copy of the current session headers.

        Returns:
            A dictionary of HTTP headers.
        """
        return dict(self.session.headers)

    def _request(
        self,
        method: str,
        path: str,
        data: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Send an HTTP request to the API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH).
            path: API endpoint path (appended to ``/api/v1``).
            data: Optional JSON-serialisable request body.

        Returns:
            The parsed JSON response, or an error dict on failure.
        """
        url = f"{self.base_url}{API_PREFIX}{path}"
        try:
            resp = self.session.request(
                method, url, json=data, timeout=DEFAULT_TIMEOUT
            )
            resp.raise_for_status()
            if resp.content:
                return resp.json()
            return {}
        except requests.HTTPError as exc:
            try:
                msg = exc.response.json().get("message", str(exc))
            except (json.JSONDecodeError, AttributeError):
                msg = str(exc)
            logger.warning("HTTP error %s: %s", exc.response.status_code, msg)
            return {"error": msg}
        except requests.ConnectionError as exc:
            logger.warning("Connection failed: %s", exc)
            return {"error": f"Connection failed: {exc}"}
        except requests.Timeout:
            logger.warning("Request timed out: %s %s", method, path)
            return {"error": "Request timed out"}

    def _get(self, path: str) -> Any:
        """Send a GET request.

        Args:
            path: API endpoint path.

        Returns:
            The parsed JSON response.
        """
        return self._request("GET", path)

    def _post(
        self, path: str, data: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Send a POST request.

        Args:
            path: API endpoint path.
            data: Optional JSON payload.

        Returns:
            The parsed JSON response.
        """
        return self._request("POST", path, data)

    def _put(
        self, path: str, data: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Send a PUT request.

        Args:
            path: API endpoint path.
            data: Optional JSON payload.

        Returns:
            The parsed JSON response.
        """
        return self._request("PUT", path, data)

    def _delete(self, path: str) -> Any:
        """Send a DELETE request.

        Args:
            path: API endpoint path.

        Returns:
            The parsed JSON response.
        """
        return self._request("DELETE", path)

    # ------------------------------------------------------------------
    # Authentication
    # ------------------------------------------------------------------

    def login(self, api_key: str) -> Any:
        """Authenticate with an API key.

        Args:
            api_key: The API key to authenticate with.

        Returns:
            Response data containing a ``token`` on success.
        """
        return self._request("POST", "/auth/login", {"api_key": api_key})

    def logout(self) -> Any:
        """Invalidate the current session.

        Returns:
            Response data.
        """
        return self._request("POST", "/auth/logout")

    # ------------------------------------------------------------------
    # Server management
    # ------------------------------------------------------------------

    def list_servers(self) -> Any:
        """List all servers."""
        return self._request("GET", "/servers")

    def get_server(self, server_id: str) -> Any:
        """Get details for a specific server.

        Args:
            server_id: The server ID.

        Returns:
            Server details.
        """
        return self._request("GET", f"/servers/{server_id}")

    def create_server(
        self,
        name: str,
        server_type: str,
        memory: Optional[int] = None,
    ) -> Any:
        """Create a new server.

        Args:
            name: Server name.
            server_type: Server type identifier.
            memory: Optional memory limit in MB.

        Returns:
            Created server details.
        """
        return self._request(
            "POST",
            "/servers",
            {"name": name, "type": server_type, "memory": memory},
        )

    def delete_server(self, server_id: str) -> Any:
        """Delete a server.

        Args:
            server_id: The server ID.
        """
        return self._request("DELETE", f"/servers/{server_id}")

    def server_status(self, server_id: str) -> Any:
        """Get server status.

        Args:
            server_id: The server ID.
        """
        return self._request("GET", f"/servers/{server_id}/status")

    def get_logs(
        self, server_id: str, lines: int = 50, follow: bool = False
    ) -> Any:
        """Fetch server logs.

        Args:
            server_id: The server ID.
            lines: Number of log lines to return.
            follow: Whether to follow (stream) log output.
        """
        return self._request(
            "GET",
            f"/servers/{server_id}/logs?lines={lines}&follow={follow}",
        )

    def list_backups(self, server_id: Optional[str] = None) -> Any:
        """List backups for a server or all backups.

        Args:
            server_id: Optional server ID to filter by.
        """
        path = f"/backups/{server_id}" if server_id else "/backups"
        return self._request("GET", path)

    def create_backup(self, server_id: str) -> Any:
        """Create a backup of a server.

        Args:
            server_id: The server ID.
        """
        return self._request("POST", f"/servers/{server_id}/backups")

    def deploy(self, server_id: str, branch: str) -> Any:
        """Deploy a branch to a server.

        Args:
            server_id: The server ID.
            branch: The branch name to deploy.
        """
        return self._request(
            "POST",
            f"/servers/{server_id}/deploy",
            {"branch": branch},
        )

    def health_check(self) -> Any:
        """Check API health."""
        return self._request("GET", "/health")

    # ------------------------------------------------------------------
    # Edge devices
    # ------------------------------------------------------------------

    def list_edge_devices(
        self,
        device_type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Any:
        """List edge devices.

        Args:
            device_type: Optional filter by device type.
            status: Optional filter by status.
        """
        params = {}
        if device_type:
            params["device_type"] = device_type
        if status:
            params["status"] = status
        qs = requests.compat.urlencode(params)
        return self._request("GET", f"/edge/devices?{qs}")

    def register_edge_device(
        self, name: str, device_type: str, hardware_id: str
    ) -> Any:
        """Register a new edge device.

        Args:
            name: Device name.
            device_type: Device type identifier.
            hardware_id: MAC or serial number.
        """
        return self._request(
            "POST",
            "/edge/devices",
            {
                "name": name,
                "device_type": device_type,
                "hardware_id": hardware_id,
            },
        )

    def edge_device_status(self, device_id: str) -> Any:
        """Get edge device status.

        Args:
            device_id: The device ID.
        """
        return self._request("GET", f"/edge/devices/{device_id}")

    def edge_device_command(self, device_id: str, command: str) -> Any:
        """Send a command to an edge device.

        Args:
            device_id: The device ID.
            command: The command to execute.
        """
        return self._request(
            "POST",
            f"/edge/devices/{device_id}/command",
            {"command": command},
        )

    def backup_edge_device(self, device_id: str) -> Any:
        """Backup an edge device.

        Args:
            device_id: The device ID.
        """
        return self._request("POST", f"/edge/devices/{device_id}/backup")

    def list_edge_functions(
        self, device_id: Optional[str] = None
    ) -> Any:
        """List edge functions.

        Args:
            device_id: Optional filter by device.
        """
        path = (
            f"/edge/functions?device_id={device_id}"
            if device_id
            else "/edge/functions"
        )
        return self._request("GET", path)

    def deploy_edge_function(
        self,
        name: str,
        runtime: str,
        device_id: str,
        source: str,
        handler: str,
    ) -> Any:
        """Deploy an edge function.

        Args:
            name: Function name.
            runtime: Runtime type (wasm, container, native).
            device_id: Target device ID.
            source: Function source URL.
            handler: Entry handler name.
        """
        return self._request(
            "POST",
            "/edge/functions",
            {
                "name": name,
                "runtime": runtime,
                "device_id": device_id,
                "source": source,
                "handler": handler,
            },
        )

    def invoke_edge_function(
        self, func_id: str, payload: Optional[str] = None
    ) -> Any:
        """Invoke an edge function.

        Args:
            func_id: Function ID.
            payload: Optional JSON payload string.
        """
        return self._request(
            "POST",
            f"/edge/functions/{func_id}/invoke",
            {"payload": payload},
        )

    def list_ml_models(self, device_id: Optional[str] = None) -> Any:
        """List ML models.

        Args:
            device_id: Optional filter by device.
        """
        path = (
            f"/edge/ml/models?device_id={device_id}"
            if device_id
            else "/edge/ml/models"
        )
        return self._request("GET", path)

    def deploy_ml_model(
        self,
        name: str,
        model_format: str,
        device_id: str,
        version: str,
    ) -> Any:
        """Deploy an ML model to an edge device.

        Args:
            name: Model name.
            model_format: Format (tflite, onnx, pytorch).
            device_id: Target device ID.
            version: Model version string.
        """
        return self._request(
            "POST",
            "/edge/ml/models",
            {
                "name": name,
                "format": model_format,
                "device_id": device_id,
                "version": version,
            },
        )

    def run_inference(self, model_id: str) -> Any:
        """Run inference on a deployed ML model.

        Args:
            model_id: The model ID.
        """
        return self._request(
            "POST", f"/edge/ml/models/{model_id}/infer"
        )

    # ------------------------------------------------------------------
    # IoT provisioning
    # ------------------------------------------------------------------

    def generate_claim_codes(
        self, count: int = 10, ttl: int = 24
    ) -> Any:
        """Generate IoT device claim codes.

        Args:
            count: Number of codes to generate.
            ttl: Time-to-live in hours.
        """
        return self._request(
            "POST", "/iot/claim-codes", {"count": count, "ttl": ttl}
        )

    def enroll_device(self, code: str, device_id: str) -> Any:
        """Enroll an IoT device using a claim code.

        Args:
            code: The claim code.
            device_id: The device ID.
        """
        return self._request(
            "POST",
            "/iot/enroll",
            {"code": code, "device_id": device_id},
        )

    # ------------------------------------------------------------------
    # Edge CDN
    # ------------------------------------------------------------------

    def cdn_stats(self) -> Any:
        """Get CDN statistics."""
        return self._request("GET", "/edge/cdn/stats")

    # ------------------------------------------------------------------
    # Mesh networking
    # ------------------------------------------------------------------

    def list_mesh_networks(self) -> Any:
        """List mesh networks."""
        return self._request("GET", "/edge/mesh")

    def create_mesh_network(
        self, name: str, mesh_type: str, subnet: str
    ) -> Any:
        """Create a mesh network.

        Args:
            name: Network name.
            mesh_type: Mesh type (wireguard, tinc).
            subnet: Subnet CIDR.
        """
        return self._request(
            "POST",
            "/edge/mesh",
            {"name": name, "mesh_type": mesh_type, "subnet": subnet},
        )

    # ------------------------------------------------------------------
    # LoRaWAN gateways
    # ------------------------------------------------------------------

    def list_lorawan_gateways(
        self, status: Optional[str] = None
    ) -> Any:
        """List LoRaWAN gateways.

        Args:
            status: Optional filter by status.
        """
        path = (
            f"/edge/lorawan/gateways?status={status}"
            if status
            else "/edge/lorawan/gateways"
        )
        return self._request("GET", path)

    # ------------------------------------------------------------------
    # IoT pipeline
    # ------------------------------------------------------------------

    def pipeline_stats(self) -> Any:
        """Get IoT pipeline statistics."""
        return self._request("GET", "/edge/pipeline/stats")

    # ------------------------------------------------------------------
    # Energy management
    # ------------------------------------------------------------------

    def energy_current(self) -> Any:
        """Get current energy consumption snapshot."""
        return self._request("GET", "/energy/current")

    def energy_history(
        self,
        server_id: Optional[str] = None,
        hours: int = 24,
    ) -> Any:
        """Get historical energy consumption data.

        Args:
            server_id: Optional server filter.
            hours: Look-back window in hours.
        """
        params = f"?hours={hours}"
        if server_id:
            params += f"&server_id={server_id}"
        return self._request("GET", f"/energy/history{params}")

    def energy_summary(self, period: str = "daily") -> Any:
        """Get energy consumption summary.

        Args:
            period: Aggregation period (daily, weekly, monthly).
        """
        return self._request(
            "GET", f"/energy/summary?period={period}"
        )

    # ------------------------------------------------------------------
    # Carbon footprint
    # ------------------------------------------------------------------

    def carbon_current(self) -> Any:
        """Get current CO2 output."""
        return self._request("GET", "/carbon/current")

    def carbon_history(self) -> Any:
        """Get historical CO2 data."""
        return self._request("GET", "/carbon/history")

    # ------------------------------------------------------------------
    # Green scheduling
    # ------------------------------------------------------------------

    def green_forecast(self) -> Any:
        """Get carbon-aware scheduling forecast."""
        return self._request("GET", "/green/forecast")

    def green_jobs(self) -> Any:
        """List green computing jobs."""
        return self._request("GET", "/green/jobs")

    def green_schedule(
        self, workload_id: str, schedule_type: str
    ) -> Any:
        """Schedule a green computing job.

        Args:
            workload_id: Workload identifier.
            schedule_type: Schedule type.
        """
        return self._request(
            "POST",
            "/green/schedule",
            {"workload_id": workload_id, "schedule_type": schedule_type},
        )

    def green_report(self) -> Any:
        """Get green savings report."""
        return self._request("GET", "/green/report")

    # ------------------------------------------------------------------
    # Resource reclamation
    # ------------------------------------------------------------------

    def reclaim_list(self) -> Any:
        """List idle reclaimable resources."""
        return self._request("GET", "/reclaim/resources")

    def reclaim_scan(self) -> Any:
        """Scan for idle resources."""
        return self._request("POST", "/reclaim/scan")

    def reclaim_report(self) -> Any:
        """Get reclamation report."""
        return self._request("GET", "/reclaim/report")

    # ------------------------------------------------------------------
    # Auto-shutdown policies
    # ------------------------------------------------------------------

    def shutdown_policies(self) -> Any:
        """List auto-shutdown policies."""
        return self._request("GET", "/shutdown/policies")

    def create_shutdown_policy(
        self, name: str, schedule: str, conditions: Any
    ) -> Any:
        """Create an auto-shutdown policy.

        Args:
            name: Policy name.
            schedule: Schedule expression.
            conditions: Policy conditions.
        """
        return self._request(
            "POST",
            "/shutdown/policies",
            {"name": name, "schedule": schedule, "conditions": conditions},
        )

    def shutdown_savings(self) -> Any:
        """Get savings from auto-shutdown policies."""
        return self._request("GET", "/shutdown/savings")

    # ------------------------------------------------------------------
    # Hardware lifecycle
    # ------------------------------------------------------------------

    def list_hardware(self) -> Any:
        """List hardware assets."""
        return self._request("GET", "/hardware")

    def add_hardware(
        self, name: str, hardware_type: str, specs: Any
    ) -> Any:
        """Add a hardware asset.

        Args:
            name: Asset name.
            hardware_type: Asset type.
            specs: Asset specifications.
        """
        return self._request(
            "POST",
            "/hardware",
            {"name": name, "type": hardware_type, "specs": specs},
        )

    # ------------------------------------------------------------------
    # PUE / DCIM
    # ------------------------------------------------------------------

    def pue_current(self) -> Any:
        """Get current PUE metrics."""
        return self._request("GET", "/pue/current")

    def pue_history(self) -> Any:
        """Get PUE history."""
        return self._request("GET", "/pue/history")

    # ------------------------------------------------------------------
    # Provider rankings
    # ------------------------------------------------------------------

    def provider_rank(self) -> Any:
        """Get sustainable provider rankings."""
        return self._request("GET", "/provider/rank")

    # ------------------------------------------------------------------
    # CO2 offset
    # ------------------------------------------------------------------

    def offset_quote(self, amount: float) -> Any:
        """Get a CO2 offset quote.

        Args:
            amount: Energy consumption in kWh.
        """
        return self._request(
            "POST", "/offset/quote", {"amount": amount}
        )

    def offset_purchase(self, amount: float, provider: str) -> Any:
        """Purchase a CO2 offset.

        Args:
            amount: Offset amount.
            provider: Project provider.
        """
        return self._request(
            "POST",
            "/offset/purchase",
            {"amount": amount, "provider": provider},
        )

    def offset_certs(self) -> Any:
        """List offset certificates."""
        return self._request("GET", "/offset/certificates")

    # ------------------------------------------------------------------
    # Efficiency scorecards
    # ------------------------------------------------------------------

    def efficiency_score(self) -> Any:
        """Get efficiency score."""
        return self._request("GET", "/efficiency/score")

    def efficiency_recommendations(self) -> Any:
        """Get efficiency recommendations."""
        return self._request("GET", "/efficiency/recommendations")

    # ------------------------------------------------------------------
    # OIDC / Identity
    # ------------------------------------------------------------------

    def oidc_clients(self) -> Any:
        """List OIDC clients."""
        return self._request("GET", "/identity/oidc/clients")

    def oidc_register(
        self, name: str, redirect_uris: List[str]
    ) -> Any:
        """Register an OIDC client.

        Args:
            name: Client name.
            redirect_uris: List of allowed redirect URIs.
        """
        return self._request(
            "POST",
            "/identity/oidc/clients",
            {"name": name, "redirect_uris": redirect_uris},
        )

    def oidc_delete(self, client_id: str) -> Any:
        """Delete an OIDC client.

        Args:
            client_id: Client ID.
        """
        return self._request(
            "DELETE", f"/identity/oidc/clients/{client_id}"
        )

    def webauthn_credentials(self) -> Any:
        """List WebAuthn credentials."""
        return self._request("GET", "/identity/webauthn/credentials")

    def webauthn_remove(self, credential_id: str) -> Any:
        """Remove a WebAuthn credential.

        Args:
            credential_id: Credential ID.
        """
        return self._request(
            "DELETE",
            f"/identity/webauthn/credentials/{credential_id}",
        )

    def list_sessions(self) -> Any:
        """List active sessions."""
        return self._request("GET", "/identity/sessions")

    def revoke_session(self, session_id: str) -> Any:
        """Revoke a session.

        Args:
            session_id: Session ID.
        """
        return self._request(
            "DELETE", f"/identity/sessions/{session_id}"
        )

    def pam_requests(self) -> Any:
        """List PAM access requests."""
        return self._request("GET", "/identity/pam/requests")

    def pam_request(self, resource: str, reason: str) -> Any:
        """Create a PAM access request.

        Args:
            resource: Target resource.
            reason: Reason for access.
        """
        return self._request(
            "POST",
            "/identity/pam/requests",
            {"resource": resource, "reason": reason},
        )

    def pam_approve(self, request_id: str) -> Any:
        """Approve a PAM request.

        Args:
            request_id: Request ID.
        """
        return self._request(
            "POST",
            f"/identity/pam/requests/{request_id}/approve",
        )

    def pam_deny(self, request_id: str) -> Any:
        """Deny a PAM request.

        Args:
            request_id: Request ID.
        """
        return self._request(
            "POST",
            f"/identity/pam/requests/{request_id}/deny",
        )

    def breach_list(self) -> Any:
        """List breach notifications."""
        return self._request("GET", "/governance/breaches")

    def breach_report(self, breach_id: str, details: Any) -> Any:
        """Report a breach.

        Args:
            breach_id: Breach identifier.
            details: Breach details.
        """
        return self._request(
            "POST",
            f"/governance/breaches/{breach_id}/report",
            details,
        )

    # ------------------------------------------------------------------
    # Policy as code
    # ------------------------------------------------------------------

    def policy_list(self) -> Any:
        """List policies."""
        return self._request("GET", "/governance/policies")

    def policy_create(self, name: str, rules: Any) -> Any:
        """Create a policy.

        Args:
            name: Policy name.
            rules: Policy rules.
        """
        return self._request(
            "POST",
            "/governance/policies",
            {"name": name, "rules": rules},
        )

    def policy_evaluate(
        self, policy_id: str, resource: str
    ) -> Any:
        """Evaluate a policy against a resource.

        Args:
            policy_id: Policy ID.
            resource: Resource to evaluate.
        """
        return self._request(
            "POST",
            f"/governance/policies/{policy_id}/evaluate",
            {"resource": resource},
        )

    # ------------------------------------------------------------------
    # Compliance
    # ------------------------------------------------------------------

    def compliance_scan(self, framework: str) -> Any:
        """Run a compliance scan.

        Args:
            framework: Benchmark framework (e.g. cis_docker).
        """
        return self._request(
            "POST",
            "/governance/compliance/scan",
            {"framework": framework},
        )

    def compliance_report(self, scan_id: str) -> Any:
        """Get a compliance scan report.

        Args:
            scan_id: Scan ID.
        """
        return self._request(
            "GET", f"/governance/compliance/report/{scan_id}"
        )

    def compliance_checks(self) -> Any:
        """List available compliance checks."""
        return self._request("GET", "/governance/compliance/checks")

    # ------------------------------------------------------------------
    # Audit analytics
    # ------------------------------------------------------------------

    def audit_anomalies(self) -> Any:
        """List audit anomalies."""
        return self._request("GET", "/governance/audit/anomalies")

    def audit_trend(self) -> Any:
        """Get audit anomaly trend."""
        return self._request("GET", "/governance/audit/trend")

    def audit_summary(self) -> Any:
        """Get audit summary."""
        return self._request("GET", "/governance/audit/summary")

    # ------------------------------------------------------------------
    # Data classification
    # ------------------------------------------------------------------

    def classify_scan(self) -> Any:
        """Scan text for sensitive data."""
        return self._request("POST", "/governance/classify/scan")

    def classify_inventory(self) -> Any:
        """List data inventory."""
        return self._request("GET", "/governance/classify/inventory")

    # ------------------------------------------------------------------
    # Vendor risk
    # ------------------------------------------------------------------

    def vendor_list(self) -> Any:
        """List vendors."""
        return self._request("GET", "/governance/vendors")

    def vendor_create(self, name: str, risk_level: str) -> Any:
        """Register a vendor.

        Args:
            name: Vendor name.
            risk_level: Risk level.
        """
        return self._request(
            "POST",
            "/governance/vendors",
            {"name": name, "risk_level": risk_level},
        )

    def vendor_assess(self, vendor_id: str) -> Any:
        """Create a vendor assessment.

        Args:
            vendor_id: Vendor ID.
        """
        return self._request(
            "POST", f"/governance/vendors/{vendor_id}/assess"
        )

    # ------------------------------------------------------------------
    # Workflow automation
    # ------------------------------------------------------------------

    def workflow_list(self) -> Any:
        """List workflows."""
        return self._request("GET", "/orchestration/workflows")

    def workflow_create(self, name: str, steps: List[Any]) -> Any:
        """Create a workflow.

        Args:
            name: Workflow name.
            steps: List of workflow steps.
        """
        return self._request(
            "POST",
            "/orchestration/workflows",
            {"name": name, "steps": steps},
        )

    def workflow_run(
        self,
        workflow_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Execute a workflow.

        Args:
            workflow_id: Workflow ID.
            params: Optional parameters.
        """
        return self._request(
            "POST",
            f"/orchestration/workflows/{workflow_id}/run",
            params or {},
        )

    def infra_pipeline_list(self) -> Any:
        """List CI/CD pipelines."""
        return self._request("GET", "/orchestration/pipelines")

    def infra_pipeline_run(self, pipeline_id: str) -> Any:
        """Run a CI/CD pipeline.

        Args:
            pipeline_id: Pipeline ID.
        """
        return self._request(
            "POST", f"/orchestration/pipelines/{pipeline_id}/run"
        )

    # ------------------------------------------------------------------
    # Drift detection
    # ------------------------------------------------------------------

    def drift_scan(self) -> Any:
        """Run a configuration drift scan."""
        return self._request("POST", "/orchestration/drift/scan")

    def drift_list(self) -> Any:
        """List drift scan results."""
        return self._request("GET", "/orchestration/drift")

    # ------------------------------------------------------------------
    # Resource quotas
    # ------------------------------------------------------------------

    def quota_list(self) -> Any:
        """List resource quotas."""
        return self._request("GET", "/orchestration/quotas")

    def quota_check(self, resource: str) -> Any:
        """Check a specific quota.

        Args:
            resource: Resource type/ID.
        """
        return self._request(
            "GET", f"/orchestration/quotas/{resource}"
        )

    # ------------------------------------------------------------------
    # Auto-remediation
    # ------------------------------------------------------------------

    def remediate_rules(self) -> Any:
        """List remediation rules."""
        return self._request("GET", "/orchestration/remediation/rules")

    def remediate_history(self) -> Any:
        """List remediation history."""
        return self._request("GET", "/orchestration/remediation/history")

    # ------------------------------------------------------------------
    # Maintenance scheduling
    # ------------------------------------------------------------------

    def maintenance_list(self) -> Any:
        """List maintenance windows."""
        return self._request("GET", "/orchestration/maintenance")

    def maintenance_schedule(
        self, resource: str, window: str
    ) -> Any:
        """Schedule a maintenance window.

        Args:
            resource: Target resource.
            window: Maintenance window spec.
        """
        return self._request(
            "POST",
            "/orchestration/maintenance",
            {"resource": resource, "window": window},
        )

    # ------------------------------------------------------------------
    # Runbook templates
    # ------------------------------------------------------------------

    def runbook_list(self) -> Any:
        """List runbook templates."""
        return self._request("GET", "/orchestration/runbooks")

    def runbook_use(
        self,
        runbook_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Execute a runbook template.

        Args:
            runbook_id: Template ID.
            params: Optional execution parameters.
        """
        return self._request(
            "POST",
            f"/orchestration/runbooks/{runbook_id}/execute",
            params or {},
        )

    # ------------------------------------------------------------------
    # Chaos engineering
    # ------------------------------------------------------------------

    def chaos_experiments(self) -> Any:
        """List chaos experiments."""
        return self._request("GET", "/orchestration/chaos/experiments")

    def chaos_create(
        self, name: str, fault_type: str, target: str
    ) -> Any:
        """Create a chaos experiment.

        Args:
            name: Experiment name.
            fault_type: Type of fault to inject.
            target: Target resource.
        """
        return self._request(
            "POST",
            "/orchestration/chaos/experiments",
            {"name": name, "fault_type": fault_type, "target": target},
        )

    def chaos_run(self, experiment_id: str) -> Any:
        """Run a chaos experiment.

        Args:
            experiment_id: Experiment ID.
        """
        return self._request(
            "POST",
            f"/orchestration/chaos/experiments/{experiment_id}/run",
        )

    def chaos_stop(self, experiment_id: str) -> Any:
        """Stop a chaos experiment.

        Args:
            experiment_id: Experiment ID.
        """
        return self._request(
            "POST",
            f"/orchestration/chaos/experiments/{experiment_id}/stop",
        )

    def chaos_faults(self) -> Any:
        """List available fault types."""
        return self._request("GET", "/orchestration/chaos/faults")

    # ------------------------------------------------------------------
    # Self-healing
    # ------------------------------------------------------------------

    def heal_status(self) -> Any:
        """Get self-healing system status."""
        return self._request("GET", "/orchestration/heal/status")

    def heal_history(self) -> Any:
        """Get self-healing history."""
        return self._request("GET", "/orchestration/heal/history")

    def heal_retrain(self) -> Any:
        """Trigger self-healing model retrain."""
        return self._request("POST", "/orchestration/heal/retrain")

    # ------------------------------------------------------------------
    # SD-WAN
    # ------------------------------------------------------------------

    def sdwan_status(self) -> Any:
        """Get SD-WAN status."""
        return self._request("GET", "/networking/sdwan/status")

    def sdwan_apps(self) -> Any:
        """List SD-WAN applications."""
        return self._request("GET", "/networking/sdwan/apps")

    def sdwan_create(
        self, name: str, provider: str, bandwidth: int
    ) -> Any:
        """Create an SD-WAN link.

        Args:
            name: Link name.
            provider: Provider name.
            bandwidth: Bandwidth in Mbps.
        """
        return self._request(
            "POST",
            "/networking/sdwan/links",
            {"name": name, "provider": provider, "bandwidth": bandwidth},
        )

    def sdwan_delete(self, link_id: str) -> Any:
        """Delete an SD-WAN link.

        Args:
            link_id: Link ID.
        """
        return self._request(
            "DELETE", f"/networking/sdwan/links/{link_id}"
        )

    def sdwan_toggle(self, link_id: str) -> Any:
        """Toggle an SD-WAN link on/off.

        Args:
            link_id: Link ID.
        """
        return self._request(
            "POST",
            f"/networking/sdwan/links/{link_id}/toggle",
        )

    # ------------------------------------------------------------------
    # VPN management
    # ------------------------------------------------------------------

    def vpn_configs(self) -> Any:
        """List VPN configurations."""
        return self._request("GET", "/networking/vpn/configs")

    def vpn_create(
        self, name: str, protocol: str, server: str
    ) -> Any:
        """Create a VPN configuration.

        Args:
            name: Config name.
            protocol: VPN protocol.
            server: VPN server address.
        """
        return self._request(
            "POST",
            "/networking/vpn/configs",
            {"name": name, "protocol": protocol, "server": server},
        )

    def vpn_delete(self, config_id: str) -> Any:
        """Delete a VPN configuration.

        Args:
            config_id: Config ID.
        """
        return self._request(
            "DELETE", f"/networking/vpn/configs/{config_id}"
        )

    def vpn_status(self, config_id: str) -> Any:
        """Get VPN connection status.

        Args:
            config_id: Config ID.
        """
        return self._request(
            "GET", f"/networking/vpn/configs/{config_id}"
        )

    # ------------------------------------------------------------------
    # DNS management
    # ------------------------------------------------------------------

    def dns_zones(self) -> Any:
        """List DNS zones."""
        return self._request("GET", "/networking/dns/zones")

    def dns_create_zone(
        self, domain: str, ttl: int = 3600
    ) -> Any:
        """Create a DNS zone.

        Args:
            domain: Domain name.
            ttl: Default TTL in seconds.
        """
        return self._request(
            "POST",
            "/networking/dns/zones",
            {"domain": domain, "ttl": ttl},
        )

    def dns_delete_zone(self, zone_id: str) -> Any:
        """Delete a DNS zone.

        Args:
            zone_id: Zone ID.
        """
        return self._request(
            "DELETE", f"/networking/dns/zones/{zone_id}"
        )

    def dns_records(self, zone_id: str) -> Any:
        """List DNS records in a zone.

        Args:
            zone_id: Zone ID.
        """
        return self._request(
            "GET", f"/networking/dns/zones/{zone_id}/records"
        )

    def dns_add_record(
        self,
        zone_id: str,
        record_type: str,
        name: str,
        value: str,
        ttl: int = 300,
    ) -> Any:
        """Add a DNS record.

        Args:
            zone_id: Zone ID.
            record_type: Record type (A, AAAA, CNAME, MX, etc.).
            name: Record name.
            value: Record value.
            ttl: TTL in seconds.
        """
        return self._request(
            "POST",
            f"/networking/dns/zones/{zone_id}/records",
            {
                "type": record_type,
                "name": name,
                "value": value,
                "ttl": ttl,
            },
        )

    def dns_delete_record(
        self, zone_id: str, record_id: str
    ) -> Any:
        """Delete a DNS record.

        Args:
            zone_id: Zone ID.
            record_id: Record ID.
        """
        return self._request(
            "DELETE",
            f"/networking/dns/zones/{zone_id}/records/{record_id}",
        )

    # ------------------------------------------------------------------
    # BGP management
    # ------------------------------------------------------------------

    def bgp_sessions(self) -> Any:
        """List BGP sessions."""
        return self._request("GET", "/networking/bgp/sessions")

    def bgp_create(
        self, name: str, asn: int, neighbor: str
    ) -> Any:
        """Create a BGP session.

        Args:
            name: Session name.
            asn: Local ASN.
            neighbor: Neighbor IP.
        """
        return self._request(
            "POST",
            "/networking/bgp/sessions",
            {"name": name, "asn": asn, "neighbor": neighbor},
        )

    def bgp_delete(self, session_id: str) -> Any:
        """Delete a BGP session.

        Args:
            session_id: Session ID.
        """
        return self._request(
            "DELETE", f"/networking/bgp/sessions/{session_id}"
        )

    def bgp_routes(
        self, session_id: Optional[str] = None
    ) -> Any:
        """List BGP routes.

        Args:
            session_id: Optional session filter.
        """
        path = (
            f"/networking/bgp/routes/{session_id}"
            if session_id
            else "/networking/bgp/routes"
        )
        return self._request("GET", path)

    # ------------------------------------------------------------------
    # Proxy rules
    # ------------------------------------------------------------------

    def proxy_rules(self) -> Any:
        """List proxy rules."""
        return self._request("GET", "/networking/proxy/rules")

    def proxy_create(
        self, name: str, source: str, target: str
    ) -> Any:
        """Create a proxy rule.

        Args:
            name: Rule name.
            source: Source domain/path.
            target: Target URL.
        """
        return self._request(
            "POST",
            "/networking/proxy/rules",
            {"name": name, "source": source, "target": target},
        )

    def proxy_delete(self, rule_id: str) -> Any:
        """Delete a proxy rule.

        Args:
            rule_id: Rule ID.
        """
        return self._request(
            "DELETE", f"/networking/proxy/rules/{rule_id}"
        )

    def proxy_toggle(self, rule_id: str) -> Any:
        """Toggle a proxy rule on/off.

        Args:
            rule_id: Rule ID.
        """
        return self._request(
            "POST",
            f"/networking/proxy/rules/{rule_id}/toggle",
        )

    # ------------------------------------------------------------------
    # Network segmentation
    # ------------------------------------------------------------------

    def segment_list(self) -> Any:
        """List network segments."""
        return self._request("GET", "/networking/segments")

    def segment_create(
        self,
        name: str,
        cidr: str,
        vlan: Optional[int] = None,
    ) -> Any:
        """Create a network segment.

        Args:
            name: Segment name.
            cidr: CIDR notation.
            vlan: Optional VLAN ID.
        """
        return self._request(
            "POST",
            "/networking/segments",
            {"name": name, "cidr": cidr, "vlan": vlan},
        )

    def segment_delete(self, segment_id: str) -> Any:
        """Delete a network segment.

        Args:
            segment_id: Segment ID.
        """
        return self._request(
            "DELETE", f"/networking/segments/{segment_id}"
        )

    # ------------------------------------------------------------------
    # Packet capture
    # ------------------------------------------------------------------

    def capture_list(self) -> Any:
        """List packet captures."""
        return self._request("GET", "/networking/capture")

    def capture_start(
        self,
        interface: str,
        filter_expr: Optional[str] = None,
    ) -> Any:
        """Start a packet capture.

        Args:
            interface: Network interface.
            filter_expr: Optional BPF filter expression.
        """
        return self._request(
            "POST",
            "/networking/capture/start",
            {"interface": interface, "filter": filter_expr},
        )

    def capture_stop(self, capture_id: str) -> Any:
        """Stop a packet capture.

        Args:
            capture_id: Capture ID.
        """
        return self._request(
            "POST", f"/networking/capture/{capture_id}/stop"
        )

    # ------------------------------------------------------------------
    # DNS filtering
    # ------------------------------------------------------------------

    def dnsfilter_status(self) -> Any:
        """Get DNS filter status."""
        return self._request("GET", "/networking/dnsfilter/status")

    def dnsfilter_rules(self) -> Any:
        """List DNS filter rules."""
        return self._request("GET", "/networking/dnsfilter/rules")

    def dnsfilter_add(
        self, domain: str, action: str = "block"
    ) -> Any:
        """Add a DNS filter rule.

        Args:
            domain: Domain to filter.
            action: Action (block, allow).
        """
        return self._request(
            "POST",
            "/networking/dnsfilter/rules",
            {"domain": domain, "action": action},
        )

    def dnsfilter_remove(self, rule_id: str) -> Any:
        """Remove a DNS filter rule.

        Args:
            rule_id: Rule ID.
        """
        return self._request(
            "DELETE", f"/networking/dnsfilter/rules/{rule_id}"
        )

    # ------------------------------------------------------------------
    # DHCP
    # ------------------------------------------------------------------

    def dhcp_leases(self) -> Any:
        """List DHCP leases."""
        return self._request("GET", "/networking/dhcp/leases")

    # ------------------------------------------------------------------
    # Network cost
    # ------------------------------------------------------------------

    def netcost_show(self) -> Any:
        """Show network costs."""
        return self._request("GET", "/networking/cost")

    def netcost_budget(self, budget: float) -> Any:
        """Set network cost budget.

        Args:
            budget: Monthly budget amount.
        """
        return self._request(
            "POST",
            "/networking/cost/budget",
            {"budget": budget},
        )

    # ------------------------------------------------------------------
    # Cellular networks
    # ------------------------------------------------------------------

    def cell_networks(self) -> Any:
        """List cellular networks."""
        return self._request("GET", "/networking/cell/networks")

    def cell_register(
        self, name: str, provider: str, apn: str
    ) -> Any:
        """Register a cellular network.

        Args:
            name: Network name.
            provider: Provider name.
            apn: APN string.
        """
        return self._request(
            "POST",
            "/networking/cell/networks",
            {"name": name, "provider": provider, "apn": apn},
        )

    def cell_delete(self, network_id: str) -> Any:
        """Delete a cellular network.

        Args:
            network_id: Network ID.
        """
        return self._request(
            "DELETE", f"/networking/cell/networks/{network_id}"
        )

    def cell_status(self, network_id: str) -> Any:
        """Get cellular network status.

        Args:
            network_id: Network ID.
        """
        return self._request(
            "GET", f"/networking/cell/networks/{network_id}"
        )

    def cell_sims(self, network_id: str) -> Any:
        """List SIMs on a network.

        Args:
            network_id: Network ID.
        """
        return self._request(
            "GET", f"/networking/cell/networks/{network_id}/sims"
        )

    def cell_activate(self, sim_id: str) -> Any:
        """Activate a SIM.

        Args:
            sim_id: SIM ID.
        """
        return self._request(
            "POST", f"/networking/cell/sims/{sim_id}/activate"
        )

    def cell_deactivate(self, sim_id: str) -> Any:
        """Deactivate a SIM.

        Args:
            sim_id: SIM ID.
        """
        return self._request(
            "POST", f"/networking/cell/sims/{sim_id}/deactivate"
        )

    # ------------------------------------------------------------------
    # Marketplace - Trading
    # ------------------------------------------------------------------

    def trade_list(self) -> Any:
        """List resource trades."""
        return self._request("GET", "/marketplace/trades")

    def trade_create(
        self, resource: str, amount: float, price: float
    ) -> Any:
        """Create a resource trade listing.

        Args:
            resource: Resource type.
            amount: Quantity.
            price: Unit price.
        """
        return self._request(
            "POST",
            "/marketplace/trades",
            {"resource": resource, "amount": amount, "price": price},
        )

    def trade_accept(self, trade_id: str) -> Any:
        """Accept a trade.

        Args:
            trade_id: Trade ID.
        """
        return self._request(
            "POST", f"/marketplace/trades/{trade_id}/accept"
        )

    def trade_cancel(self, trade_id: str) -> Any:
        """Cancel a trade.

        Args:
            trade_id: Trade ID.
        """
        return self._request(
            "POST", f"/marketplace/trades/{trade_id}/cancel"
        )

    # ------------------------------------------------------------------
    # Marketplace - App marketplace
    # ------------------------------------------------------------------

    def appmarket_list(self) -> Any:
        """List marketplace apps."""
        return self._request("GET", "/marketplace/apps")

    def appmarket_install(
        self, app_id: str, target: str
    ) -> Any:
        """Install a marketplace app.

        Args:
            app_id: App ID.
            target: Target server.
        """
        return self._request(
            "POST",
            f"/marketplace/apps/{app_id}/install",
            {"target": target},
        )

    def appmarket_installations(self) -> Any:
        """List app installations."""
        return self._request("GET", "/marketplace/installations")

    # ------------------------------------------------------------------
    # Marketplace - Pay-per-use
    # ------------------------------------------------------------------

    def ppu_metrics(self) -> Any:
        """Get PPU metrics."""
        return self._request("GET", "/marketplace/ppu/metrics")

    def ppu_usage(self) -> Any:
        """Get PPU usage."""
        return self._request("GET", "/marketplace/ppu/usage")

    def ppu_budget(self) -> Any:
        """Get PPU budget."""
        return self._request("GET", "/marketplace/ppu/budget")

    # ------------------------------------------------------------------
    # Marketplace - Resellers
    # ------------------------------------------------------------------

    def reseller_list(self) -> Any:
        """List resellers."""
        return self._request("GET", "/marketplace/resellers")

    def reseller_create(
        self, name: str, email: str, commission: float
    ) -> Any:
        """Create a reseller.

        Args:
            name: Reseller name.
            email: Reseller email.
            commission: Commission rate.
        """
        return self._request(
            "POST",
            "/marketplace/resellers",
            {"name": name, "email": email, "commission": commission},
        )

    def reseller_delete(self, reseller_id: str) -> Any:
        """Delete a reseller.

        Args:
            reseller_id: Reseller ID.
        """
        return self._request(
            "DELETE", f"/marketplace/resellers/{reseller_id}"
        )

    def reseller_analytics(self, reseller_id: str) -> Any:
        """Get reseller analytics.

        Args:
            reseller_id: Reseller ID.
        """
        return self._request(
            "GET", f"/marketplace/resellers/{reseller_id}/analytics"
        )

    # ------------------------------------------------------------------
    # Marketplace - White-label
    # ------------------------------------------------------------------

    def whitelabel_settings(self) -> Any:
        """Get white-label settings."""
        return self._request("GET", "/marketplace/whitelabel")

    # ------------------------------------------------------------------
    # Marketplace - SLA management
    # ------------------------------------------------------------------

    def sla_list(self) -> Any:
        """List SLAs."""
        return self._request("GET", "/marketplace/sla")

    def sla_create(
        self,
        name: str,
        uptime: float,
        response_time: int,
    ) -> Any:
        """Create an SLA.

        Args:
            name: SLA name.
            uptime: Uptime percentage.
            response_time: Response time in seconds.
        """
        return self._request(
            "POST",
            "/marketplace/sla",
            {
                "name": name,
                "uptime": uptime,
                "response_time": response_time,
            },
        )

    def sla_delete(self, sla_id: str) -> Any:
        """Delete an SLA.

        Args:
            sla_id: SLA ID.
        """
        return self._request(
            "DELETE", f"/marketplace/sla/{sla_id}"
        )

    def sla_status(self, sla_id: str) -> Any:
        """Get SLA status.

        Args:
            sla_id: SLA ID.
        """
        return self._request("GET", f"/marketplace/sla/{sla_id}")

    # ------------------------------------------------------------------
    # Marketplace - Credits
    # ------------------------------------------------------------------

    def credit_list(self) -> Any:
        """List credits."""
        return self._request("GET", "/marketplace/credits")

    def credit_issue(
        self, customer_id: str, amount: float, reason: str
    ) -> Any:
        """Issue a credit.

        Args:
            customer_id: Customer ID.
            amount: Credit amount.
            reason: Reason for credit.
        """
        return self._request(
            "POST",
            "/marketplace/credits",
            {
                "customer_id": customer_id,
                "amount": amount,
                "reason": reason,
            },
        )

    # ------------------------------------------------------------------
    # Marketplace - Crypto
    # ------------------------------------------------------------------

    def crypto_wallets(self) -> Any:
        """List crypto wallets."""
        return self._request("GET", "/marketplace/crypto/wallets")

    def crypto_create_wallet(
        self, currency: str, label: str
    ) -> Any:
        """Create a crypto wallet.

        Args:
            currency: Cryptocurrency type.
            label: Wallet label.
        """
        return self._request(
            "POST",
            "/marketplace/crypto/wallets",
            {"currency": currency, "label": label},
        )

    def crypto_transactions(
        self, wallet_id: Optional[str] = None
    ) -> Any:
        """List crypto transactions.

        Args:
            wallet_id: Optional wallet filter.
        """
        path = (
            f"/marketplace/crypto/transactions/{wallet_id}"
            if wallet_id
            else "/marketplace/crypto/transactions"
        )
        return self._request("GET", path)

    def crypto_rates(self) -> Any:
        """Get crypto exchange rates."""
        return self._request("GET", "/marketplace/crypto/rates")

    # ------------------------------------------------------------------
    # Marketplace - Plans
    # ------------------------------------------------------------------

    def plans_list(self) -> Any:
        """List plans."""
        return self._request("GET", "/marketplace/plans")

    def plans_create(
        self, name: str, price: float, features: List[str]
    ) -> Any:
        """Create a plan.

        Args:
            name: Plan name.
            price: Plan price.
            features: List of features.
        """
        return self._request(
            "POST",
            "/marketplace/plans",
            {"name": name, "price": price, "features": features},
        )

    def plans_delete(self, plan_id: str) -> Any:
        """Delete a plan.

        Args:
            plan_id: Plan ID.
        """
        return self._request(
            "DELETE", f"/marketplace/plans/{plan_id}"
        )

    def plans_subscriptions(self) -> Any:
        """List plan subscriptions."""
        return self._request("GET", "/marketplace/plans/subscriptions")

    # ------------------------------------------------------------------
    # Marketplace - Recommendations
    # ------------------------------------------------------------------

    def reco_list(self) -> Any:
        """List recommendations."""
        return self._request("GET", "/marketplace/recommendations")

    def reco_summary(self) -> Any:
        """Get recommendations summary."""
        return self._request(
            "GET", "/marketplace/recommendations/summary"
        )

    def reco_implement(self, reco_id: str) -> Any:
        """Implement a recommendation.

        Args:
            reco_id: Recommendation ID.
        """
        return self._request(
            "POST",
            f"/marketplace/recommendations/{reco_id}/implement",
        )

    def reco_dismiss(self, reco_id: str) -> Any:
        """Dismiss a recommendation.

        Args:
            reco_id: Recommendation ID.
        """
        return self._request(
            "POST",
            f"/marketplace/recommendations/{reco_id}/dismiss",
        )

    # ------------------------------------------------------------------
    # Marketplace - Tax
    # ------------------------------------------------------------------

    def tax_rates(self) -> Any:
        """Get tax rates."""
        return self._request("GET", "/marketplace/tax/rates")

    def tax_invoices(self) -> Any:
        """List tax invoices."""
        return self._request("GET", "/marketplace/tax/invoices")

    def tax_generate(self, customer_id: str, period: str) -> Any:
        """Generate a tax invoice.

        Args:
            customer_id: Customer ID.
            period: Billing period.
        """
        return self._request(
            "POST",
            "/marketplace/tax/invoices/generate",
            {"customer_id": customer_id, "period": period},
        )

    def tax_pay(self, invoice_id: str) -> Any:
        """Pay a tax invoice.

        Args:
            invoice_id: Invoice ID.
        """
        return self._request(
            "POST", f"/marketplace/tax/invoices/{invoice_id}/pay"
        )

    def tax_summary(self) -> Any:
        """Get tax summary."""
        return self._request("GET", "/marketplace/tax/summary")

    def tax_file(self, tax_year: int) -> Any:
        """File a tax report.

        Args:
            tax_year: Tax year.
        """
        return self._request(
            "POST",
            "/marketplace/tax/file",
            {"tax_year": tax_year},
        )

    # ------------------------------------------------------------------
    # Marketplace - Loyalty
    # ------------------------------------------------------------------

    def loyalty_status(self) -> Any:
        """Get loyalty status."""
        return self._request("GET", "/marketplace/loyalty/status")

    def loyalty_badges(self) -> Any:
        """List loyalty badges."""
        return self._request("GET", "/marketplace/loyalty/badges")

    def loyalty_rewards(self) -> Any:
        """List loyalty rewards."""
        return self._request("GET", "/marketplace/loyalty/rewards")

    def loyalty_redeem(self, reward_id: str) -> Any:
        """Redeem a loyalty reward.

        Args:
            reward_id: Reward ID.
        """
        return self._request(
            "POST",
            f"/marketplace/loyalty/rewards/{reward_id}/redeem",
        )

    def loyalty_leaderboard(self) -> Any:
        """Get loyalty leaderboard."""
        return self._request("GET", "/marketplace/loyalty/leaderboard")

    # ------------------------------------------------------------------
    # CX - Health
    # ------------------------------------------------------------------

    def cx_health_list(self) -> Any:
        """List customer health records."""
        return self._request("GET", "/cx/health")

    def cx_health_get(self, customer_id: str) -> Any:
        """Get customer health.

        Args:
            customer_id: Customer ID.
        """
        return self._request("GET", f"/cx/health/{customer_id}")

    def cx_health_compute(self, customer_id: str) -> Any:
        """Compute customer health score.

        Args:
            customer_id: Customer ID.
        """
        return self._request(
            "POST", f"/cx/health/{customer_id}/compute"
        )

    def cx_health_history(self, customer_id: str) -> Any:
        """Get customer health history.

        Args:
            customer_id: Customer ID.
        """
        return self._request(
            "GET", f"/cx/health/{customer_id}/history"
        )

    def cx_health_stats(self) -> Any:
        """Get customer health statistics."""
        return self._request("GET", "/cx/health/stats")

    # ------------------------------------------------------------------
    # CX - Tickets
    # ------------------------------------------------------------------

    def cx_ticket_list(self) -> Any:
        """List support tickets."""
        return self._request("GET", "/cx/tickets")

    def cx_ticket_create(
        self,
        customer_id: str,
        subject: str,
        description: str,
        priority: str = "medium",
    ) -> Any:
        """Create a support ticket.

        Args:
            customer_id: Customer ID.
            subject: Ticket subject.
            description: Ticket description.
            priority: Priority level.
        """
        return self._request(
            "POST",
            "/cx/tickets",
            {
                "customer_id": customer_id,
                "subject": subject,
                "description": description,
                "priority": priority,
            },
        )

    def cx_ticket_get(self, ticket_id: str) -> Any:
        """Get ticket details.

        Args:
            ticket_id: Ticket ID.
        """
        return self._request("GET", f"/cx/tickets/{ticket_id}")

    def cx_ticket_status(self, ticket_id: str, status: str) -> Any:
        """Update ticket status.

        Args:
            ticket_id: Ticket ID.
            status: New status.
        """
        return self._request(
            "PATCH",
            f"/cx/tickets/{ticket_id}/status",
            {"status": status},
        )

    def cx_ticket_comment(
        self, ticket_id: str, comment: str
    ) -> Any:
        """Add a comment to a ticket.

        Args:
            ticket_id: Ticket ID.
            comment: Comment text.
        """
        return self._request(
            "POST",
            f"/cx/tickets/{ticket_id}/comments",
            {"comment": comment},
        )

    def cx_ticket_assign(
        self, ticket_id: str, assignee: str
    ) -> Any:
        """Assign a ticket.

        Args:
            ticket_id: Ticket ID.
            assignee: Assignee user ID.
        """
        return self._request(
            "POST",
            f"/cx/tickets/{ticket_id}/assign",
            {"assignee": assignee},
        )

    def cx_ticket_stats(self) -> Any:
        """Get ticket statistics."""
        return self._request("GET", "/cx/tickets/stats")

    # ------------------------------------------------------------------
    # CX - SLA
    # ------------------------------------------------------------------

    def cx_sla_list(self) -> Any:
        """List CX SLAs."""
        return self._request("GET", "/cx/sla")

    def cx_sla_create(
        self,
        name: str,
        response_time: int,
        resolution_time: int,
    ) -> Any:
        """Create a CX SLA.

        Args:
            name: SLA name.
            response_time: Target response time in seconds.
            resolution_time: Target resolution time in seconds.
        """
        return self._request(
            "POST",
            "/cx/sla",
            {
                "name": name,
                "response_time": response_time,
                "resolution_time": resolution_time,
            },
        )

    # ------------------------------------------------------------------
    # CX - Canned responses
    # ------------------------------------------------------------------

    def cx_canned_list(self) -> Any:
        """List canned responses."""
        return self._request("GET", "/cx/canned-responses")

    def cx_canned_create(
        self, title: str, content: str, category: str
    ) -> Any:
        """Create a canned response.

        Args:
            title: Response title.
            content: Response content.
            category: Response category.
        """
        return self._request(
            "POST",
            "/cx/canned-responses",
            {"title": title, "content": content, "category": category},
        )

    # ------------------------------------------------------------------
    # CX - Sentiment
    # ------------------------------------------------------------------

    def cx_sentiment_analyze(self, customer_id: str) -> Any:
        """Analyze customer sentiment.

        Args:
            customer_id: Customer ID.
        """
        return self._request(
            "POST", f"/cx/sentiment/{customer_id}/analyze"
        )

    def cx_sentiment_profile(self, customer_id: str) -> Any:
        """Get customer sentiment profile.

        Args:
            customer_id: Customer ID.
        """
        return self._request("GET", f"/cx/sentiment/{customer_id}")

    def cx_sentiment_interactions(self, customer_id: str) -> Any:
        """Get customer sentiment interactions.

        Args:
            customer_id: Customer ID.
        """
        return self._request(
            "GET", f"/cx/sentiment/{customer_id}/interactions"
        )

    def cx_sentiment_trends(self) -> Any:
        """Get sentiment trends."""
        return self._request("GET", "/cx/sentiment/trends")

    def cx_sentiment_alerts(self) -> Any:
        """Get sentiment alerts."""
        return self._request("GET", "/cx/sentiment/alerts")

    # ------------------------------------------------------------------
    # CX - Adoption
    # ------------------------------------------------------------------

    def cx_adoption_summary(self) -> Any:
        """Get adoption summary."""
        return self._request("GET", "/cx/adoption/summary")

    def cx_adoption_features(self) -> Any:
        """List adoption features."""
        return self._request("GET", "/cx/adoption/features")

    def cx_adoption_track(
        self, customer_id: str, feature: str
    ) -> Any:
        """Track feature adoption.

        Args:
            customer_id: Customer ID.
            feature: Feature name.
        """
        return self._request(
            "POST",
            f"/cx/adoption/{customer_id}/track",
            {"feature": feature},
        )

    def cx_adoption_recommendations(self, customer_id: str) -> Any:
        """Get adoption recommendations.

        Args:
            customer_id: Customer ID.
        """
        return self._request(
            "GET", f"/cx/adoption/{customer_id}/recommendations"
        )

    def cx_adoption_stats(self) -> Any:
        """Get adoption statistics."""
        return self._request("GET", "/cx/adoption/stats")

    # ------------------------------------------------------------------
    # CX - Onboarding
    # ------------------------------------------------------------------

    def cx_onboarding_start(
        self, customer_id: str, plan: str
    ) -> Any:
        """Start customer onboarding.

        Args:
            customer_id: Customer ID.
            plan: Onboarding plan.
        """
        return self._request(
            "POST",
            f"/cx/onboarding/{customer_id}/start",
            {"plan": plan},
        )

    def cx_onboarding_get(self, customer_id: str) -> Any:
        """Get onboarding status.

        Args:
            customer_id: Customer ID.
        """
        return self._request("GET", f"/cx/onboarding/{customer_id}")

    def cx_onboarding_step(
        self, customer_id: str, step: str
    ) -> Any:
        """Complete an onboarding step.

        Args:
            customer_id: Customer ID.
            step: Step name.
        """
        return self._request(
            "POST", f"/cx/onboarding/{customer_id}/step/{step}"
        )

    def cx_onboarding_stats(self) -> Any:
        """Get onboarding statistics."""
        return self._request("GET", "/cx/onboarding/stats")

    # ------------------------------------------------------------------
    # CX - Knowledge base
    # ------------------------------------------------------------------

    def cx_kb_list(
        self, category: Optional[str] = None
    ) -> Any:
        """List knowledge base articles.

        Args:
            category: Optional category filter.
        """
        path = f"/cx/kb?category={category}" if category else "/cx/kb"
        return self._request("GET", path)

    def cx_kb_create(
        self, title: str, content: str, category: str
    ) -> Any:
        """Create a knowledge base article.

        Args:
            title: Article title.
            content: Article content.
            category: Article category.
        """
        return self._request(
            "POST",
            "/cx/kb",
            {"title": title, "content": content, "category": category},
        )

    def cx_kb_get(self, article_id: str) -> Any:
        """Get a knowledge base article.

        Args:
            article_id: Article ID.
        """
        return self._request("GET", f"/cx/kb/{article_id}")

    def cx_kb_update(self, article_id: str, content: str) -> Any:
        """Update a knowledge base article.

        Args:
            article_id: Article ID.
            content: Updated content.
        """
        return self._request(
            "PATCH", f"/cx/kb/{article_id}", {"content": content}
        )

    def cx_kb_search(self, query: str) -> Any:
        """Search knowledge base.

        Args:
            query: Search query.
        """
        return self._request("GET", f"/cx/kb/search?q={query}")

    def cx_kb_categories(self) -> Any:
        """List knowledge base categories."""
        return self._request("GET", "/cx/kb/categories")

    def cx_kb_feedback(
        self, article_id: str, helpful: bool
    ) -> Any:
        """Submit feedback on an article.

        Args:
            article_id: Article ID.
            helpful: Whether the article was helpful.
        """
        return self._request(
            "POST",
            f"/cx/kb/{article_id}/feedback",
            {"helpful": helpful},
        )

    # ------------------------------------------------------------------
    # CX - Community
    # ------------------------------------------------------------------

    def cx_community_posts(self) -> Any:
        """List community posts."""
        return self._request("GET", "/cx/community/posts")

    def cx_community_create(
        self, title: str, content: str, category: str
    ) -> Any:
        """Create a community post.

        Args:
            title: Post title.
            content: Post content.
            category: Post category.
        """
        return self._request(
            "POST",
            "/cx/community/posts",
            {"title": title, "content": content, "category": category},
        )

    def cx_community_get(self, post_id: str) -> Any:
        """Get a community post.

        Args:
            post_id: Post ID.
        """
        return self._request("GET", f"/cx/community/posts/{post_id}")

    def cx_community_vote(self, post_id: str, vote: int) -> Any:
        """Vote on a community post.

        Args:
            post_id: Post ID.
            vote: Vote value.
        """
        return self._request(
            "POST",
            f"/cx/community/posts/{post_id}/vote",
            {"vote": vote},
        )

    def cx_community_comment(
        self, post_id: str, content: str
    ) -> Any:
        """Comment on a community post.

        Args:
            post_id: Post ID.
            content: Comment content.
        """
        return self._request(
            "POST",
            f"/cx/community/posts/{post_id}/comments",
            {"content": content},
        )

    def cx_community_comments(self, post_id: str) -> Any:
        """List comments on a post.

        Args:
            post_id: Post ID.
        """
        return self._request(
            "GET", f"/cx/community/posts/{post_id}/comments"
        )

    def cx_community_requests(self) -> Any:
        """List feature requests."""
        return self._request("GET", "/cx/community/feature-requests")

    def cx_community_categories(self) -> Any:
        """List community categories."""
        return self._request("GET", "/cx/community/categories")

    def cx_community_leaderboard(self) -> Any:
        """Get community leaderboard."""
        return self._request("GET", "/cx/community/leaderboard")

    def cx_community_stats(self) -> Any:
        """Get community statistics."""
        return self._request("GET", "/cx/community/stats")

    # ------------------------------------------------------------------
    # CX - Communications
    # ------------------------------------------------------------------

    def cx_comm_send(
        self, customer_id: str, template: str, channel: str
    ) -> Any:
        """Send a communication.

        Args:
            customer_id: Customer ID.
            template: Template name.
            channel: Communication channel.
        """
        return self._request(
            "POST",
            f"/cx/comm/{customer_id}/send",
            {"template": template, "channel": channel},
        )

    def cx_comm_batches(self) -> Any:
        """List communication batches."""
        return self._request("GET", "/cx/comm/batches")

    def cx_comm_batch(self, batch_id: str) -> Any:
        """Get a communication batch.

        Args:
            batch_id: Batch ID.
        """
        return self._request("GET", f"/cx/comm/batches/{batch_id}")

    def cx_comm_maintenance_schedule(
        self, customer_id: str, message: str, scheduled_at: str
    ) -> Any:
        """Schedule a maintenance communication.

        Args:
            customer_id: Customer ID.
            message: Maintenance message.
            scheduled_at: ISO-format datetime.
        """
        return self._request(
            "POST",
            f"/cx/comm/{customer_id}/maintenance",
            {"message": message, "scheduled_at": scheduled_at},
        )

    def cx_comm_maintenance_list(self) -> Any:
        """List scheduled maintenance communications."""
        return self._request("GET", "/cx/comm/maintenance")

    def cx_comm_maintenance_complete(self, maintenance_id: str) -> Any:
        """Mark maintenance as complete.

        Args:
            maintenance_id: Maintenance ID.
        """
        return self._request(
            "POST",
            f"/cx/comm/maintenance/{maintenance_id}/complete",
        )

    def cx_comm_templates(self) -> Any:
        """List communication templates."""
        return self._request("GET", "/cx/comm/templates")

    def cx_comm_template_create(
        self, name: str, subject: str, body: str
    ) -> Any:
        """Create a communication template.

        Args:
            name: Template name.
            subject: Email subject.
            body: Template body.
        """
        return self._request(
            "POST",
            "/cx/comm/templates",
            {"name": name, "subject": subject, "body": body},
        )

    # ------------------------------------------------------------------
    # CX - NPS surveys
    # ------------------------------------------------------------------

    def cx_nps_create(
        self, name: str, targets: List[str]
    ) -> Any:
        """Create an NPS survey.

        Args:
            name: Survey name.
            targets: Target customer IDs.
        """
        return self._request(
            "POST",
            "/cx/nps/surveys",
            {"name": name, "targets": targets},
        )

    def cx_nps_list(self) -> Any:
        """List NPS surveys."""
        return self._request("GET", "/cx/nps/surveys")

    def cx_nps_get(self, survey_id: str) -> Any:
        """Get an NPS survey.

        Args:
            survey_id: Survey ID.
        """
        return self._request("GET", f"/cx/nps/surveys/{survey_id}")

    def cx_nps_send(self, survey_id: str) -> Any:
        """Send an NPS survey.

        Args:
            survey_id: Survey ID.
        """
        return self._request(
            "POST", f"/cx/nps/surveys/{survey_id}/send"
        )

    def cx_nps_respond(
        self,
        survey_id: str,
        score: int,
        comment: Optional[str] = None,
    ) -> Any:
        """Submit an NPS survey response.

        Args:
            survey_id: Survey ID.
            score: Score (0-10).
            comment: Optional comment.
        """
        return self._request(
            "POST",
            f"/cx/nps/surveys/{survey_id}/respond",
            {"score": score, "comment": comment or ""},
        )

    def cx_nps_score(self, survey_id: str) -> Any:
        """Get NPS score for a survey.

        Args:
            survey_id: Survey ID.
        """
        return self._request(
            "GET", f"/cx/nps/surveys/{survey_id}/score"
        )

    def cx_nps_trend(self, survey_id: str) -> Any:
        """Get NPS trend for a survey.

        Args:
            survey_id: Survey ID.
        """
        return self._request(
            "GET", f"/cx/nps/surveys/{survey_id}/trend"
        )

    def cx_nps_detractors(self, survey_id: str) -> Any:
        """Get NPS detractors for a survey.

        Args:
            survey_id: Survey ID.
        """
        return self._request(
            "GET", f"/cx/nps/surveys/{survey_id}/detractors"
        )

    def cx_nps_stats(self) -> Any:
        """Get NPS statistics."""
        return self._request("GET", "/cx/nps/stats")

    # ------------------------------------------------------------------
    # CX - Success plays
    # ------------------------------------------------------------------

    def cx_success_plays(self) -> Any:
        """List success plays."""
        return self._request("GET", "/cx/success/plays")

    def cx_success_create(
        self, name: str, trigger: str, actions: List[Any]
    ) -> Any:
        """Create a success play.

        Args:
            name: Play name.
            trigger: Trigger condition.
            actions: List of actions.
        """
        return self._request(
            "POST",
            "/cx/success/plays",
            {"name": name, "trigger": trigger, "actions": actions},
        )

    def cx_success_status(self, play_id: str) -> Any:
        """Get success play status.

        Args:
            play_id: Play ID.
        """
        return self._request(
            "GET", f"/cx/success/plays/{play_id}"
        )

    def cx_success_trigger(
        self, play_id: str, customer_id: str
    ) -> Any:
        """Trigger a success play.

        Args:
            play_id: Play ID.
            customer_id: Customer ID.
        """
        return self._request(
            "POST",
            f"/cx/success/plays/{play_id}/trigger",
            {"customer_id": customer_id},
        )

    def cx_success_executions(self, play_id: str) -> Any:
        """List success play executions.

        Args:
            play_id: Play ID.
        """
        return self._request(
            "GET", f"/cx/success/plays/{play_id}/executions"
        )

    def cx_success_stats(self) -> Any:
        """Get success play statistics."""
        return self._request("GET", "/cx/success/stats")

    # ------------------------------------------------------------------
    # AIOps - Root cause analysis
    # ------------------------------------------------------------------

    def aiops_rca_analyze(self, incident_id: str) -> Any:
        """Analyze an incident for root cause.

        Args:
            incident_id: Incident ID.
        """
        return self._request(
            "POST", f"/aiops/rca/{incident_id}/analyze"
        )

    def aiops_rca_incidents(self) -> Any:
        """List RCA incidents."""
        return self._request("GET", "/aiops/rca/incidents")

    def aiops_rca_events(self, incident_id: str) -> Any:
        """Get events for an RCA incident.

        Args:
            incident_id: Incident ID.
        """
        return self._request(
            "GET", f"/aiops/rca/{incident_id}/events"
        )

    def aiops_rca_deps(self, incident_id: str) -> Any:
        """Get dependencies for an RCA incident.

        Args:
            incident_id: Incident ID.
        """
        return self._request(
            "GET", f"/aiops/rca/{incident_id}/dependencies"
        )

    # ------------------------------------------------------------------
    # AIOps - Digital experience monitoring
    # ------------------------------------------------------------------

    def aiops_dem_list(self) -> Any:
        """List DEM monitors."""
        return self._request("GET", "/aiops/dem/monitors")

    def aiops_dem_create(
        self, name: str, url: str, interval: int = 60
    ) -> Any:
        """Create a DEM monitor.

        Args:
            name: Monitor name.
            url: Target URL.
            interval: Check interval in seconds.
        """
        return self._request(
            "POST",
            "/aiops/dem/monitors",
            {"name": name, "url": url, "interval": interval},
        )

    def aiops_dem_check(self, monitor_id: str) -> Any:
        """Run a DEM check.

        Args:
            monitor_id: Monitor ID.
        """
        return self._request(
            "POST", f"/aiops/dem/monitors/{monitor_id}/check"
        )

    def aiops_dem_stats(self, monitor_id: str) -> Any:
        """Get DEM monitor statistics.

        Args:
            monitor_id: Monitor ID.
        """
        return self._request(
            "GET", f"/aiops/dem/monitors/{monitor_id}/stats"
        )

    def aiops_dem_summary(self) -> Any:
        """Get DEM summary."""
        return self._request("GET", "/aiops/dem/summary")

    # ------------------------------------------------------------------
    # AIOps - Alert management
    # ------------------------------------------------------------------

    def aiops_alert_ingest(
        self,
        source: str,
        message: str,
        severity: str = "info",
    ) -> Any:
        """Ingest an alert.

        Args:
            source: Alert source.
            message: Alert message.
            severity: Severity level.
        """
        return self._request(
            "POST",
            "/aiops/alerts/ingest",
            {"source": source, "message": message, "severity": severity},
        )

    def aiops_alert_incidents(self) -> Any:
        """List alert incidents."""
        return self._request("GET", "/aiops/alerts/incidents")

    def aiops_alert_stats(self) -> Any:
        """Get alert statistics."""
        return self._request("GET", "/aiops/alerts/stats")

    def aiops_alert_suppress(self, alert_id: str) -> Any:
        """Suppress an alert.

        Args:
            alert_id: Alert ID.
        """
        return self._request(
            "POST", f"/aiops/alerts/{alert_id}/suppress"
        )

    # ------------------------------------------------------------------
    # AIOps - Predictive scaling
    # ------------------------------------------------------------------

    def aiops_scaling_predict(self, resource: str) -> Any:
        """Get scaling prediction.

        Args:
            resource: Resource name.
        """
        return self._request(
            "POST", f"/aiops/scaling/{resource}/predict"
        )

    def aiops_scaling_metrics(self, resource: str) -> Any:
        """Get scaling metrics.

        Args:
            resource: Resource name.
        """
        return self._request(
            "GET", f"/aiops/scaling/{resource}/metrics"
        )

    def aiops_scaling_policy(
        self,
        resource: str,
        min_instances: int,
        max_instances: int,
    ) -> Any:
        """Set scaling policy.

        Args:
            resource: Resource name.
            min_instances: Minimum instances.
            max_instances: Maximum instances.
        """
        return self._request(
            "POST",
            f"/aiops/scaling/{resource}/policy",
            {"min": min_instances, "max": max_instances},
        )

    def aiops_scaling_summary(self) -> Any:
        """Get scaling summary."""
        return self._request("GET", "/aiops/scaling/summary")

    # ------------------------------------------------------------------
    # AIOps - Health monitoring
    # ------------------------------------------------------------------

    def aiops_health_services(self) -> Any:
        """List health services."""
        return self._request("GET", "/aiops/health/services")

    def aiops_health_register(
        self, name: str, endpoint: str, interval: int
    ) -> Any:
        """Register a health service.

        Args:
            name: Service name.
            endpoint: Health check endpoint.
            interval: Check interval.
        """
        return self._request(
            "POST",
            "/aiops/health/services",
            {"name": name, "endpoint": endpoint, "interval": interval},
        )

    def aiops_health_forecast(self, service_id: str) -> Any:
        """Get health forecast for a service.

        Args:
            service_id: Service ID.
        """
        return self._request(
            "GET", f"/aiops/health/{service_id}/forecast"
        )

    def aiops_health_dashboard(self) -> Any:
        """Get health dashboard."""
        return self._request("GET", "/aiops/health/dashboard")

    # ------------------------------------------------------------------
    # AIOps - Assistant
    # ------------------------------------------------------------------

    def aiops_assistant_message(self, message: str) -> Any:
        """Send a message to the AI assistant.

        Args:
            message: Message text.
        """
        return self._request(
            "POST",
            "/aiops/assistant/message",
            {"message": message},
        )

    def aiops_assistant_stats(self) -> Any:
        """Get assistant statistics."""
        return self._request("GET", "/aiops/assistant/stats")

    # ------------------------------------------------------------------
    # AIOps - Change management
    # ------------------------------------------------------------------

    def aiops_change_plan(
        self, service: str, change: str, risk: str
    ) -> Any:
        """Plan a change.

        Args:
            service: Service name.
            change: Change description.
            risk: Risk level.
        """
        return self._request(
            "POST",
            "/aiops/change/plan",
            {"service": service, "change": change, "risk": risk},
        )

    def aiops_change_approve(self, plan_id: str) -> Any:
        """Approve a change plan.

        Args:
            plan_id: Plan ID.
        """
        return self._request(
            "POST", f"/aiops/change/{plan_id}/approve"
        )

    def aiops_change_stats(self) -> Any:
        """Get change management statistics."""
        return self._request("GET", "/aiops/change/stats")

    # ------------------------------------------------------------------
    # AIOps - Capacity planning
    # ------------------------------------------------------------------

    def aiops_capacity_recommend(self) -> Any:
        """Get capacity recommendations."""
        return self._request("GET", "/aiops/capacity/recommendations")

    def aiops_capacity_usage(self, resource: str) -> Any:
        """Get capacity usage.

        Args:
            resource: Resource name.
        """
        return self._request(
            "GET", f"/aiops/capacity/{resource}/usage"
        )

    def aiops_capacity_simulate(
        self, resource: str, load: float
    ) -> Any:
        """Simulate capacity load.

        Args:
            resource: Resource name.
            load: Simulated load.
        """
        return self._request(
            "POST",
            f"/aiops/capacity/{resource}/simulate",
            {"load": load},
        )

    def aiops_capacity_summary(self) -> Any:
        """Get capacity summary."""
        return self._request("GET", "/aiops/capacity/summary")

    # ------------------------------------------------------------------
    # AIOps - Chatbot
    # ------------------------------------------------------------------

    def aiops_chatbot_message(self, message: str) -> Any:
        """Send a message to the chatbot.

        Args:
            message: Message text.
        """
        return self._request(
            "POST",
            "/aiops/chatbot/message",
            {"message": message},
        )

    def aiops_chatbot_tasks(self) -> Any:
        """List chatbot tasks."""
        return self._request("GET", "/aiops/chatbot/tasks")

    def aiops_chatbot_analytics(self) -> Any:
        """Get chatbot analytics."""
        return self._request("GET", "/aiops/chatbot/analytics")

    # ------------------------------------------------------------------
    # FinOps - Commitments
    # ------------------------------------------------------------------

    def finops_commitment_list(self) -> Any:
        """List commitments."""
        return self._request("GET", "/finops/commitments")

    def finops_commitment_summary(self) -> Any:
        """Get commitment summary."""
        return self._request("GET", "/finops/commitments/summary")

    def finops_commitment_implement(self, commitment_id: str) -> Any:
        """Implement a commitment.

        Args:
            commitment_id: Commitment ID.
        """
        return self._request(
            "POST",
            f"/finops/commitments/{commitment_id}/implement",
        )

    def finops_commitment_commitments(self) -> Any:
        """List all commitments (alias)."""
        return self._request("GET", "/finops/commitments/list")

    # ------------------------------------------------------------------
    # FinOps - Spot instances
    # ------------------------------------------------------------------

    def finops_spot_list(self) -> Any:
        """List spot instance advice."""
        return self._request("GET", "/finops/spot/advice")

    def finops_spot_create(
        self,
        name: str,
        instance_type: str,
        max_price: float,
        region: str,
    ) -> Any:
        """Create a spot instance request.

        Args:
            name: Request name.
            instance_type: Instance type.
            max_price: Maximum price.
            region: AWS region.
        """
        return self._request(
            "POST",
            "/finops/spot/requests",
            {
                "name": name,
                "instance_type": instance_type,
                "max_price": max_price,
                "region": region,
            },
        )

    def finops_spot_get(self, request_id: str) -> Any:
        """Get spot request details.

        Args:
            request_id: Request ID.
        """
        return self._request(
            "GET", f"/finops/spot/requests/{request_id}"
        )

    def finops_spot_instances(self) -> Any:
        """List spot instances."""
        return self._request("GET", "/finops/spot/instances")

    def finops_spot_savings(self) -> Any:
        """Get spot savings."""
        return self._request("GET", "/finops/spot/savings")

    # ------------------------------------------------------------------
    # FinOps - Unit of economics
    # ------------------------------------------------------------------

    def finops_uoe_metrics(self) -> Any:
        """Get UoE metrics."""
        return self._request("GET", "/finops/uoe/metrics")

    def finops_uoe_record(
        self, metric: str, value: float
    ) -> Any:
        """Record a UoE metric.

        Args:
            metric: Metric name.
            value: Metric value.
        """
        return self._request(
            "POST",
            "/finops/uoe/metrics",
            {"metric": metric, "value": value},
        )

    def finops_uoe_targets(self) -> Any:
        """Get UoE targets."""
        return self._request("GET", "/finops/uoe/targets")

    # ------------------------------------------------------------------
    # SSH Session Management
    # ------------------------------------------------------------------

    def list_ssh_sessions(self, status: Optional[str] = None) -> Any:
        """List SSH sessions."""
        path = "/ssh/sessions"
        if status:
            path += f"?status={status}"
        return self._request("GET", path)

    def ssh_connect(self, server: str, user: str = "root", jump_host: Optional[str] = None, port: int = 22) -> Any:
        """Connect to a server via SSH."""
        data = {"server": server, "user": user, "port": port}
        if jump_host:
            data["jump_host"] = jump_host
        return self._request("POST", "/ssh/connect", data)

    def list_jump_hosts(self) -> Any:
        """List SSH jump hosts."""
        return self._request("GET", "/ssh/jump-hosts")

    def create_jump_host(self, name: str, host: str, user: str) -> Any:
        """Create a jump host entry."""
        return self._request("POST", "/ssh/jump-hosts", {"name": name, "host": host, "user": user})

    def list_ssh_keys(self) -> Any:
        """List SSH keys."""
        return self._request("GET", "/ssh/keys")

    def add_ssh_key(self, name: str, key: str) -> Any:
        """Add an SSH key."""
        return self._request("POST", "/ssh/keys", {"name": name, "key": key})

    def delete_ssh_key(self, key_id: str) -> Any:
        """Delete an SSH key."""
        return self._request("DELETE", f"/ssh/keys/{key_id}")

    def get_session_recording(self, session_id: str) -> Any:
        """Get SSH session recording."""
        return self._request("GET", f"/ssh/sessions/{session_id}/recording")

    def list_saved_hosts(self) -> Any:
        """List saved SSH hosts."""
        return self._request("GET", "/ssh/saved-hosts")

    def save_ssh_host(self, name: str, host: str, port: int = 22) -> Any:
        """Save an SSH host."""
        return self._request("POST", "/ssh/saved-hosts", {"name": name, "host": host, "port": port})

    def delete_saved_host(self, host_id: str) -> Any:
        """Delete a saved SSH host."""
        return self._request("DELETE", f"/ssh/saved-hosts/{host_id}")

    # ------------------------------------------------------------------
    # Server Inventory
    # ------------------------------------------------------------------

    def list_inventory(self, **filters) -> Any:
        """List server inventory with filters."""
        params = "&".join(f"{k}={v}" for k, v in filters.items() if v)
        path = f"/inventory?{params}" if params else "/inventory"
        return self._request("GET", path)

    def get_inventory(self, server_id: str) -> Any:
        """Get inventory metadata for a server."""
        return self._request("GET", f"/inventory/{server_id}")

    def update_inventory(self, server_id: str, metadata: Dict[str, Any]) -> Any:
        """Update server inventory metadata."""
        return self._request("PATCH", f"/inventory/{server_id}", metadata)

    def add_inventory_tag(self, server_id: str, tag: str) -> Any:
        """Add a tag to a server."""
        return self._request("POST", f"/inventory/{server_id}/tags", {"tag": tag})

    def remove_inventory_tag(self, server_id: str, tag: str) -> Any:
        """Remove a tag from a server."""
        return self._request("DELETE", f"/inventory/{server_id}/tags/{tag}")

    def get_inventory_tags(self, server_id: str) -> Any:
        """Get tags for a server."""
        return self._request("GET", f"/inventory/{server_id}/tags")

    def list_inventory_tags(self) -> Any:
        """List all inventory tags in use."""
        return self._request("GET", "/inventory/tags")

    # ------------------------------------------------------------------
    # Secret Management
    # ------------------------------------------------------------------

    def list_secrets(self, path: Optional[str] = None) -> Any:
        """List secrets."""
        p = f"/secrets?path={path}" if path else "/secrets"
        return self._request("GET", p)

    def get_secret(self, key: str, version: Optional[int] = None) -> Any:
        """Get a secret value."""
        p = f"/secrets/{key}"
        if version is not None:
            p += f"?version={version}"
        return self._request("GET", p)

    def set_secret(self, key: str, value: str, rotate: bool = False, rotation_days: int = 90) -> Any:
        """Set a secret value."""
        return self._request("POST", "/secrets", {"key": key, "value": value, "rotate": rotate, "rotation_days": rotation_days})

    def delete_secret(self, key: str) -> Any:
        """Delete a secret."""
        return self._request("DELETE", f"/secrets/{key}")

    def list_secret_versions(self, key: str) -> Any:
        """List versions of a secret."""
        return self._request("GET", f"/secrets/{key}/versions")

    def rotate_secret(self, key: str) -> Any:
        """Rotate a secret."""
        return self._request("POST", f"/secrets/{key}/rotate")

    def rotate_all_secrets(self) -> Any:
        """Rotate all secrets due for rotation."""
        return self._request("POST", "/secrets/rotate-all")

    def list_secrets_due_for_rotation(self) -> Any:
        """List secrets due for rotation."""
        return self._request("GET", "/secrets/due-for-rotation")

    def grant_secret_access(self, key: str, role: str) -> Any:
        """Grant role access to a secret."""
        return self._request("POST", f"/secrets/{key}/access", {"role": role})

    def revoke_secret_access(self, key: str, role: str) -> Any:
        """Revoke role access from a secret."""
        return self._request("DELETE", f"/secrets/{key}/access/{role}")

    def list_secret_access(self, key: str) -> Any:
        """List roles with access to a secret."""
        return self._request("GET", f"/secrets/{key}/access")

    # ------------------------------------------------------------------
    # Webhook Management
    # ------------------------------------------------------------------

    def list_webhooks(self) -> Any:
        """List webhooks."""
        return self._request("GET", "/webhooks")

    def create_webhook(self, name: str, url: str, events: List[str], secret: Optional[str] = None) -> Any:
        """Create a webhook."""
        data = {"name": name, "url": url, "events": events}
        if secret:
            data["secret"] = secret
        return self._request("POST", "/webhooks", data)

    def delete_webhook(self, webhook_id: str) -> Any:
        """Delete a webhook."""
        return self._request("DELETE", f"/webhooks/{webhook_id}")

    def test_webhook(self, webhook_id: Optional[str] = None, event: str = "test") -> Any:
        """Test a webhook."""
        path = f"/webhooks/{webhook_id}/test" if webhook_id else "/webhooks/test"
        return self._request("POST", path, {"event": event})

    def get_webhook_logs(self, webhook_id: Optional[str] = None) -> Any:
        """Get webhook delivery logs."""
        path = f"/webhooks/{webhook_id}/logs" if webhook_id else "/webhooks/logs"
        return self._request("GET", path)

    # ------------------------------------------------------------------
    # API Key Management
    # ------------------------------------------------------------------

    def list_api_keys(self) -> Any:
        """List API keys."""
        return self._request("GET", "/api-keys")

    def create_api_key(self, name: str, role: str = "user", expire_days: Optional[int] = None) -> Any:
        """Create an API key."""
        data = {"name": name, "role": role}
        if expire_days:
            data["expire_days"] = expire_days
        return self._request("POST", "/api-keys", data)

    def revoke_api_key(self, key_id: str) -> Any:
        """Revoke an API key."""
        return self._request("DELETE", f"/api-keys/{key_id}")

    # ------------------------------------------------------------------
    # Plugin Management
    # ------------------------------------------------------------------

    def list_plugins(self, installed_only: bool = False) -> Any:
        """List plugins."""
        path = "/plugins?installed=true" if installed_only else "/plugins"
        return self._request("GET", path)

    def install_plugin(self, name: str, source: Optional[str] = None, version: Optional[str] = None) -> Any:
        """Install a plugin."""
        data = {"name": name}
        if source: data["source"] = source
        if version: data["version"] = version
        return self._request("POST", "/plugins/install", data)

    def uninstall_plugin(self, name: str) -> Any:
        """Uninstall a plugin."""
        return self._request("POST", f"/plugins/{name}/uninstall")

    def update_plugin(self, name: str) -> Any:
        """Update a plugin."""
        return self._request("POST", f"/plugins/{name}/update")

    def update_all_plugins(self) -> Any:
        """Update all plugins."""
        return self._request("POST", "/plugins/update-all")

    def list_plugin_updates(self) -> Any:
        """List available plugin updates."""
        return self._request("GET", "/plugins/updates")

    def get_plugin_info(self, name: str) -> Any:
        """Get plugin info."""
        return self._request("GET", f"/plugins/{name}")

    # ------------------------------------------------------------------
    # Deployment Templates
    # ------------------------------------------------------------------

    def list_templates(self, template_type: Optional[str] = None) -> Any:
        """List deployment templates."""
        path = f"/templates?type={template_type}" if template_type else "/templates"
        return self._request("GET", path)

    def get_template(self, template: str) -> Any:
        """Get template details."""
        return self._request("GET", f"/templates/{template}")

    def deploy_template(self, template: str, name: str, server: Optional[str] = None, variables: Optional[Dict[str, Any]] = None, dry_run: bool = False) -> Any:
        """Deploy a template."""
        data = {"template": template, "name": name}
        if server: data["server"] = server
        if variables: data["variables"] = variables
        if dry_run: data["dry_run"] = True
        return self._request("POST", "/templates/deploy", data)

    def init_template(self, template: str, name: str, output_dir: str = ".") -> Any:
        """Initialize a project from a template."""
        return self._request("POST", "/templates/init", {"template": template, "name": name, "output_dir": output_dir})

    # ------------------------------------------------------------------
    # Doctor / Benchmark / Diagnose
    # ------------------------------------------------------------------

    def benchmark_server(self, server: str, duration: int = 10) -> Any:
        """Benchmark a server."""
        return self._request("POST", f"/doctor/benchmark/{server}", {"duration": duration})

    def benchmark_system(self, duration: int = 10) -> Any:
        """Benchmark the local system."""
        return self._request("POST", "/doctor/benchmark", {"duration": duration})

    def diagnose_server(self, server: str, issue: Optional[str] = None) -> Any:
        """Diagnose a server."""
        data = {}
        if issue: data["issue"] = issue
        return self._request("POST", f"/doctor/diagnose/{server}", data)

    def diagnose_system(self, issue: Optional[str] = None) -> Any:
        """Diagnose the local system."""
        data = {}
        if issue: data["issue"] = issue
        return self._request("POST", "/doctor/diagnose", data)

    # ------------------------------------------------------------------
    # Rollback / Change History
    # ------------------------------------------------------------------

    def list_changes(self, resource: Optional[str] = None, limit: int = 20) -> Any:
        """List recent changes."""
        params = f"?limit={limit}"
        if resource: params += f"&resource={resource}"
        return self._request("GET", f"/changes{params}")

    def undo_change(self, change_id: str, dry_run: bool = False) -> Any:
        """Undo a change."""
        return self._request("POST", f"/changes/{change_id}/undo", {"dry_run": dry_run})

    def rollback_resource(self, resource_type: str, resource_id: str, version: Optional[str] = None) -> Any:
        """Rollback a resource."""
        data = {"resource_type": resource_type, "resource_id": resource_id}
        if version: data["version"] = version
        return self._request("POST", "/rollback", data)

    def get_change_history(self, resource_type: Optional[str] = None, resource_id: Optional[str] = None) -> Any:
        """Get change history."""
        params = []
        if resource_type: params.append(f"resource_type={resource_type}")
        if resource_id: params.append(f"resource_id={resource_id}")
        qs = "&".join(params)
        path = f"/changes/history?{qs}" if qs else "/changes/history"
        return self._request("GET", path)

