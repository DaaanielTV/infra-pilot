import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Ops chatbot")

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
    result = client.aiops_chatbot_message(message_text)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def tasks(ctx: typer.Context) -> None:
    """Chatbot tasks
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_chatbot_tasks()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def analytics(ctx: typer.Context) -> None:
    """Chatbot analytics
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.aiops_chatbot_analytics()
    print_output(result, ctx.obj.get("output", "table"))