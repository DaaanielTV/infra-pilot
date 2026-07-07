import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Audit management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List audits"""
    client = _get_client(ctx)
    result = client.am_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def schedule(
    ctx: typer.Context,
    name: str = typer.Argument(help="Audit name"),
    date: str = typer.Argument(help="Audit date"),
):
    """Schedule an audit"""
    client = _get_client(ctx)
    result = client.am_schedule(name, date)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def rights(ctx: typer.Context):
    """List audit rights"""
    client = _get_client(ctx)
    result = client.am_rights()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Get audit statistics"""
    client = _get_client(ctx)
    result = client.am_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def upcoming(ctx: typer.Context):
    """List upcoming audits"""
    client = _get_client(ctx)
    result = client.am_upcoming()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def overdue(ctx: typer.Context):
    """List overdue audits"""
    client = _get_client(ctx)
    result = client.am_overdue()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def workflow(
    ctx: typer.Context,
    audit_id: str = typer.Argument(help="Audit ID"),
):
    """Get audit workflow"""
    client = _get_client(ctx)
    result = client.am_workflow(audit_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    audit_id: str = typer.Argument(help="Audit ID"),
):
    """Get audit report"""
    client = _get_client(ctx)
    result = client.am_report(audit_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("register-right")
def register_right(
    ctx: typer.Context,
    name: str = typer.Argument(help="Right name"),
    description: str = typer.Argument(help="Right description"),
):
    """Register an audit right"""
    client = _get_client(ctx)
    result = client.am_register_right(name, description)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def calendar(ctx: typer.Context):
    """Get audit calendar"""
    client = _get_client(ctx)
    result = client.am_calendar()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
