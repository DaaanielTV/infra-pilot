import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="API catalog")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List items"""
    client = _get_client(ctx)
    result = client.apicatalog_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(help="API name"),
    spec: str = typer.Argument(help="API spec"),
):
    """Register"""
    client = _get_client(ctx)
    result = client.apicatalog_register(name, spec)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    api_id: str = typer.Argument(help="API ID"),
):
    """Get item"""
    client = _get_client(ctx)
    result = client.apicatalog_get(api_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Summary"""
    client = _get_client(ctx)
    result = client.apicatalog_summary()
    print_output(result, ctx.obj.get("output", "table"))
