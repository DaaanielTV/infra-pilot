import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Auditor management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def sessions(ctx: typer.Context):
    """List auditor sessions"""
    client = _get_client(ctx)
    result = client.ap_sessions()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def evidence(
    ctx: typer.Context,
    session_id: str = typer.Argument(help="Session ID"),
):
    """Get auditor evidence"""
    client = _get_client(ctx)
    result = client.ap_evidence(session_id)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def findings(
    ctx: typer.Context,
    session_id: str = typer.Argument(help="Session ID"),
):
    """List auditor findings"""
    client = _get_client(ctx)
    result = client.ap_findings(session_id)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Get auditor statistics"""
    client = _get_client(ctx)
    result = client.ap_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command("engagement-create")
def engagement_create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Engagement name"),
    auditor_id: str = typer.Argument(help="Auditor ID"),
):
    """Create an auditor engagement"""
    client = _get_client(ctx)
    result = client.ap_engagement_create(name, auditor_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("engagement-complete")
def engagement_complete(
    ctx: typer.Context,
    engagement_id: str = typer.Argument(help="Engagement ID"),
):
    """Complete an auditor engagement"""
    client = _get_client(ctx)
    result = client.ap_engagement_complete(engagement_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("finding-create")
def finding_create(
    ctx: typer.Context,
    session_id: str = typer.Argument(help="Session ID"),
    description: str = typer.Argument(help="Finding description"),
    severity: str = typer.Argument(help="Finding severity"),
):
    """Create an auditor finding"""
    client = _get_client(ctx)
    result = client.ap_finding_create(session_id, description, severity)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("session-revoke")
def session_revoke(
    ctx: typer.Context,
    session_id: str = typer.Argument(help="Session ID"),
):
    """Revoke an auditor session"""
    client = _get_client(ctx)
    result = client.ap_session_revoke(session_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("session-extend")
def session_extend(
    ctx: typer.Context,
    session_id: str = typer.Argument(help="Session ID"),
    hours: int = typer.Argument(help="Extension hours"),
):
    """Extend an auditor session"""
    client = _get_client(ctx)
    result = client.ap_session_extend(session_id, hours)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("finding-update")
def finding_update(
    ctx: typer.Context,
    finding_id: str = typer.Argument(help="Finding ID"),
    status: str = typer.Argument(help="New status"),
):
    """Update an auditor finding"""
    client = _get_client(ctx)
    result = client.ap_finding_update(finding_id, status)
    print_output(result, ctx.obj.get("output", "table"))
