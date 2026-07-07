import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Root cause analysis")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def analyze(ctx: typer.Context, incident_id: str = typer.Argument(..., help="Incident ID")):
    """Analyze root cause for an incident"""
    client = _get_client(ctx)
    result = client.aiops_rca_analyze(incident_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def incidents(ctx: typer.Context):
    """List all incidents"""
    client = _get_client(ctx)
    result = client.aiops_rca_incidents()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def events(ctx: typer.Context, incident_id: str = typer.Argument(..., help="Incident ID")):
    """List events for an incident"""
    client = _get_client(ctx)
    result = client.aiops_rca_events(incident_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def deps(ctx: typer.Context, incident_id: str = typer.Argument(..., help="Incident ID")):
    """List dependencies for an incident"""
    client = _get_client(ctx)
    result = client.aiops_rca_deps(incident_id)
    print_output(result, ctx.obj.get("output", "table"))
