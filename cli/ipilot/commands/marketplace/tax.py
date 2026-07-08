import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Tax management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def rates(ctx: typer.Context):
    """Get tax rates"""
    client = _get_client(ctx)
    result = client.tax_rates()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def invoices(ctx: typer.Context):
    """List tax invoices"""
    client = _get_client(ctx)
    result = client.tax_invoices()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def generate(
    ctx: typer.Context,
    period: str = typer.Argument(help="Tax period"),
):
    """Generate a tax invoice"""
    client = _get_client(ctx)
    result = client.tax_generate(period)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def pay(
    ctx: typer.Context,
    invoice_id: str = typer.Argument(help="Invoice ID"),
):
    """Pay a tax invoice"""
    client = _get_client(ctx)
    result = client.tax_pay(invoice_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Get tax summary"""
    client = _get_client(ctx)
    result = client.tax_summary()
    print_output(result, ctx.obj.get("output", "table"))


@app.command("file")
def file_tax(
    ctx: typer.Context,
    period: str = typer.Argument(help="Tax period"),
):
    """File a tax return"""
    client = _get_client(ctx)
    result = client.tax_file(period)
    print_output(result, ctx.obj.get("output", "table"))