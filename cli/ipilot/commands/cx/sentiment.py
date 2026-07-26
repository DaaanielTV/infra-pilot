import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Sentiment analysis")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def analyze(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
) -> None:
    """Analyze sentiment
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_sentiment_analyze(customer_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def profile(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
) -> None:
    """Sentiment profile
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_sentiment_profile(customer_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def interactions(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
) -> None:
    """List interactions
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_sentiment_interactions(customer_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def trends(ctx: typer.Context) -> None:
    """Sentiment trends
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_sentiment_trends()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def alerts(ctx: typer.Context) -> None:
    """Sentiment alerts
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_sentiment_alerts()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))