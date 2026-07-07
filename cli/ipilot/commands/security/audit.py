import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Audit log analysis")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def anomalies(ctx: typer.Context):
    """Detect audit anomalies"""
    client = _get_client(ctx)
    result = client.audit_anomalies()
    data = result if isinstance(result, _list_type) else result.get("anomalies", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def trend(ctx: typer.Context):
    """Show audit activity trends"""
    client = _get_client(ctx)
    result = client.audit_trend()
    data = result if isinstance(result, _list_type) else result.get("trends", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Audit summary statistics"""
    client = _get_client(ctx)
    result = client.audit_summary()
    print_output(result, ctx.obj.get("output", "table"))
