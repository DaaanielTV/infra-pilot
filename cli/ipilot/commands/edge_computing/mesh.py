import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Mesh network management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List mesh networks"""
    client = _get_client(ctx)
    result = client.list_mesh_networks()
    data = result if isinstance(result, _list_type) else result.get("networks", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Network name"),
    mesh_type: str = typer.Argument(..., help="Mesh type (wireguard/tinc)"),
    subnet: str = typer.Argument(..., help="Subnet CIDR"),
):
    """Create mesh network"""
    client = _get_client(ctx)
    result = client.create_mesh_network(name, mesh_type, subnet)
    print_output(result, ctx.obj.get("output", "table"))
