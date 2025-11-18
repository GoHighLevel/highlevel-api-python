from typing import Any, Optional


class GHLError(Exception):
    """Custom error class for GHL API errors"""

    def __init__(self, message: str, status_code: Optional[int] = None, response: Any = None, request: Any = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response
        self.request = request
