import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Template registry")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List templates
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.templatereg_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Template name"),
    content: str = typer.Argument(help="Template content"),
) -> None:
    """Create
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.templatereg_create(name, content)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    template_id: str = typer.Argument(help="Template ID"),
) -> None:
    """Get template
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.templatereg_get(template_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("use")
def use_template(
    ctx: typer.Context,
    template_id: str = typer.Argument(help="Template ID"),
    params: str = typer.Argument(help="Template params"),
) -> None:
    """Use
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.templatereg_use(template_id, params)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context) -> None:
    """Summary
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.templatereg_summary()
    print_output(result, ctx.obj.get("output", "table"))