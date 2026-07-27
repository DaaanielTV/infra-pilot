import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Network cost")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def show(ctx: typer.Context) -> None:
    """Show network costs
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.netcost_show()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def budget(
    ctx: typer.Context,
    budget: float = typer.Argument(..., help="Budget amount"),
) -> None:
    """Set cost budget
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.netcost_budget(budget)
    print_output(result, ctx.obj.get("output", "table"))