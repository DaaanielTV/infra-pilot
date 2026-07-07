import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Smart contracts")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List smart contracts"""
    client = _get_client(ctx)
    result = client.contracts_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def deploy(
    ctx: typer.Context,
    name: str = typer.Argument(help="Contract name"),
    source: str = typer.Argument(help="Contract source"),
):
    """Deploy a smart contract"""
    client = _get_client(ctx)
    result = client.contracts_deploy(name, source)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    contract_id: str = typer.Argument(help="Contract ID"),
):
    """Get a smart contract"""
    client = _get_client(ctx)
    result = client.contracts_get(contract_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def events(
    ctx: typer.Context,
    contract_id: str = typer.Argument(help="Contract ID"),
):
    """Get smart contract events"""
    client = _get_client(ctx)
    result = client.contracts_events(contract_id)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
