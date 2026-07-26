import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="DNS filter")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def status(ctx: typer.Context) -> None:
    """Show DNS filter status
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.dnsfilter_status()
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def rules(ctx: typer.Context) -> None:
    """List DNS filter rules
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.dnsfilter_rules()
    data = result if isinstance(result, list) else result.get("rules", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def add(
    ctx: typer.Context,
    domain: str = typer.Argument(..., help="Domain to filter"),
    action: str = typer.Option("block", "--action", "-a", help="Action (block, allow)"),
) -> None:
    """Add DNS filter rule
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.dnsfilter_add(domain, action)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def remove(
    ctx: typer.Context,
    rule_id: str = typer.Argument(..., help="Rule ID"),
) -> None:
    """Remove DNS filter rule
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.dnsfilter_remove(rule_id)
    print_output(result, ctx.obj.get("output", "table"))