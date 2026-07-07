import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="DNS filtering management commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def status(ctx: typer.Context):
    """Show DNS filter status"""
    client = _get_client(ctx)
    result = client.dnsfilter_status()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def rules(ctx: typer.Context):
    """List DNS filter rules"""
    client = _get_client(ctx)
    result = client.dnsfilter_rules()
    data = result if isinstance(result, _list_type) else result.get("rules", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def add(
    ctx: typer.Context,
    domain: str = typer.Argument(..., help="Domain to filter"),
    action: str = typer.Option("block", "--action", "-a", help="Filter action (block, allow)"),
):
    """Add a DNS filter rule"""
    client = _get_client(ctx)
    result = client.dnsfilter_add(domain, action)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def remove(
    ctx: typer.Context,
    rule_id: str = typer.Argument(..., help="Rule ID"),
):
    """Remove a DNS filter rule"""
    client = _get_client(ctx)
    result = client.dnsfilter_remove(rule_id)
    print_output(result, ctx.obj.get("output", "table"))
