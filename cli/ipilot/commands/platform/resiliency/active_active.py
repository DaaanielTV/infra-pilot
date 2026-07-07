import typer
from ....output.formatters import print_output

app = typer.Typer(help="Active-active configuration")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def regions(ctx: typer.Context):
    """List active-active regions"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(help="Region name"),
    endpoint: str = typer.Argument(help="Region endpoint"),
):
    """Register an active-active region"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    region_id: str = typer.Argument(help="Region ID"),
):
    """Get active-active region status"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def health(ctx: typer.Context):
    """Get active-active health"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def weight(
    ctx: typer.Context,
    region_id: str = typer.Argument(help="Region ID"),
    weight: int = typer.Argument(help="Traffic weight"),
):
    """Set active-active region weight"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def replication(
    ctx: typer.Context,
    region_id: str = typer.Argument(help="Region ID"),
):
    """Get replication status"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def capacity(
    ctx: typer.Context,
    region_id: str = typer.Argument(help="Region ID"),
):
    """Get region capacity"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def availability(ctx: typer.Context):
    """Get active-active availability"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
