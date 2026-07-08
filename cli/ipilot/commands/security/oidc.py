import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="OIDC management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def clients(ctx: typer.Context):
    """List clients"""
    client = _get_client(ctx)
    result = client.oidc_clients()
    data = result if isinstance(result, list) else result.get("clients", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Client name"),
    redirect_uris: str = typer.Option(..., "--redirect-uris", help="Comma-separated redirect URIs"),
):
    """Register client"""
    client = _get_client(ctx)
    uris = [u.strip() for u in redirect_uris.split(",")]
    result = client.oidc_register(name, uris)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete(
    ctx: typer.Context,
    client_id: str = typer.Argument(..., help="OIDC client ID"),
):
    """Delete client"""
    client = _get_client(ctx)
    result = client.oidc_delete(client_id)
    print_output(result, ctx.obj.get("output", "table"))
