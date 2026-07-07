import builtins
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Edge ML management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def models(
    ctx: typer.Context,
    device_id: str = typer.Option(None, "--device-id", help="Filter by device"),
):
    """List ML models"""
    client = _get_client(ctx)
    result = client.list_ml_models(device_id)
    data = result if isinstance(result, _list_type) else result.get("models", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def deploy(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Model name"),
    model_format: str = typer.Argument(..., help="Model format (tflite/onnx/pytorch)"),
    device_id: str = typer.Argument(..., help="Target device"),
    version: str = typer.Argument(..., help="Model version"),
):
    """Deploy ML model"""
    client = _get_client(ctx)
    result = client.deploy_ml_model(name, model_format, device_id, version)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def infer(
    ctx: typer.Context,
    model_id: str = typer.Argument(..., help="Model ID"),
):
    """Run inference"""
    client = _get_client(ctx)
    result = client.run_inference(model_id)
    print_output(result, ctx.obj.get("output", "table"))
