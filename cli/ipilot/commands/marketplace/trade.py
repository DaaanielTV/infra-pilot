import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Marketplace trades")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List trades"""
    client = _get_client(ctx)
    result = client.trade_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    resource: str = typer.Argument(help="Resource type"),
    quantity: int = typer.Argument(help="Quantity"),
):
    """Create a trade"""
    client = _get_client(ctx)
    result = client.trade_create(resource, quantity)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def accept(
    ctx: typer.Context,
    trade_id: str = typer.Argument(help="Trade ID"),
):
    """Accept a trade"""
    client = _get_client(ctx)
    result = client.trade_accept(trade_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def cancel(
    ctx: typer.Context,
    trade_id: str = typer.Argument(help="Trade ID"),
):
    """Cancel a trade"""
    client = _get_client(ctx)
    result = client.trade_cancel(trade_id)
    print_output(result, ctx.obj.get("output", "table"))
