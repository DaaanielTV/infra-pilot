import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Marketplace plans")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List plans"""
    client = _get_client(ctx)
    result = client.plans_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Plan name"),
    price: float = typer.Argument(help="Plan price"),
):
    """Create a plan"""
    client = _get_client(ctx)
    result = client.plans_create(name, price)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete(
    ctx: typer.Context,
    plan_id: str = typer.Argument(help="Plan ID"),
):
    """Delete a plan"""
    client = _get_client(ctx)
    result = client.plans_delete(plan_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def subscriptions(ctx: typer.Context):
    """List subscriptions"""
    client = _get_client(ctx)
    result = client.plans_subscriptions()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
