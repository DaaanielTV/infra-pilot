import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="SLA management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List SLAs"""
    client = _get_client(ctx)
    result = client.cx_sla_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="SLA name"),
    response_time: int = typer.Argument(help="Response time (minutes)"),
    resolution_time: int = typer.Argument(help="Resolution time (minutes)"),
):
    """Create an SLA"""
    client = _get_client(ctx)
    result = client.cx_sla_create(name, response_time, resolution_time)
    print_output(result, ctx.obj.get("output", "table"))
