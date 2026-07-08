import typer
from ....output.formatters import print_output

app = typer.Typer(help="Runbook execution")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List runbooks"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Runbook name"),
    steps: str = typer.Argument(help="Runbook steps (JSON)"),
):
    """Create"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def execute(
    ctx: typer.Context,
    runbook_id: str = typer.Argument(help="Runbook ID"),
):
    """Execute"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def templates(ctx: typer.Context):
    """Templates"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def audit(
    ctx: typer.Context,
    runbook_id: str = typer.Argument(help="Runbook ID"),
):
    """Audit"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def versions(
    ctx: typer.Context,
    runbook_id: str = typer.Argument(help="Runbook ID"),
):
    """Versions"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def approve(
    ctx: typer.Context,
    runbook_id: str = typer.Argument(help="Runbook ID"),
):
    """Approve"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
