import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Resource quotas")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List all resource quotas"""
    client = _get_client(ctx)
    result = client.quota_list()
    data = result if isinstance(result, list) else result.get("quotas", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def check(
    ctx: typer.Context,
    resource_type: str = typer.Argument(..., help="Resource type to check"),
    amount: int = typer.Argument(..., help="Amount to check against quota"),
):
    """Check if a resource request exceeds quota"""
    client = _get_client(ctx)
    result = client.quota_check(resource_type, amount)
    print_output(result, ctx.obj.get("output", "table"))