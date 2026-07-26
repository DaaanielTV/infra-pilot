import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Workflow automation")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List all workflows
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.workflow_list()
    data = result if isinstance(result, list) else result.get("workflows", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Workflow name"),
    definition: str = typer.Argument(..., help="Workflow definition (YAML/JSON)"),
) -> None:
    """Create a new workflow
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.workflow_create(name, definition)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    workflow_id: str = typer.Argument(..., help="Workflow ID"),
    params: str = typer.Option(None, "--params", help="Runtime parameters (JSON)"),
) -> None:
    """Run a workflow
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.workflow_run(workflow_id, params)
    print_output(result, ctx.obj.get("output", "table"))