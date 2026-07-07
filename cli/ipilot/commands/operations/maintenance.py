import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="Maintenance scheduling commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List scheduled maintenance windows"""
    client = _get_client(ctx)
    result = client.maintenance_list()
    data = result if isinstance(result, _list_type) else result.get("maintenance", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def schedule(
    ctx: typer.Context,
    resource_id: str = typer.Argument(..., help="Resource ID"),
    start_time: str = typer.Argument(..., help="Start time (ISO 8601)"),
    end_time: str = typer.Argument(..., help="End time (ISO 8601)"),
    description: str = typer.Option(None, "--description", help="Maintenance description"),
):
    """Schedule a maintenance window"""
    client = _get_client(ctx)
    result = client.maintenance_schedule(resource_id, start_time, end_time, description)
    print_output(result, ctx.obj.get("output", "table"))
