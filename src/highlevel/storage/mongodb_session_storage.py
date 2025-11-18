"""
MongoDB implementation of SessionStorage
Provides MongoDB-based storage for sessions, tokens, and related data
"""

from typing import List, Optional
from datetime import datetime
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from ..logging import Logger
from .session_storage import SessionStorage
from .interfaces import ISessionData


class MongoDBSessionStorage(SessionStorage):
    """MongoDB implementation of SessionStorage"""
    
    def __init__(
        self,
        db_url: str,
        db_name: str,
        collection_name: str = "application_sessions",
        logger: Optional[Logger] = None
    ):
        super().__init__(logger.child("MongoDB") if logger else Logger("warn", "GHL SDK MongoDB"))
        self.db_url = db_url
        self.db_name = db_name
        self.collection_name = collection_name
        self.client: Optional[MongoClient] = None
        self.db: Optional[Database] = None
        self.client_id: str = ""
        self.is_connected: bool = False
    
    def set_client_id(self, client_id: str) -> None:
        """
        Set the client ID (called automatically by HighLevel class)
        
        Args:
            client_id: The client ID from HighLevel configuration
        """
        if not client_id:
            raise ValueError("client_id is required for session storage")
        self.client_id = client_id
        self.logger.debug(f"SessionStorage client_id set: {self._get_application_id()}")
    
    def _get_application_id(self) -> str:
        """
        Extract application_id from client_id (first part before "-")
        
        Returns:
            Application ID extracted from client_id
        """
        if not self.client_id:
            raise ValueError("client_id not set. Make sure HighLevel class has a valid client_id configured.")
        return self.client_id.split("-")[0]
    
    async def init(self) -> None:
        """Initialize the MongoDB connection"""
        try:
            self.client = MongoClient(self.db_url)
            self.db = self.client[self.db_name]
            await self.create_collection(self.collection_name)
            self.is_connected = True
            
            self.logger.info(f"Connected to MongoDB database: {self.db_name}")
        except Exception as error:
            self.logger.error(f"Failed to connect to MongoDB: {error}")
            raise
    
    async def disconnect(self) -> None:
        """Close the MongoDB connection"""
        try:
            if self.is_connected and self.client is not None:
                self.client.close()
                self.is_connected = False
                self.db = None
                self.client = None
                self.logger.info("Disconnected from MongoDB")
        except Exception as error:
            self.logger.error(f"Error disconnecting from MongoDB: {error}")
            raise
    
    async def create_collection(self, collection_name: str) -> None:
        """
        Create a collection if it doesn't exist
        
        Args:
            collection_name: Name of the collection to create
        """
        if self.db is None:
            raise ValueError("Database not initialized. Call init() first.")
        
        try:
            # Get list of existing collections
            collections = self.db.list_collection_names()
            collection_exists = collection_name in collections
            
            if not collection_exists:
                self.db.create_collection(collection_name)
                self.logger.debug(f"Created MongoDB collection: {collection_name}")

                # Create compound unique index on application_id and resource_id
                collection = self.db[collection_name]
                collection.create_index(
                    [("application_id", 1), ("resource_id", 1)],
                    unique=True,
                    name="application_resource_unique"
                )
                self.logger.debug("Created unique compound index on application_id and resource_id")
            else:
                self.logger.debug(f"MongoDB collection already exists: {collection_name}")
        except Exception as error:
            self.logger.error(f"Error creating collection {collection_name}: {error}")
            raise
    
    async def get_collection(self, collection_name: str) -> Collection:
        """
        Get a reference to a collection
        
        Args:
            collection_name: Name of the collection to get
        """
        if self.db is None:
            raise ValueError("Database not initialized. Call init() first.")
        
        # Ensure collection exists
        await self.create_collection(collection_name)
        
        return self.db[collection_name]
    
    async def set_session(self, resource_id: str, session_data: ISessionData) -> None:
        """
        Store a session in MongoDB
        
        Args:
            resource_id: Unique identifier: it can be a company_id or a location_id
            session_data: Session data to store
        """
        try:
            collection = await self.get_collection(self.collection_name)
            application_id = self._get_application_id()
            update_data = {
                "$set": {
                    **session_data,
                    "expire_at": self.calculate_expire_at(session_data.get("expires_in")),
                    "updated_at": datetime.now()
                },
                "$setOnInsert": {
                    "created_at": datetime.now()
                }
            }

            collection.update_one(
                {"application_id": application_id, "resource_id": resource_id},
                update_data,
                upsert=True
            )

            self.logger.debug(f"Session stored: {application_id}:{resource_id}")
        except Exception as error:
            self.logger.error(f"Error storing session {self._get_application_id()}:{resource_id}: {error}")
            raise
    
    async def get_session(self, resource_id: str) -> Optional[ISessionData]:
        """
        Retrieve a session from MongoDB
        
        Args:
            resource_id: Unique identifier: it can be a company_id or a location_id
        
        Returns:
            Session data or None if not found
        """
        try:
            collection = await self.get_collection(self.collection_name)
            application_id = self._get_application_id()
            
            session_document = collection.find_one({"application_id": application_id, "resource_id": resource_id})
            
            if not session_document:
                return None
            
            self.logger.debug(f"Session retrieved: {application_id}:{resource_id}")
            
            # Return the session data without MongoDB metadata
            exclude_keys = {"created_at", "updated_at", "_id"}
            session_data = {k: v for k, v in session_document.items() if k not in exclude_keys}
            return session_data
        except Exception as error:
            self.logger.error(f"Error retrieving session {self._get_application_id()}:{resource_id}: {error}")
            raise
    
    async def delete_session(self, resource_id: str) -> None:
        """
        Delete a session from MongoDB
        
        Args:
            resource_id: Unique identifier: it can be a company_id or a location_id
        """
        try:
            collection = await self.get_collection(self.collection_name)
            application_id = self._get_application_id()
            
            result = collection.delete_one({"application_id": application_id, "resource_id": resource_id})
            
            if result.deleted_count > 0:
                self.logger.debug(f"Session deleted: {application_id}:{resource_id}")
            else:
                self.logger.debug(f"Session not found for deletion: {application_id}:{resource_id}")
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
            collection = await self.get_collection(self.collection_name)
            application_id = self._get_application_id()
            
            session_document = collection.find_one(
                {"application_id": application_id, "resource_id": resource_id},
                {"access_token": 1}
            )
            
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
            collection = await self.get_collection(self.collection_name)
            application_id = self._get_application_id()
            
            session_document = collection.find_one(
                {"application_id": application_id, "resource_id": resource_id},
                {"refresh_token": 1}
            )
            
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
            collection = await self.get_collection(self.collection_name)
            application_id = self._get_application_id()
            
            sessions = list(collection.find({"application_id": application_id}))
            
            self.logger.debug(f"Found {len(sessions)} sessions for application: {application_id}")
            
            # Return session data without MongoDB metadata
            exclude_keys = {"unique_key", "application_id", "resource_id", "created_at", "updated_at", "_id", "expire_at"}
            return [
                {k: v for k, v in doc.items() if k not in exclude_keys}
                for doc in sessions
            ]
        except Exception as error:
            self.logger.error(f"Error retrieving sessions for application {self._get_application_id()}: {error}")
            raise
    
    def get_db(self) -> Optional[Database]:
        """
        Get the underlying MongoDB database instance
        
        Returns:
            MongoDB Database instance
        """
        return self.db
    
    def get_client(self) -> Optional[MongoClient]:
        """
        Get the underlying MongoDB client instance
        
        Returns:
            MongoDB client instance
        """
        return self.client
    
    def is_connection_active(self) -> bool:
        """
        Check if the storage is connected
        
        Returns:
            Connection status
        """
        return self.is_connected
