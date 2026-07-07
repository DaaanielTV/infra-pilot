import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="SD-WAN management commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def status(ctx: typer.Context):
    """Show SD-WAN status"""
    client = _get_client(ctx)
    result = client.sdwan_status()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def apps(ctx: typer.Context):
    """List SD-WAN applications"""
    client = _get_client(ctx)
    result = client.sdwan_apps()
    data = result if isinstance(result, _list_type) else result.get("apps", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Link name"),
    provider: str = typer.Argument(..., help="Provider name"),
    bandwidth: int = typer.Argument(..., help="Bandwidth in Mbps"),
):
    """Create a new SD-WAN link"""
    client = _get_client(ctx)
    result = client.sdwan_create(name, provider, bandwidth)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete(
    ctx: typer.Context,
    link_id: str = typer.Argument(..., help="Link ID"),
):
    """Delete an SD-WAN link"""
    client = _get_client(ctx)
    result = client.sdwan_delete(link_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def toggle(
    ctx: typer.Context,
    link_id: str = typer.Argument(..., help="Link ID"),
):
    """Toggle an SD-WAN link on/off"""
    client = _get_client(ctx)
    result = client.sdwan_toggle(link_id)
    print_output(result, ctx.obj.get("output", "table"))
