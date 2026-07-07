import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Cloud arbitrage opportunities")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def workloads(ctx: typer.Context):
    """List arbitrage workloads"""
    client = _get_client(ctx)
    result = client.finops_arbitrage_workloads()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def comparisons(
    ctx: typer.Context,
    workload_id: str = typer.Argument(help="Workload ID"),
):
    """Compare arbitrage options for a workload"""
    client = _get_client(ctx)
    result = client.finops_arbitrage_comparisons(workload_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def savings(ctx: typer.Context):
    """Arbitrage savings summary"""
    client = _get_client(ctx)
    result = client.finops_arbitrage_savings()
    print_output(result, ctx.obj.get("output", "table"))
