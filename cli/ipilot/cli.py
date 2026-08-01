"""Legacy argparse CLI. Deprecated in favor of the Typer-based CLI (ipilot --help).

All commands available here are being migrated to the Typer system.
"""

import argparse
import json
import sys
import warnings

from . import __version__
from .client import ApiClient
from .config import get, load_config, save_config, set_key
from .output import print_output


def cmd_health(args):
    """Health Check Befehl - zeigt den Status aller Systemkomponenten"""
    client = get_client()
    health_data = client.health_check()
    print_output(health_data, args.output)


def get_client():
    config = load_config()
    return ApiClient(
        config.get("api_url", "http://localhost:8080"), config.get("token")
    )


def cmd_login(args):
    result = get_client().login(args.api_key)
    if "token" in result:
        set_key("token", result["token"])
        print_output({"status": "Logged in successfully"}, args.output)
    else:
        print_output(result, args.output)


def cmd_logout(args):
    result = get_client().logout()
    set_key("token", None)
    print_output(result or {"status": "Logged out"}, args.output)


def cmd_server_list(args):
    result = get_client().list_servers()
    data = result if isinstance(result, list) else result.get("servers", result)
    print_output(data, args.output)


def cmd_server_create(args):
    result = get_client().create_server(args.name, args.type, args.memory)
    print_output(result, args.output)


def cmd_server_delete(args):
    result = get_client().delete_server(args.server)
    print_output(result, args.output)


def cmd_server_status(args):
    result = get_client().server_status(args.server)
    print_output(result, args.output)


def cmd_logs(args):
    result = get_client().get_logs(args.server, args.lines, args.follow)
    print_output(result, args.output)


def cmd_backup_list(args):
    result = get_client().list_backups(args.server)
    data = result if isinstance(result, list) else result.get("backups", result)
    print_output(data, args.output)


def cmd_backup_create(args):
    result = get_client().create_backup(args.server)
    print_output(result, args.output)


def cmd_deploy(args):
    result = get_client().deploy(args.server, args.branch)
    print_output(result, args.output)


def cmd_config_get(args):
    config = load_config()
    if args.key:
        value = config.get(args.key)
        print_output({args.key: value}, args.output)
    else:
        print_output(config, args.output)


def cmd_config_set(args):
    set_key(args.key, args.value)
    print_output({args.key: args.value, "status": "set"}, args.output)


# === Edge & IoT Commands ===


# === Green Computing Commands ===


# === v3 Networking Commands ===


def cmd_sdwan_status(args):
    result = get_client().sdwan_status()
    print_output(result, args.output)


def cmd_sdwan_apps(args):
    result = get_client().sdwan_list_apps()
    data = result if isinstance(result, list) else result.get("apps", result)
    print_output(data, args.output)


def cmd_sdwan_create(args):
    result = get_client().sdwan_create_app(args.name, args.provider, args.bandwidth)
    print_output(result, args.output)


def cmd_sdwan_delete(args):
    result = get_client().sdwan_delete_app(args.app_id)
    print_output(result, args.output)


def cmd_sdwan_toggle(args):
    result = get_client().sdwan_toggle(args.app_id)
    print_output(result, args.output)


def cmd_vpn_configs(args):
    result = get_client().vpn_list_configs()
    data = result if isinstance(result, list) else result.get("configs", result)
    print_output(data, args.output)


def cmd_vpn_create(args):
    result = get_client().vpn_create_config(
        args.name, args.server, args.port, args.protocol
    )
    print_output(result, args.output)


def cmd_vpn_delete(args):
    result = get_client().vpn_delete_config(args.config_id)
    print_output(result, args.output)


def cmd_vpn_status(args):
    result = get_client().vpn_status()
    print_output(result, args.output)


def cmd_dns_zones(args):
    result = get_client().dns_list_zones()
    data = result if isinstance(result, list) else result.get("zones", result)
    print_output(data, args.output)


def cmd_dns_create_zone(args):
    result = get_client().dns_create_zone(args.domain, args.ttl)
    print_output(result, args.output)


def cmd_dns_delete_zone(args):
    result = get_client().dns_delete_zone(args.zone_id)
    print_output(result, args.output)


def cmd_dns_records(args):
    result = get_client().dns_list_records(args.zone_id)
    data = result if isinstance(result, list) else result.get("records", result)
    print_output(data, args.output)


def cmd_dns_add_record(args):
    result = get_client().dns_create_record(
        args.zone_id, args.name, args.type, args.value, args.ttl
    )
    print_output(result, args.output)


def cmd_dns_delete_record(args):
    result = get_client().dns_delete_record(args.zone_id, args.record_id)
    print_output(result, args.output)


def cmd_bgp_sessions(args):
    result = get_client().bgp_list_sessions()
    data = result if isinstance(result, list) else result.get("sessions", result)
    print_output(data, args.output)


def cmd_bgp_create(args):
    result = get_client().bgp_create_session(args.name, args.peer_as, args.peer_ip)
    print_output(result, args.output)


def cmd_bgp_delete(args):
    result = get_client().bgp_delete_session(args.session_id)
    print_output(result, args.output)


def cmd_bgp_routes(args):
    result = get_client().bgp_routes()
    data = result if isinstance(result, list) else result.get("routes", result)
    print_output(data, args.output)


def cmd_proxy_rules(args):
    result = get_client().proxy_list_rules()
    data = result if isinstance(result, list) else result.get("rules", result)
    print_output(data, args.output)


def cmd_proxy_create(args):
    result = get_client().proxy_create_rule(args.domain, args.target, args.tls)
    print_output(result, args.output)


def cmd_proxy_delete(args):
    result = get_client().proxy_delete_rule(args.rule_id)
    print_output(result, args.output)


def cmd_proxy_toggle(args):
    result = get_client().proxy_toggle(args.rule_id)
    print_output(result, args.output)


def cmd_seg_list(args):
    result = get_client().seg_list_segments()
    data = result if isinstance(result, list) else result.get("segments", result)
    print_output(data, args.output)


