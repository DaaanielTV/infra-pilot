import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Hardware lifecycle")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(ctx: typer.Context):
    """List hardware assets"""
    client = _get_client(ctx)
    result = client.list_hardware()
    data = result if isinstance(result, list) else result.get("hardware", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def add(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Hardware name"),
    hardware_type: str = typer.Argument(..., help="Hardware type"),
    specs: str = typer.Argument(..., help="Hardware specs (JSON)"),
):
    """Add hardware asset"""
    client = _get_client(ctx)
    result = client.add_hardware(name, hardware_type, specs)
    print_output(result, ctx.obj.get("output", "table"))
