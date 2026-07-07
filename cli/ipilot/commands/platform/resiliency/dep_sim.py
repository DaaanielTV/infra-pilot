import typer
from ....output.formatters import print_output

app = typer.Typer(help="Dependency simulation")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List dependency simulations"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Simulation name"),
    config: str = typer.Argument(help="Simulation config"),
):
    """Create a dependency simulation"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    simulation_id: str = typer.Argument(help="Simulation ID"),
):
    """Run a dependency simulation"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def classify(
    ctx: typer.Context,
    simulation_id: str = typer.Argument(help="Simulation ID"),
):
    """Classify dependencies"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def health(
    ctx: typer.Context,
    simulation_id: str = typer.Argument(help="Simulation ID"),
):
    """Get dependency health"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    simulation_id: str = typer.Argument(help="Simulation ID"),
):
    """Get dependency simulation report"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
