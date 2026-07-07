import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Energy consumption")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def current(ctx: typer.Context):
    """Current energy snapshot"""
    client = _get_client(ctx)
    result = client.energy_current()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def history(
    ctx: typer.Context,
    server_id: str = typer.Option(None, "--server-id", help="Server ID"),
    hours: int = typer.Option(24, "--hours", help="Hours of history"),
):
    """Historical energy data"""
    client = _get_client(ctx)
    result = client.energy_history(server_id, hours)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(
    ctx: typer.Context,
    period: str = typer.Option("daily", "--period", help="Period (daily/weekly/monthly)"),
):
    """Energy summary"""
    client = _get_client(ctx)
    result = client.energy_summary(period)
    print_output(result, ctx.obj.get("output", "table"))
