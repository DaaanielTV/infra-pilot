import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Compliance")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def scan(
    ctx: typer.Context,
    framework: str = typer.Argument(..., help="Compliance framework (e.g. SOC2, ISO27001)"),
):
    """Scan framework"""
    client = _get_client(ctx)
    result = client.compliance_scan(framework)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    scan_id: str = typer.Argument(..., help="Scan ID"),
):
    """Compliance report"""
    client = _get_client(ctx)
    result = client.compliance_report(scan_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def checks(ctx: typer.Context):
    """List checks"""
    client = _get_client(ctx)
    result = client.compliance_checks()
    data = result if isinstance(result, list) else result.get("checks", result)
    print_output(data, ctx.obj.get("output", "table"))
