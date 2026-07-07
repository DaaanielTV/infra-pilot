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
    """List data residency configurations"""
    client = _get_client(ctx)
    result = client.dr_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def register(
    ctx: typer.Context,
    name: str = typer.Argument(help="Configuration name"),
    region: str = typer.Argument(help="Region"),
):
    """Register a data residency config"""
    client = _get_client(ctx)
    result = client.dr_register(name, region)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def check(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
):
    """Check data residency compliance"""
    client = _get_client(ctx)
    result = client.dr_check(config_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Get data residency summary"""
    client = _get_client(ctx)
    result = client.dr_summary()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def flows(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
):
    """Get data flows"""
    client = _get_client(ctx)
    result = client.dr_flows(config_id)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def move(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
    target_region: str = typer.Argument(help="Target region"),
):
    """Move data to a new region"""
    client = _get_client(ctx)
    result = client.dr_move(config_id, target_region)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def audit(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
):
    """Audit data residency"""
    client = _get_client(ctx)
    result = client.dr_audit(config_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def violations(ctx: typer.Context):
    """List data residency violations"""
    client = _get_client(ctx)
    result = client.dr_violations()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command("compliance-report")
def compliance_report(
    ctx: typer.Context,
    config_id: str = typer.Argument(help="Config ID"),
):
    """Get data residency compliance report"""
    client = _get_client(ctx)
    result = client.dr_compliance_report(config_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("asset-search")
def asset_search(
    ctx: typer.Context,
    query: str = typer.Argument(help="Search query"),
):
    """Search data residency assets"""
    client = _get_client(ctx)
    result = client.dr_asset_search(query)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
