import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Cost anomaly detection")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List cost anomalies"""
    client = _get_client(ctx)
    result = client.finops_anomaly_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Anomaly summary"""
    client = _get_client(ctx)
    result = client.finops_anomaly_summary()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def investigate(
    ctx: typer.Context,
    anomaly_id: str = typer.Argument(help="Anomaly ID"),
):
    """Investigate a cost anomaly"""
    client = _get_client(ctx)
    result = client.finops_anomaly_investigate(anomaly_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def resolve(
    ctx: typer.Context,
    anomaly_id: str = typer.Argument(help="Anomaly ID"),
):
    """Resolve a cost anomaly"""
    client = _get_client(ctx)
    result = client.finops_anomaly_resolve(anomaly_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def profiles(ctx: typer.Context):
    """List anomaly detection profiles"""
    client = _get_client(ctx)
    result = client.finops_anomaly_profiles()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command(name="create-profile")
def create_profile(
    ctx: typer.Context,
    name: str = typer.Argument(help="Profile name"),
    rules: str = typer.Argument(help="Profile rules (JSON)"),
):
    """Create an anomaly detection profile"""
    client = _get_client(ctx)
    result = client.finops_anomaly_create_profile(name, rules)
    print_output(result, ctx.obj.get("output", "table"))
