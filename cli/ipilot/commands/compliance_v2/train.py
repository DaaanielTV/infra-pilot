import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Compliance training")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def modules(ctx: typer.Context):
    """List training modules"""
    client = _get_client(ctx)
    result = client.ct_modules()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def assign(
    ctx: typer.Context,
    user_id: str = typer.Argument(help="User ID"),
    module_id: str = typer.Argument(help="Module ID"),
):
    """Assign a training module"""
    client = _get_client(ctx)
    result = client.ct_assign(user_id, module_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    user_id: str = typer.Argument(help="User ID"),
):
    """Get training status"""
    client = _get_client(ctx)
    result = client.ct_status(user_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Get training statistics"""
    client = _get_client(ctx)
    result = client.ct_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def certifications(ctx: typer.Context):
    """List certifications"""
    client = _get_client(ctx)
    result = client.ct_certifications()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def expiring(ctx: typer.Context):
    """Get expiring certifications"""
    client = _get_client(ctx)
    result = client.ct_expiring()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def search(
    ctx: typer.Context,
    query: str = typer.Argument(help="Search query"),
):
    """Search training content"""
    client = _get_client(ctx)
    result = client.ct_search(query)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    module_id: str = typer.Argument(help="Module ID"),
):
    """Get training report"""
    client = _get_client(ctx)
    result = client.ct_report(module_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def progress(
    ctx: typer.Context,
    user_id: str = typer.Argument(help="User ID"),
):
    """Get training progress"""
    client = _get_client(ctx)
    result = client.ct_progress(user_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("batch-assign")
def batch_assign(
    ctx: typer.Context,
    user_ids: str = typer.Argument(help="User IDs (JSON)"),
    module_id: str = typer.Argument(help="Module ID"),
):
    """Batch assign training modules"""
    client = _get_client(ctx)
    result = client.ct_batch_assign(user_ids, module_id)
    print_output(result, ctx.obj.get("output", "table"))
