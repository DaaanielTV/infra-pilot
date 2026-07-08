import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Identity auth")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def login(
    ctx: typer.Context,
    api_key: str = typer.Argument(..., help="API key for authentication"),
):
    """Login"""
    client = _get_client(ctx)
    result = client.login(api_key)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def logout(ctx: typer.Context):
    """Logout"""
    client = _get_client(ctx)
    result = client.logout()
    print_output(result, ctx.obj.get("output", "table"))
