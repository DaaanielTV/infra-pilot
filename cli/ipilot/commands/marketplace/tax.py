import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Tax management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def rates(ctx: typer.Context) -> None:
    """Get tax rates
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.tax_rates()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def invoices(ctx: typer.Context) -> None:
    """List tax invoices
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.tax_invoices()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def generate(
    ctx: typer.Context,
    period: str = typer.Argument(help="Tax period"),
) -> None:
    """Generate a tax invoice
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.tax_generate(period)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def pay(
    ctx: typer.Context,
    invoice_id: str = typer.Argument(help="Invoice ID"),
) -> None:
    """Pay a tax invoice
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.tax_pay(invoice_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context) -> None:
    """Get tax summary
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.tax_summary()
    print_output(result, ctx.obj.get("output", "table"))


@app.command("file")
def file_tax(
    ctx: typer.Context,
    period: str = typer.Argument(help="Tax period"),
) -> None:
    """File a tax return
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.tax_file(period)
    print_output(result, ctx.obj.get("output", "table"))