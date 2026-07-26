import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Customer health")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(ctx: typer.Context) -> None:
    """List health scores
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_health_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def get(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
) -> None:
    """Get health
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_health_get(customer_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def compute(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
) -> None:
    """Compute health score
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_health_compute(customer_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def history(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
) -> None:
    """Health history
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_health_history(customer_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def stats(ctx: typer.Context) -> None:
    """Health stats
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_health_stats()
    print_output(result, ctx.obj.get("output", "table"))