import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Web3 identity")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List identities
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.web3id_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    alias: str = typer.Argument(help="Identity alias"),
) -> None:
    """Create
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.web3id_create(alias)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def auth(
    ctx: typer.Context,
    identity_id: str = typer.Argument(help="Identity ID"),
    challenge: str = typer.Argument(help="Authentication challenge"),
) -> None:
    """Authenticate
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.web3id_auth(identity_id, challenge)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def sessions(
    ctx: typer.Context,
    identity_id: str = typer.Argument(help="Identity ID"),
) -> None:
    """Sessions
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.web3id_sessions(identity_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))