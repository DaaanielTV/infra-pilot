import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Scaffolding")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List scaffolds"""
    client = _get_client(ctx)
    result = client.scaffold_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def generate(
    ctx: typer.Context,
    template: str = typer.Argument(help="Template name"),
    name: str = typer.Argument(help="Project name"),
):
    """Generate a scaffold"""
    client = _get_client(ctx)
    result = client.scaffold_generate(template, name)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    scaffold_id: str = typer.Argument(help="Scaffold ID"),
):
    """Get scaffold status"""
    client = _get_client(ctx)
    result = client.scaffold_status(scaffold_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command("step")
def step_command(
    ctx: typer.Context,
    scaffold_id: str = typer.Argument(help="Scaffold ID"),
    step_name: str = typer.Argument(help="Step name"),
):
    """Execute a scaffold step"""
    client = _get_client(ctx)
    result = client.scaffold_step(scaffold_id, step_name)
    print_output(result, ctx.obj.get("output", "table"))
