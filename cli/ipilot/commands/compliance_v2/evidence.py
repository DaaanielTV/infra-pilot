import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Evidence collection")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List evidence"""
    client = _get_client(ctx)
    result = client.ec_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def collect(
    ctx: typer.Context,
    source: str = typer.Argument(help="Evidence source"),
):
    """Collect"""
    client = _get_client(ctx)
    result = client.ec_collect(source)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def packages(ctx: typer.Context):
    """Packages"""
    client = _get_client(ctx)
    result = client.ec_packages()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context):
    """Stats"""
    client = _get_client(ctx)
    result = client.ec_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command("auto-collect")
def auto_collect(ctx: typer.Context):
    """Auto collect"""
    client = _get_client(ctx)
    result = client.ec_auto_collect()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def search(
    ctx: typer.Context,
    query: str = typer.Argument(help="Search query"),
):
    """Search"""
    client = _get_client(ctx)
    result = client.ec_search(query)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def validate(
    ctx: typer.Context,
    evidence_id: str = typer.Argument(help="Evidence ID"),
):
    """Validate"""
    client = _get_client(ctx)
    result = client.ec_validate(evidence_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("package-create")
def package_create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Package name"),
    evidence_ids: str = typer.Argument(help="Evidence IDs (JSON)"),
):
    """Create package"""
    client = _get_client(ctx)
    result = client.ec_package_create(name, evidence_ids)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def expired(ctx: typer.Context):
    """Expired evidence"""
    client = _get_client(ctx)
    result = client.ec_expired()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def custody(
    ctx: typer.Context,
    evidence_id: str = typer.Argument(help="Evidence ID"),
):
    """Custody chain"""
    client = _get_client(ctx)
    result = client.ec_custody(evidence_id)
    print_output(result, ctx.obj.get("output", "table"))
