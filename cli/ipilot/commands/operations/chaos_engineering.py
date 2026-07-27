import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Chaos engineering")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def experiments(ctx: typer.Context) -> None:
    """List chaos experiments
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.chaos_experiments()
    data = result if isinstance(result, list) else result.get("experiments", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Experiment name"),
    target: str = typer.Argument(..., help="Target resource"),
    fault_type: str = typer.Argument(..., help="Type of fault to inject"),
) -> None:
    """Create a new chaos experiment
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.chaos_create(name, target, fault_type)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(..., help="Experiment ID"),
) -> None:
    """Run a chaos experiment
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.chaos_run(experiment_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def stop(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(..., help="Experiment ID"),
) -> None:
    """Stop a running chaos experiment
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.chaos_stop(experiment_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def faults(ctx: typer.Context) -> None:
    """List available fault types
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.chaos_faults()
    data = result if isinstance(result, list) else result.get("faults", result)
    print_output(data, ctx.obj.get("output", "table"))