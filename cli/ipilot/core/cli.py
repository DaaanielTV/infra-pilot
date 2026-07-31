"""Core CLI utilities: app creation, config loading, and the legacy bridge."""

import argparse
import logging
from typing import Callable, Dict, Optional

import typer

from ..client import ApiClient
from ..config import load_config

logger = logging.getLogger(__name__)

DEFAULT_API_URL = "http://localhost:8080"


def create_app() -> typer.Typer:
    """Create and configure the main Typer CLI application.

    Returns:
        A configured Typer app instance.
    """
    app = typer.Typer(
        name="ipilot",
        help="Infra Pilot CLI - tool for managing your infrastructure",
        no_args_is_help=True,
        rich_markup_mode="rich",
    )

    @app.callback()
    def main_options(
        ctx: typer.Context,
        output: Optional[str] = typer.Option(
            None,
            "--output",
            "-o",
            help="Output format: json, table, yaml, or plain",
        ),
        profile: Optional[str] = typer.Option(
            None,
            "--profile",
            "-p",
            help="Which config profile to use",
        ),
        no_color: bool = typer.Option(
            False,
            "--no-color",
            help="Turn off colored output",
        ),
    ):
        ctx.ensure_object(dict)
        config = load_config()
        ctx.obj["output"] = output or config.get("output_format", "table")
        ctx.obj["profile"] = profile
        ctx.obj["no_color"] = no_color

    return app


def get_client(ctx: typer.Context) -> ApiClient:
    """Build an ApiClient from the current Typer context.

    Args:
        ctx: The current Typer context (must have a ``profile`` key).

    Returns:
        An initialized ApiClient instance.
    """
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(
        base_url=config.get("api_url", DEFAULT_API_URL),
        token=config.get("token"),
    )


class LegacyBridge:
    """Bridges old-style argparse command handlers with the new Typer app.

    Allows gradual migration by dispatching flat and grouped commands
    through Typer's exit mechanism.
    """

    def __init__(self):
        self._cmd_map: Dict[str, Callable] = {}
        self._sub_router: Dict[str, Dict[str, Callable]] = {}

    def add_flat(self, name: str, func: Callable):
        """Register a flat (non-grouped) command handler.

        Args:
            name: The command name.
            func: The callable to invoke.
        """
        self._cmd_map[name] = func

    def add_group(self, name: str, subcommands: Dict[str, Callable]):
        """Register a command group with sub-command handlers.

        Args:
            name: The group name.
            subcommands: Mapping of sub-command name to callable.
        """
        self._sub_router[name] = subcommands

    def dispatch(self, cmd: str, subcmd: Optional[str], args: argparse.Namespace):
        """Dispatch a command to its registered handler.

        Args:
            cmd: The top-level command name.
            subcmd: An optional sub-command name.
            args: Parsed command-line arguments.

        Raises:
            typer.Exit: When no handler is found (exit code 1).
        """
        if cmd in self._sub_router and subcmd in self._sub_router[cmd]:
            self._sub_router[cmd][subcmd](args)
        elif cmd in self._cmd_map:
            self._cmd_map[cmd](args)
        else:
            logger.error("No handler found for command: %s (subcmd: %s)", cmd, subcmd)
            raise typer.Exit(code=1)


legacy_bridge = LegacyBridge()

__all__ = [
    "create_app",
    "get_client",
    "LegacyBridge",
    "legacy_bridge",
]
