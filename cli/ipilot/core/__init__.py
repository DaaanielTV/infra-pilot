"""Core CLI utilities."""

from .cli import create_app, get_client, LegacyBridge, legacy_bridge
from .command_registry import register, discover_commands, attach_to_app, get_registry
from .exceptions import (
    CLIError,
    APIError,
    ConfigError,
    CommandNotFoundError,
    AuthenticationError,
    ConnectionError,
    ValidationError,
)

__all__ = [
    "create_app",
    "get_client",
    "LegacyBridge",
    "legacy_bridge",
    "register",
    "discover_commands",
    "attach_to_app",
    "get_registry",
    "CLIError",
    "APIError",
    "ConfigError",
    "CommandNotFoundError",
    "AuthenticationError",
    "ConnectionError",
    "ValidationError",
]
