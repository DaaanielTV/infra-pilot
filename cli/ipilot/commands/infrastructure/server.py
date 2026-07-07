import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="Server management commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List all servers"""
    client = _get_client(ctx)
    result = client.list_servers()
    data = result if isinstance(result, _list_type) else result.get("servers", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Server name"),
    server_type: str = typer.Option(..., "--type", "-t", help="Server type"),
    memory: int = typer.Option(None, "--memory", "-m", help="Memory in MB"),
):
    """Create a new server"""
    client = _get_client(ctx)
    result = client.create_server(name, server_type, memory)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete(
    ctx: typer.Context,
    server: str = typer.Argument(..., help="Server ID or name"),
):
    """Delete a server"""
    client = _get_client(ctx)
    result = client.delete_server(server)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    server: str = typer.Argument(..., help="Server ID or name"),
):
    """Get server status"""
    client = _get_client(ctx)
    result = client.server_status(server)
    print_output(result, ctx.obj.get("output", "table"))
