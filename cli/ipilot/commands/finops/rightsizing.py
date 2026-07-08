import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Rightsizing")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(ctx: typer.Context):
    """List recommendations"""
    client = _get_client(ctx)
    result = client.finops_rightsizing_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def summary(ctx: typer.Context):
    """Rightsizing summary"""
    client = _get_client(ctx)
    result = client.finops_rightsizing_summary()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def approve(
    ctx: typer.Context,
    suggestion_id: str = typer.Argument(help="Suggestion ID"),
):
    """Approve suggestion"""
    client = _get_client(ctx)
    result = client.finops_rightsizing_approve(suggestion_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def implement(
    ctx: typer.Context,
    suggestion_id: str = typer.Argument(help="Suggestion ID"),
):
    """Implement suggestion"""
    client = _get_client(ctx)
    result = client.finops_rightsizing_implement(suggestion_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def dismiss(
    ctx: typer.Context,
    suggestion_id: str = typer.Argument(help="Suggestion ID"),
):
    """Dismiss suggestion"""
    client = _get_client(ctx)
    result = client.finops_rightsizing_dismiss(suggestion_id)
    print_output(result, ctx.obj.get("output", "table"))
