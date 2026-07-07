import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Decentralized compute network")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List DCN jobs"""
    client = _get_client(ctx)
    result = client.dcn_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def submit(
    ctx: typer.Context,
    name: str = typer.Argument(help="Job name"),
    workload: str = typer.Argument(help="Workload spec"),
):
    """Submit a DCN job"""
    client = _get_client(ctx)
    result = client.dcn_submit(name, workload)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def status(
    ctx: typer.Context,
    job_id: str = typer.Argument(help="Job ID"),
):
    """Get DCN job status"""
    client = _get_client(ctx)
    result = client.dcn_status(job_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def workers(
    ctx: typer.Context,
    job_id: str = typer.Argument(help="Job ID"),
):
    """List DCN workers"""
    client = _get_client(ctx)
    result = client.dcn_workers(job_id)
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))
