import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Idle resource reclamation")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List reclaimable resources"""
    client = _get_client(ctx)
    result = client.reclaim_list()
    data = result if isinstance(result, _list_type) else result.get("resources", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def scan(ctx: typer.Context):
    """Scan for idle resources"""
    client = _get_client(ctx)
    result = client.reclaim_scan()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def report(ctx: typer.Context):
    """Reclamation report"""
    client = _get_client(ctx)
    result = client.reclaim_report()
    print_output(result, ctx.obj.get("output", "table"))
