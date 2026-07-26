import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Runbook templates")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List runbook templates
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.runbook_list()
    data = result if isinstance(result, list) else result.get("runbooks", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def use(
    ctx: typer.Context,
    runbook_id: str = typer.Argument(..., help="Runbook ID"),
    target_id: str = typer.Argument(..., help="Target resource ID"),
    params: str = typer.Option(None, "--params", help="Runbook parameters (JSON)"),
) -> None:
    """Execute a runbook template against a resource
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.runbook_use(runbook_id, target_id, params)
    print_output(result, ctx.obj.get("output", "table"))