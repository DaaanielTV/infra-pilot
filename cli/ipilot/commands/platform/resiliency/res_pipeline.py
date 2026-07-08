import typer
from ....output.formatters import print_output

app = typer.Typer(help="Resiliency pipeline")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List pipelines"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Pipeline name"),
    config: str = typer.Argument(help="Pipeline config"),
):
    """Create"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def trigger(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """Trigger"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def steps(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """Steps"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def webhooks(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """Webhooks"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def triggers(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """Triggers"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def analytics(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """Analytics"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
