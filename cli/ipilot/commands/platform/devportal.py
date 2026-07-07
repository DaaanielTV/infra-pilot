import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Developer portal")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List developer portal items"""
    client = _get_client(ctx)
    result = client.devportal_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(help="Item name"),
    spec: str = typer.Argument(help="Item spec"),
):
    """Register a developer portal item"""
    client = _get_client(ctx)
    result = client.devportal_register(name, spec)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    item_id: str = typer.Argument(help="Item ID"),
):
    """Get a developer portal item"""
    client = _get_client(ctx)
    result = client.devportal_get(item_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Get developer portal summary"""
    client = _get_client(ctx)
    result = client.devportal_summary()
    print_output(result, ctx.obj.get("output", "table"))