def cmd_seg_create(args):
    result = get_client().seg_create_segment(args.name, args.cidr, args.env)
    print_output(result, args.output)


def cmd_seg_delete(args):
    result = get_client().seg_delete_segment(args.segment_id)
    print_output(result, args.output)


def cmd_cap_list(args):
    result = get_client().cap_list_captures()
    data = result if isinstance(result, list) else result.get("captures", result)
    print_output(data, args.output)


def cmd_cap_start(args):
    result = get_client().cap_start_capture(args.interface, args.duration, args.filter)
    print_output(result, args.output)


def cmd_cap_stop(args):
    result = get_client().cap_stop_capture(args.capture_id)
    print_output(result, args.output)


def cmd_dnsfilter_status(args):
    result = get_client().dnsfilter_status()
    print_output(result, args.output)


def cmd_dnsfilter_rules(args):
    result = get_client().dnsfilter_list_rules()
    data = result if isinstance(result, list) else result.get("rules", result)
    print_output(data, args.output)


def cmd_dnsfilter_add(args):
    result = get_client().dnsfilter_create_rule(args.domain, args.action)
    print_output(result, args.output)


def cmd_dnsfilter_remove(args):
    result = get_client().dnsfilter_delete_rule(args.rule_id)
    print_output(result, args.output)


def cmd_dhcp_leases(args):
    result = get_client().dhcp_leases()
    data = result if isinstance(result, list) else result.get("leases", result)
    print_output(data, args.output)


def cmd_netcost_show(args):
    result = get_client().cost_get_costs()
    print_output(result, args.output)


def cmd_netcost_budget(args):
    result = get_client().cost_set_budget(args.monthly_budget)
    print_output(result, args.output)


def cmd_cell_networks(args):
    result = get_client().cell_list_networks()
    data = result if isinstance(result, list) else result.get("networks", result)
    print_output(data, args.output)


def cmd_cell_register(args):
    result = get_client().cell_register_network(args.name, args.provider, args.apn)
    print_output(result, args.output)


def cmd_cell_delete(args):
    result = get_client().cell_delete_network(args.network_id)
    print_output(result, args.output)


def cmd_cell_status(args):
    result = get_client().cell_status()
    print_output(result, args.output)


def cmd_cell_sims(args):
    result = get_client().cell_list_sims()
    data = result if isinstance(result, list) else result.get("sims", result)
    print_output(data, args.output)


def cmd_cell_activate(args):
    result = get_client().cell_activate_sim(args.sim_id)
    print_output(result, args.output)


def cmd_cell_deactivate(args):
    result = get_client().cell_deactivate_sim(args.sim_id)
    print_output(result, args.output)


# === v3 Marketplace Commands ===


# === v4 Emerging Tech Handler Functions ===


