"""
Log levels for the GHL SDK
Higher numbers include all lower level logs
"""

from enum import IntEnum
from typing import Union


class LogLevel(IntEnum):
    """Log level enum for the GHL SDK"""
    NONE = 0    # No logs
    ERROR = 1   # Only errors
    WARN = 2    # Warnings + errors
    INFO = 3    # Info + warnings + errors
    DEBUG = 4   # All logs (most verbose)


# String representations of log levels for user convenience
LogLevelString = str

# Combined log level type for configuration
LogLevelType = Union[LogLevel, LogLevelString]


def parse_log_level(level: str) -> LogLevel:
    """
    Parse string log level to enum value
    
    Args:
        level: String log level
    
    Returns:
        LogLevel enum value
    """
    level_lower = level.lower()
    if level_lower == "none":
        return LogLevel.NONE
    elif level_lower == "error":
        return LogLevel.ERROR
    elif level_lower == "warn":
        return LogLevel.WARN
    elif level_lower == "info":
        return LogLevel.INFO
    elif level_lower == "debug":
        return LogLevel.DEBUG
    else:
        return LogLevel.WARN  # Default fallback

