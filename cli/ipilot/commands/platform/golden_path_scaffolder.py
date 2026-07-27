import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Scaffolding")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List scaffolds
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.scaffold_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def generate(
    ctx: typer.Context,
    template: str = typer.Argument(help="Template name"),
    name: str = typer.Argument(help="Project name"),
) -> None:
    """Generate
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.scaffold_generate(template, name)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    scaffold_id: str = typer.Argument(help="Scaffold ID"),
) -> None:
    """Status
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.scaffold_status(scaffold_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("step")
def step_command(
    ctx: typer.Context,
    scaffold_id: str = typer.Argument(help="Scaffold ID"),
    step_name: str = typer.Argument(help="Step name"),
) -> None:
    """Step
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.scaffold_step(scaffold_id, step_name)
    print_output(result, ctx.obj.get("output", "table"))