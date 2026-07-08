import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="CO2 offset")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def quote(
    ctx: typer.Context,
    amount: float = typer.Argument(..., help="CO2 amount in tonnes"),
):
    """Get offset quote"""
    client = _get_client(ctx)
    result = client.offset_quote(amount)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def purchase(
    ctx: typer.Context,
    amount: float = typer.Argument(..., help="CO2 amount in tonnes"),
    provider: str = typer.Argument(..., help="Offset provider"),
):
    """Purchase carbon offset"""
    client = _get_client(ctx)
    result = client.offset_purchase(amount, provider)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def certs(ctx: typer.Context):
    """List carbon offset certificates"""
    client = _get_client(ctx)
    result = client.offset_certs()
    data = result if isinstance(result, list) else result.get("certificates", result)
    print_output(data, ctx.obj.get("output", "table"))
