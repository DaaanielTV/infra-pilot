import typer
from ....client import ApiClient
from ....config import load_config
from ....output.formatters import print_output

app = typer.Typer(help="Incident management")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def remediate(ctx: typer.Context) -> None:
    """Remediation suggestions
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))

@app.command()
def analytics(ctx: typer.Context) -> None:
    """Incident analytics
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))

@app.command()
def mttr(ctx: typer.Context) -> None:
    """MTTR metrics
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))