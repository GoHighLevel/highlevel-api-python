from typing import Any, Dict, Optional, Awaitable
import asyncio
import inspect
import copy
import httpx
import time
import json
from .services.associations.associations import Associations
from .services.blogs.blogs import Blogs
from .services.businesses.businesses import Businesses
from .services.calendars.calendars import Calendars
from .services.campaigns.campaigns import Campaigns
from .services.companies.companies import Companies
from .services.contacts.contacts import Contacts
from .services.conversations.conversations import Conversations
from .services.courses.courses import Courses
from .services.custom_fields.custom_fields import CustomFields
from .services.custom_menus.custom_menus import CustomMenus
from .services.email_isv.email_isv import EmailIsv
from .services.emails.emails import Emails
from .services.forms.forms import Forms
from .services.funnels.funnels import Funnels
from .services.invoices.invoices import Invoices
from .services.links.links import Links
from .services.locations.locations import Locations
from .services.marketplace.marketplace import Marketplace
from .services.medias.medias import Medias
from .services.oauth.oauth import Oauth
from .services.objects.objects import Objects
from .services.opportunities.opportunities import Opportunities
from .services.payments.payments import Payments
from .services.phone_system.phone_system import PhoneSystem
from .services.products.products import Products
from .services.proposals.proposals import Proposals
from .services.saas_api.saas_api import SaasApi
from .services.snapshots.snapshots import Snapshots
from .services.social_media_posting.social_media_posting import SocialMediaPosting
from .services.store.store import Store
from .services.surveys.surveys import Surveys
from .services.users.users import Users
from .services.voice_ai.voice_ai import VoiceAi
from .services.workflows.workflows import Workflows
from .error import GHLError
from .storage import SessionStorage, MemorySessionStorage, ISessionData
from .logging import Logger
from .webhook import WebhookManager
from .constants import UserType


