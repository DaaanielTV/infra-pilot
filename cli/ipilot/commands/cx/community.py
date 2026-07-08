import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Community")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def posts(ctx: typer.Context):
    """List posts"""
    client = _get_client(ctx)
    result = client.cx_community_posts()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def create(
    ctx: typer.Context,
    title: str = typer.Argument(help="Post title"),
    content: str = typer.Argument(help="Post content"),
    category: str = typer.Argument(help="Post category"),
):
    """Create a post"""
    client = _get_client(ctx)
    result = client.cx_community_create(title, content, category)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def get(
    ctx: typer.Context,
    post_id: str = typer.Argument(help="Post ID"),
):
    """Get a post"""
    client = _get_client(ctx)
    result = client.cx_community_get(post_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def vote(
    ctx: typer.Context,
    post_id: str = typer.Argument(help="Post ID"),
    vote: int = typer.Argument(help="Vote value"),
):
    """Vote on a post"""
    client = _get_client(ctx)
    result = client.cx_community_vote(post_id, vote)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def comment(
    ctx: typer.Context,
    post_id: str = typer.Argument(help="Post ID"),
    content: str = typer.Argument(help="Comment content"),
):
    """Comment on a post"""
    client = _get_client(ctx)
    result = client.cx_community_comment(post_id, content)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def comments(
    ctx: typer.Context,
    post_id: str = typer.Argument(help="Post ID"),
):
    """List comments"""
    client = _get_client(ctx)
    result = client.cx_community_comments(post_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def requests(ctx: typer.Context):
    """Feature requests"""
    client = _get_client(ctx)
    result = client.cx_community_requests()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def categories(ctx: typer.Context):
    """List categories"""
    client = _get_client(ctx)
    result = client.cx_community_categories()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def leaderboard(ctx: typer.Context):
    """Leaderboard"""
    client = _get_client(ctx)
    result = client.cx_community_leaderboard()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def stats(ctx: typer.Context):
    """Community stats"""
    client = _get_client(ctx)
    result = client.cx_community_stats()
    print_output(result, ctx.obj.get("output", "table"))
