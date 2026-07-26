import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Root cause analysis")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def analyze(ctx: typer.Context, incident_id: str = typer.Argument(..., help="Incident ID")) -> None:
    """Analyze root cause
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_rca_analyze(incident_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def incidents(ctx: typer.Context) -> None:
    """List incidents
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_rca_incidents()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def events(ctx: typer.Context, incident_id: str = typer.Argument(..., help="Incident ID")) -> None:
    """List events
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_rca_events(incident_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def deps(ctx: typer.Context, incident_id: str = typer.Argument(..., help="Incident ID")) -> None:
    """List dependencies
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_rca_deps(incident_id)
    print_output(result, ctx.obj.get("output", "table"))