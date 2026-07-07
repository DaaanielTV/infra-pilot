import builtins
from typing import Any, Optional
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="Security Operations Center (SOC)")

soar_app = typer.Typer(help="SOAR playbooks")
threatintel_app = typer.Typer(help="Threat intelligence")
decoy_app = typer.Typer(help="Deception technology")
vuln_app = typer.Typer(help="Vulnerability management")
incident_app = typer.Typer(help="Incident response")
ueba_app = typer.Typer(help="UEBA (User and Entity Behavior Analytics)")
cspm_app = typer.Typer(help="Cloud Security Posture Management")
ndr_app = typer.Typer(help="Network Detection and Response")
secrets_app = typer.Typer(help="Secrets management")
training_app = typer.Typer(help="Security training")

app.add_typer(soar_app, name="soar")
app.add_typer(threatintel_app, name="threatintel")
app.add_typer(decoy_app, name="decoy")
app.add_typer(vuln_app, name="vuln")
app.add_typer(incident_app, name="incident")
app.add_typer(ueba_app, name="ueba")
app.add_typer(cspm_app, name="cspm")
app.add_typer(ndr_app, name="ndr")
app.add_typer(secrets_app, name="secrets")
app.add_typer(training_app, name="training")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


# --- SOAR ---

@soar_app.command()
def playbooks(ctx: typer.Context):
    """List SOAR playbooks"""
    client = _get_client(ctx)
    result = client.soar_playbooks()
    data = result if isinstance(result, _list_type) else result.get("playbooks", result)
    print_output(data, ctx.obj.get("output", "table"))


@soar_app.command()
def playbook(
    ctx: typer.Context,
    playbook_id: str = typer.Argument(..., help="Playbook ID"),
):
    """Get playbook details"""
    client = _get_client(ctx)
    result = client.soar_playbook(playbook_id)
    print_output(result, ctx.obj.get("output", "table"))


@soar_app.command()
def run(
    ctx: typer.Context,
    playbook_id: str = typer.Argument(..., help="Playbook ID"),
    params: str = typer.Option("{}", "--params", "-p", help="JSON parameters"),
):
    """Run a SOAR playbook"""
    client = _get_client(ctx)
    import json
    parsed = json.loads(params)
    result = client.soar_run(playbook_id, parsed)
    print_output(result, ctx.obj.get("output", "table"))


@soar_app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Playbook name"),
    steps: str = typer.Option(..., "--steps", "-s", help="JSON steps"),
    trigger: str = typer.Option(..., "--trigger", "-t", help="Trigger event"),
):
    """Create a SOAR playbook"""
    client = _get_client(ctx)
    import json
    parsed_steps = json.loads(steps)
    result = client.soar_create(name, parsed_steps, trigger)
    print_output(result, ctx.obj.get("output", "table"))


@soar_app.command()
def cases(ctx: typer.Context):
    """List SOAR cases"""
    client = _get_client(ctx)
    result = client.soar_cases()
    data = result if isinstance(result, _list_type) else result.get("cases", result)
    print_output(data, ctx.obj.get("output", "table"))


@soar_app.command()
def connectors(ctx: typer.Context):
    """List SOAR connectors"""
    client = _get_client(ctx)
    result = client.soar_connectors()
    data = result if isinstance(result, _list_type) else result.get("connectors", result)
    print_output(data, ctx.obj.get("output", "table"))


# --- Threat Intelligence ---

@threatintel_app.command()
def feeds(ctx: typer.Context):
    """List threat intelligence feeds"""
    client = _get_client(ctx)
    result = client.ti_feeds()
    data = result if isinstance(result, _list_type) else result.get("feeds", result)
    print_output(data, ctx.obj.get("output", "table"))


@threatintel_app.command()
def iocs(
    ctx: typer.Context,
    feed_id: str = typer.Option(None, "--feed-id", "-f", help="Filter by feed ID"),
):
    """List IoCs"""
    client = _get_client(ctx)
    result = client.ti_iocs(feed_id)
    data = result if isinstance(result, _list_type) else result.get("iocs", result)
    print_output(data, ctx.obj.get("output", "table"))


@threatintel_app.command()
def blocklist(ctx: typer.Context):
    """Show blocklist"""
    client = _get_client(ctx)
    result = client.ti_blocklist()
    data = result if isinstance(result, _list_type) else result.get("blocklist", result)
    print_output(data, ctx.obj.get("output", "table"))


