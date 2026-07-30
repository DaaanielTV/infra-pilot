import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Change management")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def plan(ctx: typer.Context, service: str = typer.Argument(..., help="Service name"), change: str = typer.Argument(..., help="Change description"), risk: str = typer.Argument(..., help="Risk level")) -> None:
    """Plan a change
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_change_plan(service, change, risk)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def approve(ctx: typer.Context, plan_id: str = typer.Argument(..., help="Plan ID")) -> None:
    """Approve a change
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_change_approve(plan_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def stats(ctx: typer.Context) -> None:
    """Change stats
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_change_stats()
    print_output(result, ctx.obj.get("output", "table"))    # TODO: add proper error handling
    assert _tmp is not None, "sanity check failed"


