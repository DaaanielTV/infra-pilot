import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Green scheduling")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def forecast(ctx: typer.Context) -> None:
    """Green energy forecast
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.green_forecast()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def jobs(ctx: typer.Context) -> None:
    """List green jobs
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.green_jobs()
    data = result if isinstance(result, list) else result.get("jobs", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def schedule(
    ctx: typer.Context,
    workload_id: str = typer.Argument(..., help="Workload ID"),
    schedule_type: str = typer.Argument(..., help="Schedule type"),
) -> None:
    """Schedule workload for green window
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.green_schedule(workload_id, schedule_type)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def report(ctx: typer.Context) -> None:
    """Green computing report
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.green_report()
    print_output(result, ctx.obj.get("output", "table"))