@threatintel_app.command(name="add-ioc")
def add_ioc(
    ctx: typer.Context,
    ioc: str = typer.Argument(..., help="IOC value (IP, domain, hash)"),
    ioc_type: str = typer.Option(..., "--type", "-t", help="IOC type (ip, domain, hash, url)"),
    confidence: str = typer.Option("medium", "--confidence", "-c", help="Confidence (low/medium/high)"),
):
    """Add an IoC"""
    client = _get_client(ctx)
    result = client.ti_add_ioc(ioc, ioc_type, confidence)
    print_output(result, ctx.obj.get("output", "table"))


@threatintel_app.command()
def analyze(
    ctx: typer.Context,
    ioc: str = typer.Argument(..., help="IOC to analyze"),
):
    """Analyze an IoC"""
    client = _get_client(ctx)
    result = client.ti_analyze(ioc)
    print_output(result, ctx.obj.get("output", "table"))


# --- Decoy ---

@decoy_app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List decoys"""
    client = _get_client(ctx)
    result = client.decoy_list()
    data = result if isinstance(result, _list_type) else result.get("decoys", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@decoy_app.command()
def tokens(ctx: typer.Context):
    """List decoy tokens"""
    client = _get_client(ctx)
    result = client.decoy_tokens()
    data = result if isinstance(result, _list_type) else result.get("tokens", result)
    print_output(data, ctx.obj.get("output", "table"))


@decoy_app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Decoy name"),
    decoy_type: str = typer.Option(..., "--type", "-t", help="Decoy type"),
    target: str = typer.Option(..., "--target", help="Decoy target"),
):
    """Create a decoy"""
    client = _get_client(ctx)
    result = client.decoy_create(name, decoy_type, target)
    print_output(result, ctx.obj.get("output", "table"))


@decoy_app.command()
def deploy(
    ctx: typer.Context,
    decoy_id: str = typer.Argument(..., help="Decoy ID"),
):
    """Deploy a decoy"""
    client = _get_client(ctx)
    result = client.decoy_deploy(decoy_id)
    print_output(result, ctx.obj.get("output", "table"))


# --- Vulnerability ---

@vuln_app.command()
def cves(
    ctx: typer.Context,
    severity: str = typer.Option(None, "--severity", "-s", help="Filter by severity (low/medium/high/critical)"),
):
    """List CVEs"""
    client = _get_client(ctx)
    result = client.vuln_cves(severity)
    data = result if isinstance(result, _list_type) else result.get("cves", result)
    print_output(data, ctx.obj.get("output", "table"))


@vuln_app.command()
def scan(
    ctx: typer.Context,
    target: str = typer.Argument(..., help="Target to scan"),
):
    """Run a vulnerability scan"""
    client = _get_client(ctx)
    result = client.vuln_scan(target)
    print_output(result, ctx.obj.get("output", "table"))


@vuln_app.command()
def patch(
    ctx: typer.Context,
    cve_id: str = typer.Argument(..., help="CVE ID to patch"),
):
    """Patch a CVE"""
    client = _get_client(ctx)
    result = client.vuln_patch(cve_id)
    print_output(result, ctx.obj.get("output", "table"))


@vuln_app.command()
def summary(ctx: typer.Context):
    """Vulnerability summary"""
    client = _get_client(ctx)
    result = client.vuln_summary()
    print_output(result, ctx.obj.get("output", "table"))


# --- Incident Response ---

@incident_app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List incidents"""
    client = _get_client(ctx)
    result = client.ir_list()
    data = result if isinstance(result, _list_type) else result.get("incidents", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@incident_app.command()
def get(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
):
    """Get incident details"""
    client = _get_client(ctx)
    result = client.ir_get(incident_id)
    print_output(result, ctx.obj.get("output", "table"))


@incident_app.command()
def create(
    ctx: typer.Context,
    title: str = typer.Argument(..., help="Incident title"),
    severity: str = typer.Option(..., "--severity", "-s", help="Severity (critical/high/medium/low)"),
    description: str = typer.Option(..., "--description", "-d", help="Incident description"),
):
    """Create an incident"""
    client = _get_client(ctx)
    result = client.ir_create(title, severity, description)
    print_output(result, ctx.obj.get("output", "table"))


@incident_app.command()
def status(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
    status_value: str = typer.Argument(..., help="New status"),
):
    """Update incident status"""
    client = _get_client(ctx)
    result = client.ir_status(incident_id, status_value)
    print_output(result, ctx.obj.get("output", "table"))


@incident_app.command()
def evidence(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
    file: str = typer.Argument(..., help="Evidence file path"),
):
    """Add evidence to an incident"""
    client = _get_client(ctx)
    result = client.ir_evidence(incident_id, file)
    print_output(result, ctx.obj.get("output", "table"))


@incident_app.command()
def timeline(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
):
    """Get incident timeline"""
    client = _get_client(ctx)
    result = client.ir_timeline(incident_id)
    data = result if isinstance(result, _list_type) else result.get("timeline", result)
    print_output(data, ctx.obj.get("output", "table"))


@incident_app.command()
def report(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
):
    """Generate incident report"""
    client = _get_client(ctx)
    result = client.ir_report(incident_id)
    print_output(result, ctx.obj.get("output", "table"))


# --- UEBA ---

@ueba_app.command()
def entities(ctx: typer.Context):
    """List UEBA entities"""
    client = _get_client(ctx)
    result = client.ueba_entities()
    data = result if isinstance(result, _list_type) else result.get("entities", result)
    print_output(data, ctx.obj.get("output", "table"))


@ueba_app.command()
def alerts(ctx: typer.Context):
    """List UEBA alerts"""
    client = _get_client(ctx)
    result = client.ueba_alerts()
    data = result if isinstance(result, _list_type) else result.get("alerts", result)
    print_output(data, ctx.obj.get("output", "table"))


# --- CSPM ---

@cspm_app.command()
def accounts(ctx: typer.Context):
    """List CSPM accounts"""
    client = _get_client(ctx)
    result = client.cspm_accounts()
    data = result if isinstance(result, _list_type) else result.get("accounts", result)
    print_output(data, ctx.obj.get("output", "table"))


@cspm_app.command()
def results(
    ctx: typer.Context,
    account_id: str = typer.Argument(..., help="CSPM account ID"),
):
    """Get CSPM scan results for an account"""
    client = _get_client(ctx)
    result = client.cspm_results(account_id)
    data = result if isinstance(result, _list_type) else result.get("results", result)
    print_output(data, ctx.obj.get("output", "table"))


@cspm_app.command()
def scan(
    ctx: typer.Context,
    account_id: str = typer.Argument(..., help="CSPM account ID"),
):
    """Run a CSPM scan on an account"""
    client = _get_client(ctx)
    result = client.cspm_scan(account_id)
    print_output(result, ctx.obj.get("output", "table"))


# --- NDR ---

@ndr_app.command()
def flows(ctx: typer.Context):
    """List NDR flows"""
    client = _get_client(ctx)
    result = client.ndr_flows()
    data = result if isinstance(result, _list_type) else result.get("flows", result)
    print_output(data, ctx.obj.get("output", "table"))


@ndr_app.command()
def alerts(ctx: typer.Context):
    """List NDR alerts"""
    client = _get_client(ctx)
    result = client.ndr_alerts()
    data = result if isinstance(result, _list_type) else result.get("alerts", result)
    print_output(data, ctx.obj.get("output", "table"))


# --- Secrets ---

@secrets_app.command()
def findings(ctx: typer.Context):
    """List secrets findings"""
    client = _get_client(ctx)
    result = client.secrets_findings()
    data = result if isinstance(result, _list_type) else result.get("findings", result)
    print_output(data, ctx.obj.get("output", "table"))


@secrets_app.command()
def targets(ctx: typer.Context):
    """List secrets scan targets"""
    client = _get_client(ctx)
    result = client.secrets_targets()
    data = result if isinstance(result, _list_type) else result.get("targets", result)
    print_output(data, ctx.obj.get("output", "table"))


@secrets_app.command()
def rotate(
    ctx: typer.Context,
    finding_id: str = typer.Argument(..., help="Finding ID"),
):
    """Rotate a leaked secret"""
    client = _get_client(ctx)
    result = client.secrets_rotate(finding_id)
    print_output(result, ctx.obj.get("output", "table"))


# --- Training ---

@training_app.command()
def modules(ctx: typer.Context):
    """List security training modules"""
    client = _get_client(ctx)
    result = client.training_modules()
    data = result if isinstance(result, _list_type) else result.get("modules", result)
    print_output(data, ctx.obj.get("output", "table"))


@training_app.command()
def campaigns(ctx: typer.Context):
    """List training campaigns"""
    client = _get_client(ctx)
    result = client.training_campaigns()
    data = result if isinstance(result, _list_type) else result.get("campaigns", result)
    print_output(data, ctx.obj.get("output", "table"))


@training_app.command()
def assignments(ctx: typer.Context):
    """List training assignments"""
    client = _get_client(ctx)
    result = client.training_assignments()
    data = result if isinstance(result, _list_type) else result.get("assignments", result)
    print_output(data, ctx.obj.get("output", "table"))
