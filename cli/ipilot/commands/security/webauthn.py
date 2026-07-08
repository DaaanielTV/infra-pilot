import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="WebAuthn")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def credentials(ctx: typer.Context):
    """List credentials"""
    client = _get_client(ctx)
    result = client.webauthn_credentials()
    data = result if isinstance(result, list) else result.get("credentials", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def remove(
    ctx: typer.Context,
    credential_id: str = typer.Argument(..., help="WebAuthn credential ID"),
):
    """Remove credential"""
    client = _get_client(ctx)
    result = client.webauthn_remove(credential_id)
    print_output(result, ctx.obj.get("output", "table"))
