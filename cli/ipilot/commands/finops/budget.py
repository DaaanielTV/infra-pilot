import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Budget management")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(ctx: typer.Context):
    """List budgets"""
    client = _get_client(ctx)
    result = client.finops_budget_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Budget name"),
    amount: float = typer.Argument(help="Budget amount"),
    period: str = typer.Argument(help="Budget period"),
):
    """Create a budget"""
    client = _get_client(ctx)
    result = client.finops_budget_create(name, amount, period)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def get(
    ctx: typer.Context,
    budget_id: str = typer.Argument(help="Budget ID"),
):
    """Get a budget"""
    client = _get_client(ctx)
    result = client.finops_budget_get(budget_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def spend(
    ctx: typer.Context,
    budget_id: str = typer.Argument(help="Budget ID"),
):
    """Budget spend"""
    client = _get_client(ctx)
    result = client.finops_budget_spend(budget_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def forecast(
    ctx: typer.Context,
    budget_id: str = typer.Argument(help="Budget ID"),
):
    """Budget forecast"""
    client = _get_client(ctx)
    result = client.finops_budget_forecast(budget_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def scenario(
    ctx: typer.Context,
    budget_id: str = typer.Argument(help="Budget ID"),
    adjustments: str = typer.Argument(help="Adjustments (JSON)"),
):
    """Run scenario"""
    client = _get_client(ctx)
    result = client.finops_budget_scenario(budget_id, adjustments)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def summary(ctx: typer.Context):
    """Budget summary"""
    client = _get_client(ctx)
    result = client.finops_budget_summary()
    print_output(result, ctx.obj.get("output", "table"))
