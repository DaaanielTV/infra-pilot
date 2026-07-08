import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Capacity management")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def recommend(ctx: typer.Context):
    """Capacity recommendations"""
    client = _get_client(ctx)
    result = client.aiops_capacity_recommend()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def usage(ctx: typer.Context, resource: str = typer.Argument(..., help="Resource name")):
    """Capacity usage"""
    client = _get_client(ctx)
    result = client.aiops_capacity_usage(resource)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def simulate(ctx: typer.Context, resource: str = typer.Argument(..., help="Resource name"), load: float = typer.Argument(..., help="Load factor")):
    """Simulate load"""
    client = _get_client(ctx)
    result = client.aiops_capacity_simulate(resource, load)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def summary(ctx: typer.Context):
    """Capacity summary"""
    client = _get_client(ctx)
    result = client.aiops_capacity_summary()
    print_output(result, ctx.obj.get("output", "table"))
