import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Attestation")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List attestations
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ar_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def generate(
    ctx: typer.Context,
    framework: str = typer.Argument(help="Framework name"),
) -> None:
    """Generate
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ar_generate(framework)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def sign(
    ctx: typer.Context,
    attestation_id: str = typer.Argument(help="Attestation ID"),
) -> None:
    """Sign
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ar_sign(attestation_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def stats(ctx: typer.Context) -> None:
    """Stats
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ar_stats()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def approve(
    ctx: typer.Context,
    attestation_id: str = typer.Argument(help="Attestation ID"),
) -> None:
    """Approve
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ar_approve(attestation_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def verify(
    ctx: typer.Context,
    attestation_id: str = typer.Argument(help="Attestation ID"),
) -> None:
    """Verify
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ar_verify(attestation_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def compare(
    ctx: typer.Context,
    attestation_id_a: str = typer.Argument(help="First attestation ID"),
    attestation_id_b: str = typer.Argument(help="Second attestation ID"),
) -> None:
    """Compare
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ar_compare(attestation_id_a, attestation_id_b)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def schedule(
    ctx: typer.Context,
    cron: str = typer.Argument(help="Cron expression"),
    framework: str = typer.Argument(help="Framework name"),
) -> None:
    """Schedule
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ar_schedule(cron, framework)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def coverage(ctx: typer.Context) -> None:
    """Coverage
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.ar_coverage()
    print_output(result, ctx.obj.get("output", "table"))