import typer
from ....output.formatters import print_output

app = typer.Typer(help="BC dashboard")


def _get_client(ctx: typer.Context) -> ApiClient:
    return None


@app.command()
def show(ctx: typer.Context) -> None:
    """Show dashboard
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def report(ctx: typer.Context) -> None:
    """Report
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def scenarios(ctx: typer.Context) -> None:
    """Scenarios
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def subscribe(
    ctx: typer.Context,
    email: str = typer.Argument(help="Subscription email"),
) -> None:
    """Subscribe
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def simulate(
    ctx: typer.Context,
    scenario: str = typer.Argument(help="Scenario name"),
) -> None:
    """Simulate
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))