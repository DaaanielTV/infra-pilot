import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Web3 identity")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List Web3 identities"""
    client = _get_client(ctx)
    result = client.web3id_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    alias: str = typer.Argument(help="Identity alias"),
):
    """Create a Web3 identity"""
    client = _get_client(ctx)
    result = client.web3id_create(alias)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def auth(
    ctx: typer.Context,
    identity_id: str = typer.Argument(help="Identity ID"),
    challenge: str = typer.Argument(help="Authentication challenge"),
):
    """Authenticate with Web3 identity"""
    client = _get_client(ctx)
    result = client.web3id_auth(identity_id, challenge)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def sessions(
    ctx: typer.Context,
    identity_id: str = typer.Argument(help="Identity ID"),
):
    """List Web3 identity sessions"""
    client = _get_client(ctx)
    result = client.web3id_sessions(identity_id)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
