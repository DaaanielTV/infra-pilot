import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Decentralized storage")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List storage providers"""
    client = _get_client(ctx)
    result = client.storage_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Storage name"),
    provider: str = typer.Argument(help="Provider type"),
):
    """Create a storage resource"""
    client = _get_client(ctx)
    result = client.storage_create(name, provider)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def pin(
    ctx: typer.Context,
    cid: str = typer.Argument(help="Content ID"),
):
    """Pin content to storage"""
    client = _get_client(ctx)
    result = client.storage_pin(cid)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    storage_id: str = typer.Argument(help="Storage ID"),
):
    """Get storage status"""
    client = _get_client(ctx)
    result = client.storage_status(storage_id)
    print_output(result, ctx.obj.get("output", "table"))
