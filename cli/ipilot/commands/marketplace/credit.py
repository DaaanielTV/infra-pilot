import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Marketplace credit")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List credits"""
    client = _get_client(ctx)
    result = client.credit_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def issue(
    ctx: typer.Context,
    customer: str = typer.Argument(help="Customer ID"),
    amount: float = typer.Argument(help="Credit amount"),
):
    """Issue a credit"""
    client = _get_client(ctx)
    result = client.credit_issue(customer, amount)
    print_output(result, ctx.obj.get("output", "table"))