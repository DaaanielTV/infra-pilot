import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Auto-shutdown policies")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def policies(ctx: typer.Context):
    """List shutdown policies"""
    client = _get_client(ctx)
    result = client.shutdown_policies()
    data = result if isinstance(result, _list_type) else result.get("policies", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Policy name"),
    schedule: str = typer.Argument(..., help="Cron schedule"),
    conditions: str = typer.Argument(..., help="Conditions (JSON)"),
):
    """Create shutdown policy"""
    client = _get_client(ctx)
    result = client.create_shutdown_policy(name, schedule, conditions)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def savings(ctx: typer.Context):
    """Show savings from auto-shutdown"""
    client = _get_client(ctx)
    result = client.shutdown_savings()
    print_output(result, ctx.obj.get("output", "table"))
