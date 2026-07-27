import json

import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="SOC")

soar_app = typer.Typer(help="SOAR")
threatintel_app = typer.Typer(help="Threat intel")
decoy_app = typer.Typer(help="Decoy")
vuln_app = typer.Typer(help="Vulnerability")
incident_app = typer.Typer(help="Incidents")
ueba_app = typer.Typer(help="UEBA")
cspm_app = typer.Typer(help="CSPM")
ndr_app = typer.Typer(help="NDR")
secrets_app = typer.Typer(help="Secrets")
training_app = typer.Typer(help="Training")

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


@soar_app.command()
def playbooks(ctx: typer.Context) -> None:
    """List playbooks
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.soar_playbooks()
    data = result if isinstance(result, list) else result.get("playbooks", result)
    print_output(data, ctx.obj.get("output", "table"))


@soar_app.command()
def playbook(
    ctx: typer.Context,
    playbook_id: str = typer.Argument(..., help="Playbook ID"),
):
    """Get playbook
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.soar_playbook(playbook_id)
    print_output(result, ctx.obj.get("output", "table"))


@soar_app.command()
def run(
    ctx: typer.Context,
    playbook_id: str = typer.Argument(..., help="Playbook ID"),
    params: str = typer.Option("{}", "--params", "-p", help="JSON parameters"),
):
    """Run playbook
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
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
    """Create playbook
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    parsed_steps = json.loads(steps)
    result = client.soar_create(name, parsed_steps, trigger)
    print_output(result, ctx.obj.get("output", "table"))


@soar_app.command()
def cases(ctx: typer.Context):
    """List cases
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.soar_cases()
    data = result if isinstance(result, list) else result.get("cases", result)
    print_output(data, ctx.obj.get("output", "table"))


@soar_app.command()
def connectors(ctx: typer.Context):
    """List connectors
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.soar_connectors()
    data = result if isinstance(result, list) else result.get("connectors", result)
    print_output(data, ctx.obj.get("output", "table"))


@threatintel_app.command()
def feeds(ctx: typer.Context):
    """List feeds
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ti_feeds()
    data = result if isinstance(result, list) else result.get("feeds", result)
    print_output(data, ctx.obj.get("output", "table"))


@threatintel_app.command()
def iocs(
    ctx: typer.Context,
    feed_id: str = typer.Option(None, "--feed-id", "-f", help="Filter by feed ID"),
):
    """List IoCs
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ti_iocs(feed_id)
    data = result if isinstance(result, list) else result.get("iocs", result)
    print_output(data, ctx.obj.get("output", "table"))


@threatintel_app.command()
def blocklist(ctx: typer.Context):
    """Blocklist
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ti_blocklist()
    data = result if isinstance(result, list) else result.get("blocklist", result)
    print_output(data, ctx.obj.get("output", "table"))


@threatintel_app.command(name="add-ioc")
def add_ioc(
    ctx: typer.Context,
    ioc: str = typer.Argument(..., help="IOC value (IP, domain, hash)"),
    ioc_type: str = typer.Option(..., "--type", "-t", help="IOC type (ip, domain, hash, url)"),
    confidence: str = typer.Option("medium", "--confidence", "-c", help="Confidence (low/medium/high)"),
):
    """Add IoC
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ti_add_ioc(ioc, ioc_type, confidence)
    print_output(result, ctx.obj.get("output", "table"))


@threatintel_app.command()
def analyze(
    ctx: typer.Context,
    ioc: str = typer.Argument(..., help="IOC to analyze"),
):
    """Analyze IoC
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ti_analyze(ioc)
    print_output(result, ctx.obj.get("output", "table"))


@decoy_app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List decoys
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.decoy_list()
    data = result if isinstance(result, list) else result.get("decoys", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@decoy_app.command()
def tokens(ctx: typer.Context):
    """List tokens
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.decoy_tokens()
    data = result if isinstance(result, list) else result.get("tokens", result)
    print_output(data, ctx.obj.get("output", "table"))


@decoy_app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Decoy name"),
    decoy_type: str = typer.Option(..., "--type", "-t", help="Decoy type"),
    target: str = typer.Option(..., "--target", help="Decoy target"),
):
    """Create decoy
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.decoy_create(name, decoy_type, target)
    print_output(result, ctx.obj.get("output", "table"))


@decoy_app.command()
def deploy(
    ctx: typer.Context,
    decoy_id: str = typer.Argument(..., help="Decoy ID"),
):
    """Deploy decoy
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.decoy_deploy(decoy_id)
    print_output(result, ctx.obj.get("output", "table"))


@vuln_app.command()
def cves(
    ctx: typer.Context,
    severity: str = typer.Option(None, "--severity", "-s", help="Filter by severity (low/medium/high/critical)"),
):
    """List CVEs
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.vuln_cves(severity)
    data = result if isinstance(result, list) else result.get("cves", result)
    print_output(data, ctx.obj.get("output", "table"))


@vuln_app.command()
def scan(
    ctx: typer.Context,
    target: str = typer.Argument(..., help="Target to scan"),
):
    """Vuln scan
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.vuln_scan(target)
    print_output(result, ctx.obj.get("output", "table"))


