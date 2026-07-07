import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Regulatory intelligence")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def changes(ctx: typer.Context):
    """Get regulatory changes"""
    client = _get_client(ctx)
    result = client.ri_changes()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def detect(
    ctx: typer.Context,
    change_id: str = typer.Argument(help="Change ID"),
):
    """Detect regulatory impact"""
    client = _get_client(ctx)
    result = client.ri_detect(change_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def sources(ctx: typer.Context):
    """List regulatory sources"""
    client = _get_client(ctx)
    result = client.ri_sources()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Get regulatory intelligence stats"""
    client = _get_client(ctx)
    result = client.ri_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def impact(
    ctx: typer.Context,
    change_id: str = typer.Argument(help="Change ID"),
):
    """Get regulatory impact analysis"""
    client = _get_client(ctx)
    result = client.ri_impact(change_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def matrix(
    ctx: typer.Context,
    framework: str = typer.Argument(help="Framework name"),
):
    """Get regulatory matrix"""
    client = _get_client(ctx)
    result = client.ri_matrix(framework)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def calendar(ctx: typer.Context):
    """Get regulatory calendar"""
    client = _get_client(ctx)
    result = client.ri_calendar()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def notify(
    ctx: typer.Context,
    change_id: str = typer.Argument(help="Change ID"),
    email: str = typer.Argument(help="Notification email"),
):
    """Set up regulatory notification"""
    client = _get_client(ctx)
    result = client.ri_notify(change_id, email)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def pending(ctx: typer.Context):
    """Get pending regulatory items"""
    client = _get_client(ctx)
    result = client.ri_pending()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def search(
    ctx: typer.Context,
    query: str = typer.Argument(help="Search query"),
):
    """Search regulatory content"""
    client = _get_client(ctx)
    result = client.ri_search(query)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
