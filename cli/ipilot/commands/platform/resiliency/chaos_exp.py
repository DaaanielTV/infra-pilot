import typer
from ....output.formatters import print_output

app = typer.Typer(help="Chaos engineering experiments")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List chaos experiments"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Experiment name"),
    config: str = typer.Argument(help="Experiment config"),
):
    """Create a chaos experiment"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Run a chaos experiment"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def approve(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Approve a chaos experiment"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def results(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Get chaos experiment results"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command("blast-radius")
def blast_radius(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Get blast radius analysis"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def metrics(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Get chaos experiment metrics"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def notifications(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Get chaos experiment notifications"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
