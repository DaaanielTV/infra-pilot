import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="PUE/DCIM")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def current(ctx: typer.Context):
    """Current PUE"""
    client = _get_client(ctx)
    result = client.pue_current()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def history(ctx: typer.Context):
    """Historical PUE data"""
    client = _get_client(ctx)
    result = client.pue_history()
    print_output(result, ctx.obj.get("output", "table"))
