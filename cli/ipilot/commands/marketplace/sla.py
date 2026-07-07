import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Marketplace SLA")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List SLAs"""
    client = _get_client(ctx)
    result = client.sla_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="SLA name"),
    terms: str = typer.Argument(help="SLA terms"),
):
    """Create an SLA"""
    client = _get_client(ctx)
    result = client.sla_create(name, terms)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete(
    ctx: typer.Context,
    sla_id: str = typer.Argument(help="SLA ID"),
):
    """Delete an SLA"""
    client = _get_client(ctx)
    result = client.sla_delete(sla_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    sla_id: str = typer.Argument(help="SLA ID"),
):
    """Get SLA status"""
    client = _get_client(ctx)
    result = client.sla_status(sla_id)
    print_output(result, ctx.obj.get("output", "table"))
