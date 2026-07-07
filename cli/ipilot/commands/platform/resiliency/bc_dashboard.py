import typer
from ....output.formatters import print_output

app = typer.Typer(help="Business continuity dashboard")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def show(ctx: typer.Context):
    """Show business continuity dashboard"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def report(ctx: typer.Context):
    """Get business continuity report"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def scenarios(ctx: typer.Context):
    """List business continuity scenarios"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def subscribe(
    ctx: typer.Context,
    email: str = typer.Argument(help="Subscription email"),
):
    """Subscribe to BC dashboard updates"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def simulate(
    ctx: typer.Context,
    scenario: str = typer.Argument(help="Scenario name"),
):
    """Run a business continuity simulation"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
