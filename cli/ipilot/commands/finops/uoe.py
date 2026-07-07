import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Unit of economics")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def metrics(ctx: typer.Context):
    """List unit of economics metrics"""
    client = _get_client(ctx)
    result = client.finops_uoe_metrics()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def record(
    ctx: typer.Context,
    metric: str = typer.Argument(help="Metric name"),
    value: float = typer.Argument(help="Metric value"),
):
    """Record a unit of economics metric"""
    client = _get_client(ctx)
    result = client.finops_uoe_record(metric, value)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def targets(ctx: typer.Context):
    """List UoE targets"""
    client = _get_client(ctx)
    result = client.finops_uoe_targets()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command(name="set-target")
def set_target(
    ctx: typer.Context,
    metric: str = typer.Argument(help="Metric name"),
    target: float = typer.Argument(help="Target value"),
):
    """Set a UoE target"""
    client = _get_client(ctx)
    result = client.finops_uoe_set_target(metric, target)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def violations(ctx: typer.Context):
    """List UoE violations"""
    client = _get_client(ctx)
    result = client.finops_uoe_violations()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def overview(ctx: typer.Context):
    """UoE overview"""
    client = _get_client(ctx)
    result = client.finops_uoe_overview()
    print_output(result, ctx.obj.get("output", "table"))
