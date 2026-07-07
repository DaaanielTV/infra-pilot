import typer
from ....output.formatters import print_output

app = typer.Typer(help="Resiliency pipeline")


def _get_client(ctx: typer.Context):
    return None


@app.command()
def list(ctx: typer.Context):
    """List resiliency pipelines"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Pipeline name"),
    config: str = typer.Argument(help="Pipeline config"),
):
    """Create a resiliency pipeline"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def trigger(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """Trigger a resiliency pipeline"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def steps(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """List pipeline steps"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def webhooks(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """List pipeline webhooks"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def triggers(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """List pipeline triggers"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))


@app.command()
def analytics(
    ctx: typer.Context,
    pipeline_id: str = typer.Argument(help="Pipeline ID"),
):
    """Get pipeline analytics"""
    print_output({"status": "not implemented"}, ctx.obj.get("output", "table"))
