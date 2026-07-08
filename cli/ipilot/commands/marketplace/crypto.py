import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Cryptocurrency")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def wallets(ctx: typer.Context):
    """List crypto wallets"""
    client = _get_client(ctx)
    result = client.crypto_wallets()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command("create-wallet")
def create_wallet(
    ctx: typer.Context,
    currency: str = typer.Argument(help="Currency"),
):
    """Create a crypto wallet"""
    client = _get_client(ctx)
    result = client.crypto_create_wallet(currency)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def transactions(
    ctx: typer.Context,
    wallet_id: str = typer.Argument(help="Wallet ID"),
):
    """List crypto transactions"""
    client = _get_client(ctx)
    result = client.crypto_transactions(wallet_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def rates(ctx: typer.Context):
    """Get crypto exchange rates"""
    client = _get_client(ctx)
    result = client.crypto_rates()
    print_output(result, ctx.obj.get("output", "table"))