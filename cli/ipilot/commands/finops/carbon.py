import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Carbon footprint")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(ctx: typer.Context) -> None:
    """List carbon data
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_carbon_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def assets(ctx: typer.Context) -> None:
    """List assets
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_carbon_assets()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(help="Asset name"),
    asset_type: str = typer.Argument(help="Asset type"),
    emissions: float = typer.Argument(help="Emissions value"),
) -> None:
    """Register asset
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_carbon_register(name, asset_type, emissions)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def sustainability(ctx: typer.Context) -> None:
    """Sustainability metrics
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.finops_carbon_sustainability()
    print_output(result, ctx.obj.get("output", "table"))