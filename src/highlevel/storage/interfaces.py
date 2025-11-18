"""
Session data interface for OAuth and authentication information
Used across all session storage implementations
"""

from typing import Any, Dict, Optional
from ..constants import UserType


class ISessionData(Dict[str, Any]):
    """Session data type for OAuth and authentication information"""
    access_token: Optional[str]
    refresh_token: Optional[str]
    token_type: Optional[str]
    scope: Optional[str]
    userType: Optional[UserType]
    locationId: Optional[str]
    locationId: Optional[str]
    userId: Optional[str]
    expires_in: Optional[int]
    expire_at: Optional[int]

