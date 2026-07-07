import typer
from ....output.formatters import print_output

app = typer.Typer(help="Resiliency scoring")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def score(
    ctx: typer.Context,
    target_id: str = typer.Argument(help="Target ID"),
):
    """Get resiliency score"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def list(ctx: typer.Context):
    """List resiliency scores"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Get resiliency score summary"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def alerts(ctx: typer.Context):
    """Get resiliency score alerts"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def trend(ctx: typer.Context):
    """Get resiliency score trend"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def forecast(ctx: typer.Context):
    """Get resiliency score forecast"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command("export")
def export_score(
    ctx: typer.Context,
    format: str = typer.Argument(help="Export format"),
):
    """Export resiliency scores"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
