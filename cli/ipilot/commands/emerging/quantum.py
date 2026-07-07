import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Quantum computing")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List quantum resources"""
    client = _get_client(ctx)
    result = client.quantum_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def generate(
    ctx: typer.Context,
    key_type: str = typer.Argument(help="Key type"),
):
    """Generate quantum-safe keys"""
    client = _get_client(ctx)
    result = client.quantum_generate(key_type)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def cert(
    ctx: typer.Context,
    name: str = typer.Argument(help="Certificate name"),
):
    """Generate a quantum-safe certificate"""
    client = _get_client(ctx)
    result = client.quantum_cert(name)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def encrypt(
    ctx: typer.Context,
    data: str = typer.Argument(help="Data to encrypt"),
    key_id: str = typer.Argument(help="Key ID"),
):
    """Encrypt with quantum-safe algorithm"""
    client = _get_client(ctx)
    result = client.quantum_encrypt(data, key_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def decrypt(
    ctx: typer.Context,
    data: str = typer.Argument(help="Data to decrypt"),
    key_id: str = typer.Argument(help="Key ID"),
):
    """Decrypt with quantum-safe algorithm"""
    client = _get_client(ctx)
    result = client.quantum_decrypt(data, key_id)
    print_output(result, ctx.obj.get("output", "table"))
