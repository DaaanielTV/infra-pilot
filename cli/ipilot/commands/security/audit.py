import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Audit analysis")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def anomalies(ctx: typer.Context):
    """Anomalies"""
    client = _get_client(ctx)
    result = client.audit_anomalies()
    data = result if isinstance(result, list) else result.get("anomalies", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def trend(ctx: typer.Context):
    """Trends"""
    client = _get_client(ctx)
    result = client.audit_trend()
    data = result if isinstance(result, list) else result.get("trends", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Summary"""
    client = _get_client(ctx)
    result = client.audit_summary()
    print_output(result, ctx.obj.get("output", "table"))
