import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Privileged Access Management (PAM)")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def requests(ctx: typer.Context):
    """List PAM access requests"""
    client = _get_client(ctx)
    result = client.pam_requests()
    data = result if isinstance(result, _list_type) else result.get("requests", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def request(
    ctx: typer.Context,
    resource: str = typer.Argument(..., help="Resource to access"),
    reason: str = typer.Argument(..., help="Reason for access"),
):
    """Request privileged access"""
    client = _get_client(ctx)
    result = client.pam_request(resource, reason)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def approve(
    ctx: typer.Context,
    request_id: str = typer.Argument(..., help="PAM request ID"),
):
    """Approve a PAM request"""
    client = _get_client(ctx)
    result = client.pam_approve(request_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def deny(
    ctx: typer.Context,
    request_id: str = typer.Argument(..., help="PAM request ID"),
):
    """Deny a PAM request"""
    client = _get_client(ctx)
    result = client.pam_deny(request_id)
    print_output(result, ctx.obj.get("output", "table"))
