import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Federated learning")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List jobs"""
    client = _get_client(ctx)
    result = client.federated_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Job name"),
    config: str = typer.Argument(help="Job config (JSON)"),
):
    """Create"""
    client = _get_client(ctx)
    result = client.federated_create(name, config)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    job_id: str = typer.Argument(help="Job ID"),
):
    """Status"""
    client = _get_client(ctx)
    result = client.federated_status(job_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def rounds(
    ctx: typer.Context,
    job_id: str = typer.Argument(help="Job ID"),
):
    """Rounds"""
    client = _get_client(ctx)
    result = client.federated_rounds(job_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
