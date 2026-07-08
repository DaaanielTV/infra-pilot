import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Technical debt")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List items"""
    client = _get_client(ctx)
    result = client.techdebt_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def report(ctx: typer.Context):
    """Report"""
    client = _get_client(ctx)
    result = client.techdebt_report()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    debt_id: str = typer.Argument(help="Debt ID"),
):
    """Get item"""
    client = _get_client(ctx)
    result = client.techdebt_get(debt_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("fix")
def fix_debt(
    ctx: typer.Context,
    debt_id: str = typer.Argument(help="Debt ID"),
):
    """Fix"""
    client = _get_client(ctx)
    result = client.techdebt_fix(debt_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Summary"""
    client = _get_client(ctx)
    result = client.techdebt_summary()
    print_output(result, ctx.obj.get("output", "table"))
