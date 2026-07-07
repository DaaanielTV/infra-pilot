import builtins
from typing import Any
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Data breach management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List reported breaches"""
    client = _get_client(ctx)
    result = client.breach_list()
    data = result if isinstance(result, _list_type) else result.get("breaches", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    breach_id: str = typer.Argument(..., help="Breach ID"),
    details: str = typer.Option("{}", "--details", "-d", help="JSON details"),
):
    """Report a data breach"""
    client = _get_client(ctx)
    import json
    parsed = json.loads(details)
    result = client.breach_report(breach_id, parsed)
    print_output(result, ctx.obj.get("output", "table"))
