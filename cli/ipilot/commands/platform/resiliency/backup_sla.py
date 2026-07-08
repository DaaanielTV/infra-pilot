import typer
from ....output.formatters import print_output

app = typer.Typer(help="Backup SLA")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List SLAs"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="SLA name"),
    rto: str = typer.Argument(help="Recovery time objective"),
    rpo: str = typer.Argument(help="Recovery point objective"),
):
    """Create"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def verify(
    ctx: typer.Context,
    sla_id: str = typer.Argument(help="SLA ID"),
):
    """Verify"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    sla_id: str = typer.Argument(help="SLA ID"),
):
    """Report"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def policy(
    ctx: typer.Context,
    sla_id: str = typer.Argument(help="SLA ID"),
):
    """Policy"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def storage(
    ctx: typer.Context,
    sla_id: str = typer.Argument(help="SLA ID"),
):
    """Storage"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
