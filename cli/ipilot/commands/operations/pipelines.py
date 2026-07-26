import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="CI/CD pipelines")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List all infrastructure pipelines
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.infra_pipeline_list()
    data = result if isinstance(result, list) else result.get("pipelines", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(..., help="Pipeline ID"),
    branch: str = typer.Option(None, "--branch", help="Branch to run"),
) -> None:
    """Run an infrastructure pipeline
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.infra_pipeline_run(pipeline_id, branch)
    print_output(result, ctx.obj.get("output", "table"))