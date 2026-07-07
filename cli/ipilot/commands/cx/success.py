import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Customer success plays")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def plays(ctx: typer.Context):
    """List success plays"""
    client = _get_client(ctx)
    result = client.cx_success_plays()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Play name"),
    trigger: str = typer.Argument(help="Trigger condition"),
    actions: str = typer.Argument(help="Actions (JSON)"),
):
    """Create a success play"""
    client = _get_client(ctx)
    result = client.cx_success_create(name, trigger, actions)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    play_id: str = typer.Argument(help="Play ID"),
):
    """Get success play status"""
    client = _get_client(ctx)
    result = client.cx_success_status(play_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def trigger(
    ctx: typer.Context,
    play_id: str = typer.Argument(help="Play ID"),
    customer_id: str = typer.Argument(help="Customer ID"),
):
    """Trigger a success play for a customer"""
    client = _get_client(ctx)
    result = client.cx_success_trigger(play_id, customer_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def executions(
    ctx: typer.Context,
    play_id: str = typer.Argument(help="Play ID"),
):
    """List executions for a success play"""
    client = _get_client(ctx)
    result = client.cx_success_executions(play_id)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Success play statistics"""
    client = _get_client(ctx)
    result = client.cx_success_stats()
    print_output(result, ctx.obj.get("output", "table"))
