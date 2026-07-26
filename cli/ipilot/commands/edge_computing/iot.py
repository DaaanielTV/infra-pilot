import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="IoT provisioning")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def codes(
    ctx: typer.Context,
    count: int = typer.Option(10, "--count", help="Number of codes"),
    ttl: int = typer.Option(24, "--ttl", help="TTL in hours"),
) -> None:
    """Generate claim codes
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.generate_claim_codes(count, ttl)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def enroll(
    ctx: typer.Context,
    code: str = typer.Argument(..., help="Claim code"),
    device_id: str = typer.Argument(..., help="Device ID"),
) -> None:
    """Enroll device
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.enroll_device(code, device_id)
    print_output(result, ctx.obj.get("output", "table"))