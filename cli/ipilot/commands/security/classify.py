import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Data classification")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def scan(ctx: typer.Context):
    """Scan for unclassified data"""
    client = _get_client(ctx)
    result = client.classify_scan()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def inventory(ctx: typer.Context):
    """Show data classification inventory"""
    client = _get_client(ctx)
    result = client.classify_inventory()
    data = result if isinstance(result, _list_type) else result.get("inventory", result)
    print_output(data, ctx.obj.get("output", "table"))
