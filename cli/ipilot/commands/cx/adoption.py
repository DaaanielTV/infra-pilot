import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Feature adoption")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def summary(ctx: typer.Context):
    """Adoption summary"""
    client = _get_client(ctx)
    result = client.cx_adoption_summary()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def features(ctx: typer.Context):
    """Feature adoption metrics"""
    client = _get_client(ctx)
    result = client.cx_adoption_features()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def track(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
    feature: str = typer.Argument(help="Feature name"),
):
    """Track adoption"""
    client = _get_client(ctx)
    result = client.cx_adoption_track(customer_id, feature)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def recommendations(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
):
    """Adoption recommendations"""
    client = _get_client(ctx)
    result = client.cx_adoption_recommendations(customer_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def stats(ctx: typer.Context):
    """Adoption statistics"""
    client = _get_client(ctx)
    result = client.cx_adoption_stats()
    print_output(result, ctx.obj.get("output", "table"))
