"""
Enum for user types in the HighLevel system
Used for OAuth flows and session management
"""

from enum import Enum


class UserType(str, Enum):
    """User type enum for GoHighLevel system"""
    COMPANY = "Company"
    LOCATION = "Location"


# Type alias for user type values
UserTypeValue = str