@vuln_app.command()
def patch(
    ctx: typer.Context,
    cve_id: str = typer.Argument(..., help="CVE ID to patch"),
):
    """Patch CVE
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.vuln_patch(cve_id)
    print_output(result, ctx.obj.get("output", "table"))


@vuln_app.command()
def summary(ctx: typer.Context):
    """Vuln summary
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.vuln_summary()
    print_output(result, ctx.obj.get("output", "table"))


@incident_app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List incidents
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ir_list()
    data = result if isinstance(result, list) else result.get("incidents", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@incident_app.command()
def get(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
):
    """Get incident
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
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
    """Create incident
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ir_create(title, severity, description)
    print_output(result, ctx.obj.get("output", "table"))


@incident_app.command()
def status(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
    status_value: str = typer.Argument(..., help="New status"),
):
    """Update status
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ir_status(incident_id, status_value)
    print_output(result, ctx.obj.get("output", "table"))


@incident_app.command()
def evidence(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
    file: str = typer.Argument(..., help="Evidence file path"),
):
    """Add evidence
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ir_evidence(incident_id, file)
    print_output(result, ctx.obj.get("output", "table"))


@incident_app.command()
def timeline(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
):
    """Timeline
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ir_timeline(incident_id)
    data = result if isinstance(result, list) else result.get("timeline", result)
    print_output(data, ctx.obj.get("output", "table"))


@incident_app.command()
def report(
    ctx: typer.Context,
    incident_id: str = typer.Argument(..., help="Incident ID"),
):
    """Generate report
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ir_report(incident_id)
    print_output(result, ctx.obj.get("output", "table"))


@ueba_app.command()
def entities(ctx: typer.Context):
    """List entities
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ueba_entities()
    data = result if isinstance(result, list) else result.get("entities", result)
    print_output(data, ctx.obj.get("output", "table"))


@ueba_app.command()
def alerts(ctx: typer.Context):
    """Alerts
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ueba_alerts()
    data = result if isinstance(result, list) else result.get("alerts", result)
    print_output(data, ctx.obj.get("output", "table"))


@cspm_app.command()
def accounts(ctx: typer.Context):
    """Accounts
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cspm_accounts()
    data = result if isinstance(result, list) else result.get("accounts", result)
    print_output(data, ctx.obj.get("output", "table"))


@cspm_app.command()
def results(
    ctx: typer.Context,
    account_id: str = typer.Argument(..., help="CSPM account ID"),
):
    """Scan results
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cspm_results(account_id)
    data = result if isinstance(result, list) else result.get("results", result)
    print_output(data, ctx.obj.get("output", "table"))


@cspm_app.command()
def scan(
    ctx: typer.Context,
    account_id: str = typer.Argument(..., help="CSPM account ID"),
):
    """Run scan
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cspm_scan(account_id)
    print_output(result, ctx.obj.get("output", "table"))


@ndr_app.command()
def flows(ctx: typer.Context):
    """Flows
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ndr_flows()
    data = result if isinstance(result, list) else result.get("flows", result)
    print_output(data, ctx.obj.get("output", "table"))


@ndr_app.command()
def alerts(ctx: typer.Context):
    """Alerts
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ndr_alerts()
    data = result if isinstance(result, list) else result.get("alerts", result)
    print_output(data, ctx.obj.get("output", "table"))


@secrets_app.command()
def findings(ctx: typer.Context):
    """Findings
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.secrets_findings()
    data = result if isinstance(result, list) else result.get("findings", result)
    print_output(data, ctx.obj.get("output", "table"))


@secrets_app.command()
def targets(ctx: typer.Context):
    """Targets
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.secrets_targets()
    data = result if isinstance(result, list) else result.get("targets", result)
    print_output(data, ctx.obj.get("output", "table"))


@secrets_app.command()
def rotate(
    ctx: typer.Context,
    finding_id: str = typer.Argument(..., help="Finding ID"),
):
    """Rotate secret
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.secrets_rotate(finding_id)
    print_output(result, ctx.obj.get("output", "table"))


@training_app.command()
def modules(ctx: typer.Context):
    """Modules
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.training_modules()
    data = result if isinstance(result, list) else result.get("modules", result)
    print_output(data, ctx.obj.get("output", "table"))


@training_app.command()
def campaigns(ctx: typer.Context):
    """Campaigns
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.training_campaigns()
    data = result if isinstance(result, list) else result.get("campaigns", result)
    print_output(data, ctx.obj.get("output", "table"))


@training_app.command()
def assignments(ctx: typer.Context):
    """Assignments
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.training_assignments()
    data = result if isinstance(result, list) else result.get("assignments", result)
    print_output(data, ctx.obj.get("output", "table"))