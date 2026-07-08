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
    """Score"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def list(ctx: typer.Context):
    """List scores"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Summary"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def alerts(ctx: typer.Context):
    """Alerts"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def trend(ctx: typer.Context):
    """Trend"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def forecast(ctx: typer.Context):
    """Forecast"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command("export")
def export_score(
    ctx: typer.Context,
    format: str = typer.Argument(help="Export format"),
):
    """Export"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
