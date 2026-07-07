import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Alert management")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def ingest(ctx: typer.Context, source: str = typer.Argument(..., help="Alert source"), message: str = typer.Argument(..., help="Alert message"), severity: str = typer.Option("info", help="Severity level")):
    """Ingest an alert"""
    client = _get_client(ctx)
    result = client.aiops_alert_ingest(source, message, severity)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def incidents(ctx: typer.Context):
    """List alert incidents"""
    client = _get_client(ctx)
    result = client.aiops_alert_incidents()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def stats(ctx: typer.Context):
    """Get alert stats"""
    client = _get_client(ctx)
    result = client.aiops_alert_stats()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def suppress(ctx: typer.Context, alert_id: str = typer.Argument(..., help="Alert ID to suppress")):
    """Suppress an alert"""
    client = _get_client(ctx)
    result = client.aiops_alert_suppress(alert_id)
    print_output(result, ctx.obj.get("output", "table"))
