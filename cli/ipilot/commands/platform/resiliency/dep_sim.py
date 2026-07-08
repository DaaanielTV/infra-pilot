import typer
from ....output.formatters import print_output

app = typer.Typer(help="Dependency simulation")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List simulations"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Simulation name"),
    config: str = typer.Argument(help="Simulation config"),
):
    """Create"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    simulation_id: str = typer.Argument(help="Simulation ID"),
):
    """Run"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def classify(
    ctx: typer.Context,
    simulation_id: str = typer.Argument(help="Simulation ID"),
):
    """Classify"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def health(
    ctx: typer.Context,
    simulation_id: str = typer.Argument(help="Simulation ID"),
):
    """Health"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    simulation_id: str = typer.Argument(help="Simulation ID"),
):
    """Report"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
