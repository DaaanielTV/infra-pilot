import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Quantum computing")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List resources
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.quantum_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def generate(
    ctx: typer.Context,
    key_type: str = typer.Argument(help="Key type"),
) -> None:
    """Generate keys
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.quantum_generate(key_type)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def cert(
    ctx: typer.Context,
    name: str = typer.Argument(help="Certificate name"),
) -> None:
    """Certificate
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.quantum_cert(name)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def encrypt(
    ctx: typer.Context,
    data: str = typer.Argument(help="Data to encrypt"),
    key_id: str = typer.Argument(help="Key ID"),
) -> None:
    """Encrypt
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.quantum_encrypt(data, key_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def decrypt(
    ctx: typer.Context,
    data: str = typer.Argument(help="Data to decrypt"),
    key_id: str = typer.Argument(help="Key ID"),
) -> None:
    """Decrypt
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.quantum_decrypt(data, key_id)
    print_output(result, ctx.obj.get("output", "table"))