import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Cloud arbitrage")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def workloads(ctx: typer.Context) -> None:
    """List workloads
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_arbitrage_workloads()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def comparisons(
    ctx: typer.Context,
    workload_id: str = typer.Argument(help="Workload ID"),
) -> None:
    """Compare options
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_arbitrage_comparisons(workload_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def savings(ctx: typer.Context) -> None:
    """Savings summary
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_arbitrage_savings()
    print_output(result, ctx.obj.get("output", "table"))