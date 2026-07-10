"""Bridges old CLI commands to the new system so nothing breaks."""
# TODO: remove this bridge when everyone migrates to new cli
# NOTE: this is a hack to keep backward compatability
import argparse
import sys

from .. import __version__
from ..config import load_config, save_config, set_key, get as config_get
from ..client import ApiClient
from ..output.formatters import print_output

_legacy_module = None


# HACK: lazy import cuz circular dependancy issues
def _get_legacy():
    global _legacy_module
    if _legacy_module is None:
        from .. import cli as _legacy_module
    return _legacy_module


def build_legacy_parser():
    leg = _get_legacy()
    return leg.build_parser()


# FIXME: this function doesnt handle all arg types properly
def dispatch_legacy(cmd_name: str, subcmd_name: str = None, **kwargs):
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


# NOTE: duplicate of core.cli.get_client() - why does this exist???
def get_client():
    config = load_config()
    return ApiClient(config.get('api_url', 'http://localhost:8080'), config.get('token'))