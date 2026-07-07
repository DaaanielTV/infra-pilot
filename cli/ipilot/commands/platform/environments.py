import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Environment management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List environments"""
    client = _get_client(ctx)
    result = client.environments_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Environment name"),
    env_type: str = typer.Argument(help="Environment type"),
):
    """Create an environment"""
    client = _get_client(ctx)
    result = client.environments_create(name, env_type)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    env_id: str = typer.Argument(help="Environment ID"),
):
    """Get an environment"""
    client = _get_client(ctx)
    result = client.environments_get(env_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete(
    ctx: typer.Context,
    env_id: str = typer.Argument(help="Environment ID"),
):
    """Delete an environment"""
    client = _get_client(ctx)
    result = client.environments_delete(env_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def extend(
    ctx: typer.Context,
    env_id: str = typer.Argument(help="Environment ID"),
    extensions: str = typer.Argument(help="Extensions (JSON)"),
):
    """Extend an environment"""
    client = _get_client(ctx)
    result = client.environments_extend(env_id, extensions)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Get environment summary"""
    client = _get_client(ctx)
    result = client.environments_summary()
    print_output(result, ctx.obj.get("output", "table"))
