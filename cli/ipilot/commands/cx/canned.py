import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Canned responses")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List canned responses"""
    client = _get_client(ctx)
    result = client.cx_canned_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    title: str = typer.Argument(help="Response title"),
    content: str = typer.Argument(help="Response content"),
    category: str = typer.Argument(help="Response category"),
):
    """Create a canned response"""
    client = _get_client(ctx)
    result = client.cx_canned_create(title, content, category)
    print_output(result, ctx.obj.get("output", "table"))
