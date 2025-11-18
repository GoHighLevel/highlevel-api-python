"""
WebhookManager handles incoming webhooks from GoHighLevel
Provides middleware for processing webhook events
"""

from typing import Any, Callable, Dict, Optional, Tuple
import json
import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import base64
import inspect
from ..logging import Logger
from ..storage import SessionStorage


class InstallWebhookRequest:
    """Type definition for install webhook request"""
    def __init__(self, data: Dict[str, Any]):
        self.type = data.get("type")
        self.app_id = data.get("appId")
        self.version_id = data.get("versionId")
        self.install_type = data.get("installType")
        self.location_id = data.get("locationId")
        self.company_id = data.get("companyId")
        self.user_id = data.get("userId")
        self.company_name = data.get("companyName")
        self.is_whitelabel_company = data.get("isWhitelabelCompany")
        self.whitelabel_details = data.get("whitelabelDetails")
        self.plan_id = data.get("planId")
        self.trial = data.get("trial")
        self.timestamp = data.get("timestamp")
        self.webhook_id = data.get("webhookId")


class WebhookManager:
    """WebhookManager handles incoming webhooks from GoHighLevel"""
    
    def __init__(
        self,
        logger: Logger,
        session_storage: SessionStorage,
        oauth_service: Any
    ):
        """
        Initialize WebhookManager
        
        Args:
            logger: Logger instance
            session_storage: Session storage instance
            oauth_service: OAuth service instance
        """
        self.logger = logger
        self.session_storage = session_storage
        self.oauth_service = oauth_service
    
    def subscribe(self) -> Callable:
        """
        Returns middleware for handling GoHighLevel webhooks
        For all webhooks, it will validate the webhook signature if received.
        This middleware will handle INSTALL and UNINSTALL webhooks.
        It will automatically generate token and store it for INSTALL webhook event
        It will automatically remove token for UNINSTALL webhook event

        Returns:
            Middleware function compatible with common Python frameworks
        """
        async def webhook_middleware(request: Any, *args: Any, **kwargs: Any) -> None:
            """
            Webhook middleware function that processes webhooks and continues

            Args:
                request: Request object with body, headers, method, url attributes
            """
            headers_obj = getattr(request, "headers", {})
            try:
                header_snapshot = dict(headers_obj)
            except Exception:
                header_snapshot = {}

            self.logger.debug("Webhook received", {
                "method": getattr(request, "method", "UNKNOWN"),
                "url": str(getattr(request, "url", "UNKNOWN")),
                "headers": header_snapshot,
            })

            try:
                body, raw_body_bytes = await self._extract_request_body(request)

                if not isinstance(body, dict):
                    self.logger.warn("Webhook body is not a JSON object, skipping webhook processing")
                    return

                client_id = os.environ.get("CLIENT_ID", "")
                app_id = client_id.split("-")[0] if client_id else ""

                if not app_id:
                    self.logger.warn("App ID not found, skipping webhook processing")
                    return

                if app_id != body.get("appId"):
                    self.logger.warn("App ID mismatch, skipping webhook processing")
                    return

                # Initialize request attributes for signature validation status
                if hasattr(request, "state"):
                    request.state.skipped_signature_verification = False
                    request.state.is_signature_valid = False
                else:
                    setattr(request, "skipped_signature_verification", False)
                    setattr(request, "is_signature_valid", False)

                signature = self._get_header_value(headers_obj, "x-wh-signature")
                public_key = os.environ.get("WEBHOOK_PUBLIC_KEY")

                if signature and public_key:
                    payload = self._ensure_payload_text(raw_body_bytes, body)

                    is_valid = self.verify_signature(payload, signature, public_key)

                    if hasattr(request, "state"):
                        request.state.is_signature_valid = is_valid
                    else:
                        setattr(request, "is_signature_valid", is_valid)

                    if not is_valid:
                        self.logger.warn("Invalid webhook signature")
                        return
                else:
                    self.logger.warn("Skipping signature verification - missing signature or public key")
                    if hasattr(request, "state"):
                        request.state.skipped_signature_verification = True
                    else:
                        setattr(request, "skipped_signature_verification", True)
                    return

                request_body = InstallWebhookRequest(body)
                company_id = request_body.company_id
                location_id = request_body.location_id

                if request_body.type == "INSTALL":
                    if company_id and location_id:
                        await self._generate_location_access_token(company_id, location_id)
                elif request_body.type == "UNINSTALL":
                    if location_id or company_id:
                        resource_id = location_id or company_id
                        await self.session_storage.delete_session(resource_id)

                self.logger.debug("Webhook processed successfully")

            except Exception as error:
                self.logger.error(f"Webhook processing failed: {error}")

        return webhook_middleware
    
    async def _extract_request_body(self, request: Any) -> Tuple[Any, Optional[bytes]]:
        """Extract raw bytes and JSON body from the incoming request"""
        raw_body = await self._get_raw_body(request)
        body: Any = None

        if raw_body is not None:
            try:
                decoded = raw_body.decode("utf-8")
                body = json.loads(decoded)
            except (UnicodeDecodeError, ValueError):
                body = None

        if body is None:
            body = await self._get_parsed_body(request)

        if body is None:
            body = {}

        if raw_body is None and isinstance(body, dict):
            raw_body = json.dumps(body, separators=(",", ":")).encode("utf-8")

        return body, raw_body

    async def _get_parsed_body(self, request: Any) -> Optional[Dict[str, Any]]:
        """Attempt to retrieve a parsed JSON body from common request interfaces"""
        for attr in ("json", "get_json"):
            if not hasattr(request, attr):
                continue

            candidate = getattr(request, attr)
            try:
                value = candidate() if callable(candidate) else candidate
            except TypeError:
                # Method might require args (e.g., force, silent); skip
                continue

            if inspect.isawaitable(value):
                value = await value

            if isinstance(value, (bytes, bytearray)):
                try:
                    value = json.loads(bytes(value).decode("utf-8"))
                except (UnicodeDecodeError, ValueError):
                    continue
            elif isinstance(value, str):
                try:
                    value = json.loads(value)
                except ValueError:
                    continue

            if isinstance(value, dict):
                return value
        return None

    async def _get_raw_body(self, request: Any) -> Optional[bytes]:
        """Read the raw body payload from the request if available"""
        body_sources = [
            getattr(request, "body", None),
            getattr(request, "data", None),
            getattr(request, "get_data", None),
        ]

        # Some frameworks expose a stream-like interface
        stream = getattr(request, "stream", None)
        if stream and hasattr(stream, "read"):
            body_sources.append(stream.read)

        for source in body_sources:
            if source is None:
                continue

            try:
                value = source() if callable(source) else source
            except TypeError:
                # If callable expects args, skip
                continue

            if inspect.isawaitable(value):
                value = await value

            raw_bytes = self._coerce_to_bytes(value)
            if raw_bytes is not None:
                return raw_bytes

        return None

    def _coerce_to_bytes(self, value: Any) -> Optional[bytes]:
        """Convert common body representations to bytes"""
        if value is None:
            return None
        if isinstance(value, bytes):
            return value
        if isinstance(value, bytearray):
            return bytes(value)
        if isinstance(value, str):
            return value.encode("utf-8")
        return None

    def _get_header_value(self, headers: Any, key: str) -> Optional[str]:
        """Retrieve a header value from dict-like or object headers"""
        if headers is None:
            return None

        if isinstance(headers, dict):
            return headers.get(key) or headers.get(key.lower())

        getter = getattr(headers, "get", None)
        if callable(getter):
            value = getter(key)
            if value is not None:
                return value
            return getter(key.lower())

        return None

    def _ensure_payload_text(self, raw_body: Optional[bytes], body: Dict[str, Any]) -> str:
        """Return a string payload suitable for signature verification"""
        if isinstance(raw_body, bytes):
            return raw_body.decode("utf-8", errors="replace")
        if isinstance(raw_body, bytearray):
            return bytes(raw_body).decode("utf-8", errors="replace")
        if isinstance(raw_body, str):
            return raw_body
        return json.dumps(body or {}, separators=(",", ":"))

    def verify_signature(
        self,
        payload: str,
        signature: str,
        public_key: str
    ) -> bool:
        """
        Verify webhook signature using GoHighLevel's public key
        
        Args:
            payload: The JSON stringified request body
            signature: The signature from x-wh-signature header
            public_key: The public key from environment variable
        
        Returns:
            True if signature is valid, False otherwise
        """
        try:
            self.logger.debug("Verifying webhook signature")
            
            # Load the public key
            public_key_obj = serialization.load_pem_public_key(
                public_key.encode(),
                backend=default_backend()
            )
            
            # Decode the signature
            signature_bytes = base64.b64decode(signature)
            
            # Verify the signature
            try:
                public_key_obj.verify(
                    signature_bytes,
                    payload.encode(),
                    padding.PKCS1v15(),
                    hashes.SHA256()
                )
                return True
            except Exception:
                return False
        
        except Exception as error:
            self.logger.error(f"Error verifying webhook signature: {error}")
            return False
    
    async def _generate_location_access_token(
        self,
        company_id: str,
        location_id: str
    ) -> None:
        """
        Generate location access token and store it using company token
        
        Args:
            company_id: The company ID
            location_id: The location ID
        """
        try:
            # Get the token for the company from the store
            company_token = await self.session_storage.get_access_token(company_id)
            if not company_token:
                self.logger.warn(
                    f"Company token not found for company_id: {company_id}, "
                    f"skipping location access token generation"
                )
                return
            
            self.logger.debug(f"Generating location access token for location: {location_id}")
            
            # Get location access token using OAuth service
            location_token_response = await self.oauth_service.get_location_access_token({
                "company_id": company_id,
                "location_id": location_id,
            })
            
            # Store the location token in session storage
            await self.session_storage.set_session(location_id, location_token_response)
            
            self.logger.debug(
                f"Location access token generated and stored for location: {location_id}"
            )
        except Exception as error:
            self.logger.error(f"Failed to generate location access token: {error}")
