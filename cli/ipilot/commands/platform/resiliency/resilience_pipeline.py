import typer
from ....client import ApiClient
from ....output.formatters import print_output

app = typer.Typer(help="Resiliency pipeline")


def _get_client(ctx: typer.Context) -> ApiClient:
    return None


@app.command()
def list(ctx: typer.Context) -> None:
    """List pipelines
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Pipeline name"),
    config: str = typer.Argument(help="Pipeline config"),
) -> None:
    """Create
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def trigger(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
) -> None:
    """Trigger
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def steps(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
) -> None:
    """Steps
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def webhooks(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
) -> None:
    """Webhooks
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def triggers(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
) -> None:
    """Triggers
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def analytics(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
) -> None:
    """Analytics
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