def build_parser() -> argparse.ArgumentParser:
    """Build and configure the argparse-based CLI parser with all subcommands.

    Returns:
        A fully configured ``ArgumentParser`` instance.
    """
    parser = argparse.ArgumentParser(
        prog="ipilot",
        description="Infra Pilot CLI - Infrastructure management tool",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "--output",
        "-o",
        choices=["json", "table", "yaml", "plain"],
        default=get("output_format", "table"),
        help="Output format (default: table)",
    )

    sub = parser.add_subparsers(dest="command")

    p_login = sub.add_parser("login", help="Authenticate with the API")
    p_login.add_argument("api_key", help="API key")

    sub.add_parser("logout", help="Clear authentication token")

    p_health = sub.add_parser("health", help="System health check")
    p_health.set_defaults(func=cmd_health)

    p_server = sub.add_parser("server", help="Server management commands")
    p_server_sub = p_server.add_subparsers(dest="subcommand")

    p_server_list = p_server_sub.add_parser("list", help="List all servers")
    p_server_create = p_server_sub.add_parser("create", help="Create a new server")
    p_server_create.add_argument("name", help="Server name")
    p_server_create.add_argument("--type", "-t", required=True, help="Server type")
    p_server_create.add_argument("--memory", "-m", type=int, help="Memory in MB")
    p_server_delete = p_server_sub.add_parser("delete", help="Delete a server")
    p_server_delete.add_argument("server", help="Server ID or name")
    p_server_status = p_server_sub.add_parser("status", help="Get server status")
    p_server_status.add_argument("server", help="Server ID or name")

    p_logs = sub.add_parser("logs", help="Fetch server logs")
    p_logs.add_argument("server", help="Server ID or name")
    p_logs.add_argument("--lines", "-n", type=int, default=50, help="Number of lines")
    p_logs.add_argument("--follow", "-f", action="store_true", help="Follow log output")

    p_backup = sub.add_parser("backup", help="Backup management")
    p_backup_sub = p_backup.add_subparsers(dest="subcommand")
    p_backup_list = p_backup_sub.add_parser("list", help="List backups")
    p_backup_list.add_argument("server", nargs="?", help="Server ID (optional)")
    p_backup_create = p_backup_sub.add_parser("create", help="Create a backup")
    p_backup_create.add_argument("server", help="Server ID or name")

    p_deploy = sub.add_parser("deploy", help="Deploy a branch to a server")
    p_deploy.add_argument("server", help="Server ID or name")
    p_deploy.add_argument("branch", help="Branch to deploy")

    p_config = sub.add_parser("config", help="Configuration management")
    p_config_sub = p_config.add_subparsers(dest="subcommand")
    p_config_get = p_config_sub.add_parser("get", help="Get config value(s)")
    p_config_get.add_argument("key", nargs="?", help="Config key")
    p_config_set = p_config_sub.add_parser("set", help="Set a config value")
    p_config_set.add_argument("key", help="Config key")
    p_config_set.add_argument("value", help="Config value")

    # === Edge & IoT Commands ===
    p_audit = sub.add_parser("audit", help="Audit analytics")
    p_audit_sub = p_audit.add_subparsers(dest="subcommand")
    p_audit_anomalies = p_audit_sub.add_parser("anomalies", help="List anomalies")
    p_audit_trend = p_audit_sub.add_parser("trend", help="Get anomaly trend")
    p_audit_trend.add_argument("user_id", help="User ID")
    p_audit_summary = p_audit_sub.add_parser("summary", help="Audit summary")

    p_quota = sub.add_parser("quota", help="Resource quota management")
    p_quota_sub = p_quota.add_subparsers(dest="subcommand")
    p_quota_list = p_quota_sub.add_parser("list", help="List quotas")
    p_quota_check = p_quota_sub.add_parser("check", help="Check quota")
    p_quota_check.add_argument("entity_type", help="Entity type (org/team/project)")
    p_quota_check.add_argument("entity_id", help="Entity ID")
    p_quota_check.add_argument("--cpu", type=int, help="CPU cores requested")
    p_quota_check.add_argument("--memory", type=int, help="Memory GB requested")

    p_maintenance = sub.add_parser("maintenance", help="Maintenance scheduling")
    p_maintenance_sub = p_maintenance.add_subparsers(dest="subcommand")
    p_maintenance_list = p_maintenance_sub.add_parser(
        "list", help="List maintenance windows"
    )
    p_maintenance_schedule = p_maintenance_sub.add_parser(
        "schedule", help="Schedule maintenance"
    )
    p_maintenance_schedule.add_argument("name", help="Window name")
    p_maintenance_schedule.add_argument(
        "--start", required=True, help="Start time (ISO format)"
    )
    p_maintenance_schedule.add_argument(
        "--end", required=True, help="End time (ISO format)"
    )
    p_maintenance_schedule.add_argument(
        "--systems", required=True, help="Comma-separated affected systems"
    )

    p_sdwan = sub.add_parser("sdwan", help="SD-WAN controller")
    p_sdwan_sub = p_sdwan.add_subparsers(dest="subcommand")
    p_sdwan_status = p_sdwan_sub.add_parser("status", help="SD-WAN status")
    p_sdwan_apps = p_sdwan_sub.add_parser("apps", help="List SD-WAN apps")
    p_sdwan_create = p_sdwan_sub.add_parser("create", help="Create SD-WAN app")
    p_sdwan_create.add_argument("name", help="App name")
    p_sdwan_create.add_argument("provider", help="Provider (aws, azure, gcp)")
    p_sdwan_create.add_argument(
        "--bandwidth", type=int, default=100, help="Bandwidth Mbps"
    )
    p_sdwan_delete = p_sdwan_sub.add_parser("delete", help="Delete SD-WAN app")
    p_sdwan_delete.add_argument("app_id", help="App ID")
    p_sdwan_toggle = p_sdwan_sub.add_parser("toggle", help="Toggle SD-WAN app")
    p_sdwan_toggle.add_argument("app_id", help="App ID")

    p_vpn = sub.add_parser("vpn", help="VPN as a service")
    p_vpn_sub = p_vpn.add_subparsers(dest="subcommand")
    p_vpn_configs = p_vpn_sub.add_parser("configs", help="List VPN configs")
    p_vpn_create = p_vpn_sub.add_parser("create", help="Create VPN config")
    p_vpn_create.add_argument("name", help="Config name")
    p_vpn_create.add_argument("server", help="VPN server")
    p_vpn_create.add_argument("--port", type=int, default=1194, help="Port")
    p_vpn_create.add_argument(
        "--protocol", default="udp", choices=["udp", "tcp"], help="Protocol"
    )
    p_vpn_delete = p_vpn_sub.add_parser("delete", help="Delete VPN config")
    p_vpn_delete.add_argument("config_id", help="Config ID")
    p_vpn_status = p_vpn_sub.add_parser("status", help="VPN status")

    p_dns = sub.add_parser("dns", help="DNS management")
    p_dns_sub = p_dns.add_subparsers(dest="subcommand")
    p_dns_zones = p_dns_sub.add_parser("zones", help="List DNS zones")
    p_dns_create_zone = p_dns_sub.add_parser("create-zone", help="Create DNS zone")
    p_dns_create_zone.add_argument("domain", help="Domain name")
    p_dns_create_zone.add_argument("--ttl", type=int, default=3600, help="TTL")
    p_dns_delete_zone = p_dns_sub.add_parser("delete-zone", help="Delete DNS zone")
    p_dns_delete_zone.add_argument("zone_id", help="Zone ID")
    p_dns_records = p_dns_sub.add_parser("records", help="List DNS records")
    p_dns_records.add_argument("zone_id", help="Zone ID")
    p_dns_add_record = p_dns_sub.add_parser("add-record", help="Add DNS record")
    p_dns_add_record.add_argument("zone_id", help="Zone ID")
    p_dns_add_record.add_argument("name", help="Record name")
    p_dns_add_record.add_argument(
        "type", choices=["A", "AAAA", "CNAME", "MX", "TXT", "NS"], help="Record type"
    )
    p_dns_add_record.add_argument("value", help="Record value")
    p_dns_add_record.add_argument("--ttl", type=int, default=3600, help="TTL")
    p_dns_delete_record = p_dns_sub.add_parser(
        "delete-record", help="Delete DNS record"
    )
    p_dns_delete_record.add_argument("zone_id", help="Zone ID")
    p_dns_delete_record.add_argument("record_id", help="Record ID")

    p_bgp = sub.add_parser("bgp", help="BGP route manager")
    p_bgp_sub = p_bgp.add_subparsers(dest="subcommand")
    p_bgp_sessions = p_bgp_sub.add_parser("sessions", help="List BGP sessions")
    p_bgp_create = p_bgp_sub.add_parser("create", help="Create BGP session")
    p_bgp_create.add_argument("name", help="Session name")
    p_bgp_create.add_argument(
        "--peer-as", required=True, type=int, help="Peer AS number"
    )
    p_bgp_create.add_argument("--peer-ip", required=True, help="Peer IP address")
    p_bgp_delete = p_bgp_sub.add_parser("delete", help="Delete BGP session")
    p_bgp_delete.add_argument("session_id", help="Session ID")
    p_bgp_routes = p_bgp_sub.add_parser("routes", help="Show BGP routes")

    p_proxy = sub.add_parser("proxy", help="Reverse proxy catalog")
    p_proxy_sub = p_proxy.add_subparsers(dest="subcommand")
    p_proxy_rules = p_proxy_sub.add_parser("rules", help="List proxy rules")
    p_proxy_create = p_proxy_sub.add_parser("create", help="Create proxy rule")
    p_proxy_create.add_argument("domain", help="Domain name")
    p_proxy_create.add_argument("target", help="Target URL")
    p_proxy_create.add_argument("--tls", action="store_true", help="Enable TLS")
    p_proxy_delete = p_proxy_sub.add_parser("delete", help="Delete proxy rule")
    p_proxy_delete.add_argument("rule_id", help="Rule ID")
    p_proxy_toggle = p_proxy_sub.add_parser("toggle", help="Toggle proxy rule")
    p_proxy_toggle.add_argument("rule_id", help="Rule ID")

    p_segment = sub.add_parser("segment", help="Network segmentation")
    p_segment_sub = p_segment.add_subparsers(dest="subcommand")
    p_seg_list = p_segment_sub.add_parser("list", help="List segments")
    p_seg_create = p_segment_sub.add_parser("create", help="Create segment")
    p_seg_create.add_argument("name", help="Segment name")
    p_seg_create.add_argument("cidr", help="CIDR range")
    p_seg_create.add_argument("--env", default="production", help="Environment")
    p_seg_delete = p_segment_sub.add_parser("delete", help="Delete segment")
    p_seg_delete.add_argument("segment_id", help="Segment ID")

    p_capture = sub.add_parser("capture", help="Packet capture studio")
    p_capture_sub = p_capture.add_subparsers(dest="subcommand")
    p_cap_list = p_capture_sub.add_parser("list", help="List captures")
    p_cap_start = p_capture_sub.add_parser("start", help="Start capture")
    p_cap_start.add_argument("--interface", default="eth0", help="Interface")
    p_cap_start.add_argument(
        "--duration", type=int, default=60, help="Duration seconds"
    )
    p_cap_start.add_argument("--filter", default="", help="BPF filter")
    p_cap_stop = p_capture_sub.add_parser("stop", help="Stop capture")
    p_cap_stop.add_argument("capture_id", help="Capture ID")

    p_dnsfilter = sub.add_parser("dnsfilter", help="DNS filtering & DHCP")
    p_dnsfilter_sub = p_dnsfilter.add_subparsers(dest="subcommand")
    p_dnsfilter_status = p_dnsfilter_sub.add_parser("status", help="DNS filter status")
    p_dnsfilter_rules = p_dnsfilter_sub.add_parser("rules", help="List filtering rules")
    p_dnsfilter_add = p_dnsfilter_sub.add_parser("add", help="Add filtering rule")
    p_dnsfilter_add.add_argument("domain", help="Domain to filter")
    p_dnsfilter_add.add_argument(
        "--action",
        default="block",
        choices=["block", "allow", "redirect"],
        help="Action",
    )
    p_dnsfilter_remove = p_dnsfilter_sub.add_parser(
        "remove", help="Remove filtering rule"
    )
    p_dnsfilter_remove.add_argument("rule_id", help="Rule ID")

    p_dhcp = sub.add_parser("dhcp", help="DHCP management")
    p_dhcp_sub = p_dhcp.add_subparsers(dest="subcommand")
    p_dhcp_leases = p_dhcp_sub.add_parser("leases", help="List DHCP leases")

    p_netcost = sub.add_parser("netcost", help="Network cost analyzer")
    p_netcost_sub = p_netcost.add_subparsers(dest="subcommand")
    p_netcost_show = p_netcost_sub.add_parser("show", help="Show network costs")
    p_netcost_budget = p_netcost_sub.add_parser("budget", help="Set cost budget")
    p_netcost_budget.add_argument("monthly_budget", type=float, help="Monthly budget")

    p_cell = sub.add_parser("cell", help="5G/LTE cellular integration")
    p_cell_sub = p_cell.add_subparsers(dest="subcommand")
    p_cell_networks = p_cell_sub.add_parser("networks", help="List cellular networks")
    p_cell_register = p_cell_sub.add_parser("register", help="Register network")
    p_cell_register.add_argument("name", help="Network name")
    p_cell_register.add_argument("provider", help="Provider (att, verizon, tmobile)")
    p_cell_register.add_argument("apn", help="APN")
    p_cell_delete = p_cell_sub.add_parser("delete", help="Delete network")
    p_cell_delete.add_argument("network_id", help="Network ID")
    p_cell_status = p_cell_sub.add_parser("status", help="Cellular status")
    p_cell_sims = p_cell_sub.add_parser("sims", help="List SIM cards")
    p_cell_activate = p_cell_sub.add_parser("activate", help="Activate SIM")
    p_cell_activate.add_argument("sim_id", help="SIM ID")
    p_cell_deactivate = p_cell_sub.add_parser("deactivate", help="Deactivate SIM")
    p_cell_deactivate.add_argument("sim_id", help="SIM ID")

    # === v3 Marketplace Commands ===
    p_devportal = sub.add_parser("devportal", help="Developer portal")
    p_devportal_sub = p_devportal.add_subparsers(dest="subcommand")
    p_devportal_list = p_devportal_sub.add_parser("list", help="List components")
    p_devportal_list.add_argument("--domain", help="Filter by domain")
    p_devportal_register = p_devportal_sub.add_parser(
        "register", help="Register component"
    )
    p_devportal_register.add_argument("name", help="Component name")
    p_devportal_register.add_argument("domain", help="Domain")
    p_devportal_register.add_argument(
        "--description", "-d", default="", help="Description"
    )
    p_devportal_register.add_argument(
        "--owner", "-o", default="platform", help="Owner team"
    )
    p_devportal_get = p_devportal_sub.add_parser("get", help="Get component details")
    p_devportal_get.add_argument("component_id", help="Component ID")
    p_devportal_summary = p_devportal_sub.add_parser("summary", help="Portal summary")

    p_scaffold = sub.add_parser("scaffold", help="Golden path scaffold")
    p_scaffold_sub = p_scaffold.add_subparsers(dest="subcommand")
    p_scaffold_list = p_scaffold_sub.add_parser("list", help="List templates")
    p_scaffold_generate = p_scaffold_sub.add_parser(
        "generate", help="Generate from template"
    )
    p_scaffold_generate.add_argument("template_id", help="Template ID")
    p_scaffold_generate.add_argument("project_name", help="Project name")
    p_scaffold_generate.add_argument("--params", "-p", default="{}", help="JSON params")
    p_scaffold_status = p_scaffold_sub.add_parser("status", help="Generation status")
    p_scaffold_status.add_argument("generation_id", help="Generation ID")
    p_scaffold_step = p_scaffold_sub.add_parser("step", help="Complete a step")
    p_scaffold_step.add_argument("generation_id", help="Generation ID")
    p_scaffold_step.add_argument("step_name", help="Step name")
    p_scaffold_step.add_argument("--outputs", default="{}", help="JSON step outputs")

    p_catalog = sub.add_parser("service-catalog", help="Service catalog")
    p_catalog_sub = p_catalog.add_subparsers(dest="subcommand")
    p_catalog_list = p_catalog_sub.add_parser("list", help="List services")
    p_catalog_register = p_catalog_sub.add_parser("register", help="Register service")
    p_catalog_register.add_argument("name", help="Service name")
    p_catalog_register.add_argument("domain", help="Domain")
    p_catalog_register.add_argument(
        "--description", "-d", default="", help="Description"
    )
    p_catalog_register.add_argument("--owner", "-o", default="platform", help="Owner")
    p_catalog_get = p_catalog_sub.add_parser("get", help="Get service details")
    p_catalog_get.add_argument("service_id", help="Service ID")
    p_catalog_score = p_catalog_sub.add_parser("score", help="Score service readiness")
    p_catalog_score.add_argument("service_id", help="Service ID")
    p_catalog_summary = p_catalog_sub.add_parser("summary", help="Catalog summary")

    p_scorecards = sub.add_parser("scorecards", help="DORA scorecards")
    p_scorecards_sub = p_scorecards.add_subparsers(dest="subcommand")
    p_scorecards_list = p_scorecards_sub.add_parser("list", help="List scorecards")
    p_scorecards_create = p_scorecards_sub.add_parser("create", help="Create scorecard")
    p_scorecards_create.add_argument("name", help="Scorecard name")
    p_scorecards_create.add_argument("team", help="Team name")
    p_scorecards_create.add_argument(
        "--dora", action="store_true", help="Include DORA metrics"
    )
    p_scorecards_get = p_scorecards_sub.add_parser("get", help="Get scorecard")
    p_scorecards_get.add_argument("scorecard_id", help="Scorecard ID")
    p_scorecards_update = p_scorecards_sub.add_parser("update", help="Update metric")
    p_scorecards_update.add_argument("scorecard_id", help="Scorecard ID")
    p_scorecards_update.add_argument("metric", help="Metric name")
    p_scorecards_update.add_argument("value", help="Metric value")
    p_scorecards_summary = p_scorecards_sub.add_parser(
        "summary", help="Scorecards summary"
    )

    p_templatereg = sub.add_parser("template-registry", help="Template registry")
    p_templatereg_sub = p_templatereg.add_subparsers(dest="subcommand")
    p_templatereg_list = p_templatereg_sub.add_parser("list", help="List templates")
    p_templatereg_create = p_templatereg_sub.add_parser(
        "create", help="Create template"
    )
    p_templatereg_create.add_argument("name", help="Template name")
    p_templatereg_create.add_argument("category", help="Category")
    p_templatereg_create.add_argument(
        "--params", "-p", default="{}", help="JSON params schema"
    )
    p_templatereg_get = p_templatereg_sub.add_parser("get", help="Get template")
    p_templatereg_get.add_argument("template_id", help="Template ID")
    p_templatereg_use = p_templatereg_sub.add_parser(
        "use", help="Record template usage"
    )
    p_templatereg_use.add_argument("template_id", help="Template ID")
    p_templatereg_summary = p_templatereg_sub.add_parser(
        "summary", help="Registry summary"
    )

    p_techdebt = sub.add_parser("techdebt", help="Tech debt tracker")
    p_techdebt_sub = p_techdebt.add_subparsers(dest="subcommand")
    p_techdebt_list = p_techdebt_sub.add_parser("list", help="List debt items")
    p_techdebt_list.add_argument("--severity", help="Filter by severity")
    p_techdebt_report = p_techdebt_sub.add_parser("report", help="Report debt item")
    p_techdebt_report.add_argument("title", help="Title")
    p_techdebt_report.add_argument(
        "severity", choices=["low", "medium", "high", "critical"], help="Severity"
    )
    p_techdebt_report.add_argument("effort_hours", type=int, help="Effort hours")
    p_techdebt_report.add_argument("--area", "-a", default="code", help="Area")
    p_techdebt_get = p_techdebt_sub.add_parser("get", help="Get debt item")
    p_techdebt_get.add_argument("debt_id", help="Debt ID")
    p_techdebt_fix = p_techdebt_sub.add_parser("fix", help="Mark as fixed")
    p_techdebt_fix.add_argument("debt_id", help="Debt ID")
    p_techdebt_summary = p_techdebt_sub.add_parser("summary", help="Debt summary")

    p_environments = sub.add_parser("environments", help="Ephemeral environments")
    p_environments_sub = p_environments.add_subparsers(dest="subcommand")
    p_environments_list = p_environments_sub.add_parser(
        "list", help="List environments"
    )
    p_environments_list.add_argument("--status", help="Filter by status")
    p_environments_create = p_environments_sub.add_parser(
        "create", help="Create environment"
    )
    p_environments_create.add_argument("name", help="Environment name")
    p_environments_create.add_argument("template", help="Environment template")
    p_environments_create.add_argument(
        "--ttl", "-t", type=int, default=24, help="TTL hours"
    )
    p_environments_create.add_argument(
        "--branch", "-b", default="main", help="Git branch"
    )
    p_environments_get = p_environments_sub.add_parser("get", help="Get environment")
    p_environments_get.add_argument("env_id", help="Environment ID")
    p_environments_delete = p_environments_sub.add_parser(
        "delete", help="Delete environment"
    )
    p_environments_delete.add_argument("env_id", help="Environment ID")
    p_environments_extend = p_environments_sub.add_parser("extend", help="Extend TTL")
    p_environments_extend.add_argument("env_id", help="Environment ID")
    p_environments_extend.add_argument("hours", type=int, help="Additional hours")
    p_environments_summary = p_environments_sub.add_parser(
        "summary", help="Environment stats"
    )

    p_apicatalog = sub.add_parser("api-catalog", help="API catalog")
    p_apicatalog_sub = p_apicatalog.add_subparsers(dest="subcommand")
    p_apicatalog_list = p_apicatalog_sub.add_parser("list", help="List APIs")
    p_apicatalog_register = p_apicatalog_sub.add_parser(
        "register", help="Register API from spec"
    )
    p_apicatalog_register.add_argument("name", help="API name")
    p_apicatalog_register.add_argument("version", help="API version")
    p_apicatalog_register.add_argument("spec", help="OpenAPI spec file path")
    p_apicatalog_get = p_apicatalog_sub.add_parser("get", help="Get API details")
    p_apicatalog_get.add_argument("api_id", help="API ID")
    p_apicatalog_summary = p_apicatalog_sub.add_parser(
        "summary", help="Catalog summary"
    )

    p_docgen = sub.add_parser("docgen", help="Doc generator")
    p_docgen_sub = p_docgen.add_subparsers(dest="subcommand")
    p_docgen_list = p_docgen_sub.add_parser("list", help="List documents")
    p_docgen_generate = p_docgen_sub.add_parser("generate", help="Generate document")
    p_docgen_generate.add_argument("title", help="Document title")
    p_docgen_generate.add_argument(
        "doc_type",
        choices=["adr", "c4_context", "c4_container", "c4_component"],
        help="Document type",
    )
    p_docgen_get = p_docgen_sub.add_parser("get", help="Get document")
    p_docgen_get.add_argument("doc_id", help="Document ID")
    p_docgen_summary = p_docgen_sub.add_parser("summary", help="Doc generator stats")

    p_pulse = sub.add_parser("pulse", help="Developer pulse surveys")
    p_pulse_sub = p_pulse.add_subparsers(dest="subcommand")
    p_pulse_list = p_pulse_sub.add_parser("list", help="List surveys")
    p_pulse_create = p_pulse_sub.add_parser("create", help="Create survey")
    p_pulse_create.add_argument("title", help="Survey title")
    p_pulse_create.add_argument("questions_json", help="JSON array of questions")
    p_pulse_respond = p_pulse_sub.add_parser("respond", help="Submit response")
    p_pulse_respond.add_argument("survey_id", help="Survey ID")
    p_pulse_respond.add_argument("respondent", help="Respondent identifier")
    p_pulse_respond.add_argument("answers_json", help="JSON answers object")
    p_pulse_results = p_pulse_sub.add_parser("results", help="Get survey results")
    p_pulse_results.add_argument("survey_id", help="Survey ID")
    p_pulse_summary = p_pulse_sub.add_parser("summary", help="Pulse summary")

    # === v4 AIOps Commands ===
    return parser


