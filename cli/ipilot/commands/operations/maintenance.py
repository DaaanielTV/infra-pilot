import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Maintenance scheduling")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List scheduled maintenance windows
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.maintenance_list()
    data = result if isinstance(result, list) else result.get("maintenance", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def schedule(
    ctx: typer.Context,
    resource_id: str = typer.Argument(..., help="Resource ID"),
    start_time: str = typer.Argument(..., help="Start time (ISO 8601)"),
    end_time: str = typer.Argument(..., help="End time (ISO 8601)"),
    description: str = typer.Option(None, "--description", help="Maintenance description"),
) -> None:
    """Schedule a maintenance window
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.maintenance_schedule(resource_id, start_time, end_time, description)
    print_output(result, ctx.obj.get("output", "table"))