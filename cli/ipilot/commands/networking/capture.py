import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Packet capture")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List active captures"""
    client = _get_client(ctx)
    result = client.capture_list()
    data = result if isinstance(result, list) else result.get("captures", result)
    print_output(data, output or ctx.obj.get("output", "table"))

@app.command()
def start(
    ctx: typer.Context,
    interface: str = typer.Argument(..., help="Network interface"),
    filter_expr: str = typer.Option(None, "--filter", "-f", help="BPF filter"),
):
    """Start packet capture"""
    client = _get_client(ctx)
    result = client.capture_start(interface, filter_expr)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def stop(
    ctx: typer.Context,
    capture_id: str = typer.Argument(..., help="Capture ID"),
):
    """Stop packet capture"""
    client = _get_client(ctx)
    result = client.capture_stop(capture_id)
    print_output(result, ctx.obj.get("output", "table"))