# === v4 Customer Experience Commands ===


# === v3 Identity & Governance Commands ===


def cmd_audit_anomalies(args):
    result = get_client().audit_get_anomalies()
    data = result if isinstance(result, list) else result.get("anomalies", result)
    print_output(data, args.output)


def cmd_audit_trend(args):
    result = get_client().audit_get_trend(args.user_id)
    print_output(result, args.output)


def cmd_audit_summary(args):
    result = get_client().audit_get_summary()
    print_output(result, args.output)


def cmd_quota_list(args):
    result = get_client().quota_list()
    data = result if isinstance(result, list) else result.get("quotas", result)
    print_output(data, args.output)


def cmd_quota_check(args):
    resources = {}
    if args.cpu:
        resources["cpu"] = args.cpu
    if args.memory:
        resources["memory"] = args.memory
    result = get_client().quota_check(args.entity_type, args.entity_id, resources)
    print_output(result, args.output)


def cmd_maintenance_list(args):
    result = get_client().maintenance_list_windows()
    data = result if isinstance(result, list) else result.get("windows", result)
    print_output(data, args.output)


def cmd_maintenance_schedule(args):
    systems = [s.strip() for s in args.systems.split(",")]
    result = get_client().maintenance_schedule(args.name, args.start, args.end, systems)
    print_output(result, args.output)

    # === v4 Platform Engineering Commands ===


