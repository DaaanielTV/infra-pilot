import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Edge device management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    device_type: str = typer.Option(None, "--device-type", "-t", help="Filter by device type"),
    status: str = typer.Option(None, "--status", "-s", help="Filter by status"),
):
    """List edge devices"""
    client = _get_client(ctx)
    result = client.list_edge_devices(device_type, status)
    data = result if isinstance(result, _list_type) else result.get("devices", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Device name"),
    device_type: str = typer.Argument(..., help="Device type (raspberry_pi, jetson_nano, etc)"),
    hardware_id: str = typer.Argument(..., help="Hardware MAC/serial"),
):
    """Register edge device"""
    client = _get_client(ctx)
    result = client.register_edge_device(name, device_type, hardware_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    device_id: str = typer.Argument(..., help="Device ID"),
):
    """Get device status"""
    client = _get_client(ctx)
    result = client.edge_device_status(device_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def command(
    ctx: typer.Context,
    device_id: str = typer.Argument(..., help="Device ID"),
    command_text: str = typer.Argument(..., help="Command to execute"),
):
    """Send command to device"""
    client = _get_client(ctx)
    result = client.edge_device_command(device_id, command_text)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def backup(
    ctx: typer.Context,
    device_id: str = typer.Argument(..., help="Device ID"),
):
    """Backup edge device"""
    client = _get_client(ctx)
    result = client.backup_edge_device(device_id)
    print_output(result, ctx.obj.get("output", "table"))
