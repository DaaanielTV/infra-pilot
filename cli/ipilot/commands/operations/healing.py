import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Self-healing")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def status(ctx: typer.Context) -> None:
    """Show self-healing system status
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.heal_status()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def history(ctx: typer.Context) -> None:
    """Show self-healing action history
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.heal_history()
    data = result if isinstance(result, list) else result.get("history", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def retrain(ctx: typer.Context) -> None:
    """Retrain the healing model
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.heal_retrain()
    print_output(result, ctx.obj.get("output", "table"))