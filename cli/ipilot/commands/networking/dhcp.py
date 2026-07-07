import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="DHCP management commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def leases(ctx: typer.Context):
    """List DHCP leases"""
    client = _get_client(ctx)
    result = client.dhcp_leases()
    data = result if isinstance(result, _list_type) else result.get("leases", result)
    print_output(data, ctx.obj.get("output", "table"))
