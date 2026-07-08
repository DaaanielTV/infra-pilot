import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="VPN commands")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def configs(ctx: typer.Context):
    """List VPN configs"""
    client = _get_client(ctx)
    result = client.vpn_configs()
    data = result if isinstance(result, list) else result.get("configs", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Config name"),
    protocol: str = typer.Argument(..., help="VPN protocol"),
    server: str = typer.Argument(..., help="Server address"),
):
    """Create VPN config"""
    client = _get_client(ctx)
    result = client.vpn_create(name, protocol, server)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def delete(
    ctx: typer.Context,
    config_id: str = typer.Argument(..., help="Config ID"),
):
    """Delete VPN config"""
    client = _get_client(ctx)
    result = client.vpn_delete(config_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def status(
    ctx: typer.Context,
    config_id: str = typer.Argument(..., help="Config ID"),
):
    """Get VPN status"""
    client = _get_client(ctx)
    result = client.vpn_status(config_id)
    print_output(result, ctx.obj.get("output", "table"))
