import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Loyalty program")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def status(ctx: typer.Context):
    """Get loyalty status"""
    client = _get_client(ctx)
    result = client.loyalty_status()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def badges(ctx: typer.Context):
    """List loyalty badges"""
    client = _get_client(ctx)
    result = client.loyalty_badges()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def rewards(ctx: typer.Context):
    """List available rewards"""
    client = _get_client(ctx)
    result = client.loyalty_rewards()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def redeem(
    ctx: typer.Context,
    reward_id: str = typer.Argument(help="Reward ID"),
):
    """Redeem a reward"""
    client = _get_client(ctx)
    result = client.loyalty_redeem(reward_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def leaderboard(ctx: typer.Context):
    """Get loyalty leaderboard"""
    client = _get_client(ctx)
    result = client.loyalty_leaderboard()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))