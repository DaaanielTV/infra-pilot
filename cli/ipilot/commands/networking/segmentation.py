import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="Network segmentation (VLAN) management commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List network segments"""
    client = _get_client(ctx)
    result = client.segment_list()
    data = result if isinstance(result, _list_type) else result.get("segments", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Segment name"),
    cidr: str = typer.Argument(..., help="CIDR notation"),
    vlan: int = typer.Option(None, "--vlan", help="VLAN ID"),
):
    """Create a new network segment"""
    client = _get_client(ctx)
    result = client.segment_create(name, cidr, vlan)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete(
    ctx: typer.Context,
    segment_id: str = typer.Argument(..., help="Segment ID"),
):
    """Delete a network segment"""
    client = _get_client(ctx)
    result = client.segment_delete(segment_id)
    print_output(result, ctx.obj.get("output", "table"))
