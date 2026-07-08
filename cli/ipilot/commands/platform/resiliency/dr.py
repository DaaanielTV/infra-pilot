import typer
from ....output.formatters import print_output

app = typer.Typer(help="Disaster recovery")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List plans"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Plan name"),
    config: str = typer.Argument(help="Plan config"),
):
    """Create"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    plan_id: str = typer.Argument(help="Plan ID"),
):
    """Status"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def failover(
    ctx: typer.Context,
    plan_id: str = typer.Argument(help="Plan ID"),
):
    """Failover"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def readiness(ctx: typer.Context):
    """Readiness"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def delete(
    ctx: typer.Context,
    plan_id: str = typer.Argument(help="Plan ID"),
):
    """Delete"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def scenarios(
    ctx: typer.Context,
    plan_id: str = typer.Argument(help="Plan ID"),
):
    """Scenarios"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def versions(
    ctx: typer.Context,
    plan_id: str = typer.Argument(help="Plan ID"),
):
    """Versions"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def notifications(
    ctx: typer.Context,
    plan_id: str = typer.Argument(help="Plan ID"),
):
    """Notifications"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def compliance(
    ctx: typer.Context,
    plan_id: str = typer.Argument(help="Plan ID"),
):
    """Compliance"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
