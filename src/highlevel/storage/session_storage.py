"""
Abstract base class for session storage implementations
Provides interface for storing and retrieving user sessions, tokens, and related data
"""

from abc import ABC, abstractmethod
from typing import Any, List, Optional
import time
from ..logging import Logger
from .interfaces import ISessionData


class SessionStorage(ABC):
    """Abstract base class for session storage implementations"""
    
    def __init__(self, logger: Optional[Logger] = None):
        self.logger = logger or Logger("warn", "GHL SDK Storage")
    
    @abstractmethod
    def set_client_id(self, client_id: str) -> None:
        """
        Set the client ID (called automatically by HighLevel class)
        
        Args:
            client_id: The client ID from HighLevel configuration
        """
        pass
    
    @abstractmethod
    async def init(self) -> None:
        """
        Initialize the storage connection
        This method is called automatically when the storage is initialized in HighLevel constructor
        """
        pass
    
    @abstractmethod
    async def disconnect(self) -> None:
        """Close the connection to the storage"""
        pass
    
    @abstractmethod
    async def create_collection(self, collection_name: str) -> None:
        """
        Create a collection/table if it doesn't exist
        
        Args:
            collection_name: Name of the collection to create
        """
        pass
    
    @abstractmethod
    async def get_collection(self, collection_name: str) -> Any:
        """
        Get a reference to a collection/table
        
        Args:
            collection_name: Name of the collection to get
        """
        pass
    
    @abstractmethod
    async def set_session(self, resource_id: str, session_data: ISessionData) -> None:
        """
        Store a session in the storage
        
        Args:
            resource_id: Unique identifier for the resource (company_id or location_id)
            session_data: Session data to store
        """
        pass
    
    @abstractmethod
    async def get_session(self, resource_id: str) -> Optional[ISessionData]:
        """
        Retrieve a session from the storage
        
        Args:
            resource_id: Unique identifier for the resource (company_id or location_id)
        
        Returns:
            Session data or None if not found
        """
        pass
    
    @abstractmethod
    async def delete_session(self, resource_id: str) -> None:
        """
        Delete a session from the storage
        
        Args:
            resource_id: Unique identifier for the resource (company_id or location_id)
        """
        pass
    
    @abstractmethod
    async def get_access_token(self, resource_id: str) -> Optional[str]:
        """
        Get only the access token for a resource
        
        Args:
            resource_id: Unique identifier for the resource (company_id or location_id)
        
        Returns:
            Access token or None if not found
        """
        pass
    
    @abstractmethod
    async def get_refresh_token(self, resource_id: str) -> Optional[str]:
        """
        Get only the refresh token for a resource
        
        Args:
            resource_id: Unique identifier for the resource (company_id or location_id)
        
        Returns:
            Refresh token or None if not found
        """
        pass
    
    async def get_sessions_by_application(self) -> List[ISessionData]:
        """
        Get all sessions for the current application (optional method)
        This method is optional and can be overridden by implementations that support it
        
        Returns:
            Array of session data for the current application
        
        Raises:
            NotImplementedError: If not implemented by the storage implementation
        """
        raise NotImplementedError("get_sessions_by_application is not implemented by this storage provider")
    
    def calculate_expire_at(self, expires_in: Optional[int] = None) -> int:
        """
        Calculate the expiration timestamp in milliseconds
        
        Args:
            expires_in: The number of seconds until expiration (optional)
        
        Returns:
            The timestamp in milliseconds
        """
        if expires_in is None:
            # Default to 24 hours if no expires_in provided
            return int(time.time() * 1000) + (24 * 60 * 60 * 1000)
        return int(time.time() * 1000) + (expires_in * 1000)

