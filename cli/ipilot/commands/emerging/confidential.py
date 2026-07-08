import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Confidential computing")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List enclaves"""
    client = _get_client(ctx)
    result = client.confidential_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Enclave name"),
    image: str = typer.Argument(help="Enclave image"),
):
    """Create"""
    client = _get_client(ctx)
    result = client.confidential_create(name, image)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def attest(
    ctx: typer.Context,
    enclave_id: str = typer.Argument(help="Enclave ID"),
):
    """Attest"""
    client = _get_client(ctx)
    result = client.confidential_attest(enclave_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def secrets(
    ctx: typer.Context,
    enclave_id: str = typer.Argument(help="Enclave ID"),
):
    """Secrets"""
    client = _get_client(ctx)
    result = client.confidential_secrets(enclave_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
