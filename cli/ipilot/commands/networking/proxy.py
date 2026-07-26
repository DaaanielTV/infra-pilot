import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Proxy commands")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def rules(ctx: typer.Context) -> None:
    """List proxy rules
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.proxy_rules()
    data = result if isinstance(result, list) else result.get("rules", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Rule name"),
    source: str = typer.Argument(..., help="Source pattern"),
    target: str = typer.Argument(..., help="Target URL"),
) -> None:
    """Create proxy rule
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.proxy_create(name, source, target)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def delete(
    ctx: typer.Context,
    rule_id: str = typer.Argument(..., help="Rule ID"),
) -> None:
    """Delete proxy rule
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.proxy_delete(rule_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def toggle(
    ctx: typer.Context,
    rule_id: str = typer.Argument(..., help="Rule ID"),
) -> None:
    """Toggle proxy rule
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.proxy_toggle(rule_id)
    print_output(result, ctx.obj.get("output", "table"))