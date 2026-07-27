import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Waste detection")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(ctx: typer.Context) -> None:
    """List findings
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_waste_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def summary(ctx: typer.Context) -> None:
    """Waste summary
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_waste_summary()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def scan(ctx: typer.Context) -> None:
    """Run scan
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_waste_scan()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def approve(
    ctx: typer.Context,
    waste_id: str = typer.Argument(help="Waste ID"),
) -> None:
    """Approve finding
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_waste_approve(waste_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def cleanup(
    ctx: typer.Context,
    waste_id: str = typer.Argument(help="Waste ID"),
) -> None:
    """Clean up
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_waste_cleanup(waste_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def dismiss(
    ctx: typer.Context,
    waste_id: str = typer.Argument(help="Waste ID"),
) -> None:
    """Dismiss finding
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_waste_dismiss(waste_id)
    print_output(result, ctx.obj.get("output", "table"))