import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Backup management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    server: str = typer.Argument(None, help="Server ID (optional)"),
):
    """List backups"""
    client = _get_client(ctx)
    result = client.list_backups(server)
    data = result if isinstance(result, list) else result.get("backups", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    server: str = typer.Argument(..., help="Server ID or name"),
):
    """Create a backup"""
    client = _get_client(ctx)
    result = client.create_backup(server)
    print_output(result, ctx.obj.get("output", "table"))
