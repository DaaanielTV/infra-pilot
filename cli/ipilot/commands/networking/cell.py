import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Cellular commands")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def networks(ctx: typer.Context) -> None:
    """List cellular networks
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cell_networks()
    data = result if isinstance(result, list) else result.get("networks", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Network name"),
    provider: str = typer.Argument(..., help="Provider name"),
    apn: str = typer.Argument(..., help="APN name"),
) -> None:
    """Register cellular network
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cell_register(name, provider, apn)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def delete(
    ctx: typer.Context,
    network_id: str = typer.Argument(..., help="Network ID"),
) -> None:
    """Delete cellular network
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cell_delete(network_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def status(
    ctx: typer.Context,
    network_id: str = typer.Argument(..., help="Network ID"),
) -> None:
    """Get network status
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cell_status(network_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def sims(
    ctx: typer.Context,
    network_id: str = typer.Argument(..., help="Network ID"),
) -> None:
    """List SIM cards
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cell_sims(network_id)
    data = result if isinstance(result, list) else result.get("sims", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def activate(
    ctx: typer.Context,
    sim_id: str = typer.Argument(..., help="SIM ID"),
) -> None:
    """Activate SIM card
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cell_activate(sim_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def deactivate(
    ctx: typer.Context,
    sim_id: str = typer.Argument(..., help="SIM ID"),
) -> None:
    """Deactivate SIM card
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cell_deactivate(sim_id)
    print_output(result, ctx.obj.get("output", "table"))