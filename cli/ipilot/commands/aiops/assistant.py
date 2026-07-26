import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="AI assistant")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def message(ctx: typer.Context, message_text: str = typer.Argument(..., help="Message text")) -> None:
    """Send a message
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_assistant_message(message_text)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def stats(ctx: typer.Context) -> None:
    """Assistant stats
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_assistant_stats()
    print_output(result, ctx.obj.get("output", "table"))