import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Vulnerability and compliance management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List vendors"""
    client = _get_client(ctx)
    result = client.vc_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(help="Vendor name"),
    tier: str = typer.Argument(help="Vendor tier"),
):
    """Register a vendor"""
    client = _get_client(ctx)
    result = client.vc_register(name, tier)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def assess(
    ctx: typer.Context,
    vendor_id: str = typer.Argument(help="Vendor ID"),
):
    """Assess a vendor"""
    client = _get_client(ctx)
    result = client.vc_assess(vendor_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def risk(
    ctx: typer.Context,
    vendor_id: str = typer.Argument(help="Vendor ID"),
):
    """Get vendor risk score"""
    client = _get_client(ctx)
    result = client.vc_risk(vendor_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def scorecard(
    ctx: typer.Context,
    vendor_id: str = typer.Argument(help="Vendor ID"),
):
    """Get vendor scorecard"""
    client = _get_client(ctx)
    result = client.vc_scorecard(vendor_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def assessments(ctx: typer.Context):
    """List all vendor assessments"""
    client = _get_client(ctx)
    result = client.vc_assessments()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command("migrate-tier")
def migrate_tier(
    ctx: typer.Context,
    vendor_id: str = typer.Argument(help="Vendor ID"),
    new_tier: str = typer.Argument(help="New tier"),
):
    """Migrate vendor tier"""
    client = _get_client(ctx)
    result = client.vc_migrate_tier(vendor_id, new_tier)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def categories(ctx: typer.Context):
    """List vendor categories"""
    client = _get_client(ctx)
    result = client.vc_categories()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def discover(ctx: typer.Context):
    """Discover vendors"""
    client = _get_client(ctx)
    result = client.vc_discover()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def remediation(
    ctx: typer.Context,
    vendor_id: str = typer.Argument(help="Vendor ID"),
):
    """Get vendor remediation plan"""
    client = _get_client(ctx)
    result = client.vc_remediation(vendor_id)
    print_output(result, ctx.obj.get("output", "table"))
