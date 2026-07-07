import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="Network cost management commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def show(ctx: typer.Context):
    """Show network costs"""
    client = _get_client(ctx)
    result = client.netcost_show()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def budget(
    ctx: typer.Context,
    budget: float = typer.Argument(..., help="Budget amount"),
):
    """Set network cost budget"""
    client = _get_client(ctx)
    result = client.netcost_budget(budget)
    print_output(result, ctx.obj.get("output", "table"))
