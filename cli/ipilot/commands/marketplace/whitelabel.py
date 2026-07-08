import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="White-label settings")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def settings(ctx: typer.Context):
    """Get white-label settings"""
    client = _get_client(ctx)
    result = client.whitelabel_settings()
    print_output(result, ctx.obj.get("output", "table"))