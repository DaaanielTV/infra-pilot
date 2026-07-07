import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Commitment-based discounts")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List commitment-based discounts"""
    client = _get_client(ctx)
    result = client.finops_commitment_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Commitment discount summary"""
    client = _get_client(ctx)
    result = client.finops_commitment_summary()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def implement(
    ctx: typer.Context,
    commitment_id: str = typer.Argument(help="Commitment ID"),
):
    """Implement a commitment-based discount"""
    client = _get_client(ctx)
    result = client.finops_commitment_implement(commitment_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def commitments(ctx: typer.Context):
    """List all commitments"""
    client = _get_client(ctx)
    result = client.finops_commitment_commitments()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
