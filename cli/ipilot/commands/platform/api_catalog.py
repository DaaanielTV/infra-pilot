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
    """List API catalog items"""
    client = _get_client(ctx)
    result = client.apicatalog_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(help="API name"),
    spec: str = typer.Argument(help="API spec"),
):
    """Register an API"""
    client = _get_client(ctx)
    result = client.apicatalog_register(name, spec)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    api_id: str = typer.Argument(help="API ID"),
):
    """Get an API catalog item"""
    client = _get_client(ctx)
    result = client.apicatalog_get(api_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Get API catalog summary"""
    client = _get_client(ctx)
    result = client.apicatalog_summary()
    print_output(result, ctx.obj.get("output", "table"))
