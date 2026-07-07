import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Waste detection")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List waste findings"""
    client = _get_client(ctx)
    result = client.finops_waste_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Waste summary"""
    client = _get_client(ctx)
    result = client.finops_waste_summary()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def scan(ctx: typer.Context):
    """Run a waste scan"""
    client = _get_client(ctx)
    result = client.finops_waste_scan()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def approve(
    ctx: typer.Context,
    waste_id: str = typer.Argument(help="Waste ID"),
):
    """Approve a waste finding"""
    client = _get_client(ctx)
    result = client.finops_waste_approve(waste_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def cleanup(
    ctx: typer.Context,
    waste_id: str = typer.Argument(help="Waste ID"),
):
    """Clean up a waste finding"""
    client = _get_client(ctx)
    result = client.finops_waste_cleanup(waste_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def dismiss(
    ctx: typer.Context,
    waste_id: str = typer.Argument(help="Waste ID"),
):
    """Dismiss a waste finding"""
    client = _get_client(ctx)
    result = client.finops_waste_dismiss(waste_id)
    print_output(result, ctx.obj.get("output", "table"))
