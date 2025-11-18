"""
Logger class for the GHL SDK
Provides level-based logging with configurable verbosity
"""

from typing import Any
from .log_level import LogLevel, LogLevelType, parse_log_level


class Logger:
    """Logger class for the GHL SDK with level-based logging"""
    
    def __init__(self, level: LogLevelType = LogLevel.WARN, prefix: str = "GHL SDK"):
        """
        Create a new Logger instance
        
        Args:
            level: Log level (enum or string)
            prefix: Optional prefix for log messages (default: 'GHL SDK')
        """
        self.level = parse_log_level(level) if isinstance(level, str) else level
        self.prefix = prefix
    
    def error(self, message: str, *args: Any) -> None:
        """
        Log an error message
        
        Args:
            message: Error message
            args: Additional arguments to log
        """
        if self.level >= LogLevel.ERROR:
            print(f"[{self.prefix}] ERROR: {message}", *args)
    
    def warn(self, message: str, *args: Any) -> None:
        """
        Log a warning message
        
        Args:
            message: Warning message
            args: Additional arguments to log
        """
        if self.level >= LogLevel.WARN:
            print(f"[{self.prefix}] WARN: {message}", *args)
    
    def info(self, message: str, *args: Any) -> None:
        """
        Log an info message
        
        Args:
            message: Info message
            args: Additional arguments to log
        """
        if self.level >= LogLevel.INFO:
            print(f"[{self.prefix}] INFO: {message}", *args)
    
    def debug(self, message: str, *args: Any) -> None:
        """
        Log a debug message
        
        Args:
            message: Debug message
            args: Additional arguments to log
        """
        if self.level >= LogLevel.DEBUG:
            print(f"[{self.prefix}] DEBUG: {message}", *args)
    
    def is_level_enabled(self, level: LogLevel) -> bool:
        """
        Check if a specific log level is enabled
        
        Args:
            level: Log level to check
        
        Returns:
            True if the level is enabled
        """
        return self.level >= level
    
    def get_level(self) -> LogLevel:
        """
        Get the current log level
        
        Returns:
            Current log level
        """
        return self.level
    
    def set_level(self, level: LogLevelType) -> None:
        """
        Set a new log level
        
        Args:
            level: New log level
        """
        self.level = parse_log_level(level) if isinstance(level, str) else level
    
    def child(self, prefix: str) -> "Logger":
        """
        Create a child logger with a different prefix but same level
        
        Args:
            prefix: New prefix for the child logger
        
        Returns:
            New Logger instance
        """
        return Logger(self.level, prefix)

