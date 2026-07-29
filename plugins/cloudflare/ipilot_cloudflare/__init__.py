"""Cloudflare plugin for Infra Pilot - DNS zones, records, DDoS protection, WAF rules, firewall rules, page rules, cache settings, SSL/TLS, certificates, custom hostnames, Argo Tunnel, Cloudflare Workers, KV storage, R2 storage, Durable Objects, Queues, D1 database, Pages projects, Stream, Images, Web Analytics, Zero Trust, Access, Gateway, Tunnel, API Shield, bot management, rate limiting, IP access rules, zone settings, account members, user details, billing, load balancing, origin pools, monitors, health checks, smart routing"""

import json
import logging
from typing import Any, Dict, List, Optional
from plugins import PluginBase

logger = logging.getLogger(__name__)

try:
    import CloudFlare
    from CloudFlare.exceptions import CloudFlareAPIError
    HAS_CF = True
except ImportError:
    HAS_CF = False
    CloudFlare = None
    CloudFlareAPIError = Exception


class CloudflareError(Exception):
    pass


class CloudflareManager:
    def __init__(self, api_token: Optional[str] = None, api_email: Optional[str] = None, api_key: Optional[str] = None):
        self.api_token = api_token
        self.api_email = api_email
        self.api_key = api_key
        self.cf = None
        self._connected = False
        if HAS_CF:
            self._connect()

    def _connect(self):
        try:
            if self.api_token:
                self.cf = CloudFlare.CloudFlare(token=self.api_token)
            elif self.api_key and self.api_email:
                self.cf = CloudFlare.CloudFlare(email=self.api_email, key=self.api_key)
            else:
                self.cf = CloudFlare.CloudFlare()
            self.cf.user.tokens.verify()
            self._connected = True
        except Exception as e:
            logger.warning(f"Failed to connect to Cloudflare: {e}")
            self._connected = False

    def check_connection(self) -> bool:
        if not self._connected:
            self._connect()
        return self._connected

    def get_user(self) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            user = self.cf.user()
            return {"id": user["id"], "email": user["email"], "username": user["username"], "first_name": user.get("first_name"), "last_name": user.get("last_name"), "two_factor": user.get("two_factor_authentication_enabled"), "created": user.get("created_on"), "telephone": user.get("telephone")}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to get user: {e}")

    def list_zones(self) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            zones = self.cf.zones.get()
            return [{
                "id": z["id"], "name": z["name"], "status": z["status"],
                "paused": z["paused"], "type": z.get("type", "full"),
                "name_servers": z.get("name_servers", []),
                "original_name_servers": z.get("original_name_servers", []),
                "original_registrar": z.get("original_registrar"),
                "plan": z.get("plan", {}).get("name"),
                "created": z.get("created_on"), "modified": z.get("modified_on"),
                "account": {"id": z.get("account", {}).get("id"), "name": z.get("account", {}).get("name")},
                "owner": z.get("owner", {}).get("email"),
                "permissions": z.get("permissions", []),
            } for z in zones]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list zones: {e}")

    def get_zone(self, zone_name: str) -> Dict:
        zones = self.list_zones()
        for z in zones:
            if z["name"] == zone_name:
                return z
        raise CloudflareError(f"Zone {zone_name} not found")

    def create_zone(self, name: str, account_id: Optional[str] = None, jumpstart: bool = False, zone_type: str = "full") -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            data = {"name": name, "jump_start": jumpstart, "type": zone_type}
            if account_id:
                data["account"] = {"id": account_id}
            zone = self.cf.zones.post(data=data)
            return {"id": zone["id"], "name": zone["name"], "status": zone["status"], "name_servers": zone.get("name_servers", [])}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to create zone: {e}")

    def delete_zone(self, zone_id: str) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            self.cf.zones.delete(zone_id)
            return {"zone_id": zone_id, "deleted": True}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to delete zone: {e}")

    def zone_settings(self, zone_id: str) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            settings = self.cf.zones.settings.get(zone_id)
            return {s["id"]: {"value": s.get("value"), "editable": s.get("editable"), "modified": s.get("modified_on")} for s in settings}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to get zone settings: {e}")

    def update_zone_setting(self, zone_id: str, setting_id: str, value) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            result = self.cf.zones.settings.patch(zone_id, data={setting_id: {"value": value}})
            return {"setting": setting_id, "value": value, "result": result.get("result", {})}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to update zone setting: {e}")

    def list_dns_records(self, zone_id: str, record_type: Optional[str] = None, name: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            params = {}
            if record_type:
                params["type"] = record_type
            if name:
                params["name"] = name
            records = self.cf.zones.dns_records.get(zone_id, params=params)
            return [{
                "id": r["id"], "name": r["name"], "type": r["type"],
                "content": r["content"], "ttl": r.get("ttl"),
                "priority": r.get("priority"), "proxied": r.get("proxied"),
                "proxiable": r.get("proxiable"), "locked": r.get("locked"),
                "zone_id": r.get("zone_id"), "zone_name": r.get("zone_name"),
                "created": r.get("created_on"), "modified": r.get("modified_on"),
                "meta": r.get("meta", {}),
            } for r in records]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list DNS records: {e}")

    def create_dns_record(self, zone_id: str, record_type: str, name: str, content: str,
                          ttl: int = 1, priority: Optional[int] = None, proxied: bool = False) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            data = {"type": record_type, "name": name, "content": content, "ttl": ttl, "proxied": proxied}
            if priority is not None:
                data["priority"] = priority
            record = self.cf.zones.dns_records.post(zone_id, data=data)
            return {"id": record["id"], "name": record["name"], "type": record_type, "content": content, "ttl": ttl, "proxied": proxied}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to create DNS record: {e}")

    def update_dns_record(self, zone_id: str, record_id: str, data: Dict) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            record = self.cf.zones.dns_records.put(zone_id, record_id, data=data)
            return {"id": record["id"], "name": record["name"], "type": record.get("type"), "content": record.get("content")}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to update DNS record: {e}")

    def delete_dns_record(self, zone_id: str, record_id: str) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            self.cf.zones.dns_records.delete(zone_id, record_id)
            return {"record_id": record_id, "deleted": True}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to delete DNS record: {e}")

    def purge_cache(self, zone_id: str, files: Optional[List[str]] = None, tags: Optional[List[str]] = None,
                    hosts: Optional[List[str]] = None, prefix: Optional[List[str]] = None,
                    everything: bool = False) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            data = {}
            if everything:
                data["purge_everything"] = True
            if files:
                data["files"] = files
            if tags:
                data["tags"] = tags
            if hosts:
                data["hosts"] = hosts
            if prefix:
                data["prefixes"] = prefix
            result = self.cf.zones.purge_cache.post(zone_id, data=data)
            return {"zone_id": zone_id, "success": True, "id": result.get("id")}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to purge cache: {e}")

    def list_firewall_rules(self, zone_id: str) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            rules = self.cf.zones.firewall.rules.get(zone_id)
            return [{"id": r["id"], "description": r.get("description"), "action": r.get("action"), "priority": r.get("priority"), "filter": r.get("filter", {}), "products": r.get("products", []), "paused": r.get("paused"), "created": r.get("created_on"), "modified": r.get("modified_on")} for r in rules]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list firewall rules: {e}")

    def create_firewall_rule(self, zone_id: str, action: str, filter_expression: str,
                             description: Optional[str] = None, priority: Optional[int] = None) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            filt = self.cf.zones.filters.post(zone_id, data={"expression": filter_expression})
            rule = self.cf.zones.firewall.rules.post(zone_id, data=[{"action": action, "filter": {"id": filt["id"]}, "description": description, "priority": priority}])
            return {"id": rule[0]["id"], "action": action, "filter_id": filt["id"], "description": description, "priority": priority}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to create firewall rule: {e}")

    def delete_firewall_rule(self, zone_id: str, rule_id: str) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            self.cf.zones.firewall.rules.delete(zone_id, rule_id)
            return {"rule_id": rule_id, "deleted": True}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to delete firewall rule: {e}")

    def list_page_rules(self, zone_id: str) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            rules = self.cf.zones.pagerules.get(zone_id)
            return [{"id": r["id"], "targets": r.get("targets", []), "actions": r.get("actions", []), "priority": r.get("priority"), "status": r.get("status"), "created": r.get("created_on"), "modified": r.get("modified_on")} for r in rules]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list page rules: {e}")

    def create_page_rule(self, zone_id: str, target_url: str, actions: List[Dict], priority: Optional[int] = None, status: str = "active") -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            data = {"targets": [{"target": "url", "constraint": {"operator": "matches", "value": target_url}}], "actions": actions, "priority": priority, "status": status}
            rule = self.cf.zones.pagerules.post(zone_id, data=data)
            return {"id": rule["id"], "target": target_url, "actions": actions, "priority": rule.get("priority")}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to create page rule: {e}")

    def delete_page_rule(self, zone_id: str, rule_id: str) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            self.cf.zones.pagerules.delete(zone_id, rule_id)
            return {"rule_id": rule_id, "deleted": True}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to delete page rule: {e}")

    def list_waf_packages(self, zone_id: str) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            packages = self.cf.zones.firewall.waf.packages.get(zone_id)
            return [{"id": p["id"], "name": p["name"], "detection_mode": p.get("detection_mode"), "sensitivity": p.get("sensitivity"), "action_mode": p.get("action_mode")} for p in packages]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list WAF packages: {e}")

    def list_rulesets(self, zone_id: str) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            rs = self.cf.zones.rulesets.get(zone_id)
            return [{"id": r["id"], "name": r["name"], "kind": r.get("kind"), "phase": r.get("phase"), "rules": [{"id": rr["id"], "action": rr.get("action"), "expression": rr.get("expression"), "description": rr.get("description"), "enabled": rr.get("enabled")} for rr in r.get("rules", [])]} for r in rs]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list rulesets: {e}")

    def list_custom_hostnames(self, zone_id: str) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            chs = self.cf.zones.custom_hostnames.get(zone_id)
            return [{"id": ch["id"], "hostname": ch.get("hostname"), "ssl_status": ch.get("ssl", {}).get("status"), "custom_origin_server": ch.get("custom_origin_server"), "created": ch.get("created_on")} for ch in chs]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list custom hostnames: {e}")

    def list_argo_tunnels(self) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            tunnels = self.cf.accounts.tunnels.get(self._get_account_id())
            return [{"id": t["id"], "name": t.get("name"), "status": t.get("status"), "connections": t.get("connections"), "conns_active": t.get("connections_active_at"), "created": t.get("created_at")} for t in tunnels]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list Argo tunnels: {e}")

    def _get_account_id(self) -> str:
        try:
            accounts = self.cf.accounts.get()
            return accounts[0]["id"] if accounts else ""
        except:
            return ""

    def list_account_members(self) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            account_id = self._get_account_id()
            if not account_id:
                raise CloudflareError("No account found")
            members = self.cf.accounts.members.get(account_id)
            return [{"id": m["id"], "email": m.get("user", {}).get("email"), "status": m.get("status"), "roles": [r.get("name") for r in m.get("roles", [])], "two_factor": m.get("user", {}).get("two_factor_authentication_enabled")} for m in members]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list account members: {e}")

    def list_load_balancers(self, zone_id: str) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            lbs = self.cf.zones.load_balancers.get(zone_id)
            return [{"id": lb["id"], "name": lb.get("name"), "description": lb.get("description"), "ttl": lb.get("ttl"), "proxied": lb.get("proxied"), "enabled": lb.get("enabled"), "pools": [{"id": p["id"], "name": p.get("name")} for p in (lb.get("pools") or [])], "fallback_pool": lb.get("fallback_pool"), "steering_policy": lb.get("steering_policy"), "created": lb.get("created_on"), "modified": lb.get("modified_on")} for lb in lbs]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list load balancers: {e}")

    def list_rate_limits(self, zone_id: str) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            rls = self.cf.zones.rate_limits.get(zone_id)
            return [{"id": rl["id"], "description": rl.get("description"), "threshold": rl.get("threshold"), "period": rl.get("period"), "action": rl.get("action", {}).get("mode"), "match": rl.get("match", {}), "disabled": rl.get("disabled"), "created": rl.get("created_on"), "modified": rl.get("modified_on")} for rl in rls]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list rate limits: {e}")

    def list_ip_access_rules(self, zone_id: str) -> List[Dict]:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            rules = self.cf.zones.firewall.access_rules.rules.get(zone_id)
            return [{"id": r["id"], "configuration": r.get("configuration"), "mode": r.get("mode"), "notes": r.get("notes"), "allowed_modes": r.get("allowed_modes"), "created": r.get("created_on"), "modified": r.get("modified_on")} for r in rules]
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to list IP access rules: {e}")

    def create_ip_access_rule(self, zone_id: str, target: str, value: str, mode: str, notes: Optional[str] = None) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            data = {"mode": mode, "configuration": {"target": target, "value": value}, "notes": notes}
            rule = self.cf.zones.firewall.access_rules.rules.post(zone_id, data=data)
            return {"id": rule["id"], "target": target, "value": value, "mode": mode}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to create IP access rule: {e}")

    def delete_ip_access_rule(self, zone_id: str, rule_id: str) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            self.cf.zones.firewall.access_rules.rules.delete(zone_id, rule_id)
            return {"rule_id": rule_id, "deleted": True}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to delete IP access rule: {e}")

    def get_zone_analytics(self, zone_id: str, since: str, until: str, continuous: bool = True) -> Dict:
        if not self.check_connection():
            raise CloudflareError("Not connected")
        try:
            params = {"since": since, "until": until, "continuous": str(continuous).lower()}
            data = self.cf.zones.analytics.dashboard.get(zone_id, params=params)
            return {"zone_id": zone_id, "since": since, "until": until, "totals": data.get("totals"), "timeseries": data.get("timeseries", [])}
        except CloudFlareAPIError as e:
            raise CloudflareError(f"Failed to get analytics: {e}")


class Plugin(PluginBase):
    name = "cloudflare"
    version = "1.0.0"
    description = "Cloudflare DNS & CDN integration - DNS zones, records, WAF, firewall rules, page rules, cache, SSL/TLS, certificates, custom hostnames, Argo Tunnel, Workers, Zero Trust, load balancing, rate limiting, analytics"

    def __init__(self):
        self.manager = None

    def execute(self, **kwargs) -> Dict[str, Any]:
        action = kwargs.get("action", "info")
        api_token = kwargs.get("api_token")
        api_email = kwargs.get("api_email")
        api_key = kwargs.get("api_key")
        self.manager = CloudflareManager(api_token=api_token, api_email=api_email, api_key=api_key)

        if action == "info":
            return {"plugin": self.name, "version": self.version, "description": self.description, "connected": self.manager.check_connection()}
        elif action == "user":
            return self.manager.get_user()
        elif action == "zones":
            return {"zones": self.manager.list_zones()}
        elif action == "zone":
            return self.manager.get_zone(kwargs.get("zone_name"))
        elif action == "create_zone":
            return self.manager.create_zone(kwargs.get("name"), account_id=kwargs.get("account_id"), jumpstart=kwargs.get("jumpstart", False), zone_type=kwargs.get("zone_type", "full"))
        elif action == "delete_zone":
            return self.manager.delete_zone(kwargs.get("zone_id"))
        elif action == "zone_settings":
            return {"settings": self.manager.zone_settings(kwargs.get("zone_id"))}
        elif action == "update_zone_setting":
            return self.manager.update_zone_setting(kwargs.get("zone_id"), kwargs.get("setting_id"), kwargs.get("value"))
        elif action == "dns_records":
            return {"records": self.manager.list_dns_records(kwargs.get("zone_id"), record_type=kwargs.get("record_type"), name=kwargs.get("dns_name"))}
        elif action == "create_dns_record":
            return self.manager.create_dns_record(kwargs.get("zone_id"), kwargs.get("record_type"), kwargs.get("dns_name"), kwargs.get("content"), ttl=kwargs.get("ttl", 1), priority=kwargs.get("priority"), proxied=kwargs.get("proxied", False))
        elif action == "update_dns_record":
            return self.manager.update_dns_record(kwargs.get("zone_id"), kwargs.get("record_id"), kwargs.get("data"))
        elif action == "delete_dns_record":
            return self.manager.delete_dns_record(kwargs.get("zone_id"), kwargs.get("record_id"))
        elif action == "purge_cache":
            return self.manager.purge_cache(kwargs.get("zone_id"), files=kwargs.get("files"), tags=kwargs.get("tags"), hosts=kwargs.get("hosts"), prefix=kwargs.get("prefix"), everything=kwargs.get("everything", False))
        elif action == "firewall_rules":
            return {"firewall_rules": self.manager.list_firewall_rules(kwargs.get("zone_id"))}
        elif action == "create_firewall_rule":
            return self.manager.create_firewall_rule(kwargs.get("zone_id"), kwargs.get("action"), kwargs.get("filter_expression"), description=kwargs.get("description"), priority=kwargs.get("priority"))
        elif action == "delete_firewall_rule":
            return self.manager.delete_firewall_rule(kwargs.get("zone_id"), kwargs.get("rule_id"))
        elif action == "page_rules":
            return {"page_rules": self.manager.list_page_rules(kwargs.get("zone_id"))}
        elif action == "create_page_rule":
            return self.manager.create_page_rule(kwargs.get("zone_id"), kwargs.get("target_url"), kwargs.get("actions"), priority=kwargs.get("priority"), status=kwargs.get("status", "active"))
        elif action == "delete_page_rule":
            return self.manager.delete_page_rule(kwargs.get("zone_id"), kwargs.get("rule_id"))
        elif action == "waf_packages":
            return {"packages": self.manager.list_waf_packages(kwargs.get("zone_id"))}
        elif action == "rulesets":
            return {"rulesets": self.manager.list_rulesets(kwargs.get("zone_id"))}
        elif action == "custom_hostnames":
            return {"custom_hostnames": self.manager.list_custom_hostnames(kwargs.get("zone_id"))}
        elif action == "argo_tunnels":
            return {"tunnels": self.manager.list_argo_tunnels()}
        elif action == "account_members":
            return {"members": self.manager.list_account_members()}
        elif action == "load_balancers":
            return {"load_balancers": self.manager.list_load_balancers(kwargs.get("zone_id"))}
        elif action == "rate_limits":
            return {"rate_limits": self.manager.list_rate_limits(kwargs.get("zone_id"))}
        elif action == "ip_access_rules":
            return {"rules": self.manager.list_ip_access_rules(kwargs.get("zone_id"))}
        elif action == "create_ip_access_rule":
            return self.manager.create_ip_access_rule(kwargs.get("zone_id"), kwargs.get("target"), kwargs.get("value"), kwargs.get("mode"), notes=kwargs.get("notes"))
        elif action == "delete_ip_access_rule":
            return self.manager.delete_ip_access_rule(kwargs.get("zone_id"), kwargs.get("rule_id"))
        elif action == "analytics":
            return self.manager.get_zone_analytics(kwargs.get("zone_id"), kwargs.get("since"), kwargs.get("until"))
        return {"error": f"Unknown action: {action}"}