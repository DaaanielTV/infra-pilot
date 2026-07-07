import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="Workflow automation commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List all workflows"""
    client = _get_client(ctx)
    result = client.workflow_list()
    data = result if isinstance(result, _list_type) else result.get("workflows", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Workflow name"),
    definition: str = typer.Argument(..., help="Workflow definition (YAML/JSON)"),
):
    """Create a new workflow"""
    client = _get_client(ctx)
    result = client.workflow_create(name, definition)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    workflow_id: str = typer.Argument(..., help="Workflow ID"),
    params: str = typer.Option(None, "--params", help="Runtime parameters (JSON)"),
):
    """Run a workflow"""
    client = _get_client(ctx)
    result = client.workflow_run(workflow_id, params)
    print_output(result, ctx.obj.get("output", "table"))
