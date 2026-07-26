import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Edge functions")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    device_id: str = typer.Option(None, "--device-id", help="Filter by device"),
) -> None:
    """List edge functions
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.list_edge_functions(device_id)
    data = result if isinstance(result, list) else result.get("functions", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def deploy(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Function name"),
    runtime: str = typer.Argument(..., help="Runtime type (wasm/container/native)"),
    device_id: str = typer.Argument(..., help="Target device"),
    source: str = typer.Argument(..., help="Function source URL"),
    handler: str = typer.Argument(..., help="Entry handler"),
) -> None:
    """Deploy edge function
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.deploy_edge_function(name, runtime, device_id, source, handler)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def invoke(
    ctx: typer.Context,
    func_id: str = typer.Argument(..., help="Function ID"),
    payload: str = typer.Option(None, "--payload", "-p", help="JSON payload"),
) -> None:
    """Invoke edge function
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.invoke_edge_function(func_id, payload)
    print_output(result, ctx.obj.get("output", "table"))