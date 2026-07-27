"""Bridges old CLI commands to the new system so nothing breaks.

This module provides backward compatibility by wrapping the legacy argparse
CLI (cli.py) so that callers can dispatch old-style commands programmatically.
New code should use the Typer-based interface from ipilot.main instead.
"""
import argparse
import sys
import warnings

from .. import __version__
from ..config import load_config
from ..client import ApiClient

_legacy_module = None


def _get_legacy():
    global _legacy_module
    if _legacy_module is None:
        from .. import cli as _legacy_module
    return _legacy_module


def build_legacy_parser():
    leg = _get_legacy()
    return leg.build_parser()


def dispatch_legacy(cmd_name: str, subcmd_name: str = None, **kwargs):
    warnings.warn(
        "bridge.dispatch_legacy() is deprecated. Use the Typer CLI directly via `ipilot`.",
        DeprecationWarning, stacklevel=2,
    )
    leg = _get_legacy()
    parser = leg.build_parser()
    args_list = [cmd_name]
    if subcmd_name:
        args_list.append(subcmd_name)
    for k, v in kwargs.items():
        if isinstance(v, bool):
            if v:
                args_list.append(f"--{k.replace('_', '-')}")
        elif v is not None:
            args_list.append(f"--{k.replace('_', '-')}")
            args_list.append(str(v))
    args = parser.parse_args(args_list)
    leg.main_inner(args)


def get_client():
    """Return an ApiClient using the shared config (bridge-friendly, no Typer context needed)."""
    config = load_config()
    return ApiClient(config.get('api_url', 'http://localhost:8080'), config.get('token'))
