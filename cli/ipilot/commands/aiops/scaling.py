import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Auto-scaling management")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def predict(ctx: typer.Context, resource: str = typer.Argument(..., help="Resource name")):
    """Predict scaling needs for a resource"""
    client = _get_client(ctx)
    result = client.aiops_scaling_predict(resource)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def metrics(ctx: typer.Context, resource: str = typer.Argument(..., help="Resource name")):
    """Get scaling metrics for a resource"""
    client = _get_client(ctx)
    result = client.aiops_scaling_metrics(resource)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def policy(ctx: typer.Context, resource: str = typer.Argument(..., help="Resource name"), min_instances: int = typer.Argument(..., help="Minimum instances"), max_instances: int = typer.Argument(..., help="Maximum instances")):
    """Set scaling policy for a resource"""
    client = _get_client(ctx)
    result = client.aiops_scaling_policy(resource, min_instances, max_instances)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def summary(ctx: typer.Context):
    """Get scaling summary"""
    client = _get_client(ctx)
    result = client.aiops_scaling_summary()
    print_output(result, ctx.obj.get("output", "table"))
