import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Customer communications")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def send(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
    template: str = typer.Argument(help="Template name"),
    channel: str = typer.Argument(help="Channel (email/sms/push)"),
):
    """Send a communication to a customer"""
    client = _get_client(ctx)
    result = client.cx_comm_send(customer_id, template, channel)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def batches(ctx: typer.Context):
    """List communication batches"""
    client = _get_client(ctx)
    result = client.cx_comm_batches()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def batch(
    ctx: typer.Context,
    batch_id: str = typer.Argument(help="Batch ID"),
):
    """Get a communication batch"""
    client = _get_client(ctx)
    result = client.cx_comm_batch(batch_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command(name="maintenance-schedule")
def maintenance_schedule(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
    message: str = typer.Argument(help="Maintenance message"),
    scheduled_at: str = typer.Argument(help="Scheduled time"),
):
    """Schedule a maintenance notification"""
    client = _get_client(ctx)
    result = client.cx_comm_maintenance_schedule(customer_id, message, scheduled_at)
    print_output(result, ctx.obj.get("output", "table"))


@app.command(name="maintenance-list")
def maintenance_list(ctx: typer.Context):
    """List maintenance notifications"""
    client = _get_client(ctx)
    result = client.cx_comm_maintenance_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command(name="maintenance-complete")
def maintenance_complete(
    ctx: typer.Context,
    maintenance_id: str = typer.Argument(help="Maintenance ID"),
):
    """Mark maintenance as complete"""
    client = _get_client(ctx)
    result = client.cx_comm_maintenance_complete(maintenance_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def templates(ctx: typer.Context):
    """List communication templates"""
    client = _get_client(ctx)
    result = client.cx_comm_templates()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command(name="template-create")
def template_create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Template name"),
    subject: str = typer.Argument(help="Template subject"),
    body: str = typer.Argument(help="Template body"),
):
    """Create a communication template"""
    client = _get_client(ctx)
    result = client.cx_comm_template_create(name, subject, body)
    print_output(result, ctx.obj.get("output", "table"))
