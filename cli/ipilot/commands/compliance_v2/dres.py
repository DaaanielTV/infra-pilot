import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Data residency")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List configs"""
    client = _get_client(ctx)
    result = client.dr_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(help="Configuration name"),
    region: str = typer.Argument(help="Region"),
):
    """Register"""
    client = _get_client(ctx)
    result = client.dr_register(name, region)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def check(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
):
    """Check compliance"""
    client = _get_client(ctx)
    result = client.dr_check(config_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Summary"""
    client = _get_client(ctx)
    result = client.dr_summary()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def flows(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
):
    """Data flows"""
    client = _get_client(ctx)
    result = client.dr_flows(config_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def move(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
    target_region: str = typer.Argument(help="Target region"),
):
    """Move data"""
    client = _get_client(ctx)
    result = client.dr_move(config_id, target_region)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def audit(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
):
    """Audit"""
    client = _get_client(ctx)
    result = client.dr_audit(config_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def violations(ctx: typer.Context):
    """Violations"""
    client = _get_client(ctx)
    result = client.dr_violations()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command("compliance-report")
def compliance_report(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
):
    """Compliance report"""
    client = _get_client(ctx)
    result = client.dr_compliance_report(config_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("asset-search")
def asset_search(
    ctx: typer.Context,
    query: str = typer.Argument(help="Search query"),
):
    """Asset search"""
    client = _get_client(ctx)
    result = client.dr_asset_search(query)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
