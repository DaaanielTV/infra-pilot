import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Blockchain")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List networks"""
    client = _get_client(ctx)
    result = client.blockchain_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Network name"),
    consensus: str = typer.Argument(help="Consensus mechanism"),
):
    """Create"""
    client = _get_client(ctx)
    result = client.blockchain_create(name, consensus)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    network_id: str = typer.Argument(help="Network ID"),
):
    """Status"""
    client = _get_client(ctx)
    result = client.blockchain_status(network_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def validators(
    ctx: typer.Context,
    network_id: str = typer.Argument(help="Network ID"),
):
    """Validators"""
    client = _get_client(ctx)
    result = client.blockchain_validators(network_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
