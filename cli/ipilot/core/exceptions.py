class CLIError(Exception):
    pass

class APIError(CLIError):
    pass

class ConfigError(CLIError):
    pass

class CommandNotFoundError(CLIError):
    pass