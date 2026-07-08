import typer
from ....output.formatters import print_output

app = typer.Typer(help="Chaos experiments")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List experiments"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Experiment name"),
    config: str = typer.Argument(help="Experiment config"),
):
    """Create"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Run"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def approve(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Approve"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def results(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Results"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command("blast-radius")
def blast_radius(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Blast radius"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def metrics(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Metrics"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def notifications(
    ctx: typer.Context,
    experiment_id: str = typer.Argument(help="Experiment ID"),
):
    """Notifications"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