def cmd_devportal_list(args):
    result = get_client().devportal_list_components(args.domain)
    data = result if isinstance(result, list) else result.get("components", result)
    print_output(data, args.output)


def cmd_devportal_register(args):
    result = get_client().devportal_register_component(
        args.name, args.domain, args.description, args.owner
    )
    print_output(result, args.output)


def cmd_devportal_get(args):
    result = get_client().devportal_get_component(args.component_id)
    print_output(result, args.output)


def cmd_devportal_summary(args):
    result = get_client().devportal_summary()
    print_output(result, args.output)


def cmd_scaffold_list(args):
    result = get_client().scaffold_list_templates()
    data = result if isinstance(result, list) else result.get("templates", result)
    print_output(data, args.output)


def cmd_scaffold_generate(args):
    params = json.loads(args.params) if args.params else {}
    result = get_client().scaffold_generate(args.template_id, args.project_name, params)
    print_output(result, args.output)


def cmd_scaffold_status(args):
    result = get_client().scaffold_status(args.generation_id)
    print_output(result, args.output)


def cmd_scaffold_step(args):
    outputs = json.loads(args.outputs) if args.outputs else {}
    result = get_client().scaffold_complete_step(
        args.generation_id, args.step_name, outputs
    )
    print_output(result, args.output)


