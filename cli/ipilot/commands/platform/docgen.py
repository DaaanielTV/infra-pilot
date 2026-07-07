import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Document generation")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List generated docs"""
    client = _get_client(ctx)
    result = client.docgen_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def generate(
    ctx: typer.Context,
    template: str = typer.Argument(help="Doc template"),
    params: str = typer.Argument(help="Doc params (JSON)"),
):
    """Generate a document"""
    client = _get_client(ctx)
    result = client.docgen_generate(template, params)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    doc_id: str = typer.Argument(help="Doc ID"),
):
    """Get a generated document"""
    client = _get_client(ctx)
    result = client.docgen_get(doc_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Get doc generation summary"""
    client = _get_client(ctx)
    result = client.docgen_summary()
    print_output(result, ctx.obj.get("output", "table"))
