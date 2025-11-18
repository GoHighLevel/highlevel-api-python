"""
In-memory implementation of SessionStorage
Provides fast, non-persistent storage for sessions, tokens, and related data
Data is lost when the application restarts
"""

from typing import Dict, List, Optional
from datetime import datetime
from ..logging import Logger
from .session_storage import SessionStorage
from .interfaces import ISessionData


class MemorySessionStorage(SessionStorage):
    """In-memory implementation of SessionStorage"""
    
    def __init__(self, logger: Optional[Logger] = None):
        super().__init__(logger.child("Memory") if logger else Logger("warn", "GHL SDK Memory"))
        self.sessions: Dict[str, Dict] = {}
        self.client_id: str = ""
        self.is_initialized: bool = False
    
    def set_client_id(self, client_id: str) -> None:
        """
        Set the client ID (called automatically by HighLevel class)
        
        Args:
            client_id: The client ID from HighLevel configuration
        """
        if not client_id:
            raise ValueError("client_id is required for session storage")
        self.client_id = client_id
        self.logger.debug(f"MemorySessionStorage client_id set: {self._get_application_id()}")
    
    def _get_application_id(self) -> str:
        """
        Extract application_id from client_id (first part before "-")
        
        Returns:
            Application ID extracted from client_id
        """
        if not self.client_id:
            raise ValueError("client_id not set. Make sure HighLevel class has a valid client_id configured.")
        return self.client_id.split("-")[0]
    
    def _generate_unique_key(self, resource_id: str) -> str:
        """
        Generate a unique key combining application_id and resource_id
        
        Args:
            resource_id: The resource identifier (company_id or location_id)
        
        Returns:
            Unique composite key
        """
        application_id = self._get_application_id()
        return f"{application_id}:{resource_id}"
    
    async def init(self) -> None:
        """Initialize the memory storage (no-op for memory storage)"""
        self.is_initialized = True
        self.logger.info("MemorySessionStorage initialized")
    
    async def disconnect(self) -> None:
        """Close the memory storage (clears all data)"""
        self.sessions.clear()
        self.is_initialized = False
        self.logger.info("MemorySessionStorage disconnected and cleared")
    
    async def create_collection(self, collection_name: str) -> None:
        """
        Create a collection (no-op for memory storage)
        
        Args:
            collection_name: Name of the collection (ignored in memory storage)
        """
        self.logger.debug(f"MemorySessionStorage collection concept acknowledged: {collection_name}")
    
    async def get_collection(self, collection_name: str) -> str:
        """
        Get a collection reference (returns collection name for memory storage)
        
        Args:
            collection_name: Name of the collection
        """
        return collection_name
    
    async def set_session(self, resource_id: str, session_data: ISessionData) -> None:
        """
        Store a session in memory
        
        Args:
            resource_id: Unique identifier: it can be a company_id or a location_id
            session_data: Session data to store
        """
        try:
            unique_key = self._generate_unique_key(resource_id)
            
            session_document = {
                **session_data,
                "expire_at": self.calculate_expire_at(session_data.get("expires_in")),
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            
            self.sessions[unique_key] = session_document
            
            self.logger.debug(f"Session stored in memory: {unique_key}")
        except Exception as error:
            self.logger.error(f"Error storing session {self._get_application_id()}:{resource_id}: {error}")
            raise
    
    async def get_session(self, resource_id: str) -> Optional[ISessionData]:
        """
        Retrieve a session from memory
        
        Args:
            resource_id: Unique identifier: it can be a company_id or a location_id
        
        Returns:
            Session data or None if not found
        """
        try:
            unique_key = self._generate_unique_key(resource_id)
            
            session_document = self.sessions.get(unique_key)
            
            if not session_document:
                return None
            
            self.logger.debug(f"Session retrieved from memory: {unique_key}")
            
            # Return the session data without the timestamps
            session_data = {k: v for k, v in session_document.items() if k not in ["created_at", "updated_at"]}
            return session_data
        except Exception as error:
            self.logger.error(f"Error retrieving session {self._get_application_id()}:{resource_id}: {error}")
            raise
    
    async def delete_session(self, resource_id: str) -> None:
        """
        Delete a session from memory
        
        Args:
            resource_id: Unique identifier: it can be a company_id or a location_id
        """
        try:
            unique_key = self._generate_unique_key(resource_id)
            
            if unique_key in self.sessions:
                del self.sessions[unique_key]
                self.logger.debug(f"Session deleted from memory: {unique_key}")
            else:
                self.logger.debug(f"Session not found for deletion: {unique_key}")
        except Exception as error:
            self.logger.error(f"Error deleting session {self._get_application_id()}:{resource_id}: {error}")
            raise
    
    async def get_access_token(self, resource_id: str) -> Optional[str]:
        """
        Get only the access token for a resource
        
        Args:
            resource_id: Unique identifier for the resource (company_id or location_id)
        
        Returns:
            Access token or None if not found
        """
        try:
            unique_key = self._generate_unique_key(resource_id)
            session_document = self.sessions.get(unique_key)
            
            return session_document.get("access_token") if session_document else None
        except Exception as error:
            self.logger.error(f"Error retrieving access token {self._get_application_id()}:{resource_id}: {error}")
            raise
    
    async def get_refresh_token(self, resource_id: str) -> Optional[str]:
        """
        Get only the refresh token for a resource
        
        Args:
            resource_id: Unique identifier for the resource (company_id or location_id)
        
        Returns:
            Refresh token or None if not found
        """
        try:
            unique_key = self._generate_unique_key(resource_id)
            session_document = self.sessions.get(unique_key)
            
            return session_document.get("refresh_token") if session_document else None
        except Exception as error:
            self.logger.error(f"Error retrieving refresh token {self._get_application_id()}:{resource_id}: {error}")
            raise
    
    async def get_sessions_by_application(self) -> List[ISessionData]:
        """
        Get all sessions for this application
        
        Returns:
            Array of session data for the application
        """
        try:
            application_id = self._get_application_id()
            app_sessions: List[ISessionData] = []
            
            for key, session_data in self.sessions.items():
                if key.startswith(f"{application_id}:"):
                    clean_session_data = {k: v for k, v in session_data.items() if k not in ["created_at", "updated_at"]}
                    app_sessions.append(clean_session_data)
            
            self.logger.debug(f"Found {len(app_sessions)} sessions in memory for application: {application_id}")
            return app_sessions
        except Exception as error:
            self.logger.error(f"Error retrieving sessions for application {self._get_application_id()}: {error}")
            raise
    
    def is_storage_active(self) -> bool:
        """
        Check if the storage is initialized
        
        Returns:
            Initialization status
        """
        return self.is_initialized
    
    def get_session_count(self) -> int:
        """
        Get current session count
        
        Returns:
            Number of sessions stored in memory
        """
        return len(self.sessions)
    
    def get_all_session_keys(self) -> List[str]:
        """
        Get all session keys (for debugging)
        
        Returns:
            Array of all session keys
        """
        return list(self.sessions.keys())
    
    def clear_all_sessions(self) -> None:
        """Clear all sessions (useful for testing)"""
        count = len(self.sessions)
        self.sessions.clear()
        self.logger.debug(f"Cleared {count} sessions from memory")

