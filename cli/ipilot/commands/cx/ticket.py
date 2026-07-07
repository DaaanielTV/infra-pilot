import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Support tickets")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List support tickets"""
    client = _get_client(ctx)
    result = client.cx_ticket_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
    subject: str = typer.Argument(help="Ticket subject"),
    description: str = typer.Argument(help="Ticket description"),
    priority: str = typer.Option("medium", "--priority", help="Priority (low/medium/high/critical)"),
):
    """Create a support ticket"""
    client = _get_client(ctx)
    result = client.cx_ticket_create(customer_id, subject, description, priority)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    ticket_id: str = typer.Argument(help="Ticket ID"),
):
    """Get a support ticket"""
    client = _get_client(ctx)
    result = client.cx_ticket_get(ticket_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    ticket_id: str = typer.Argument(help="Ticket ID"),
    status: str = typer.Argument(help="New status"),
):
    """Update ticket status"""
    client = _get_client(ctx)
    result = client.cx_ticket_status(ticket_id, status)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def comment(
    ctx: typer.Context,
    ticket_id: str = typer.Argument(help="Ticket ID"),
    comment: str = typer.Argument(help="Comment text"),
):
    """Add a comment to a ticket"""
    client = _get_client(ctx)
    result = client.cx_ticket_comment(ticket_id, comment)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def assign(
    ctx: typer.Context,
    ticket_id: str = typer.Argument(help="Ticket ID"),
    assignee: str = typer.Argument(help="Assignee name"),
):
    """Assign a ticket"""
    client = _get_client(ctx)
    result = client.cx_ticket_assign(ticket_id, assignee)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Ticket statistics"""
    client = _get_client(ctx)
    result = client.cx_ticket_stats()
    print_output(result, ctx.obj.get("output", "table"))
