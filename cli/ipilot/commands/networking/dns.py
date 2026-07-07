import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list

app = typer.Typer(help="DNS management commands")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def zones(ctx: typer.Context):
    """List DNS zones"""
    client = _get_client(ctx)
    result = client.dns_zones()
    data = result if isinstance(result, _list_type) else result.get("zones", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create_zone(
    ctx: typer.Context,
    domain: str = typer.Argument(..., help="Domain name"),
    ttl: int = typer.Option(3600, "--ttl", help="TTL in seconds"),
):
    """Create a new DNS zone"""
    client = _get_client(ctx)
    result = client.dns_create_zone(domain, ttl)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete_zone(
    ctx: typer.Context,
    zone_id: str = typer.Argument(..., help="Zone ID"),
):
    """Delete a DNS zone"""
    client = _get_client(ctx)
    result = client.dns_delete_zone(zone_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def records(
    ctx: typer.Context,
    zone_id: str = typer.Argument(..., help="Zone ID"),
):
    """List DNS records for a zone"""
    client = _get_client(ctx)
    result = client.dns_records(zone_id)
    data = result if isinstance(result, _list_type) else result.get("records", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def add_record(
    ctx: typer.Context,
    zone_id: str = typer.Argument(..., help="Zone ID"),
    record_type: str = typer.Argument(..., help="Record type (A, AAAA, CNAME, MX, etc.)"),
    name: str = typer.Argument(..., help="Record name"),
    value: str = typer.Argument(..., help="Record value"),
    ttl: int = typer.Option(300, "--ttl", help="TTL in seconds"),
):
    """Add a DNS record to a zone"""
    client = _get_client(ctx)
    result = client.dns_add_record(zone_id, record_type, name, value, ttl)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def delete_record(
    ctx: typer.Context,
    zone_id: str = typer.Argument(..., help="Zone ID"),
    record_id: str = typer.Argument(..., help="Record ID"),
):
    """Delete a DNS record from a zone"""
    client = _get_client(ctx)
    result = client.dns_delete_record(zone_id, record_id)
    print_output(result, ctx.obj.get("output", "table"))
