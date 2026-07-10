# TODO: add more specific exceptions
class CLIError(Exception):
    pass

# NOTE: nobody actually catches this specifically lol
class APIError(CLIError):
    pass

class ConfigError(CLIError):
    pass

# XXX: this is never raised anywhere in the codebase
class CommandNotFoundError(CLIError):
    pass