def cmd_catalog_list(args):
    result = get_client().catalog_list_services()
    data = result if isinstance(result, list) else result.get("services", result)
    print_output(data, args.output)


def cmd_catalog_register(args):
    result = get_client().catalog_register_service(
        args.name, args.domain, args.description, args.owner
    )
    print_output(result, args.output)


def cmd_catalog_get(args):
    result = get_client().catalog_get_service(args.service_id)
    print_output(result, args.output)


def cmd_catalog_score(args):
    result = get_client().catalog_score_service(args.service_id)
    print_output(result, args.output)


def cmd_catalog_summary(args):
    result = get_client().catalog_summary()
    print_output(result, args.output)


def cmd_scorecards_list(args):
    result = get_client().scorecards_list()
    data = result if isinstance(result, list) else result.get("scorecards", result)
    print_output(data, args.output)


def cmd_scorecards_create(args):
    result = get_client().scorecards_create(args.name, args.team, args.dora)
    print_output(result, args.output)


def cmd_scorecards_get(args):
    result = get_client().scorecards_get(args.scorecard_id)
    print_output(result, args.output)


def cmd_scorecards_update(args):
    result = get_client().scorecards_update_metric(
        args.scorecard_id, args.metric, args.value
    )
    print_output(result, args.output)


def cmd_scorecards_summary(args):
    result = get_client().scorecards_summary()
    print_output(result, args.output)


