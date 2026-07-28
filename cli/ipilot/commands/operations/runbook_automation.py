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
    params: str = typer.Option(None, "--params", help="Runbook parameters (JSON)"),
) -> None:
    """Execute a runbook template against a resource
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.runbook_use(runbook_id, params)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Runbook name"),
    description: str = typer.Option("", "--description", "-d", help="Runbook description"),
    steps: str = typer.Option(None, "--steps", "-s", help="Steps as JSON array"),
) -> None:
    """Create a new runbook"""
    import json
    client = _get_client(ctx)
    steps_list = json.loads(steps) if steps else [{"action": "notify", "target": "discord"}]
    result = client._post("/runbooks", {"name": name, "description": description, "steps": steps_list})
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def execute(
    ctx: typer.Context,
    runbook_id: str = typer.Argument(..., help="Runbook ID"),
) -> None:
    """Execute a runbook by ID (API-based execution)"""
    client = _get_client(ctx)
    result = client._post(f"/runbooks/{runbook_id}/execute", {})
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def show(
    ctx: typer.Context,
    runbook_id: str = typer.Argument(..., help="Runbook ID"),
) -> None:
    """Show runbook details and steps"""
    client = _get_client(ctx)
    result = client._get(f"/runbooks/{runbook_id}") if not runbook_id.startswith("builtin-") else {"id": runbook_id, "note": "Built-in runbook - use 'ipilot runbook list' to see details"}
    print_output(result, ctx.obj.get("output", "table"))