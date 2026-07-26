import typer
from ....client import ApiClient
from ....config import load_config
from ....output.formatters import print_output

app = typer.Typer(help="Operations assistant")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def chat(ctx: typer.Context) -> None:
    """Chat assistant
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))

@app.command()
def tasks(ctx: typer.Context) -> None:
    """Ops tasks
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))

@app.command()
def priorities(ctx: typer.Context) -> None:
    """Ops priorities
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))