import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Pay-per-use")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def metrics(ctx: typer.Context):
    """Get PPU metrics"""
    client = _get_client(ctx)
    result = client.ppu_metrics()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def usage(ctx: typer.Context):
    """Get PPU usage"""
    client = _get_client(ctx)
    result = client.ppu_usage()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def budget(ctx: typer.Context):
    """Get PPU budget"""
    client = _get_client(ctx)
    result = client.ppu_budget()
    print_output(result, ctx.obj.get("output", "table"))
