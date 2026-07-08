import typer
from ....output.formatters import print_output

app = typer.Typer(help="Data integrity")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List checks"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Check name"),
    target: str = typer.Argument(help="Check target"),
):
    """Create"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def run(
    ctx: typer.Context,
    check_id: str = typer.Argument(help="Check ID"),
):
    """Run"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def schedule(
    ctx: typer.Context,
    check_id: str = typer.Argument(help="Check ID"),
    cron: str = typer.Argument(help="Cron expression"),
):
    """Schedule"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def alerts(
    ctx: typer.Context,
    check_id: str = typer.Argument(help="Check ID"),
):
    """Alerts"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def health(ctx: typer.Context):
    """Health"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def audit(
    ctx: typer.Context,
    check_id: str = typer.Argument(help="Check ID"),
):
    """Audit"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
