import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Efficiency scorecards")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def score(ctx: typer.Context) -> None:
    """Get efficiency score
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.efficiency_score()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def recommendations(ctx: typer.Context) -> None:
    """Get efficiency recommendations
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.efficiency_recommendations()
    print_output(result, ctx.obj.get("output", "table"))