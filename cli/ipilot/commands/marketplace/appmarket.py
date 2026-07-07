import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="App marketplace")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List available apps"""
    client = _get_client(ctx)
    result = client.appmarket_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def install(
    ctx: typer.Context,
    app_id: str = typer.Argument(help="App ID"),
):
    """Install an app"""
    client = _get_client(ctx)
    result = client.appmarket_install(app_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def installations(ctx: typer.Context):
    """List installations"""
    client = _get_client(ctx)
    result = client.appmarket_installations()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
