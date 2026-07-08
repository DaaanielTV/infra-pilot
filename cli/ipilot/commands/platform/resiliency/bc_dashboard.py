import typer
from ....output.formatters import print_output

app = typer.Typer(help="BC dashboard")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def show(ctx: typer.Context):
    """Show dashboard"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def report(ctx: typer.Context):
    """Report"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def scenarios(ctx: typer.Context):
    """Scenarios"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def subscribe(
    ctx: typer.Context,
    email: str = typer.Argument(help="Subscription email"),
):
    """Subscribe"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def simulate(
    ctx: typer.Context,
    scenario: str = typer.Argument(help="Scenario name"),
):
    """Simulate"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
