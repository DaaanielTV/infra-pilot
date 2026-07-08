import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Provider rankings")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def rank(ctx: typer.Context):
    """Rank providers by green score"""
    client = _get_client(ctx)
    result = client.provider_rank()
    print_output(result, ctx.obj.get("output", "table"))
