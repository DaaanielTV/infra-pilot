import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Deployment commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def deploy(
    ctx: typer.Context,
    server: str = typer.Argument(..., help="Server ID or name"),
    branch: str = typer.Argument(..., help="Branch to deploy"),
):
    """Deploy a branch to a server"""
    client = _get_client(ctx)
    result = client.deploy(server, branch)
    print_output(result, ctx.obj.get("output", "table"))
