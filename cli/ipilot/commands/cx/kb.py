import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Knowledge base")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(
    ctx: typer.Context,
    category: str = typer.Option(None, "--category", help="Filter category"),
) -> None:
    """List articles
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_kb_list(category)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def create(
    ctx: typer.Context,
    title: str = typer.Argument(help="Article title"),
    content: str = typer.Argument(help="Article content"),
    category: str = typer.Argument(help="Article category"),
) -> None:
    """Create an article
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_kb_create(title, content, category)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def get(
    ctx: typer.Context,
    article_id: str = typer.Argument(help="Article ID"),
) -> None:
    """Get an article
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_kb_get(article_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def update(
    ctx: typer.Context,
    article_id: str = typer.Argument(help="Article ID"),
    content: str = typer.Argument(help="New content"),
) -> None:
    """Update an article
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_kb_update(article_id, content)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def search(
    ctx: typer.Context,
    query: str = typer.Argument(help="Search query"),
) -> None:
    """Search KB
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_kb_search(query)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def categories(ctx: typer.Context) -> None:
    """List categories
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_kb_categories()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def feedback(
    ctx: typer.Context,
    article_id: str = typer.Argument(help="Article ID"),
    helpful: bool = typer.Argument(help="Was helpful?"),
) -> None:
    """Article feedback
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_kb_feedback(article_id, helpful)
    print_output(result, ctx.obj.get("output", "table"))