import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Spot instance management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List spot instance advice"""
    client = _get_client(ctx)
    result = client.finops_spot_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Request name"),
    instance_type: str = typer.Argument(help="Instance type"),
    max_price: float = typer.Argument(help="Maximum price"),
    region: str = typer.Argument(help="Region"),
):
    """Create a spot instance request"""
    client = _get_client(ctx)
    result = client.finops_spot_create(name, instance_type, max_price, region)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    request_id: str = typer.Argument(help="Request ID"),
):
    """Get a spot instance request"""
    client = _get_client(ctx)
    result = client.finops_spot_get(request_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def instances(ctx: typer.Context):
    """List spot instances"""
    client = _get_client(ctx)
    result = client.finops_spot_instances()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def savings(ctx: typer.Context):
    """Spot instance savings"""
    client = _get_client(ctx)
    result = client.finops_spot_savings()
    print_output(result, ctx.obj.get("output", "table"))
