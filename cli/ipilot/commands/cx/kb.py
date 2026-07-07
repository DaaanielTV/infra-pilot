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
    category: str = typer.Option(None, "--category", help="Filter by category"),
):
    """List knowledge base articles"""
    client = _get_client(ctx)
    result = client.cx_kb_list(category)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    title: str = typer.Argument(help="Article title"),
    content: str = typer.Argument(help="Article content"),
    category: str = typer.Argument(help="Article category"),
):
    """Create a knowledge base article"""
    client = _get_client(ctx)
    result = client.cx_kb_create(title, content, category)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    article_id: str = typer.Argument(help="Article ID"),
):
    """Get a knowledge base article"""
    client = _get_client(ctx)
    result = client.cx_kb_get(article_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def update(
    ctx: typer.Context,
    article_id: str = typer.Argument(help="Article ID"),
    content: str = typer.Argument(help="New content"),
):
    """Update a knowledge base article"""
    client = _get_client(ctx)
    result = client.cx_kb_update(article_id, content)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def search(
    ctx: typer.Context,
    query: str = typer.Argument(help="Search query"),
):
    """Search knowledge base"""
    client = _get_client(ctx)
    result = client.cx_kb_search(query)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def categories(ctx: typer.Context):
    """List knowledge base categories"""
    client = _get_client(ctx)
    result = client.cx_kb_categories()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def feedback(
    ctx: typer.Context,
    article_id: str = typer.Argument(help="Article ID"),
    helpful: bool = typer.Argument(help="Was this article helpful?"),
):
    """Submit feedback on an article"""
    client = _get_client(ctx)
    result = client.cx_kb_feedback(article_id, helpful)
    print_output(result, ctx.obj.get("output", "table"))
