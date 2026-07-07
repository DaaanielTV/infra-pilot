import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Digital experience monitoring")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(ctx: typer.Context):
    """List all DEM monitors"""
    client = _get_client(ctx)
    result = client.aiops_dem_list()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def create(ctx: typer.Context, name: str = typer.Argument(..., help="Monitor name"), url: str = typer.Argument(..., help="Target URL"), interval: int = typer.Option(60, help="Check interval in seconds")):
    """Create a new DEM monitor"""
    client = _get_client(ctx)
    result = client.aiops_dem_create(name, url, interval)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def check(ctx: typer.Context, monitor_id: str = typer.Argument(..., help="Monitor ID")):
    """Run a check on a DEM monitor"""
    client = _get_client(ctx)
    result = client.aiops_dem_check(monitor_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def stats(ctx: typer.Context, monitor_id: str = typer.Argument(..., help="Monitor ID")):
    """Get stats for a DEM monitor"""
    client = _get_client(ctx)
    result = client.aiops_dem_stats(monitor_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def summary(ctx: typer.Context):
    """Get DEM summary"""
    client = _get_client(ctx)
    result = client.aiops_dem_summary()
    print_output(result, ctx.obj.get("output", "table"))
