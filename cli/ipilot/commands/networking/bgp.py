import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="BGP management commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def sessions(ctx: typer.Context):
    """List BGP sessions"""
    client = _get_client(ctx)
    result = client.bgp_sessions()
    data = result if isinstance(result, _list_type) else result.get("sessions", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Session name"),
    asn: int = typer.Argument(..., help="ASN number"),
    neighbor: str = typer.Argument(..., help="Neighbor IP"),
):
    """Create a new BGP session"""
    client = _get_client(ctx)
    result = client.bgp_create(name, asn, neighbor)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete(
    ctx: typer.Context,
    session_id: str = typer.Argument(..., help="Session ID"),
):
    """Delete a BGP session"""
    client = _get_client(ctx)
    result = client.bgp_delete(session_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def routes(
    ctx: typer.Context,
    session_id: str = typer.Option(None, "--session-id", "-s", help="Session ID (optional)"),
):
    """Show BGP routes"""
    client = _get_client(ctx)
    result = client.bgp_routes(session_id)
    data = result if isinstance(result, _list_type) else result.get("routes", result)
    print_output(data, ctx.obj.get("output", "table"))
