import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Regulatory intelligence")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def changes(ctx: typer.Context) -> None:
    """Changes
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_changes()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def detect(
    ctx: typer.Context,
    change_id: str = typer.Argument(help="Change ID"),
) -> None:
    """Detect impact
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_detect(change_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def sources(ctx: typer.Context) -> None:
    """Sources
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_sources()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context) -> None:
    """Stats
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def impact(
    ctx: typer.Context,
    change_id: str = typer.Argument(help="Change ID"),
) -> None:
    """Impact analysis
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_impact(change_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def matrix(
    ctx: typer.Context,
    framework: str = typer.Argument(help="Framework name"),
) -> None:
    """Regulatory matrix
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_matrix(framework)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def calendar(ctx: typer.Context) -> None:
    """Calendar
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_calendar()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def notify(
    ctx: typer.Context,
    change_id: str = typer.Argument(help="Change ID"),
    email: str = typer.Argument(help="Notification email"),
) -> None:
    """Notify
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_notify(change_id, email)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def pending(ctx: typer.Context) -> None:
    """Pending items
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_pending()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def search(
    ctx: typer.Context,
    query: str = typer.Argument(help="Search query"),
) -> None:
    """Search
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ri_search(query)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))