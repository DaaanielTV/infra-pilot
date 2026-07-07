import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Carbon footprint")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def current(ctx: typer.Context):
    """Current CO2 output"""
    client = _get_client(ctx)
    result = client.carbon_current()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def history(ctx: typer.Context):
    """Historical CO2 data"""
    client = _get_client(ctx)
    result = client.carbon_history()
    print_output(result, ctx.obj.get("output", "table"))
