import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="FinOps reports")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(ctx: typer.Context) -> None:
    """List reports
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_reports_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def summary(ctx: typer.Context) -> None:
    """Reports summary
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_reports_summary()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def generate(
    ctx: typer.Context,
    report_type: str = typer.Argument(help="Report type"),
    period: str = typer.Argument(help="Report period"),
) -> None:
    """Generate report
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_reports_generate(report_type, period)
    print_output(result, ctx.obj.get("output", "table"))