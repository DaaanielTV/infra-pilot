import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Zero-knowledge proofs")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List ZK proofs"""
    client = _get_client(ctx)
    result = client.zkp_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def generate(
    ctx: typer.Context,
    circuit_id: str = typer.Argument(help="Circuit ID"),
    inputs: str = typer.Argument(help="Inputs (JSON)"),
):
    """Generate a ZK proof"""
    client = _get_client(ctx)
    result = client.zkp_generate(circuit_id, inputs)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def verify(
    ctx: typer.Context,
    proof_id: str = typer.Argument(help="Proof ID"),
):
    """Verify a ZK proof"""
    client = _get_client(ctx)
    result = client.zkp_verify(proof_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def circuits(ctx: typer.Context):
    """List ZK circuits"""
    client = _get_client(ctx)
    result = client.zkp_circuits()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
