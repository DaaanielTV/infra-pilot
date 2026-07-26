import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Customer onboarding")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def start(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
    plan: str = typer.Argument(help="Onboarding plan"),
) -> None:
    """Start onboarding
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_onboarding_start(customer_id, plan)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def get(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
) -> None:
    """Onboarding status
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_onboarding_get(customer_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def step(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
    step: str = typer.Argument(help="Step name"),
) -> None:
    """Complete a step
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_onboarding_step(customer_id, step)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def stats(ctx: typer.Context) -> None:
    """Onboarding stats
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_onboarding_stats()
    print_output(result, ctx.obj.get("output", "table"))