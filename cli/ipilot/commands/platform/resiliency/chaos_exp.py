import typer
from ....output.formatters import print_output

app = typer.Typer(help="Chaos experiments")


def _get_client(ctx: typer.Context) -> ApiClient:
    return None


@app.command()
def list(ctx: typer.Context) -> None:
    """List experiments
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Experiment name"),
    config: str = typer.Argument(help="Experiment config"),
) -> None:
    """Create
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
) -> None:
    """Run
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def approve(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
) -> None:
    """Approve
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def results(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
) -> None:
    """Results
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command("blast-radius")
def blast_radius(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
) -> None:
    """Blast radius
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def metrics(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
) -> None:
    """Metrics
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def notifications(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
) -> None:
    """Notifications
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))