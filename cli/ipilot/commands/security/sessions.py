import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Session management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List active sessions"""
    client = _get_client(ctx)
    result = client.list_sessions()
    data = result if isinstance(result, _list_type) else result.get("sessions", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@app.command()
def revoke(
    ctx: typer.Context,
    session_id: str = typer.Argument(..., help="Session ID"),
):
    """Revoke a session"""
    client = _get_client(ctx)
    result = client.revoke_session(session_id)
    print_output(result, ctx.obj.get("output", "table"))
