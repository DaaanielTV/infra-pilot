import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Customer health")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List customer health scores"""
    client = _get_client(ctx)
    result = client.cx_health_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
):
    """Get customer health"""
    client = _get_client(ctx)
    result = client.cx_health_get(customer_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def compute(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
):
    """Compute customer health score"""
    client = _get_client(ctx)
    result = client.cx_health_compute(customer_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def history(
    ctx: typer.Context,
    customer_id: str = typer.Argument(help="Customer ID"),
):
    """Get customer health history"""
    client = _get_client(ctx)
    result = client.cx_health_history(customer_id)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Customer health stats"""
    client = _get_client(ctx)
    result = client.cx_health_stats()
    print_output(result, ctx.obj.get("output", "table"))
