import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Cloud compliance")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def status(ctx: typer.Context) -> None:
    """Status
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_status()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def scan(
    ctx: typer.Context,
    target: str = typer.Argument(help="Scan target"),
) -> None:
    """Scan
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_scan(target)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def alerts(ctx: typer.Context) -> None:
    """Alerts
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_alerts()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context) -> None:
    """Summary
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_summary()
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def remediate(
    ctx: typer.Context,
    finding_id: str = typer.Argument(help="Finding ID"),
) -> None:
    """Remediate
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_remediate(finding_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def drift(
    ctx: typer.Context,
    baseline_id: str = typer.Argument(help="Baseline ID"),
) -> None:
    """Drift
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_drift(baseline_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def compare(
    ctx: typer.Context,
    scan_id_a: str = typer.Argument(help="First scan ID"),
    scan_id_b: str = typer.Argument(help="Second scan ID"),
) -> None:
    """Compare
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_compare(scan_id_a, scan_id_b)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def report(
    ctx: typer.Context,
    scan_id: str = typer.Argument(help="Scan ID"),
) -> None:
    """Report
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_report(scan_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def schedule(
    ctx: typer.Context,
    cron: str = typer.Argument(help="Cron expression"),
    target: str = typer.Argument(help="Scan target"),
) -> None:
    """Schedule
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_schedule(cron, target)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def weakest(ctx: typer.Context) -> None:
    """Weakest areas
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cc_weakest()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))