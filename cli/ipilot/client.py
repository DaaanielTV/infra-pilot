# TODO: add retry logic with exp backoff
# FIXME: this file is WAY too long lol
import json
import requests
from typing import Any, Dict, Optional


# HACK: this class is a monster pls refactor
class ApiClient:
    """HTTP API client for Infra Pilot backend.

    Maintains full backward compatibility with existing cmd_* functions
    while adding session management, retry, and better error handling.
    """

    # TODO: add timeout as param
    def __init__(self, base_url: str, token: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    # NOTE: this is literally never used lol
    def _headers(self) -> Dict[str, str]:
        return dict(self.session.headers)

    # XXX: error handling is garbage tier
    def _request(self, method: str, path: str, data: Optional[Dict] = None) -> Any:
        url = f"{self.base_url}/api/v1{path}"
        try:
            resp = self.session.request(method, url, json=data, timeout=30)
            resp.raise_for_status()
            if resp.content:
                return resp.json()
            return {}
        except requests.HTTPError as e:
            try:
                msg = e.response.json().get("message", str(e))
            except (json.JSONDecodeError, AttributeError):
                msg = str(e)
            return {"error": msg}
        except requests.ConnectionError as e:
            return {"error": f"Connection failed: {e}"}
        except requests.Timeout:
            return {"error": "Request timed out"}

    def _get(self, path: str) -> Any:
        return self._request("GET", path)

    def _post(self, path: str, data: Optional[Dict] = None) -> Any:
        return self._request("POST", path, data)

    def _put(self, path: str, data: Optional[Dict] = None) -> Any:
        return self._request("PUT", path, data)

    def _delete(self, path: str) -> Any:
        return self._request("DELETE", path)

    def login(self, api_key: str) -> Any:
        return self._request("POST", "/auth/login", {"api_key": api_key})

    def logout(self) -> Any:
        return self._request("POST", "/auth/logout")

    def list_servers(self) -> Any:
        return self._request("GET", "/servers")

    def get_server(self, server_id: str) -> Any:
        return self._request("GET", f"/servers/{server_id}")

    def create_server(self, name: str, server_type: str, memory: Optional[int] = None) -> Any:
        return self._request("POST", "/servers", {"name": name, "type": server_type, "memory": memory})

    def delete_server(self, server_id: str) -> Any:
        return self._request("DELETE", f"/servers/{server_id}")

    def server_status(self, server_id: str) -> Any:
        return self._request("GET", f"/servers/{server_id}/status")

    def get_logs(self, server_id: str, lines: int = 50, follow: bool = False) -> Any:
        return self._request("GET", f"/servers/{server_id}/logs?lines={lines}&follow={follow}")

    def list_backups(self, server_id: Optional[str] = None) -> Any:
        path = f"/backups/{server_id}" if server_id else "/backups"
        return self._request("GET", path)

    def create_backup(self, server_id: str) -> Any:
        return self._request("POST", f"/servers/{server_id}/backups")

    def deploy(self, server_id: str, branch: str) -> Any:
        return self._request("POST", f"/servers/{server_id}/deploy", {"branch": branch})

    def health_check(self) -> Any:
        return self._request("GET", "/health")

    def list_edge_devices(self, device_type: Optional[str] = None, status: Optional[str] = None) -> Any:
        params = {}
        if device_type:
            params["device_type"] = device_type
        if status:
            params["status"] = status
        return self._request("GET", f"/edge/devices?{requests.compat.urlencode(params)}")

    def register_edge_device(self, name: str, device_type: str, hardware_id: str) -> Any:
        return self._request("POST", "/edge/devices", {"name": name, "device_type": device_type, "hardware_id": hardware_id})

    def edge_device_status(self, device_id: str) -> Any:
        return self._request("GET", f"/edge/devices/{device_id}")

    def edge_device_command(self, device_id: str, command: str) -> Any:
        return self._request("POST", f"/edge/devices/{device_id}/command", {"command": command})

    def backup_edge_device(self, device_id: str) -> Any:
        return self._request("POST", f"/edge/devices/{device_id}/backup")

    def list_edge_functions(self, device_id: Optional[str] = None) -> Any:
        path = f"/edge/functions?device_id={device_id}" if device_id else "/edge/functions"
        return self._request("GET", path)

    def deploy_edge_function(self, name: str, runtime: str, device_id: str, source: str, handler: str) -> Any:
        return self._request("POST", "/edge/functions", {"name": name, "runtime": runtime, "device_id": device_id, "source": source, "handler": handler})

    def invoke_edge_function(self, func_id: str, payload: Optional[str] = None) -> Any:
        return self._request("POST", f"/edge/functions/{func_id}/invoke", {"payload": payload})

    def list_ml_models(self, device_id: Optional[str] = None) -> Any:
        path = f"/edge/ml/models?device_id={device_id}" if device_id else "/edge/ml/models"
        return self._request("GET", path)

    def deploy_ml_model(self, name: str, model_format: str, device_id: str, version: str) -> Any:
        return self._request("POST", "/edge/ml/models", {"name": name, "format": model_format, "device_id": device_id, "version": version})

    def run_inference(self, model_id: str) -> Any:
        return self._request("POST", f"/edge/ml/models/{model_id}/infer")

    def generate_claim_codes(self, count: int = 10, ttl: int = 24) -> Any:
        return self._request("POST", "/iot/claim-codes", {"count": count, "ttl": ttl})

    def enroll_device(self, code: str, device_id: str) -> Any:
        return self._request("POST", "/iot/enroll", {"code": code, "device_id": device_id})

    def cdn_stats(self) -> Any:
        return self._request("GET", "/edge/cdn/stats")

    def list_mesh_networks(self) -> Any:
        return self._request("GET", "/edge/mesh")

    def create_mesh_network(self, name: str, mesh_type: str, subnet: str) -> Any:
        return self._request("POST", "/edge/mesh", {"name": name, "mesh_type": mesh_type, "subnet": subnet})

    def list_lorawan_gateways(self, status: Optional[str] = None) -> Any:
        path = f"/edge/lorawan/gateways?status={status}" if status else "/edge/lorawan/gateways"
        return self._request("GET", path)

    def pipeline_stats(self) -> Any:
        return self._request("GET", "/edge/pipeline/stats")

    def energy_current(self) -> Any:
        return self._request("GET", "/energy/current")

    def energy_history(self, server_id: Optional[str] = None, hours: int = 24) -> Any:
        params = f"?hours={hours}"
        if server_id:
            params += f"&server_id={server_id}"
        return self._request("GET", f"/energy/history{params}")

    def energy_summary(self, period: str = "daily") -> Any:
        return self._request("GET", f"/energy/summary?period={period}")

    def carbon_current(self) -> Any:
        return self._request("GET", "/carbon/current")

    def carbon_history(self) -> Any:
        return self._request("GET", "/carbon/history")

    def green_forecast(self) -> Any:
        return self._request("GET", "/green/forecast")

    def green_jobs(self) -> Any:
        return self._request("GET", "/green/jobs")

    def green_schedule(self, workload_id: str, schedule_type: str) -> Any:
        return self._request("POST", "/green/schedule", {"workload_id": workload_id, "schedule_type": schedule_type})

    def green_report(self) -> Any:
        return self._request("GET", "/green/report")

    def reclaim_list(self) -> Any:
        return self._request("GET", "/reclaim/resources")

    def reclaim_scan(self) -> Any:
        return self._request("POST", "/reclaim/scan")

    def reclaim_report(self) -> Any:
        return self._request("GET", "/reclaim/report")

    def shutdown_policies(self) -> Any:
        return self._request("GET", "/shutdown/policies")

    def create_shutdown_policy(self, name: str, schedule: str, conditions: Any) -> Any:
        return self._request("POST", "/shutdown/policies", {"name": name, "schedule": schedule, "conditions": conditions})

    def shutdown_savings(self) -> Any:
        return self._request("GET", "/shutdown/savings")

    def list_hardware(self) -> Any:
        return self._request("GET", "/hardware")

    def add_hardware(self, name: str, hardware_type: str, specs: Any) -> Any:
        return self._request("POST", "/hardware", {"name": name, "type": hardware_type, "specs": specs})

    def pue_current(self) -> Any:
        return self._request("GET", "/pue/current")

    def pue_history(self) -> Any:
        return self._request("GET", "/pue/history")

    def provider_rank(self) -> Any:
        return self._request("GET", "/provider/rank")

    def offset_quote(self, amount: float) -> Any:
        return self._request("POST", "/offset/quote", {"amount": amount})

    def offset_purchase(self, amount: float, provider: str) -> Any:
        return self._request("POST", "/offset/purchase", {"amount": amount, "provider": provider})

    def offset_certs(self) -> Any:
        return self._request("GET", "/offset/certificates")

    def efficiency_score(self) -> Any:
        return self._request("GET", "/efficiency/score")

    def efficiency_recommendations(self) -> Any:
        return self._request("GET", "/efficiency/recommendations")

    def oidc_clients(self) -> Any:
        return self._request("GET", "/identity/oidc/clients")

    def oidc_register(self, name: str, redirect_uris: list) -> Any:
        return self._request("POST", "/identity/oidc/clients", {"name": name, "redirect_uris": redirect_uris})

    def oidc_delete(self, client_id: str) -> Any:
        return self._request("DELETE", f"/identity/oidc/clients/{client_id}")

    def webauthn_credentials(self) -> Any:
        return self._request("GET", "/identity/webauthn/credentials")

    def webauthn_remove(self, credential_id: str) -> Any:
        return self._request("DELETE", f"/identity/webauthn/credentials/{credential_id}")

    def list_sessions(self) -> Any:
        return self._request("GET", "/identity/sessions")

    def revoke_session(self, session_id: str) -> Any:
        return self._request("DELETE", f"/identity/sessions/{session_id}")

    def pam_requests(self) -> Any:
        return self._request("GET", "/identity/pam/requests")

    def pam_request(self, resource: str, reason: str) -> Any:
        return self._request("POST", "/identity/pam/requests", {"resource": resource, "reason": reason})

    def pam_approve(self, request_id: str) -> Any:
        return self._request("POST", f"/identity/pam/requests/{request_id}/approve")

    def pam_deny(self, request_id: str) -> Any:
        return self._request("POST", f"/identity/pam/requests/{request_id}/deny")

    def breach_list(self) -> Any:
        return self._request("GET", "/governance/breaches")

    def breach_report(self, breach_id: str, details: Any) -> Any:
        return self._request("POST", f"/governance/breaches/{breach_id}/report", details)

    def policy_list(self) -> Any:
        return self._request("GET", "/governance/policies")

    def policy_create(self, name: str, rules: Any) -> Any:
        return self._request("POST", "/governance/policies", {"name": name, "rules": rules})

    def policy_evaluate(self, policy_id: str, resource: str) -> Any:
        return self._request("POST", f"/governance/policies/{policy_id}/evaluate", {"resource": resource})

    def compliance_scan(self, framework: str) -> Any:
        return self._request("POST", "/governance/compliance/scan", {"framework": framework})

    def compliance_report(self, scan_id: str) -> Any:
        return self._request("GET", f"/governance/compliance/report/{scan_id}")

    def compliance_checks(self) -> Any:
        return self._request("GET", "/governance/compliance/checks")

    def audit_anomalies(self) -> Any:
        return self._request("GET", "/governance/audit/anomalies")

    def audit_trend(self) -> Any:
        return self._request("GET", "/governance/audit/trend")

    def audit_summary(self) -> Any:
        return self._request("GET", "/governance/audit/summary")

    def classify_scan(self) -> Any:
        return self._request("POST", "/governance/classify/scan")

    def classify_inventory(self) -> Any:
        return self._request("GET", "/governance/classify/inventory")

    def vendor_list(self) -> Any:
        return self._request("GET", "/governance/vendors")

    def vendor_create(self, name: str, risk_level: str) -> Any:
        return self._request("POST", "/governance/vendors", {"name": name, "risk_level": risk_level})

    def vendor_assess(self, vendor_id: str) -> Any:
        return self._request("POST", f"/governance/vendors/{vendor_id}/assess")

    def workflow_list(self) -> Any:
        return self._request("GET", "/orchestration/workflows")

    def workflow_create(self, name: str, steps: list) -> Any:
        return self._request("POST", "/orchestration/workflows", {"name": name, "steps": steps})

    def workflow_run(self, workflow_id: str, params: Optional[Dict] = None) -> Any:
        return self._request("POST", f"/orchestration/workflows/{workflow_id}/run", params or {})

    def infra_pipeline_list(self) -> Any:
        return self._request("GET", "/orchestration/pipelines")

    def infra_pipeline_run(self, pipeline_id: str) -> Any:
        return self._request("POST", f"/orchestration/pipelines/{pipeline_id}/run")

    def drift_scan(self) -> Any:
        return self._request("POST", "/orchestration/drift/scan")

    def drift_list(self) -> Any:
        return self._request("GET", "/orchestration/drift")

    def quota_list(self) -> Any:
        return self._request("GET", "/orchestration/quotas")

    def quota_check(self, resource: str) -> Any:
        return self._request("GET", f"/orchestration/quotas/{resource}")

    def remediate_rules(self) -> Any:
        return self._request("GET", "/orchestration/remediation/rules")

    def remediate_history(self) -> Any:
        return self._request("GET", "/orchestration/remediation/history")

    def maintenance_list(self) -> Any:
        return self._request("GET", "/orchestration/maintenance")

    def maintenance_schedule(self, resource: str, window: str) -> Any:
        return self._request("POST", "/orchestration/maintenance", {"resource": resource, "window": window})

    def runbook_list(self) -> Any:
        return self._request("GET", "/orchestration/runbooks")

    def runbook_use(self, runbook_id: str, params: Optional[Dict] = None) -> Any:
        return self._request("POST", f"/orchestration/runbooks/{runbook_id}/execute", params or {})

    def chaos_experiments(self) -> Any:
        return self._request("GET", "/orchestration/chaos/experiments")

    def chaos_create(self, name: str, fault_type: str, target: str) -> Any:
        return self._request("POST", "/orchestration/chaos/experiments", {"name": name, "fault_type": fault_type, "target": target})

    def chaos_run(self, experiment_id: str) -> Any:
        return self._request("POST", f"/orchestration/chaos/experiments/{experiment_id}/run")

    def chaos_stop(self, experiment_id: str) -> Any:
        return self._request("POST", f"/orchestration/chaos/experiments/{experiment_id}/stop")

    def chaos_faults(self) -> Any:
        return self._request("GET", "/orchestration/chaos/faults")

    def heal_status(self) -> Any:
        return self._request("GET", "/orchestration/heal/status")

    def heal_history(self) -> Any:
        return self._request("GET", "/orchestration/heal/history")

    def heal_retrain(self) -> Any:
        return self._request("POST", "/orchestration/heal/retrain")

    def sdwan_status(self) -> Any:
        return self._request("GET", "/networking/sdwan/status")

    def sdwan_apps(self) -> Any:
        return self._request("GET", "/networking/sdwan/apps")

    def sdwan_create(self, name: str, provider: str, bandwidth: int) -> Any:
        return self._request("POST", "/networking/sdwan/links", {"name": name, "provider": provider, "bandwidth": bandwidth})

    def sdwan_delete(self, link_id: str) -> Any:
        return self._request("DELETE", f"/networking/sdwan/links/{link_id}")

    def sdwan_toggle(self, link_id: str) -> Any:
        return self._request("POST", f"/networking/sdwan/links/{link_id}/toggle")

    def vpn_configs(self) -> Any:
        return self._request("GET", "/networking/vpn/configs")

    def vpn_create(self, name: str, protocol: str, server: str) -> Any:
        return self._request("POST", "/networking/vpn/configs", {"name": name, "protocol": protocol, "server": server})

    def vpn_delete(self, config_id: str) -> Any:
        return self._request("DELETE", f"/networking/vpn/configs/{config_id}")

    def vpn_status(self, config_id: str) -> Any:
        return self._request("GET", f"/networking/vpn/configs/{config_id}")

    def dns_zones(self) -> Any:
        return self._request("GET", "/networking/dns/zones")

    def dns_create_zone(self, domain: str, ttl: int = 3600) -> Any:
        return self._request("POST", "/networking/dns/zones", {"domain": domain, "ttl": ttl})

    def dns_delete_zone(self, zone_id: str) -> Any:
        return self._request("DELETE", f"/networking/dns/zones/{zone_id}")

    def dns_records(self, zone_id: str) -> Any:
        return self._request("GET", f"/networking/dns/zones/{zone_id}/records")

    def dns_add_record(self, zone_id: str, record_type: str, name: str, value: str, ttl: int = 300) -> Any:
        return self._request("POST", f"/networking/dns/zones/{zone_id}/records", {"type": record_type, "name": name, "value": value, "ttl": ttl})

    def dns_delete_record(self, zone_id: str, record_id: str) -> Any:
        return self._request("DELETE", f"/networking/dns/zones/{zone_id}/records/{record_id}")

    def bgp_sessions(self) -> Any:
        return self._request("GET", "/networking/bgp/sessions")

    def bgp_create(self, name: str, asn: int, neighbor: str) -> Any:
        return self._request("POST", "/networking/bgp/sessions", {"name": name, "asn": asn, "neighbor": neighbor})

    def bgp_delete(self, session_id: str) -> Any:
        return self._request("DELETE", f"/networking/bgp/sessions/{session_id}")

    def bgp_routes(self, session_id: Optional[str] = None) -> Any:
        path = f"/networking/bgp/routes/{session_id}" if session_id else "/networking/bgp/routes"
        return self._request("GET", path)

    def proxy_rules(self) -> Any:
        return self._request("GET", "/networking/proxy/rules")

    def proxy_create(self, name: str, source: str, target: str) -> Any:
        return self._request("POST", "/networking/proxy/rules", {"name": name, "source": source, "target": target})

    def proxy_delete(self, rule_id: str) -> Any:
        return self._request("DELETE", f"/networking/proxy/rules/{rule_id}")

    def proxy_toggle(self, rule_id: str) -> Any:
        return self._request("POST", f"/networking/proxy/rules/{rule_id}/toggle")

    def segment_list(self) -> Any:
        return self._request("GET", "/networking/segments")

    def segment_create(self, name: str, cidr: str, vlan: Optional[int] = None) -> Any:
        return self._request("POST", "/networking/segments", {"name": name, "cidr": cidr, "vlan": vlan})

    def segment_delete(self, segment_id: str) -> Any:
        return self._request("DELETE", f"/networking/segments/{segment_id}")

    def capture_list(self) -> Any:
        return self._request("GET", "/networking/capture")

    def capture_start(self, interface: str, filter_expr: Optional[str] = None) -> Any:
        return self._request("POST", "/networking/capture/start", {"interface": interface, "filter": filter_expr})

    def capture_stop(self, capture_id: str) -> Any:
        return self._request("POST", f"/networking/capture/{capture_id}/stop")

    def dnsfilter_status(self) -> Any:
        return self._request("GET", "/networking/dnsfilter/status")

    def dnsfilter_rules(self) -> Any:
        return self._request("GET", "/networking/dnsfilter/rules")

    def dnsfilter_add(self, domain: str, action: str = "block") -> Any:
        return self._request("POST", "/networking/dnsfilter/rules", {"domain": domain, "action": action})

    def dnsfilter_remove(self, rule_id: str) -> Any:
        return self._request("DELETE", f"/networking/dnsfilter/rules/{rule_id}")

    def dhcp_leases(self) -> Any:
        return self._request("GET", "/networking/dhcp/leases")

    def netcost_show(self) -> Any:
        return self._request("GET", "/networking/cost")

    def netcost_budget(self, budget: float) -> Any:
        return self._request("POST", "/networking/cost/budget", {"budget": budget})

    def cell_networks(self) -> Any:
        return self._request("GET", "/networking/cell/networks")

    def cell_register(self, name: str, provider: str, apn: str) -> Any:
        return self._request("POST", "/networking/cell/networks", {"name": name, "provider": provider, "apn": apn})

    def cell_delete(self, network_id: str) -> Any:
        return self._request("DELETE", f"/networking/cell/networks/{network_id}")

    def cell_status(self, network_id: str) -> Any:
        return self._request("GET", f"/networking/cell/networks/{network_id}")

    def cell_sims(self, network_id: str) -> Any:
        return self._request("GET", f"/networking/cell/networks/{network_id}/sims")

    def cell_activate(self, sim_id: str) -> Any:
        return self._request("POST", f"/networking/cell/sims/{sim_id}/activate")

    def cell_deactivate(self, sim_id: str) -> Any:
        return self._request("POST", f"/networking/cell/sims/{sim_id}/deactivate")

    def trade_list(self) -> Any:
        return self._request("GET", "/marketplace/trades")

    def trade_create(self, resource: str, amount: float, price: float) -> Any:
        return self._request("POST", "/marketplace/trades", {"resource": resource, "amount": amount, "price": price})

    def trade_accept(self, trade_id: str) -> Any:
        return self._request("POST", f"/marketplace/trades/{trade_id}/accept")

    def trade_cancel(self, trade_id: str) -> Any:
        return self._request("POST", f"/marketplace/trades/{trade_id}/cancel")

    def appmarket_list(self) -> Any:
        return self._request("GET", "/marketplace/apps")

    def appmarket_install(self, app_id: str, target: str) -> Any:
        return self._request("POST", f"/marketplace/apps/{app_id}/install", {"target": target})

    def appmarket_installations(self) -> Any:
        return self._request("GET", "/marketplace/installations")

    def ppu_metrics(self) -> Any:
        return self._request("GET", "/marketplace/ppu/metrics")

    def ppu_usage(self) -> Any:
        return self._request("GET", "/marketplace/ppu/usage")

    def ppu_budget(self) -> Any:
        return self._request("GET", "/marketplace/ppu/budget")

    def reseller_list(self) -> Any:
        return self._request("GET", "/marketplace/resellers")

    def reseller_create(self, name: str, email: str, commission: float) -> Any:
        return self._request("POST", "/marketplace/resellers", {"name": name, "email": email, "commission": commission})

    def reseller_delete(self, reseller_id: str) -> Any:
        return self._request("DELETE", f"/marketplace/resellers/{reseller_id}")

    def reseller_analytics(self, reseller_id: str) -> Any:
        return self._request("GET", f"/marketplace/resellers/{reseller_id}/analytics")

    def whitelabel_settings(self) -> Any:
        return self._request("GET", "/marketplace/whitelabel")

    def sla_list(self) -> Any:
        return self._request("GET", "/marketplace/sla")

    def sla_create(self, name: str, uptime: float, response_time: int) -> Any:
        return self._request("POST", "/marketplace/sla", {"name": name, "uptime": uptime, "response_time": response_time})

    def sla_delete(self, sla_id: str) -> Any:
        return self._request("DELETE", f"/marketplace/sla/{sla_id}")

    def sla_status(self, sla_id: str) -> Any:
        return self._request("GET", f"/marketplace/sla/{sla_id}")

    def credit_list(self) -> Any:
        return self._request("GET", "/marketplace/credits")

    def credit_issue(self, customer_id: str, amount: float, reason: str) -> Any:
        return self._request("POST", "/marketplace/credits", {"customer_id": customer_id, "amount": amount, "reason": reason})

    def crypto_wallets(self) -> Any:
        return self._request("GET", "/marketplace/crypto/wallets")

    def crypto_create_wallet(self, currency: str, label: str) -> Any:
        return self._request("POST", "/marketplace/crypto/wallets", {"currency": currency, "label": label})

    def crypto_transactions(self, wallet_id: Optional[str] = None) -> Any:
        path = f"/marketplace/crypto/transactions/{wallet_id}" if wallet_id else "/marketplace/crypto/transactions"
        return self._request("GET", path)

    def crypto_rates(self) -> Any:
        return self._request("GET", "/marketplace/crypto/rates")

    def plans_list(self) -> Any:
        return self._request("GET", "/marketplace/plans")

    def plans_create(self, name: str, price: float, features: list) -> Any:
        return self._request("POST", "/marketplace/plans", {"name": name, "price": price, "features": features})

    def plans_delete(self, plan_id: str) -> Any:
        return self._request("DELETE", f"/marketplace/plans/{plan_id}")

    def plans_subscriptions(self) -> Any:
        return self._request("GET", "/marketplace/plans/subscriptions")

    def reco_list(self) -> Any:
        return self._request("GET", "/marketplace/recommendations")

    def reco_summary(self) -> Any:
        return self._request("GET", "/marketplace/recommendations/summary")

    def reco_implement(self, reco_id: str) -> Any:
        return self._request("POST", f"/marketplace/recommendations/{reco_id}/implement")

    def reco_dismiss(self, reco_id: str) -> Any:
        return self._request("POST", f"/marketplace/recommendations/{reco_id}/dismiss")

    def tax_rates(self) -> Any:
        return self._request("GET", "/marketplace/tax/rates")

    def tax_invoices(self) -> Any:
        return self._request("GET", "/marketplace/tax/invoices")

    def tax_generate(self, customer_id: str, period: str) -> Any:
        return self._request("POST", "/marketplace/tax/invoices/generate", {"customer_id": customer_id, "period": period})

    def tax_pay(self, invoice_id: str) -> Any:
        return self._request("POST", f"/marketplace/tax/invoices/{invoice_id}/pay")

    def tax_summary(self) -> Any:
        return self._request("GET", "/marketplace/tax/summary")

    def tax_file(self, tax_year: int) -> Any:
        return self._request("POST", "/marketplace/tax/file", {"tax_year": tax_year})

    def loyalty_status(self) -> Any:
        return self._request("GET", "/marketplace/loyalty/status")

    def loyalty_badges(self) -> Any:
        return self._request("GET", "/marketplace/loyalty/badges")

    def loyalty_rewards(self) -> Any:
        return self._request("GET", "/marketplace/loyalty/rewards")

    def loyalty_redeem(self, reward_id: str) -> Any:
        return self._request("POST", f"/marketplace/loyalty/rewards/{reward_id}/redeem")

    def loyalty_leaderboard(self) -> Any:
        return self._request("GET", "/marketplace/loyalty/leaderboard")

    def cx_health_list(self) -> Any:
        return self._request("GET", "/cx/health")

    def cx_health_get(self, customer_id: str) -> Any:
        return self._request("GET", f"/cx/health/{customer_id}")

    def cx_health_compute(self, customer_id: str) -> Any:
        return self._request("POST", f"/cx/health/{customer_id}/compute")

    def cx_health_history(self, customer_id: str) -> Any:
        return self._request("GET", f"/cx/health/{customer_id}/history")

    def cx_health_stats(self) -> Any:
        return self._request("GET", "/cx/health/stats")

    def cx_ticket_list(self) -> Any:
        return self._request("GET", "/cx/tickets")

    def cx_ticket_create(self, customer_id: str, subject: str, description: str, priority: str = "medium") -> Any:
        return self._request("POST", "/cx/tickets", {"customer_id": customer_id, "subject": subject, "description": description, "priority": priority})

    def cx_ticket_get(self, ticket_id: str) -> Any:
        return self._request("GET", f"/cx/tickets/{ticket_id}")

    def cx_ticket_status(self, ticket_id: str, status: str) -> Any:
        return self._request("PATCH", f"/cx/tickets/{ticket_id}/status", {"status": status})

    def cx_ticket_comment(self, ticket_id: str, comment: str) -> Any:
        return self._request("POST", f"/cx/tickets/{ticket_id}/comments", {"comment": comment})

    def cx_ticket_assign(self, ticket_id: str, assignee: str) -> Any:
        return self._request("POST", f"/cx/tickets/{ticket_id}/assign", {"assignee": assignee})

    def cx_ticket_stats(self) -> Any:
        return self._request("GET", "/cx/tickets/stats")

    def cx_sla_list(self) -> Any:
        return self._request("GET", "/cx/sla")

    def cx_sla_create(self, name: str, response_time: int, resolution_time: int) -> Any:
        return self._request("POST", "/cx/sla", {"name": name, "response_time": response_time, "resolution_time": resolution_time})

    def cx_canned_list(self) -> Any:
        return self._request("GET", "/cx/canned-responses")

    def cx_canned_create(self, title: str, content: str, category: str) -> Any:
        return self._request("POST", "/cx/canned-responses", {"title": title, "content": content, "category": category})

    def cx_sentiment_analyze(self, customer_id: str) -> Any:
        return self._request("POST", f"/cx/sentiment/{customer_id}/analyze")

    def cx_sentiment_profile(self, customer_id: str) -> Any:
        return self._request("GET", f"/cx/sentiment/{customer_id}")

    def cx_sentiment_interactions(self, customer_id: str) -> Any:
        return self._request("GET", f"/cx/sentiment/{customer_id}/interactions")

    def cx_sentiment_trends(self) -> Any:
        return self._request("GET", "/cx/sentiment/trends")

    def cx_sentiment_alerts(self) -> Any:
        return self._request("GET", "/cx/sentiment/alerts")

    def cx_adoption_summary(self) -> Any:
        return self._request("GET", "/cx/adoption/summary")

    def cx_adoption_features(self) -> Any:
        return self._request("GET", "/cx/adoption/features")

    def cx_adoption_track(self, customer_id: str, feature: str) -> Any:
        return self._request("POST", f"/cx/adoption/{customer_id}/track", {"feature": feature})

    def cx_adoption_recommendations(self, customer_id: str) -> Any:
        return self._request("GET", f"/cx/adoption/{customer_id}/recommendations")

    def cx_adoption_stats(self) -> Any:
        return self._request("GET", "/cx/adoption/stats")

    def cx_onboarding_start(self, customer_id: str, plan: str) -> Any:
        return self._request("POST", f"/cx/onboarding/{customer_id}/start", {"plan": plan})

    def cx_onboarding_get(self, customer_id: str) -> Any:
        return self._request("GET", f"/cx/onboarding/{customer_id}")

    def cx_onboarding_step(self, customer_id: str, step: str) -> Any:
        return self._request("POST", f"/cx/onboarding/{customer_id}/step/{step}")

    def cx_onboarding_stats(self) -> Any:
        return self._request("GET", "/cx/onboarding/stats")

    def cx_kb_list(self, category: Optional[str] = None) -> Any:
        path = f"/cx/kb?category={category}" if category else "/cx/kb"
        return self._request("GET", path)

    def cx_kb_create(self, title: str, content: str, category: str) -> Any:
        return self._request("POST", "/cx/kb", {"title": title, "content": content, "category": category})

    def cx_kb_get(self, article_id: str) -> Any:
        return self._request("GET", f"/cx/kb/{article_id}")

    def cx_kb_update(self, article_id: str, content: str) -> Any:
        return self._request("PATCH", f"/cx/kb/{article_id}", {"content": content})

    def cx_kb_search(self, query: str) -> Any:
        return self._request("GET", f"/cx/kb/search?q={query}")

    def cx_kb_categories(self) -> Any:
        return self._request("GET", "/cx/kb/categories")

    def cx_kb_feedback(self, article_id: str, helpful: bool) -> Any:
        return self._request("POST", f"/cx/kb/{article_id}/feedback", {"helpful": helpful})

    def cx_community_posts(self) -> Any:
        return self._request("GET", "/cx/community/posts")

    def cx_community_create(self, title: str, content: str, category: str) -> Any:
        return self._request("POST", "/cx/community/posts", {"title": title, "content": content, "category": category})

    def cx_community_get(self, post_id: str) -> Any:
        return self._request("GET", f"/cx/community/posts/{post_id}")

    def cx_community_vote(self, post_id: str, vote: int) -> Any:
        return self._request("POST", f"/cx/community/posts/{post_id}/vote", {"vote": vote})

    def cx_community_comment(self, post_id: str, content: str) -> Any:
        return self._request("POST", f"/cx/community/posts/{post_id}/comments", {"content": content})

    def cx_community_comments(self, post_id: str) -> Any:
        return self._request("GET", f"/cx/community/posts/{post_id}/comments")

    def cx_community_requests(self) -> Any:
        return self._request("GET", "/cx/community/feature-requests")

    def cx_community_categories(self) -> Any:
        return self._request("GET", "/cx/community/categories")

    def cx_community_leaderboard(self) -> Any:
        return self._request("GET", "/cx/community/leaderboard")

    def cx_community_stats(self) -> Any:
        return self._request("GET", "/cx/community/stats")

    def cx_comm_send(self, customer_id: str, template: str, channel: str) -> Any:
        return self._request("POST", f"/cx/comm/{customer_id}/send", {"template": template, "channel": channel})

    def cx_comm_batches(self) -> Any:
        return self._request("GET", "/cx/comm/batches")

    def cx_comm_batch(self, batch_id: str) -> Any:
        return self._request("GET", f"/cx/comm/batches/{batch_id}")

    def cx_comm_maintenance_schedule(self, customer_id: str, message: str, scheduled_at: str) -> Any:
        return self._request("POST", f"/cx/comm/{customer_id}/maintenance", {"message": message, "scheduled_at": scheduled_at})

    def cx_comm_maintenance_list(self) -> Any:
        return self._request("GET", "/cx/comm/maintenance")

    def cx_comm_maintenance_complete(self, maintenance_id: str) -> Any:
        return self._request("POST", f"/cx/comm/maintenance/{maintenance_id}/complete")

    def cx_comm_templates(self) -> Any:
        return self._request("GET", "/cx/comm/templates")

    def cx_comm_template_create(self, name: str, subject: str, body: str) -> Any:
        return self._request("POST", "/cx/comm/templates", {"name": name, "subject": subject, "body": body})

    def cx_nps_create(self, name: str, targets: list) -> Any:
        return self._request("POST", "/cx/nps/surveys", {"name": name, "targets": targets})

    def cx_nps_list(self) -> Any:
        return self._request("GET", "/cx/nps/surveys")

    def cx_nps_get(self, survey_id: str) -> Any:
        return self._request("GET", f"/cx/nps/surveys/{survey_id}")

    def cx_nps_send(self, survey_id: str) -> Any:
        return self._request("POST", f"/cx/nps/surveys/{survey_id}/send")

    def cx_nps_respond(self, survey_id: str, score: int, comment: Optional[str] = None) -> Any:
        return self._request("POST", f"/cx/nps/surveys/{survey_id}/respond", {"score": score, "comment": comment or ""})

    def cx_nps_score(self, survey_id: str) -> Any:
        return self._request("GET", f"/cx/nps/surveys/{survey_id}/score")

    def cx_nps_trend(self, survey_id: str) -> Any:
        return self._request("GET", f"/cx/nps/surveys/{survey_id}/trend")

    def cx_nps_detractors(self, survey_id: str) -> Any:
        return self._request("GET", f"/cx/nps/surveys/{survey_id}/detractors")

    def cx_nps_stats(self) -> Any:
        return self._request("GET", "/cx/nps/stats")

    def cx_success_plays(self) -> Any:
        return self._request("GET", "/cx/success/plays")

    def cx_success_create(self, name: str, trigger: str, actions: list) -> Any:
        return self._request("POST", "/cx/success/plays", {"name": name, "trigger": trigger, "actions": actions})

    def cx_success_status(self, play_id: str) -> Any:
        return self._request("GET", f"/cx/success/plays/{play_id}")

    def cx_success_trigger(self, play_id: str, customer_id: str) -> Any:
        return self._request("POST", f"/cx/success/plays/{play_id}/trigger", {"customer_id": customer_id})

    def cx_success_executions(self, play_id: str) -> Any:
        return self._request("GET", f"/cx/success/plays/{play_id}/executions")

    def cx_success_stats(self) -> Any:
        return self._request("GET", "/cx/success/stats")

    def aiops_rca_analyze(self, incident_id: str) -> Any:
        return self._request("POST", f"/aiops/rca/{incident_id}/analyze")

    def aiops_rca_incidents(self) -> Any:
        return self._request("GET", "/aiops/rca/incidents")

    def aiops_rca_events(self, incident_id: str) -> Any:
        return self._request("GET", f"/aiops/rca/{incident_id}/events")

    def aiops_rca_deps(self, incident_id: str) -> Any:
        return self._request("GET", f"/aiops/rca/{incident_id}/dependencies")

    def aiops_dem_list(self) -> Any:
        return self._request("GET", "/aiops/dem/monitors")

    def aiops_dem_create(self, name: str, url: str, interval: int = 60) -> Any:
        return self._request("POST", "/aiops/dem/monitors", {"name": name, "url": url, "interval": interval})

    def aiops_dem_check(self, monitor_id: str) -> Any:
        return self._request("POST", f"/aiops/dem/monitors/{monitor_id}/check")

    def aiops_dem_stats(self, monitor_id: str) -> Any:
        return self._request("GET", f"/aiops/dem/monitors/{monitor_id}/stats")

    def aiops_dem_summary(self) -> Any:
        return self._request("GET", "/aiops/dem/summary")

    def aiops_alert_ingest(self, source: str, message: str, severity: str = "info") -> Any:
        return self._request("POST", "/aiops/alerts/ingest", {"source": source, "message": message, "severity": severity})

    def aiops_alert_incidents(self) -> Any:
        return self._request("GET", "/aiops/alerts/incidents")

    def aiops_alert_stats(self) -> Any:
        return self._request("GET", "/aiops/alerts/stats")

    def aiops_alert_suppress(self, alert_id: str) -> Any:
        return self._request("POST", f"/aiops/alerts/{alert_id}/suppress")

    def aiops_scaling_predict(self, resource: str) -> Any:
        return self._request("POST", f"/aiops/scaling/{resource}/predict")

    def aiops_scaling_metrics(self, resource: str) -> Any:
        return self._request("GET", f"/aiops/scaling/{resource}/metrics")

    def aiops_scaling_policy(self, resource: str, min_instances: int, max_instances: int) -> Any:
        return self._request("POST", f"/aiops/scaling/{resource}/policy", {"min": min_instances, "max": max_instances})

    def aiops_scaling_summary(self) -> Any:
        return self._request("GET", "/aiops/scaling/summary")

    def aiops_health_services(self) -> Any:
        return self._request("GET", "/aiops/health/services")

    def aiops_health_register(self, name: str, endpoint: str, interval: int) -> Any:
        return self._request("POST", "/aiops/health/services", {"name": name, "endpoint": endpoint, "interval": interval})

    def aiops_health_forecast(self, service_id: str) -> Any:
        return self._request("GET", f"/aiops/health/{service_id}/forecast")

    def aiops_health_dashboard(self) -> Any:
        return self._request("GET", "/aiops/health/dashboard")

    def aiops_assistant_message(self, message: str) -> Any:
        return self._request("POST", "/aiops/assistant/message", {"message": message})

    def aiops_assistant_stats(self) -> Any:
        return self._request("GET", "/aiops/assistant/stats")

    def aiops_change_plan(self, service: str, change: str, risk: str) -> Any:
        return self._request("POST", "/aiops/change/plan", {"service": service, "change": change, "risk": risk})

    def aiops_change_approve(self, plan_id: str) -> Any:
        return self._request("POST", f"/aiops/change/{plan_id}/approve")

    def aiops_change_stats(self) -> Any:
        return self._request("GET", "/aiops/change/stats")

    def aiops_capacity_recommend(self) -> Any:
        return self._request("GET", "/aiops/capacity/recommendations")

    def aiops_capacity_usage(self, resource: str) -> Any:
        return self._request("GET", f"/aiops/capacity/{resource}/usage")

    def aiops_capacity_simulate(self, resource: str, load: float) -> Any:
        return self._request("POST", f"/aiops/capacity/{resource}/simulate", {"load": load})

    def aiops_capacity_summary(self) -> Any:
        return self._request("GET", "/aiops/capacity/summary")

    def aiops_chatbot_message(self, message: str) -> Any:
        return self._request("POST", "/aiops/chatbot/message", {"message": message})

    def aiops_chatbot_tasks(self) -> Any:
        return self._request("GET", "/aiops/chatbot/tasks")

    def aiops_chatbot_analytics(self) -> Any:
        return self._request("GET", "/aiops/chatbot/analytics")

    def finops_commitment_list(self) -> Any:
        return self._request("GET", "/finops/commitments")

    def finops_commitment_summary(self) -> Any:
        return self._request("GET", "/finops/commitments/summary")

    def finops_commitment_implement(self, commitment_id: str) -> Any:
        return self._request("POST", f"/finops/commitments/{commitment_id}/implement")

    def finops_commitment_commitments(self) -> Any:
        return self._request("GET", "/finops/commitments/list")

    def finops_spot_list(self) -> Any:
        return self._request("GET", "/finops/spot/advice")

    def finops_spot_create(self, name: str, instance_type: str, max_price: float, region: str) -> Any:
        return self._request("POST", "/finops/spot/requests", {"name": name, "instance_type": instance_type, "max_price": max_price, "region": region})

    def finops_spot_get(self, request_id: str) -> Any:
        return self._request("GET", f"/finops/spot/requests/{request_id}")

    def finops_spot_instances(self) -> Any:
        return self._request("GET", "/finops/spot/instances")

    def finops_spot_savings(self) -> Any:
        return self._request("GET", "/finops/spot/savings")

    def finops_uoe_metrics(self) -> Any:
        return self._request("GET", "/finops/uoe/metrics")

    def finops_uoe_record(self, metric: str, value: float) -> Any:
        return self._request("POST", "/finops/uoe/metrics", {"metric": metric, "value": value})

    def finops_uoe_targets(self) -> Any:
        return self._request("GET", "/finops/uoe/targets")

    def finops_uoe_set_target(self, metric: str, target: float) -> Any:
        return self._request("POST", "/finops/uoe/targets", {"metric": metric, "target": target})

    def finops_uoe_violations(self) -> Any:
        return self._request("GET", "/finops/uoe/violations")

    def finops_uoe_overview(self) -> Any:
        return self._request("GET", "/finops/uoe/overview")

    def finops_anomaly_list(self) -> Any:
        return self._request("GET", "/finops/anomalies")

    def finops_anomaly_summary(self) -> Any:
        return self._request("GET", "/finops/anomalies/summary")

    def finops_anomaly_investigate(self, anomaly_id: str) -> Any:
        return self._request("POST", f"/finops/anomalies/{anomaly_id}/investigate")

    def finops_anomaly_resolve(self, anomaly_id: str) -> Any:
        return self._request("POST", f"/finops/anomalies/{anomaly_id}/resolve")

    def finops_anomaly_profiles(self) -> Any:
        return self._request("GET", "/finops/anomalies/profiles")

    def finops_anomaly_create_profile(self, name: str, rules: Any) -> Any:
        return self._request("POST", "/finops/anomalies/profiles", {"name": name, "rules": rules})

    def finops_budget_list(self) -> Any:
        return self._request("GET", "/finops/budgets")

    def finops_budget_create(self, name: str, amount: float, period: str) -> Any:
        return self._request("POST", "/finops/budgets", {"name": name, "amount": amount, "period": period})

    def finops_budget_get(self, budget_id: str) -> Any:
        return self._request("GET", f"/finops/budgets/{budget_id}")

    def finops_budget_spend(self, budget_id: str) -> Any:
        return self._request("GET", f"/finops/budgets/{budget_id}/spend")

    def finops_budget_forecast(self, budget_id: str) -> Any:
        return self._request("GET", f"/finops/budgets/{budget_id}/forecast")

    def finops_budget_scenario(self, budget_id: str, adjustments: Any) -> Any:
        return self._request("POST", f"/finops/budgets/{budget_id}/scenario", {"adjustments": adjustments})

    def finops_budget_summary(self) -> Any:
        return self._request("GET", "/finops/budgets/summary")

    def finops_rightsizing_list(self) -> Any:
        return self._request("GET", "/finops/rightsizing")

    def finops_rightsizing_summary(self) -> Any:
        return self._request("GET", "/finops/rightsizing/summary")

    def finops_rightsizing_approve(self, suggestion_id: str) -> Any:
        return self._request("POST", f"/finops/rightsizing/{suggestion_id}/approve")

    def finops_rightsizing_implement(self, suggestion_id: str) -> Any:
        return self._request("POST", f"/finops/rightsizing/{suggestion_id}/implement")

    def finops_rightsizing_dismiss(self, suggestion_id: str) -> Any:
        return self._request("POST", f"/finops/rightsizing/{suggestion_id}/dismiss")

    def finops_waste_list(self) -> Any:
        return self._request("GET", "/finops/waste")

    def finops_waste_summary(self) -> Any:
        return self._request("GET", "/finops/waste/summary")

    def finops_waste_scan(self) -> Any:
        return self._request("POST", "/finops/waste/scan")

    def finops_waste_approve(self, waste_id: str) -> Any:
        return self._request("POST", f"/finops/waste/{waste_id}/approve")

    def finops_waste_cleanup(self, waste_id: str) -> Any:
        return self._request("POST", f"/finops/waste/{waste_id}/cleanup")

    def finops_waste_dismiss(self, waste_id: str) -> Any:
        return self._request("POST", f"/finops/waste/{waste_id}/dismiss")

    def finops_carbon_list(self) -> Any:
        return self._request("GET", "/finops/carbon")

    def finops_carbon_assets(self) -> Any:
        return self._request("GET", "/finops/carbon/assets")

    def finops_carbon_register(self, name: str, asset_type: str, emissions: float) -> Any:
        return self._request("POST", "/finops/carbon/assets", {"name": name, "asset_type": asset_type, "emissions": emissions})

    def finops_carbon_sustainability(self) -> Any:
        return self._request("GET", "/finops/carbon/sustainability")

    def finops_arbitrage_workloads(self) -> Any:
        return self._request("GET", "/finops/arbitrage/workloads")

    def finops_arbitrage_comparisons(self, workload_id: str) -> Any:
        return self._request("GET", f"/finops/arbitrage/workloads/{workload_id}/compare")

    def finops_arbitrage_savings(self) -> Any:
        return self._request("GET", "/finops/arbitrage/savings")

    def finops_reports_list(self) -> Any:
        return self._request("GET", "/finops/reports")

    def finops_reports_generate(self, report_type: str, period: str) -> Any:
        return self._request("POST", "/finops/reports", {"type": report_type, "period": period})

    def finops_reports_summary(self) -> Any:
        return self._request("GET", "/finops/reports/summary")

    def soar_playbooks(self) -> Any:
        return self._request("GET", "/soc/soar/playbooks")

    def soar_playbook(self, playbook_id: str) -> Any:
        return self._request("GET", f"/soc/soar/playbooks/{playbook_id}")

    def soar_run(self, playbook_id: str, params: Optional[Dict] = None) -> Any:
        return self._request("POST", f"/soc/soar/playbooks/{playbook_id}/run", params or {})

    def soar_create(self, name: str, steps: list, trigger: str) -> Any:
        return self._request("POST", "/soc/soar/playbooks", {"name": name, "steps": steps, "trigger": trigger})

    def soar_cases(self) -> Any:
        return self._request("GET", "/soc/soar/cases")

    def soar_connectors(self) -> Any:
        return self._request("GET", "/soc/soar/connectors")

    def ti_feeds(self) -> Any:
        return self._request("GET", "/soc/threatintel/feeds")

    def ti_iocs(self, feed_id: Optional[str] = None) -> Any:
        path = f"/soc/threatintel/iocs/{feed_id}" if feed_id else "/soc/threatintel/iocs"
        return self._request("GET", path)

    def ti_blocklist(self) -> Any:
        return self._request("GET", "/soc/threatintel/blocklist")

    def ti_add_ioc(self, ioc: str, ioc_type: str, confidence: str) -> Any:
        return self._request("POST", "/soc/threatintel/iocs", {"ioc": ioc, "type": ioc_type, "confidence": confidence})

    def ti_analyze(self, ioc: str) -> Any:
        return self._request("POST", "/soc/threatintel/analyze", {"ioc": ioc})

    def decoy_list(self) -> Any:
        return self._request("GET", "/soc/decoy/decoys")

    def decoy_tokens(self) -> Any:
        return self._request("GET", "/soc/decoy/tokens")

    def decoy_create(self, name: str, decoy_type: str, target: str) -> Any:
        return self._request("POST", "/soc/decoy/decoys", {"name": name, "type": decoy_type, "target": target})

    def decoy_deploy(self, decoy_id: str) -> Any:
        return self._request("POST", f"/soc/decoy/decoys/{decoy_id}/deploy")

    def vuln_cves(self, severity: Optional[str] = None) -> Any:
        path = f"/soc/vuln/cves?severity={severity}" if severity else "/soc/vuln/cves"
        return self._request("GET", path)

    def vuln_scan(self, target: str) -> Any:
        return self._request("POST", "/soc/vuln/scans", {"target": target})

    def vuln_patch(self, cve_id: str) -> Any:
        return self._request("POST", f"/soc/vuln/cves/{cve_id}/patch")

    def vuln_summary(self) -> Any:
        return self._request("GET", "/soc/vuln/summary")

    def ir_list(self) -> Any:
        return self._request("GET", "/soc/incidents")

    def ir_get(self, incident_id: str) -> Any:
        return self._request("GET", f"/soc/incidents/{incident_id}")

    def ir_create(self, title: str, severity: str, description: str) -> Any:
        return self._request("POST", "/soc/incidents", {"title": title, "severity": severity, "description": description})

    def ir_status(self, incident_id: str, status: str) -> Any:
        return self._request("PATCH", f"/soc/incidents/{incident_id}/status", {"status": status})

    def ir_evidence(self, incident_id: str, file: str) -> Any:
        return self._request("POST", f"/soc/incidents/{incident_id}/evidence", {"file": file})

    def ir_timeline(self, incident_id: str) -> Any:
        return self._request("GET", f"/soc/incidents/{incident_id}/timeline")

    def ir_report(self, incident_id: str) -> Any:
        return self._request("GET", f"/soc/incidents/{incident_id}/report")

    def ueba_entities(self) -> Any:
        return self._request("GET", "/soc/ueba/entities")

    def ueba_alerts(self) -> Any:
        return self._request("GET", "/soc/ueba/alerts")

    def cspm_accounts(self) -> Any:
        return self._request("GET", "/soc/cspm/accounts")

    def cspm_results(self, account_id: str) -> Any:
        return self._request("GET", f"/soc/cspm/accounts/{account_id}/results")

    def cspm_scan(self, account_id: str) -> Any:
        return self._request("POST", f"/soc/cspm/accounts/{account_id}/scan")

    def ndr_flows(self) -> Any:
        return self._request("GET", "/soc/ndr/flows")

    def ndr_alerts(self) -> Any:
        return self._request("GET", "/soc/ndr/alerts")

    def secrets_findings(self) -> Any:
        return self._request("GET", "/soc/secrets/findings")

    def secrets_targets(self) -> Any:
        return self._request("GET", "/soc/secrets/targets")

    def secrets_rotate(self, finding_id: str) -> Any:
        return self._request("POST", f"/soc/secrets/findings/{finding_id}/rotate")

    def training_modules(self) -> Any:
        return self._request("GET", "/soc/training/modules")

    def training_campaigns(self) -> Any:
        return self._request("GET", "/soc/training/campaigns")

    def training_assignments(self) -> Any:
        return self._request("GET", "/soc/training/assignments")

    def devportal_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/devportal/apis")

    def devportal_register(self, name: str, version: str, spec_url: str) -> Any:
        return self._request("POST", "/v4/platform-engineering/devportal/apis", {"name": name, "version": version, "spec_url": spec_url})

    def devportal_get(self, api_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/devportal/apis/{api_id}")

    def devportal_summary(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/devportal/summary")

    def scaffold_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/scaffold/templates")

    def scaffold_generate(self, template: str, name: str, params: Optional[Dict] = None) -> Any:
        return self._request("POST", "/v4/platform-engineering/scaffold/generate", {"template": template, "name": name, "params": params or {}})

    def scaffold_status(self, generation_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/scaffold/{generation_id}")

    def scaffold_step(self, generation_id: str, step: str, data: Any) -> Any:
        return self._request("POST", f"/v4/platform-engineering/scaffold/{generation_id}/step/{step}", {"data": data})

    def catalog_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/service-catalog")

    def catalog_register(self, name: str, description: str, version: str) -> Any:
        return self._request("POST", "/v4/platform-engineering/service-catalog", {"name": name, "description": description, "version": version})

    def catalog_get(self, service_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/service-catalog/{service_id}")

    def catalog_score(self, service_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/service-catalog/{service_id}/score")

    def catalog_summary(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/service-catalog/summary")

    def scorecards_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/scorecards")

    def scorecards_create(self, name: str, criteria: list) -> Any:
        return self._request("POST", "/v4/platform-engineering/scorecards", {"name": name, "criteria": criteria})

    def scorecards_get(self, scorecard_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/scorecards/{scorecard_id}")

    def scorecards_update(self, scorecard_id: str, criteria: list) -> Any:
        return self._request("PATCH", f"/v4/platform-engineering/scorecards/{scorecard_id}", {"criteria": criteria})

    def scorecards_summary(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/scorecards/summary")

    def templatereg_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/template-registry")

    def templatereg_create(self, name: str, template_type: str, content: str) -> Any:
        return self._request("POST", "/v4/platform-engineering/template-registry", {"name": name, "type": template_type, "content": content})

    def templatereg_get(self, template_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/template-registry/{template_id}")

    def templatereg_use(self, template_id: str, params: Optional[Dict] = None) -> Any:
        return self._request("POST", f"/v4/platform-engineering/template-registry/{template_id}/use", params or {})

    def templatereg_summary(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/template-registry/summary")

    def techdebt_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/techdebt")

    def techdebt_report(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/techdebt/report")

    def techdebt_get(self, item_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/techdebt/{item_id}")

    def techdebt_fix(self, item_id: str) -> Any:
        return self._request("POST", f"/v4/platform-engineering/techdebt/{item_id}/fix")

    def techdebt_summary(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/techdebt/summary")

    def environments_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/environments")

    def environments_create(self, name: str, env_type: str, template: str) -> Any:
        return self._request("POST", "/v4/platform-engineering/environments", {"name": name, "type": env_type, "template": template})

    def environments_get(self, env_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/environments/{env_id}")

    def environments_delete(self, env_id: str) -> Any:
        return self._request("DELETE", f"/v4/platform-engineering/environments/{env_id}")

    def environments_extend(self, env_id: str, ttl_hours: int) -> Any:
        return self._request("POST", f"/v4/platform-engineering/environments/{env_id}/extend", {"ttl_hours": ttl_hours})

    def environments_summary(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/environments/summary")

    def apicatalog_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/api-catalog")

    def apicatalog_register(self, name: str, version: str, spec: str) -> Any:
        return self._request("POST", "/v4/platform-engineering/api-catalog", {"name": name, "version": version, "spec": spec})

    def apicatalog_get(self, api_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/api-catalog/{api_id}")

    def apicatalog_summary(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/api-catalog/summary")

    def docgen_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/docgen/templates")

    def docgen_generate(self, template: str, service: str, params: Optional[Dict] = None) -> Any:
        return self._request("POST", "/v4/platform-engineering/docgen/generate", {"template": template, "service": service, "params": params or {}})

    def docgen_get(self, doc_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/docgen/{doc_id}")

    def docgen_summary(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/docgen/summary")

    def pulse_list(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/pulse/surveys")

    def pulse_create(self, title: str, questions: list) -> Any:
        return self._request("POST", "/v4/platform-engineering/pulse/surveys", {"title": title, "questions": questions})

    def pulse_respond(self, survey_id: str, responses: dict) -> Any:
        return self._request("POST", f"/v4/platform-engineering/pulse/{survey_id}/respond", {"responses": responses})

    def pulse_results(self, survey_id: str) -> Any:
        return self._request("GET", f"/v4/platform-engineering/pulse/{survey_id}/results")

    def pulse_summary(self) -> Any:
        return self._request("GET", "/v4/platform-engineering/pulse/summary")

    def cc_status(self) -> Any:
        return self._request("GET", "/api/v1/cc/status")

    def cc_scan(self, framework: str) -> Any:
        return self._request("POST", "/api/v1/cc/scan", {"framework": framework})

    def cc_alerts(self) -> Any:
        return self._request("GET", "/api/v1/cc/alerts")

    def cc_summary(self) -> Any:
        return self._request("GET", "/api/v1/cc/summary")

    def cc_remediate(self, finding_id: str) -> Any:
        return self._request("POST", f"/api/v1/cc/findings/{finding_id}/remediate")

    def cc_drift(self) -> Any:
        return self._request("GET", "/api/v1/cc/drift")

    def cc_compare(self, scan_id_1: str, scan_id_2: str) -> Any:
        return self._request("GET", f"/api/v1/cc/compare?scan1={scan_id_1}&scan2={scan_id_2}")

    def cc_report(self, framework: str) -> Any:
        return self._request("GET", f"/api/v1/cc/report/{framework}")

    def cc_schedule(self, framework: str, cron: str) -> Any:
        return self._request("POST", "/api/v1/cc/schedule", {"framework": framework, "cron": cron})

    def cc_weakest(self) -> Any:
        return self._request("GET", "/api/v1/cc/weakest")

    def ec_list(self) -> Any:
        return self._request("GET", "/api/v1/evidence")

    def ec_collect(self, evidence_type: str, target: str) -> Any:
        return self._request("POST", "/api/v1/evidence/collect", {"type": evidence_type, "target": target})

    def ec_packages(self) -> Any:
        return self._request("GET", "/api/v1/evidence/packages")

    def ec_stats(self) -> Any:
        return self._request("GET", "/api/v1/evidence/stats")

    def ec_auto_collect(self) -> Any:
        return self._request("POST", "/api/v1/evidence/auto-collect")

    def ec_search(self, query: str) -> Any:
        return self._request("GET", f"/api/v1/evidence/search?q={query}")

    def ec_validate(self, evidence_id: str) -> Any:
        return self._request("POST", f"/api/v1/evidence/{evidence_id}/validate")

    def ec_package_create(self, name: str, evidence_ids: list) -> Any:
        return self._request("POST", "/api/v1/evidence/packages", {"name": name, "evidence_ids": evidence_ids})

    def ec_expired(self) -> Any:
        return self._request("GET", "/api/v1/evidence/expired")

    def ec_custody(self, evidence_id: str) -> Any:
        return self._request("GET", f"/api/v1/evidence/{evidence_id}/custody")

    def cac_list(self) -> Any:
        return self._request("GET", "/api/v1/cac/policies")

    def cac_evaluate(self, policy_id: str) -> Any:
        return self._request("POST", f"/api/v1/cac/policies/{policy_id}/evaluate")

    def cac_templates(self) -> Any:
        return self._request("GET", "/api/v1/cac/templates")

    def cac_stats(self) -> Any:
        return self._request("GET", "/api/v1/cac/stats")

    def cac_create(self, name: str, framework: str, rules: Any) -> Any:
        return self._request("POST", "/api/v1/cac/policies", {"name": name, "framework": framework, "rules": rules})

    def cac_gap(self) -> Any:
        return self._request("GET", "/api/v1/cac/gap-analysis")

    def cac_test(self, policy_id: str, resource: str) -> Any:
        return self._request("POST", f"/api/v1/cac/policies/{policy_id}/test", {"resource": resource})

    def cac_dry_run(self, policy_id: str, resource: str) -> Any:
        return self._request("POST", f"/api/v1/cac/policies/{policy_id}/dry-run", {"resource": resource})

    def cac_version(self, policy_id: str) -> Any:
        return self._request("GET", f"/api/v1/cac/policies/{policy_id}/version")

    def ar_list(self) -> Any:
        return self._request("GET", "/api/v1/attestation")

    def ar_generate(self, framework: str, scope: str) -> Any:
        return self._request("POST", "/api/v1/attestation/generate", {"framework": framework, "scope": scope})

    def ar_sign(self, report_id: str) -> Any:
        return self._request("POST", f"/api/v1/attestation/{report_id}/sign")

    def ar_stats(self) -> Any:
        return self._request("GET", "/api/v1/attestation/stats")

    def ar_approve(self, report_id: str) -> Any:
        return self._request("POST", f"/api/v1/attestation/{report_id}/approve")

    def ar_verify(self, report_id: str) -> Any:
        return self._request("POST", f"/api/v1/attestation/{report_id}/verify")

    def ar_compare(self, report_id_1: str, report_id_2: str) -> Any:
        return self._request("GET", f"/api/v1/attestation/compare?r1={report_id_1}&r2={report_id_2}")

    def ar_schedule(self, framework: str, cron: str) -> Any:
        return self._request("POST", "/api/v1/attestation/schedule", {"framework": framework, "cron": cron})

    def ar_coverage(self, framework: str) -> Any:
        return self._request("GET", f"/api/v1/attestation/{framework}/coverage")

    def vc_list(self) -> Any:
        return self._request("GET", "/api/v1/vendor-compliance")

    def vc_register(self, name: str, tier: str) -> Any:
        return self._request("POST", "/api/v1/vendor-compliance", {"name": name, "tier": tier})

    def vc_assess(self, vendor_id: str) -> Any:
        return self._request("POST", f"/api/v1/vendor-compliance/{vendor_id}/assess")

    def vc_risk(self, vendor_id: str) -> Any:
        return self._request("GET", f"/api/v1/vendor-compliance/{vendor_id}/risk")

    def vc_scorecard(self, vendor_id: str) -> Any:
        return self._request("GET", f"/api/v1/vendor-compliance/{vendor_id}/scorecard")

    def vc_assessments(self) -> Any:
        return self._request("GET", "/api/v1/vendor-compliance/assessments")

    def vc_migrate_tier(self, vendor_id: str, new_tier: str) -> Any:
        return self._request("POST", f"/api/v1/vendor-compliance/{vendor_id}/migrate", {"tier": new_tier})

    def vc_categories(self) -> Any:
        return self._request("GET", "/api/v1/vendor-compliance/categories")

    def vc_discover(self) -> Any:
        return self._request("POST", "/api/v1/vendor-compliance/discover")

    def vc_remediation(self, vendor_id: str) -> Any:
        return self._request("GET", f"/api/v1/vendor-compliance/{vendor_id}/remediation")

    def ri_changes(self) -> Any:
        return self._request("GET", "/api/v1/regulatory-intel/changes")

    def ri_detect(self, regulation: str, jurisdiction: str) -> Any:
        return self._request("POST", "/api/v1/regulatory-intel/detect", {"regulation": regulation, "jurisdiction": jurisdiction})

    def ri_sources(self) -> Any:
        return self._request("GET", "/api/v1/regulatory-intel/sources")

    def ri_stats(self) -> Any:
        return self._request("GET", "/api/v1/regulatory-intel/stats")

    def ri_impact(self, change_id: str) -> Any:
        return self._request("GET", f"/api/v1/regulatory-intel/changes/{change_id}/impact")

    def ri_matrix(self) -> Any:
        return self._request("GET", "/api/v1/regulatory-intel/matrix")

    def ri_calendar(self) -> Any:
        return self._request("GET", "/api/v1/regulatory-intel/calendar")

    def ri_notify(self, change_id: str, channel: str) -> Any:
        return self._request("POST", f"/api/v1/regulatory-intel/changes/{change_id}/notify", {"channel": channel})

    def ri_pending(self) -> Any:
        return self._request("GET", "/api/v1/regulatory-intel/pending")

    def ri_search(self, query: str) -> Any:
        return self._request("GET", f"/api/v1/regulatory-intel/search?q={query}")

    def am_list(self) -> Any:
        return self._request("GET", "/api/v1/audit-mgmt/audits")

    def am_schedule(self, title: str, framework: str, date: str) -> Any:
        return self._request("POST", "/api/v1/audit-mgmt/audits", {"title": title, "framework": framework, "date": date})

    def am_rights(self) -> Any:
        return self._request("GET", "/api/v1/audit-mgmt/rights")

    def am_stats(self) -> Any:
        return self._request("GET", "/api/v1/audit-mgmt/stats")

    def am_upcoming(self) -> Any:
        return self._request("GET", "/api/v1/audit-mgmt/upcoming")

    def am_overdue(self) -> Any:
        return self._request("GET", "/api/v1/audit-mgmt/overdue")

    def am_workflow(self, audit_id: str, step: str) -> Any:
        return self._request("POST", f"/api/v1/audit-mgmt/audits/{audit_id}/workflow", {"step": step})

    def am_report(self, audit_id: str) -> Any:
        return self._request("GET", f"/api/v1/audit-mgmt/audits/{audit_id}/report")

    def am_register_right(self, name: str, description: str) -> Any:
        return self._request("POST", "/api/v1/audit-mgmt/rights", {"name": name, "description": description})

    def am_calendar(self) -> Any:
        return self._request("GET", "/api/v1/audit-mgmt/calendar")

    def dr_list(self) -> Any:
        return self._request("GET", "/api/v1/data-residency/records")

    def dr_register(self, name: str, region: str, data_type: str) -> Any:
        return self._request("POST", "/api/v1/data-residency/records", {"name": name, "region": region, "data_type": data_type})

    def dr_check(self, record_id: str) -> Any:
        return self._request("GET", f"/api/v1/data-residency/records/{record_id}/check")

    def dr_summary(self) -> Any:
        return self._request("GET", "/api/v1/data-residency/summary")

    def dr_flows(self) -> Any:
        return self._request("GET", "/api/v1/data-residency/flows")

    def dr_move(self, record_id: str, target_region: str) -> Any:
        return self._request("POST", f"/api/v1/data-residency/records/{record_id}/move", {"target_region": target_region})

    def dr_audit(self, record_id: str) -> Any:
        return self._request("GET", f"/api/v1/data-residency/records/{record_id}/audit")

    def dr_violations(self) -> Any:
        return self._request("GET", "/api/v1/data-residency/violations")

    def dr_compliance_report(self) -> Any:
        return self._request("GET", "/api/v1/data-residency/compliance-report")

    def dr_asset_search(self, query: str) -> Any:
        return self._request("GET", f"/api/v1/data-residency/search?q={query}")

    def ct_modules(self) -> Any:
        return self._request("GET", "/api/v1/compliance-training/modules")

    def ct_assign(self, user: str, module_id: str) -> Any:
        return self._request("POST", "/api/v1/compliance-training/assignments", {"user": user, "module_id": module_id})

    def ct_status(self, assignment_id: str) -> Any:
        return self._request("GET", f"/api/v1/compliance-training/assignments/{assignment_id}")

    def ct_stats(self) -> Any:
        return self._request("GET", "/api/v1/compliance-training/stats")

    def ct_certifications(self) -> Any:
        return self._request("GET", "/api/v1/compliance-training/certifications")

    def ct_expiring(self) -> Any:
        return self._request("GET", "/api/v1/compliance-training/expiring")

    def ct_search(self, query: str) -> Any:
        return self._request("GET", f"/api/v1/compliance-training/search?q={query}")

    def ct_report(self) -> Any:
        return self._request("GET", "/api/v1/compliance-training/report")

    def ct_progress(self, assignment_id: str) -> Any:
        return self._request("GET", f"/api/v1/compliance-training/assignments/{assignment_id}/progress")

    def ct_batch_assign(self, users: list, module_id: str) -> Any:
        return self._request("POST", "/api/v1/compliance-training/batch-assign", {"users": users, "module_id": module_id})

    def ap_sessions(self) -> Any:
        return self._request("GET", "/api/v1/auditor/sessions")

    def ap_evidence(self, session_id: str) -> Any:
        return self._request("GET", f"/api/v1/auditor/sessions/{session_id}/evidence")

    def ap_findings(self, session_id: str) -> Any:
        return self._request("GET", f"/api/v1/auditor/sessions/{session_id}/findings")

    def ap_stats(self) -> Any:
        return self._request("GET", "/api/v1/auditor/stats")

    def ap_engagement_create(self, title: str, scope: str, auditor: str) -> Any:
        return self._request("POST", "/api/v1/auditor/engagements", {"title": title, "scope": scope, "auditor": auditor})

    def ap_engagement_complete(self, engagement_id: str) -> Any:
        return self._request("POST", f"/api/v1/auditor/engagements/{engagement_id}/complete")

    def ap_finding_create(self, engagement_id: str, title: str, severity: str, description: str) -> Any:
        return self._request("POST", f"/api/v1/auditor/engagements/{engagement_id}/findings", {"title": title, "severity": severity, "description": description})

    def ap_session_revoke(self, session_id: str) -> Any:
        return self._request("POST", f"/api/v1/auditor/sessions/{session_id}/revoke")

    def ap_session_extend(self, session_id: str, hours: int) -> Any:
        return self._request("POST", f"/api/v1/auditor/sessions/{session_id}/extend", {"hours": hours})

    def ap_finding_update(self, finding_id: str, status: str) -> Any:
        return self._request("PATCH", f"/api/v1/auditor/findings/{finding_id}", {"status": status})

    def dr_list(self) -> Any:
        return self._request("GET", "/api/v1/dr/plans")

    def dr_create(self, name: str, rto: int, rpo: int, region: str) -> Any:
        return self._request("POST", "/api/v1/dr/plans", {"name": name, "rto": rto, "rpo": rpo, "region": region})

    def dr_status(self, plan_id: str) -> Any:
        return self._request("GET", f"/api/v1/dr/plans/{plan_id}")

    def dr_failover(self, plan_id: str) -> Any:
        return self._request("POST", f"/api/v1/dr/plans/{plan_id}/failover")

    def dr_readiness(self, plan_id: str) -> Any:
        return self._request("GET", f"/api/v1/dr/plans/{plan_id}/readiness")

    def dr_delete_plan(self, plan_id: str) -> Any:
        return self._request("DELETE", f"/api/v1/dr/plans/{plan_id}")

    def dr_scenarios(self) -> Any:
        return self._request("GET", "/api/v1/dr/scenarios")

    def dr_versions(self, plan_id: str) -> Any:
        return self._request("GET", f"/api/v1/dr/plans/{plan_id}/versions")

    def dr_notifications(self) -> Any:
        return self._request("GET", "/api/v1/dr/notifications")

    def dr_compliance(self, plan_id: str) -> Any:
        return self._request("GET", f"/api/v1/dr/plans/{plan_id}/compliance")

    def blockchain_list_networks(self) -> Any:
        return self._get("/api/v1/emerging-tech/blockchain/networks")

    def blockchain_create_network(self, name: str, consensus: str, chain_id: str) -> Any:
        return self._post("/api/v1/emerging-tech/blockchain/networks", {"name": name, "consensus": consensus, "chain_id": chain_id})

    def blockchain_network_status(self, network_id: str) -> Any:
        return self._get(f"/api/v1/emerging-tech/blockchain/networks/{network_id}")

    def blockchain_validators(self, network_id: str) -> Any:
        return self._get(f"/api/v1/emerging-tech/blockchain/networks/{network_id}/validators")

    def storage_list_gateways(self) -> Any:
        return self._get("/api/v1/emerging-tech/storage/gateways")

    def storage_create_gateway(self, name: str, provider: str) -> Any:
        return self._post("/api/v1/emerging-tech/storage/gateways", {"name": name, "provider": provider})

    def storage_pin_content(self, cid: str) -> Any:
        return self._post("/api/v1/emerging-tech/storage/pin", {"cid": cid})

    def storage_gateway_status(self, gateway_id: str) -> Any:
        return self._get(f"/api/v1/emerging-tech/storage/gateways/{gateway_id}")

    def quantum_list_keys(self) -> Any:
        return self._get("/api/v1/emerging-tech/quantum/keys")

    def quantum_generate_key(self, algorithm: str) -> Any:
        return self._post("/api/v1/emerging-tech/quantum/keys", {"algorithm": algorithm})

    def quantum_create_certificate(self, name: str, key_id: str) -> Any:
        return self._post("/api/v1/emerging-tech/quantum/certificates", {"name": name, "key_id": key_id})

    def quantum_encrypt(self, key_id: str, message: str) -> Any:
        return self._post("/api/v1/emerging-tech/quantum/encrypt", {"key_id": key_id, "message": message})

    def quantum_decrypt(self, key_id: str, ciphertext: str) -> Any:
        return self._post("/api/v1/emerging-tech/quantum/decrypt", {"key_id": key_id, "ciphertext": ciphertext})

    def contracts_list(self) -> Any:
        return self._get("/api/v1/emerging-tech/contracts")

    def contracts_deploy(self, name: str, network: str, bytecode: str) -> Any:
        return self._post("/api/v1/emerging-tech/contracts", {"name": name, "network": network, "bytecode": bytecode})

    def contracts_get(self, contract_id: str) -> Any:
        return self._get(f"/api/v1/emerging-tech/contracts/{contract_id}")

    def contracts_events(self, contract_id: str) -> Any:
        return self._get(f"/api/v1/emerging-tech/contracts/{contract_id}/events")

    def web3id_list(self) -> Any:
        return self._get("/api/v1/emerging-tech/web3id/identities")

    def web3id_create(self, did: str) -> Any:
        return self._post("/api/v1/emerging-tech/web3id/identities", {"did": did})

    def web3id_authenticate(self, identity_id: str) -> Any:
        return self._post(f"/api/v1/emerging-tech/web3id/identities/{identity_id}/auth")

    def web3id_sessions(self) -> Any:
        return self._get("/api/v1/emerging-tech/web3id/sessions")

    def confidential_list_enclaves(self) -> Any:
        return self._get("/api/v1/emerging-tech/confidential/enclaves")

    def confidential_create_enclave(self, name: str, image: str, memory_mb: int) -> Any:
        return self._post("/api/v1/emerging-tech/confidential/enclaves", {"name": name, "image": image, "memory_mb": memory_mb})

    def confidential_attest(self, enclave_id: str) -> Any:
        return self._post(f"/api/v1/emerging-tech/confidential/enclaves/{enclave_id}/attest")

    def confidential_secrets(self, enclave_id: str) -> Any:
        return self._get(f"/api/v1/emerging-tech/confidential/enclaves/{enclave_id}/secrets")

    def federated_list_projects(self) -> Any:
        return self._get("/api/v1/emerging-tech/federated/projects")

    def federated_create_project(self, name: str, rounds: int, min_clients: int) -> Any:
        return self._post("/api/v1/emerging-tech/federated/projects", {"name": name, "rounds": rounds, "min_clients": min_clients})

    def federated_project_status(self, project_id: str) -> Any:
        return self._get(f"/api/v1/emerging-tech/federated/projects/{project_id}")

    def federated_rounds(self, project_id: str) -> Any:
        return self._get(f"/api/v1/emerging-tech/federated/projects/{project_id}/rounds")

    def zkp_list(self) -> Any:
        return self._get("/api/v1/emerging-tech/zkp/proofs")

    def zkp_generate(self, statement: str, witness: str) -> Any:
        return self._post("/api/v1/emerging-tech/zkp/proofs", {"statement": statement, "witness": witness})

    def zkp_verify(self, proof_id: str) -> Any:
        return self._post(f"/api/v1/emerging-tech/zkp/proofs/{proof_id}/verify")

    def zkp_circuits(self) -> Any:
        return self._get("/api/v1/emerging-tech/zkp/circuits")

    def dcn_list_tasks(self) -> Any:
        return self._get("/api/v1/emerging-tech/dcn/tasks")

    def dcn_submit_task(self, name: str, requirements: str, input_data: str) -> Any:
        return self._post("/api/v1/emerging-tech/dcn/tasks", {"name": name, "requirements": requirements, "input_data": input_data})

    def dcn_task_status(self, task_id: str) -> Any:
        return self._get(f"/api/v1/emerging-tech/dcn/tasks/{task_id}")

    def dcn_workers(self) -> Any:
        return self._get("/api/v1/emerging-tech/dcn/workers")
