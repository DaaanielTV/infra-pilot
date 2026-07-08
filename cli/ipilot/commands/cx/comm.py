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
    channel: str = typer.Argument(help="Email/sms/push"),
):
    """Send a communication"""
    client = _get_client(ctx)
    result = client.cx_comm_send(customer_id, template, channel)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def batches(ctx: typer.Context):
    """List communication batches"""
    client = _get_client(ctx)
    result = client.cx_comm_batches()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def batch(
    ctx: typer.Context,
    batch_id: str = typer.Argument(help="Batch ID"),
):
    """Get a batch"""
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
    """Schedule maintenance"""
    client = _get_client(ctx)
    result = client.cx_comm_maintenance_schedule(customer_id, message, scheduled_at)
    print_output(result, ctx.obj.get("output", "table"))

@app.command(name="maintenance-list")
def maintenance_list(ctx: typer.Context):
    """List maintenance"""
    client = _get_client(ctx)
    result = client.cx_comm_maintenance_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command(name="maintenance-complete")
def maintenance_complete(
    ctx: typer.Context,
    maintenance_id: str = typer.Argument(help="Maintenance ID"),
):
    """Complete maintenance"""
    client = _get_client(ctx)
    result = client.cx_comm_maintenance_complete(maintenance_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def templates(ctx: typer.Context):
    """List templates"""
    client = _get_client(ctx)
    result = client.cx_comm_templates()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command(name="template-create")
def template_create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Template name"),
    subject: str = typer.Argument(help="Template subject"),
    body: str = typer.Argument(help="Template body"),
):
    """Create a template"""
    client = _get_client(ctx)
    result = client.cx_comm_template_create(name, subject, body)
    print_output(result, ctx.obj.get("output", "table"))