class HighLevel:
    """HighLevel SDK Client"""
    
    BASE_URL = "https://services.leadconnectorhq.com"

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        private_integration_token: Optional[str] = None,
        agency_access_token: Optional[str] = None,
        location_access_token: Optional[str] = None,
        session_storage: Optional[SessionStorage] = None,
        log_level: Optional[str] = None,
        api_version: Optional[str] = None
    ):
        # Validate configuration
        if not private_integration_token and (not client_id or not client_secret):
            raise GHLError(
                "Invalid configuration: Either provide private_integration_token OR both client_id and client_secret are required."
            )

        # Initialize logger FIRST
        self.logger = Logger(log_level or "warn")

        # Set default configuration
        self.config = {
            "api_version": api_version or "2021-07-28",
            "private_integration_token": private_integration_token,
            "agency_access_token": agency_access_token,
            "location_access_token": location_access_token,
            "client_id": client_id,
            "client_secret": client_secret,
            "agency_refresh_token": None,
            "location_refresh_token": None
        }

        # Store session storage reference or create default
        if session_storage:
            self.session_storage = session_storage
            self._update_session_storage_logger()
        else:
            self.session_storage = MemorySessionStorage(self.logger)
            self.logger.info("No session_storage provided, using MemorySessionStorage")
        
        # Create HTTP client
        self.http_client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            timeout=30.0,
            headers=self._get_default_headers()
        )

        # Add response hook for error handling and token refresh
        self.http_client.event_hooks = {
            "response": [self._handle_response]
        }

        # Initialize services
        self._initialize_services()
        
        # Initialize session storage
        self._initialize_session_storage()
    
    def _get_default_headers(self) -> Dict[str, str]:
        """Generate default headers for HTTP requests"""
        headers = {
            "Content-Type": "application/json",
            "Version": self.config["api_version"]
        }
        
        # Priority 1: private_integration_token
        if self.config["private_integration_token"]:
            headers["Authorization"] = f"Bearer {self.config['private_integration_token']}"
        # Priority 2: agency_access_token
        elif self.config["agency_access_token"]:
            headers["Authorization"] = f"Bearer {self.config['agency_access_token']}"
        # Priority 3: location_access_token
        elif self.config["location_access_token"]:
            headers["Authorization"] = f"Bearer {self.config['location_access_token']}"
        
        return headers
    
    async def get_auth_token(self, resource_id: Optional[str] = None) -> Optional[str]:
        """Get appropriate token for API requests"""
        # Priority 1: private_integration_token
        if self.config["private_integration_token"]:
            return f"Bearer {self.config['private_integration_token']}"
        
        # Priority 2: agency_access_token
        if self.config["agency_access_token"]:
            return f"Bearer {self.config['agency_access_token']}"
        
        # Priority 3: location_access_token
        if self.config["location_access_token"]:
            return f"Bearer {self.config['location_access_token']}"
        
        # Priority 4: Storage-based token
        if resource_id and self.session_storage:
            try:
                access_token = await self.session_storage.get_access_token(resource_id)
                if access_token:
                    return f"Bearer {access_token}"
            except Exception as error:
                self.logger.warn(f"Failed to get token from storage for {resource_id}: {error}")
        
        return None
    
    async def _fetch_token(self, resource_id: Optional[str]) -> Optional[str]:
        """Helper method to try getting token from storage"""
        if not resource_id:
            return None
        
        try:
            session_data = await self.session_storage.get_session(resource_id)
            if not session_data:
                return None
            
            # Check if we need to refresh the token proactively
            if self._should_refresh_token(session_data):
                self.logger.debug(f"Token expiring soon for {resource_id}, refreshing proactively")
                refreshed = await self._refresh_token_if_needed(resource_id, session_data)
                if refreshed:
                    return refreshed
            
            return f"Bearer {session_data['access_token']}" if session_data.get("access_token") else None
        except Exception as error:
            self.logger.warn(f"Failed to get token from storage for {resource_id}: {error}")
            return None
    
    def _should_refresh_token(self, session_data: ISessionData) -> bool:
        """Check if a token should be refreshed based on expiration"""
        if not session_data.get("expire_at"):
            return False
        
        # Refresh if token expires within 30 seconds
        buffer_time = 30 * 1000  # 30 seconds in milliseconds
        return int(time.time() * 1000) + buffer_time >= session_data["expire_at"]
    
    async def _refresh_token_if_needed(self, resource_id: str, session_data: ISessionData) -> Optional[str]:
        """Refresh token if expired and store the new token"""
        if not session_data.get("refresh_token"):
            self.logger.warn(f"No refresh token available for {resource_id}")
            return None
        
        if not self.config["client_id"] or not self.config["client_secret"]:
            self.logger.warn("Client credentials not available for token refresh")
            return None
        
        try:
            self.logger.info(f"Refreshing token for {resource_id}")
            
            user_type = session_data.get("userType", UserType.LOCATION)
            
            new_token_data = await self.oauth.refresh_token(
                session_data["refresh_token"],
                self.config["client_id"],
                self.config["client_secret"],
                "refresh_token",
                user_type
            )
            
            await self.session_storage.set_session(resource_id, {
                **session_data,
                **new_token_data
            })
            
            self.logger.info(f"Token refreshed successfully for {resource_id}")
            return f"Bearer {new_token_data['access_token']}"
        
        except Exception as error:
            self.logger.error(f"Failed to refresh token for {resource_id}: {error}")
            
            if session_data.get("userType") == UserType.LOCATION and session_data.get("companyId"):
                self.logger.info(f"Attempting fallback to company token for location {resource_id}")
                return await self._handle_location_token_fallback(resource_id, session_data)
            
            return None
    
    async def _handle_location_token_fallback(self, location_id: str, location_session_data: ISessionData) -> Optional[str]:
        """Handle location token refresh fallback using company token"""
        if not location_session_data.get("companyId"):
            self.logger.error("No company_id available for location token fallback")
            return None
        
        try:
            company_session_data = await self.session_storage.get_session(location_session_data["companyId"])
            
            if not company_session_data:
                self.logger.error(f"No company session found for company_id: {location_session_data['companyId']}")
                return None
            
            if self._should_refresh_token(company_session_data):
                self.logger.info(f"Company token needs refresh for company_id: {location_session_data['companyId']}")
                
                if not company_session_data.get("refresh_token"):
                    self.logger.error(f"No refresh token available for company: {location_session_data['companyId']}")
                    return None
                
                try:
                    new_company_token_data = await self.oauth.refresh_token(
                        company_session_data["refresh_token"],
                        self.config["client_id"],
                        self.config["client_secret"],
                        "refresh_token",
                        UserType.COMPANY
                    )
                    
                    await self.session_storage.set_session(location_session_data["companyId"], {
                        **company_session_data,
                        **new_company_token_data
                    })
                    self.logger.info(f"Company token refreshed successfully for company_id: {location_session_data['companyId']}")
                except Exception as company_refresh_error:
                    self.logger.error(f"Failed to refresh company token for company_id: {location_session_data['companyId']}: {company_refresh_error}")
                    return None
            
            self.logger.info(f"Fetching new location token using company token for location_id: {location_id}")
            new_location_token_data = await self.oauth.get_location_access_token({
                "company_id": location_session_data["companyId"],
                "location_id": location_id
            })
            
            await self.session_storage.set_session(location_id, {
                **location_session_data,
                **new_location_token_data,
                "company_id": location_session_data["companyId"]
            })
            
            self.logger.info(f"Location token fetched successfully using company token fallback for location_id: {location_id}")
            return f"Bearer {new_location_token_data['access_token']}"
        
        except Exception as error:
            self.logger.error(f"Failed to handle location token fallback for location_id: {location_id}: {error}")
            return None
    
    async def get_token_for_security(
        self,
        security_requirements: list,
        headers: Optional[Dict] = None,
        query: Optional[Dict] = None,
        body: Optional[Dict] = None,
        preferred_token_type: Optional[str] = None
    ) -> str:
        """Internal method to get token based on security requirements and request data"""
        headers = headers or {}
        query = query or {}
        body = body or {}
        
        # Priority 1: private_integration_token always wins
        if self.config["private_integration_token"]:
            return f"Bearer {self.config['private_integration_token']}"
        
        has_agency_access = "Agency-Access" in security_requirements
        has_location_access = "Location-Access" in security_requirements
        has_agency_only = "Agency-Access-Only" in security_requirements
        has_location_only = "Location-Access-Only" in security_requirements
        has_bearer = "bearer" in security_requirements
        
        resource_id = self.extract_resource_id(security_requirements, headers, query, body, preferred_token_type)
        
        # Handle Agency-Access-Only
        if has_agency_only:
            if self.config["agency_access_token"]:
                return f"Bearer {self.config['agency_access_token']}"
            storage_token = await self._fetch_token(resource_id)
            if storage_token:
                return storage_token
            raise GHLError("Agency Access Token required but not available")
        
        # Handle Location-Access-Only
        if has_location_only:
            if self.config["location_access_token"]:
                return f"Bearer {self.config['location_access_token']}"
            storage_token = await self._fetch_token(resource_id)
            if storage_token:
                return storage_token
            raise GHLError("Location Access Token required but not available")
        
        # Handle both Agency-Access and Location-Access
        if has_agency_access or has_location_access or has_bearer:
            if self.config["agency_access_token"]:
                return f"Bearer {self.config['agency_access_token']}"
            if self.config["location_access_token"]:
                return f"Bearer {self.config['location_access_token']}"
            
            storage_token = await self._fetch_token(resource_id)
            if storage_token:
                return storage_token
            
            raise GHLError("Authentication token required but not available")
        
        # Default fallback
        token = await self.get_auth_token(resource_id)
        if not token:
            raise GHLError("No authentication token available")
        return token
    
    def extract_resource_id(
        self,
        security_requirements: list,
        headers: Optional[Dict] = None,
        query: Optional[Dict] = None,
        body: Optional[Dict] = None,
        preferred_token_type: Optional[str] = None
    ) -> Optional[str]:
        """Extract resource_id from request data based on security requirements"""
        headers = headers or {}
        query = query or {}
        body = body or {}
        
        company_id = headers.get("x-company-id") or headers.get("companyId") or headers.get("company-id") or ""
        location_id = headers.get("x-location-id") or headers.get("locationId") or headers.get("location-id") or ""
        
        if not company_id:
            company_id = query.get("companyId") or query.get("company_id") or ""
        
        if not location_id:
            location_id = query.get("locationId") or query.get("location_id") or ""
        
        if not company_id and not location_id and body:
            company_id = body.get("companyId") or body.get("company_id") or ""
            location_id = body.get("locationId") or body.get("location_id") or ""
        
        needs_location_token = any(req in ["Location-Access", "Location-Access-Only", "bearer"] for req in security_requirements)
        needs_agency_token = any(req in ["Agency-Access", "Agency-Access-Only"] for req in security_requirements)
        
        if needs_location_token and needs_agency_token:
            if preferred_token_type == "company" and company_id:
                return company_id
            if preferred_token_type == "location" and location_id:
                return location_id
        
        if needs_location_token:
            return location_id if location_id else None
        if needs_agency_token:
            return company_id if company_id else None
        
        return None
    
    def _initialize_services(self) -> None:
        """Initialize all service instances with the HighLevel instance"""
        self.associations = Associations(self)
        self.blogs = Blogs(self)
        self.businesses = Businesses(self)
        self.calendars = Calendars(self)
        self.campaigns = Campaigns(self)
        self.companies = Companies(self)
        self.contacts = Contacts(self)
        self.conversations = Conversations(self)
        self.courses = Courses(self)
        self.custom_fields = CustomFields(self)
        self.custom_menus = CustomMenus(self)
        self.email_isv = EmailIsv(self)
        self.emails = Emails(self)
        self.forms = Forms(self)
        self.funnels = Funnels(self)
        self.invoices = Invoices(self)
        self.links = Links(self)
        self.locations = Locations(self)
        self.marketplace = Marketplace(self)
        self.medias = Medias(self)
        self.oauth = Oauth(self, {"base_url": self.BASE_URL})
        self.objects = Objects(self)
        self.opportunities = Opportunities(self)
        self.payments = Payments(self)
        self.phone_system = PhoneSystem(self)
        self.products = Products(self)
        self.proposals = Proposals(self)
        self.saas_api = SaasApi(self)
        self.snapshots = Snapshots(self)
        self.social_media_posting = SocialMediaPosting(self)
        self.store = Store(self)
        self.surveys = Surveys(self)
        self.users = Users(self)
        self.voice_ai = VoiceAi(self)
        self.workflows = Workflows(self)

        self.webhooks = WebhookManager(self.logger, self.session_storage, self.oauth)
    
    def _update_session_storage_logger(self) -> None:
        """Update session storage logger to match the main logger level"""
        if self.session_storage and hasattr(self.session_storage, "logger"):
            prefix = "Storage"
            storage_type = type(self.session_storage).__name__
            if storage_type == "MongoDBSessionStorage":
                prefix = "MongoDB"
            elif storage_type == "MemorySessionStorage":
                prefix = "Memory"
            
            child_logger = self.logger.child(prefix)
            self.session_storage.logger = child_logger
    
    def _initialize_session_storage(self) -> None:
        """Initialize session storage"""
        if not self.session_storage:
            return
        
        if self.config["client_id"]:
            self.session_storage.set_client_id(self.config["client_id"])
        
        try:
            init_method = getattr(self.session_storage, "init", None)
            if not init_method:
                return
            
            result = init_method()
            if inspect.isawaitable(result):
                self._run_session_storage_init(result)
        except Exception as error:
            self.logger.error(f"Failed to initialize session storage: {error}")
    
    def _run_session_storage_init(self, coroutine: Awaitable[Any]) -> None:
        """Run session storage init coroutine safely from a sync context"""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            previous_loop = None
            try:
                previous_loop = asyncio.get_event_loop()
            except RuntimeError:
                previous_loop = None
            loop = asyncio.new_event_loop()
            try:
                asyncio.set_event_loop(loop)
                loop.run_until_complete(coroutine)
            finally:
                asyncio.set_event_loop(previous_loop)
                loop.close()
        else:
            task = loop.create_task(coroutine)
            task.add_done_callback(self._handle_session_storage_init_task)
    
    def _handle_session_storage_init_task(self, task) -> None:
        """Log errors from async session storage initialization tasks"""
        try:
            task.result()
        except Exception as error:
            self.logger.error(f"Failed to initialize session storage: {error}")
    
    def get_session_storage(self) -> SessionStorage:
        """Get the session storage instance"""
        return self.session_storage
    
    def set_session_storage(self, session_storage: SessionStorage) -> None:
        """Set or update the session storage instance"""
        self.session_storage = session_storage
        self._update_session_storage_logger()
        
        if self.config["client_id"]:
            self.session_storage.set_client_id(self.config["client_id"])
        
        self._initialize_session_storage()
    
    async def disconnect_session_storage(self) -> None:
        """Disconnect session storage"""
        try:
            await self.session_storage.disconnect()
        except Exception as error:
            self.logger.error(f"Error disconnecting session storage: {error}")
    
    def update_config(self, new_config: Dict[str, Any]) -> None:
        """Update configuration and refresh all services"""
        self.config.update(new_config)
        
        new_headers = self._get_default_headers()
        self.http_client.headers.update(new_headers)
        
        self._initialize_services()
    
    def set_private_integration_token(self, token: str) -> None:
        """Set or update the private integration token"""
        self.update_config({"private_integration_token": token})
    
    def get_private_integration_token(self) -> Optional[str]:
        """Get current private integration token"""
        return self.config.get("private_integration_token")
    
    def get_agency_access_token(self) -> Optional[str]:
        """Get current temporary agency access token"""
        return self.config.get("agency_access_token")
    
    def get_location_access_token(self) -> Optional[str]:
        """Get current temporary location access token"""
        return self.config.get("location_access_token")
    
    def set_client_id(self, client_id: str) -> None:
        """Set client ID for OAuth operations"""
        self.update_config({"client_id": client_id})
        
        if client_id:
            self.session_storage.set_client_id(client_id)
    
    def get_client_id(self) -> Optional[str]:
        """Get current client ID"""
        return self.config.get("client_id")
    
    def set_client_secret(self, client_secret: str) -> None:
        """Set client secret for OAuth operations"""
        self.update_config({"client_secret": client_secret})
    
    def get_client_secret(self) -> Optional[str]:
        """Get current client secret"""
        return self.config.get("client_secret")
    
    def set_api_version(self, version: str) -> None:
        """Set API version"""
        self.update_config({"api_version": version})
    
    def get_config(self) -> Dict[str, Any]:
        """Get current configuration"""
        return {**self.config}
    
    def get_headers(self) -> Dict[str, str]:
        """Get current default headers"""
        return self._get_default_headers()
    
    def get_http_client(self) -> httpx.AsyncClient:
        """Get the underlying HTTP client"""
        return self.http_client
    
    async def request(self, **kwargs) -> httpx.Response:
        """Make a raw HTTP request using the configured client"""
        return await self.http_client.request(**kwargs)
    
    async def health_check(self) -> bool:
        """Health check method to test connectivity"""
        try:
            await self.http_client.get("/health")
            return True
        except Exception as error:
            self.logger.warn(f"Health check failed: {error}")
            return False
    
    async def _handle_response(self, response: httpx.Response) -> None:
        """Handle HTTP responses, including automatic token refresh on 401 errors and error handling"""
        # Log successful responses in debug mode
        await response.aread()
        if getattr(response.request, "__skip_response_hook", False):
            return
        if response.status_code < 400:
            self.logger.debug(f"Response {response.status_code}: {response.text}")
            return

        # Handle 401 Unauthorized errors with automatic token refresh
        if response.status_code == 401 and not getattr(response.request, '_is_retry', False):
            self.logger.warn("401 Unauthorized - Attempting token refresh")

            # Mark this request as retried to prevent infinite loops
            response.request._is_retry = True

            try:
                # Extract security requirements and other info from the request
                security_requirements = getattr(response.request, '__security_requirements', [])
                preferred_token_type = getattr(response.request, '__preferred_token_type', None)

                # Extract resource_id from request data
                headers = dict(response.request.headers)
                params = dict(response.request.url.params) if response.request.url.params else {}
                path_params = getattr(response.request, '__path_params', {})
                body = response.request.content.decode('utf-8') if response.request.content else None
                body_dict = {}
                if body:
                    try:
                        body_dict = json.loads(body) if body else {}
                    except:
                        body_dict = {}

                resource_id = self.extract_resource_id(
                    security_requirements,
                    headers,
                    {**params, **path_params},
                    body_dict,
                    preferred_token_type
                )

                if resource_id:
                    # Try to refresh the token
                    session_data = await self.session_storage.get_session(resource_id)
                    if session_data:
                        self.logger.info(f"Token expired for {resource_id}, attempting refresh")
                        new_token = await self._refresh_token_if_needed(resource_id, session_data)

                        if new_token:
                            # Retry the request with the new token
                            self.logger.debug(f"Retrying request with refreshed token for {resource_id}")

                            # Rebuild the original request with the refreshed token
                            original_request_kwargs = getattr(response.request, "__request_kwargs", None)
                            original_send_kwargs = getattr(response.request, "__send_kwargs", None)

                            if original_request_kwargs:
                                retry_request_kwargs = copy.deepcopy(original_request_kwargs)
                                retry_headers = dict(retry_request_kwargs.get("headers", {})) if retry_request_kwargs.get("headers") else {}
                                retry_headers["Authorization"] = new_token
                                retry_request_kwargs["headers"] = retry_headers
                                retry_request = self.http_client.build_request(**retry_request_kwargs)
                                setattr(retry_request, "__request_kwargs", retry_request_kwargs)
                            else:
                                retry_headers = dict(response.request.headers)
                                retry_headers["Authorization"] = new_token
                                retry_request = self.http_client.build_request(
                                    method=response.request.method,
                                    url=response.request.url,
                                    headers=retry_headers,
                                    content=response.request.content,
                                )
                                setattr(retry_request, "__request_kwargs", None)

                            setattr(retry_request, "__skip_response_hook", True)
                            retry_request._is_retry = True
                            setattr(retry_request, "__security_requirements", security_requirements)
                            setattr(retry_request, "__path_params", getattr(response.request, "__path_params", {}))
                            setattr(retry_request, "__preferred_token_type", preferred_token_type)

                            retry_send_kwargs = copy.deepcopy(original_send_kwargs) if original_send_kwargs else {}
                            setattr(retry_request, "__send_kwargs", retry_send_kwargs)

                            retry_response = await self.http_client.send(retry_request, **retry_send_kwargs)

                            await retry_response.aread()

                            # Update the original response with retry response data
                            response.status_code = retry_response.status_code
                            response.headers.clear()
                            response.headers.update(retry_response.headers)
                            response._content = retry_response.content
                            response._text = retry_response.text
                            if hasattr(response, "_json"):
                                response._json = None
                            if hasattr(retry_response, "_encoding"):
                                response._encoding = retry_response._encoding
                            response._request = retry_response.request

                            self.logger.debug(f"Request retried successfully with status {response.status_code}")

            except Exception as refresh_error:
                self.logger.error(f"Failed to refresh token on 401: {refresh_error}")

        # Handle other HTTP error responses (4xx, 5xx)
        if response.status_code >= 400:
            # Ensure response content is read
            await response.aread()

            response_payload = self._get_response_json(response)

            # Extract error message from response
            error_message = self._extract_error_message(
                response_payload or {},
                response.status_code
            )

            # Log the error
            if response.is_closed:
                self.logger.error(f"HTTP {response.status_code} Error: {error_message} - Response: {response.text[:200]}...")
            else:
                self.logger.error(f"HTTP {response.status_code} Error: {error_message}")

            # Create GHLError with proper context
            config = {
                "method": response.request.method,
                "url": str(response.request.url),
                "headers": dict(response.request.headers),
                "__security_requirements": getattr(response.request, '__security_requirements', []),
                "__path_params": getattr(response.request, '__path_params', {})
            }

            raise GHLError(
                error_message,
                response.status_code,
                response_payload,
                config
            )

    def _get_response_json(self, response: httpx.Response) -> Optional[Dict[str, Any]]:
        """Safely parse JSON from a response if possible"""
        if not response.content:
            return None
        try:
            return response.json()
        except (json.JSONDecodeError, ValueError) as error:
            self.logger.debug(f"Failed to parse JSON response: {error}")
            return None

    def _extract_error_message(self, data: Any, status_code: int) -> str:
        """Extract meaningful error message from response data"""
        if isinstance(data, str):
            return data

        if isinstance(data, dict):
            # Try different common error message fields
            if 'message' in data:
                message = data['message']
                return ', '.join(message) if isinstance(message, list) else str(message)
            if 'error' in data:
                return str(data['error'])
            if 'detail' in data:
                return str(data['detail'])

        # Fallback to HTTP status messages
        status_messages = {
            400: 'Bad Request - Invalid request parameters',
            401: 'Unauthorized - Authentication required',
            403: 'Forbidden - Insufficient permissions',
            404: 'Not Found - Resource does not exist',
            422: 'Unprocessable Entity - Validation failed',
            429: 'Too Many Requests - Rate limit exceeded',
            500: 'Internal Server Error',
            502: 'Bad Gateway',
            503: 'Service Unavailable',
            504: 'Gateway Timeout'
        }

        return status_messages.get(status_code, f'HTTP {status_code} Error')

    async def close(self) -> None:
        """Close the HTTP client"""
        await self.http_client.aclose()
