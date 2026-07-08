import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Control automation")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List controls"""
    client = _get_client(ctx)
    result = client.cac_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def evaluate(
    ctx: typer.Context,
    control_id: str = typer.Argument(help="Control ID"),
):
    """Evaluate"""
    client = _get_client(ctx)
    result = client.cac_evaluate(control_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def templates(ctx: typer.Context):
    """Templates"""
    client = _get_client(ctx)
    result = client.cac_templates()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Stats"""
    client = _get_client(ctx)
    result = client.cac_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Control name"),
    definition: str = typer.Argument(help="Control definition"),
):
    """Create"""
    client = _get_client(ctx)
    result = client.cac_create(name, definition)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def gap(
    ctx: typer.Context,
    framework: str = typer.Argument(help="Framework name"),
):
    """Gap analysis"""
    client = _get_client(ctx)
    result = client.cac_gap(framework)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def test(
    ctx: typer.Context,
    control_id: str = typer.Argument(help="Control ID"),
):
    """Test"""
    client = _get_client(ctx)
    result = client.cac_test(control_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("dry-run")
def dry_run(
    ctx: typer.Context,
    control_id: str = typer.Argument(help="Control ID"),
):
    """Dry run"""
    client = _get_client(ctx)
    result = client.cac_dry_run(control_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def version(
    ctx: typer.Context,
    control_id: str = typer.Argument(help="Control ID"),
):
    """Version history"""
    client = _get_client(ctx)
    result = client.cac_version(control_id)
    print_output(result, ctx.obj.get("output", "table"))
