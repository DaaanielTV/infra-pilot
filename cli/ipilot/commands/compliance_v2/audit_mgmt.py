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
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def schedule(
    ctx: typer.Context,
    name: str = typer.Argument(help="Audit name"),
    date: str = typer.Argument(help="Audit date"),
):
    """Schedule"""
    client = _get_client(ctx)
    result = client.am_schedule(name, date)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def rights(ctx: typer.Context):
    """Rights"""
    client = _get_client(ctx)
    result = client.am_rights()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Stats"""
    client = _get_client(ctx)
    result = client.am_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def upcoming(ctx: typer.Context):
    """Upcoming"""
    client = _get_client(ctx)
    result = client.am_upcoming()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def overdue(ctx: typer.Context):
    """Overdue"""
    client = _get_client(ctx)
    result = client.am_overdue()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def workflow(
    ctx: typer.Context,
    audit_id: str = typer.Argument(help="Audit ID"),
):
    """Workflow"""
    client = _get_client(ctx)
    result = client.am_workflow(audit_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    audit_id: str = typer.Argument(help="Audit ID"),
):
    """Report"""
    client = _get_client(ctx)
    result = client.am_report(audit_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("register-right")
def register_right(
    ctx: typer.Context,
    name: str = typer.Argument(help="Right name"),
    description: str = typer.Argument(help="Right description"),
):
    """Register right"""
    client = _get_client(ctx)
    result = client.am_register_right(name, description)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def calendar(ctx: typer.Context):
    """Calendar"""
    client = _get_client(ctx)
    result = client.am_calendar()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
