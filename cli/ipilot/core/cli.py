import argparse
import typer
from typing import Optional, Dict, Callable

from ..config import load_config
from ..client import ApiClient


def create_app():
    app = typer.Typer(
        name="ipilot",
        help="Infra Pilot CLI - tool for managing your infrastructure",
        no_args_is_help=True,
        rich_markup_mode="rich",
    )

    @app.callback()
    def main_options(
        ctx: typer.Context,
        output: str = typer.Option(
            None, "--output", "-o",
            help="Output format: json, table, yaml, or plain",
        ),
        profile: str = typer.Option(
            None, "--profile", "-p",
            help="Which config profile to use",
        ),
        no_color: bool = typer.Option(
            False, "--no-color",
            help="Turn off colored output",
        ),
    ):
        ctx.ensure_object(dict)
        ctx.obj["output"] = output or load_config().get("output_format", "table")
        ctx.obj["profile"] = profile
        ctx.obj["no_color"] = no_color

    return app


def get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(
        base_url=config.get("api_url", "http://localhost:8080"),
        token=config.get("token"),
    )


class LegacyBridge:
    def __init__(self):
        self._cmd_map: Dict[str, Callable] = {}
        self._sub_router: Dict[str, Dict[str, Callable]] = {}

    def add_flat(self, name: str, func: Callable):
        self._cmd_map[name] = func

    def add_group(self, name: str, subcommands: Dict[str, Callable]):
        self._sub_router[name] = subcommands

    def dispatch(self, cmd: str, subcmd: Optional[str], args: argparse.Namespace):
        if cmd in self._sub_router and subcmd in self._sub_router[cmd]:
            self._sub_router[cmd][subcmd](args)
        elif cmd in self._cmd_map:
            self._cmd_map[cmd](args)
        else:
            raise typer.Exit(code=1)


legacy_bridge = LegacyBridge()