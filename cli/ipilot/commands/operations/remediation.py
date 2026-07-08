import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Auto-remediation")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def rules(ctx: typer.Context):
    """List remediation rules"""
    client = _get_client(ctx)
    result = client.remediate_rules()
    data = result if isinstance(result, list) else result.get("rules", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def history(ctx: typer.Context):
    """Show remediation history"""
    client = _get_client(ctx)
    result = client.remediate_history()
    data = result if isinstance(result, list) else result.get("history", result)
    print_output(data, ctx.obj.get("output", "table"))