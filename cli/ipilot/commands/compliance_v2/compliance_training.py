import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Compliance training")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def modules(ctx: typer.Context) -> None:
    """Modules
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ct_modules()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def assign(
    ctx: typer.Context,
    user_id: str = typer.Argument(help="User ID"),
    module_id: str = typer.Argument(help="Module ID"),
) -> None:
    """Assign
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ct_assign(user_id, module_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    user_id: str = typer.Argument(help="User ID"),
) -> None:
    """Status
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ct_status(user_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context) -> None:
    """Stats
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ct_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def certifications(ctx: typer.Context) -> None:
    """Certifications
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ct_certifications()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def expiring(ctx: typer.Context) -> None:
    """Expiring certs
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ct_expiring()
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
    result = client.ct_search(query)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    module_id: str = typer.Argument(help="Module ID"),
) -> None:
    """Report
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ct_report(module_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def progress(
    ctx: typer.Context,
    user_id: str = typer.Argument(help="User ID"),
) -> None:
    """Progress
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ct_progress(user_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("batch-assign")
def batch_assign(
    ctx: typer.Context,
    user_ids: str = typer.Argument(help="User IDs (JSON)"),
    module_id: str = typer.Argument(help="Module ID"),
) -> None:
    """Batch assign
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ct_batch_assign(user_ids, module_id)
    print_output(result, ctx.obj.get("output", "table"))