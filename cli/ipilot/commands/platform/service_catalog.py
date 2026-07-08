import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Service catalog")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List items"""
    client = _get_client(ctx)
    result = client.catalog_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(help="Service name"),
    version: str = typer.Argument(help="Service version"),
):
    """Register"""
    client = _get_client(ctx)
    result = client.catalog_register(name, version)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    item_id: str = typer.Argument(help="Item ID"),
):
    """Get item"""
    client = _get_client(ctx)
    result = client.catalog_get(item_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def score(
    ctx: typer.Context,
    item_id: str = typer.Argument(help="Item ID"),
):
    """Score"""
    client = _get_client(ctx)
    result = client.catalog_score(item_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Summary"""
    client = _get_client(ctx)
    result = client.catalog_summary()
    print_output(result, ctx.obj.get("output", "table"))
