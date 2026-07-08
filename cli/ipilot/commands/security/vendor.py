import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Vendor risk")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List vendors"""
    client = _get_client(ctx)
    result = client.vendor_list()
    data = result if isinstance(result, list) else result.get("vendors", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Vendor name"),
    risk_level: str = typer.Option(..., "--risk-level", "-r", help="Risk level (low/medium/high/critical)"),
):
    """Create vendor"""
    client = _get_client(ctx)
    result = client.vendor_create(name, risk_level)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def assess(
    ctx: typer.Context,
    vendor_id: str = typer.Argument(..., help="Vendor ID"),
):
    """Assess vendor"""
    client = _get_client(ctx)
    result = client.vendor_assess(vendor_id)
    print_output(result, ctx.obj.get("output", "table"))