def cmd_templatereg_list(args):
    result = get_client().templatereg_list()
    data = result if isinstance(result, list) else result.get("templates", result)
    print_output(data, args.output)


def cmd_templatereg_create(args):
    params = json.loads(args.params) if args.params else {}
    result = get_client().templatereg_create(args.name, args.category, params)
    print_output(result, args.output)


def cmd_templatereg_get(args):
    result = get_client().templatereg_get(args.template_id)
    print_output(result, args.output)


def cmd_templatereg_use(args):
    result = get_client().templatereg_use(args.template_id)
    print_output(result, args.output)


def cmd_templatereg_summary(args):
    result = get_client().templatereg_summary()
    print_output(result, args.output)


def cmd_techdebt_list(args):
    result = get_client().techdebt_list(args.severity)
    data = result if isinstance(result, list) else result.get("items", result)
    print_output(data, args.output)


def cmd_techdebt_report(args):
    result = get_client().techdebt_report(
        args.title, args.severity, args.effort_hours, args.area
    )
    print_output(result, args.output)


def cmd_techdebt_get(args):
    result = get_client().techdebt_get(args.debt_id)
    print_output(result, args.output)


def cmd_techdebt_fix(args):
    result = get_client().techdebt_fix(args.debt_id)
    print_output(result, args.output)


def cmd_techdebt_summary(args):
    result = get_client().techdebt_summary()
    print_output(result, args.output)


def cmd_environments_list(args):
    result = get_client().environments_list(args.status)
    data = result if isinstance(result, list) else result.get("environments", result)
    print_output(data, args.output)


def cmd_environments_create(args):
    result = get_client().environments_create(
        args.name, args.template, args.ttl, args.branch
    )
    print_output(result, args.output)


def cmd_environments_get(args):
    result = get_client().environments_get(args.env_id)
    print_output(result, args.output)


def cmd_environments_delete(args):
    result = get_client().environments_delete(args.env_id)
    print_output(result, args.output)


def cmd_environments_extend(args):
    result = get_client().environments_extend(args.env_id, args.hours)
    print_output(result, args.output)


def cmd_environments_summary(args):
    result = get_client().environments_summary()
    print_output(result, args.output)


def cmd_apicatalog_list(args):
    result = get_client().apicatalog_list()
    data = result if isinstance(result, list) else result.get("apis", result)
    print_output(data, args.output)


def cmd_apicatalog_register(args):
    with open(args.spec, "r") as f:
        spec_content = f.read()
    result = get_client().apicatalog_register(args.name, args.version, spec_content)
    print_output(result, args.output)


def cmd_apicatalog_get(args):
    result = get_client().apicatalog_get(args.api_id)
    print_output(result, args.output)


def cmd_apicatalog_summary(args):
    result = get_client().apicatalog_summary()
    print_output(result, args.output)


def cmd_docgen_list(args):
    result = get_client().docgen_list()
    data = result if isinstance(result, list) else result.get("documents", result)
    print_output(data, args.output)


def cmd_docgen_generate(args):
    result = get_client().docgen_generate(args.title, args.doc_type)
    print_output(result, args.output)


def cmd_docgen_get(args):
    result = get_client().docgen_get(args.doc_id)
    print_output(result, args.output)


def cmd_docgen_summary(args):
    result = get_client().docgen_summary()
    print_output(result, args.output)


def cmd_pulse_list(args):
    result = get_client().pulse_list_surveys()
    data = result if isinstance(result, list) else result.get("surveys", result)
    print_output(data, args.output)


def cmd_pulse_create(args):
    questions = json.loads(args.questions_json)
    result = get_client().pulse_create_survey(args.title, questions)
    print_output(result, args.output)


def cmd_pulse_respond(args):
    answers = json.loads(args.answers_json)
    result = get_client().pulse_respond(args.survey_id, args.respondent, answers)
    print_output(result, args.output)


def cmd_pulse_results(args):
    result = get_client().pulse_results(args.survey_id)
    print_output(result, args.output)


def cmd_pulse_summary(args):
    result = get_client().pulse_summary()
    print_output(result, args.output)


# === v4 AIOps Commands ===


# === v4 FinOps Commands ===


# === v4 SOC Commands ===


