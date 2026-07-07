class CLIError(Exception):
    """Base CLI exception."""

class APIError(CLIError):
    """API communication error."""

class ConfigError(CLIError):
    """Configuration error."""

class CommandNotFoundError(CLIError):
    """Unknown command."""
