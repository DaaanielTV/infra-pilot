import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Health monitoring")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def services(ctx: typer.Context):
    """List health services"""
    client = _get_client(ctx)
    result = client.aiops_health_services()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def register(ctx: typer.Context, name: str = typer.Argument(..., help="Service name"), endpoint: str = typer.Argument(..., help="Health endpoint"), interval: int = typer.Argument(..., help="Check interval in seconds")):
    """Register a health service"""
    client = _get_client(ctx)
    result = client.aiops_health_register(name, endpoint, interval)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def forecast(ctx: typer.Context, service_id: str = typer.Argument(..., help="Service ID")):
    """Get health forecast for a service"""
    client = _get_client(ctx)
    result = client.aiops_health_forecast(service_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def dashboard(ctx: typer.Context):
    """Get health dashboard"""
    client = _get_client(ctx)
    result = client.aiops_health_dashboard()
    print_output(result, ctx.obj.get("output", "table"))