def main_inner(args, parser=None):
    warnings.warn(
        "This argparse-based CLI is deprecated. Use the Typer-based CLI via `ipilot` instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    if parser is None:
        parser = build_parser()
    cmd_map = {
        "login": cmd_login,
        "logout": cmd_logout,
        "health": cmd_health,
    }

    sub_router = {
        "server": {
            "list": cmd_server_list,
            "create": cmd_server_create,
            "delete": cmd_server_delete,
            "status": cmd_server_status,
        },
        "backup": {"list": cmd_backup_list, "create": cmd_backup_create},
        "config": {"get": cmd_config_get, "set": cmd_config_set},
        "audit": {
            "anomalies": cmd_audit_anomalies,
            "trend": cmd_audit_trend,
            "summary": cmd_audit_summary,
        },
        "quota": {"list": cmd_quota_list, "check": cmd_quota_check},
        "maintenance": {
            "list": cmd_maintenance_list,
            "schedule": cmd_maintenance_schedule,
        },
        "sdwan": {
            "status": cmd_sdwan_status,
            "apps": cmd_sdwan_apps,
            "create": cmd_sdwan_create,
            "delete": cmd_sdwan_delete,
            "toggle": cmd_sdwan_toggle,
        },
        "vpn": {
            "configs": cmd_vpn_configs,
            "create": cmd_vpn_create,
            "delete": cmd_vpn_delete,
            "status": cmd_vpn_status,
        },
        "dns": {
            "zones": cmd_dns_zones,
            "create-zone": cmd_dns_create_zone,
            "delete-zone": cmd_dns_delete_zone,
            "records": cmd_dns_records,
            "add-record": cmd_dns_add_record,
            "delete-record": cmd_dns_delete_record,
        },
        "bgp": {
            "sessions": cmd_bgp_sessions,
            "create": cmd_bgp_create,
            "delete": cmd_bgp_delete,
            "routes": cmd_bgp_routes,
        },
        "proxy": {
            "rules": cmd_proxy_rules,
            "create": cmd_proxy_create,
            "delete": cmd_proxy_delete,
            "toggle": cmd_proxy_toggle,
        },
        "segment": {
            "list": cmd_seg_list,
            "create": cmd_seg_create,
            "delete": cmd_seg_delete,
        },
        "capture": {"list": cmd_cap_list, "start": cmd_cap_start, "stop": cmd_cap_stop},
        "dnsfilter": {
            "status": cmd_dnsfilter_status,
            "rules": cmd_dnsfilter_rules,
            "add": cmd_dnsfilter_add,
            "remove": cmd_dnsfilter_remove,
        },
        "dhcp": {"leases": cmd_dhcp_leases},
        "netcost": {"show": cmd_netcost_show, "budget": cmd_netcost_budget},
        "cell": {
            "networks": cmd_cell_networks,
            "register": cmd_cell_register,
            "delete": cmd_cell_delete,
            "status": cmd_cell_status,
            "sims": cmd_cell_sims,
            "activate": cmd_cell_activate,
            "deactivate": cmd_cell_deactivate,
        },
        "devportal": {
            "list": cmd_devportal_list,
            "register": cmd_devportal_register,
            "get": cmd_devportal_get,
            "summary": cmd_devportal_summary,
        },
        "scaffold": {
            "list": cmd_scaffold_list,
            "generate": cmd_scaffold_generate,
            "status": cmd_scaffold_status,
            "step": cmd_scaffold_step,
        },
        "service-catalog": {
            "list": cmd_catalog_list,
            "register": cmd_catalog_register,
            "get": cmd_catalog_get,
            "score": cmd_catalog_score,
            "summary": cmd_catalog_summary,
        },
        "scorecards": {
            "list": cmd_scorecards_list,
            "create": cmd_scorecards_create,
            "get": cmd_scorecards_get,
            "update": cmd_scorecards_update,
            "summary": cmd_scorecards_summary,
        },
        "template-registry": {
            "list": cmd_templatereg_list,
            "create": cmd_templatereg_create,
            "get": cmd_templatereg_get,
            "use": cmd_templatereg_use,
            "summary": cmd_templatereg_summary,
        },
        "techdebt": {
            "list": cmd_techdebt_list,
            "report": cmd_techdebt_report,
            "get": cmd_techdebt_get,
            "fix": cmd_techdebt_fix,
            "summary": cmd_techdebt_summary,
        },
        "environments": {
            "list": cmd_environments_list,
            "create": cmd_environments_create,
            "get": cmd_environments_get,
            "delete": cmd_environments_delete,
            "extend": cmd_environments_extend,
            "summary": cmd_environments_summary,
        },
        "api-catalog": {
            "list": cmd_apicatalog_list,
            "register": cmd_apicatalog_register,
            "get": cmd_apicatalog_get,
            "summary": cmd_apicatalog_summary,
        },
        "docgen": {
            "list": cmd_docgen_list,
            "generate": cmd_docgen_generate,
            "get": cmd_docgen_get,
            "summary": cmd_docgen_summary,
        },
        "pulse": {
            "list": cmd_pulse_list,
            "create": cmd_pulse_create,
            "respond": cmd_pulse_respond,
            "results": cmd_pulse_results,
            "summary": cmd_pulse_summary,
        },
    }

    if args.command in sub_router:
        sub_map = sub_router[args.command]
        entry = sub_map.get(args.subcommand)
        if isinstance(entry, dict):
            action = getattr(args, "action", None)
            if action and action in entry:
                inner = entry[action]
                if isinstance(inner, dict):
                    maint_action = getattr(args, "maint_action", None)
                    inner.get(maint_action, lambda _args: parser.print_help())(args)
                else:
                    inner(args)
            else:
                parser.print_help()
        elif entry:
            entry(args)
        else:
            parser.print_help()
    elif args.command == "logs":
        cmd_logs(args)
    elif args.command == "deploy":
        cmd_deploy(args)
    elif args.command in cmd_map:
        cmd_map[args.command](args)
    else:
        parser.print_help()


def main():
    parser = build_parser()
    args = parser.parse_args()
    main_inner(args, parser)


if __name__ == "__main__":
    main()
