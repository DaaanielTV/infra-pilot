import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="Drift detection commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def scan(
    ctx: typer.Context,
    resource_id: str = typer.Option(None, "--resource-id", help="Specific resource to scan"),
):
    """Scan for configuration drift"""
    client = _get_client(ctx)
    result = client.drift_scan(resource_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def list(ctx: typer.Context):
    """List drift detection results"""
    client = _get_client(ctx)
    result = client.drift_list()
    data = result if isinstance(result, _list_type) else result.get("drifts", result)
    print_output(data, ctx.obj.get("output", "table"))
