import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="LoRaWAN gateways")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    status: str = typer.Option(None, "--status", help="Filter by status"),
):
    """List gateways"""
    client = _get_client(ctx)
    result = client.list_lorawan_gateways(status)
    data = result if isinstance(result, list) else result.get("gateways", result)
    print_output(data, ctx.obj.get("output", "table"))