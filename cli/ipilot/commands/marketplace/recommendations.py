import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Recommendations")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List recommendations
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.reco_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context) -> None:
    """Get recommendation summary
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.reco_summary()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def implement(
    ctx: typer.Context,
    reco_id: str = typer.Argument(help="Recommendation ID"),
) -> None:
    """Implement a recommendation
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.reco_implement(reco_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def dismiss(
    ctx: typer.Context,
    reco_id: str = typer.Argument(help="Recommendation ID"),
) -> None:
    """Dismiss a recommendation
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.reco_dismiss(reco_id)
    print_output(result, ctx.obj.get("output", "table"))