# @generated
# File generated from our OpenAPI spec

from __future__ import annotations
from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class Conversations:
    """
    Conversations Service
    Documentation for Conversations API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def search_conversation(
        self,
        location_id: str,
        contact_id: Optional[str] = None,
        assigned_to: Optional[str] = None,
        followers: Optional[str] = None,
        mentions: Optional[str] = None,
        query: Optional[str] = None,
        sort: Optional[str] = None,
        start_after_date: Optional[Any] = None,
        id: Optional[str] = None,
        limit: Optional[float] = None,
        last_message_type: Optional[str] = None,
        last_message_action: Optional[str] = None,
        last_message_direction: Optional[str] = None,
        status: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_score_profile: Optional[str] = None,
        score_profile: Optional[str] = None,
        score_profile_min: Optional[float] = None,
        score_profile_max: Optional[float] = None,
        start_date: Optional[float] = None,
        end_date: Optional[float] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> SendConversationResponseDto:
        """
        Search Conversations
        Returns a list of all conversations matching the search criteria along with the sort and filter options selected.
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "contactId", "in": "query"}, {"name": "assignedTo", "in": "query"}, {"name": "followers", "in": "query"}, {"name": "mentions", "in": "query"}, {"name": "query", "in": "query"}, {"name": "sort", "in": "query"}, {"name": "startAfterDate", "in": "query"}, {"name": "id", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "lastMessageType", "in": "query"}, {"name": "lastMessageAction", "in": "query"}, {"name": "lastMessageDirection", "in": "query"}, {"name": "status", "in": "query"}, {"name": "sortBy", "in": "query"}, {"name": "sortScoreProfile", "in": "query"}, {"name": "scoreProfile", "in": "query"}, {"name": "scoreProfileMin", "in": "query"}, {"name": "scoreProfileMax", "in": "query"}, {"name": "startDate", "in": "query"}, {"name": "endDate", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "contact_id": contact_id, "assigned_to": assigned_to, "followers": followers, "mentions": mentions, "query": query, "sort": sort, "start_after_date": start_after_date, "id": id, "limit": limit, "last_message_type": last_message_type, "last_message_action": last_message_action, "last_message_direction": last_message_direction, "status": status, "sort_by": sort_by, "sort_score_profile": sort_score_profile, "score_profile": score_profile, "score_profile_min": score_profile_min, "score_profile_max": score_profile_max, "start_date": start_date, "end_date": end_date }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/conversations/search", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def get_conversation(
        self,
        conversation_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetConversationByIdResponse:
        """
        Get Conversation
        Get the conversation details based on the conversation ID
        """
        param_defs = [{"name": "conversationId", "in": "path"}]
        extracted = extract_params({ "conversation_id": conversation_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/conversations/{conversationId}", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def update_conversation(
        self,
        conversation_id: str,
        request_body: UpdateConversationDto,
        options: Optional[Dict[str, Any]] = None
    ) -> GetConversationSuccessfulResponse:
        """
        Update Conversation
        Update the conversation details based on the conversation ID
        """
        param_defs = [{"name": "conversationId", "in": "path"}]
        extracted = extract_params({ "conversation_id": conversation_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/conversations/{conversationId}", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def delete_conversation(
        self,
        conversation_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteConversationSuccessfulResponse:
        """
        Delete Conversation
        Delete the conversation details based on the conversation ID
        """
        param_defs = [{"name": "conversationId", "in": "path"}]
        extracted = extract_params({ "conversation_id": conversation_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/conversations/{conversationId}", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def get_email_by_id(
        self,
        options: Optional[Dict[str, Any]] = None
    ) -> GetEmailMessageResponseDto:
        """
        Get email by Id
        Get email by Id
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/conversations/messages/email/{id}", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def cancel_scheduled_email_message(
        self,
        email_message_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> CancelScheduledResponseDto:
        """
        Cancel a scheduled email message.
        Post the messageId for the API to delete a scheduled email message. &lt;br /&gt;
        """
        param_defs = [{"name": "emailMessageId", "in": "path"}]
        extracted = extract_params({ "email_message_id": email_message_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/conversations/messages/email/{emailMessageId}/schedule", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def update_email_message_status(
        self,
        id: str,
        request_body: UpdateEmailMessageStatusDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateEmailMessageStatusResponseDto:
        """
        Update email message status
        Update delivery events, per-recipient statuses, and the overall message status for an email sent via a custom conversation provider.

### Authorization
- Requires the &#x60;conversations/message.write&#x60; OAuth scope.
- The calling OAuth app must own the conversation provider that originally sent the email.
- Attempts to update emails sent via LC Email or Mailgun will return &#x60;403 Forbidden&#x60;.

### Updatable Fields
**&#x60;status&#x60;** is required on every request. You may also include **&#x60;events&#x60;** and/or **&#x60;recipients&#x60;**.

**&#x60;events&#x60;** — Aggregate delivery event counters (integers). Counters are merged into the existing values (not replaced). Setting a counter to &#x60;0&#x60; is treated as no-op and will **not** reset the stored value.

**&#x60;recipients&#x60;** — Per-recipient delivery statuses. Each entry maps a recipient email address to a &#x60;MessageStatus&#x60; value. Use &#x60;failReason&#x60; to capture bounce or rejection details when the status is &#x60;failed&#x60;.

**&#x60;status&#x60;** — The overall message status. Accepts any &#x60;MessageStatus&#x60; enum value.

### Event Inference
The API automatically infers related events to maintain data consistency:
- **&#x60;clicked&#x60;, &#x60;complained&#x60;, &#x60;unsubscribed&#x60;, or &#x60;replied&#x60;** → implies &#x60;opened&#x60; (set to 1 if not already provided and open tracking is enabled) and &#x60;delivered&#x60; (set to 1).
- **&#x60;opened&#x60;** → implies &#x60;delivered&#x60; (set to 1 if not provided).
- **&#x60;delivered&#x60;, &#x60;permanent_fail&#x60;, or &#x60;temporary_fail&#x60;** → implies &#x60;accepted&#x60; (set to 1 if not provided).

### Timestamps
The API automatically records server-side timestamps on first occurrence for &#x60;delivered&#x60;, &#x60;opened&#x60;, and &#x60;clicked&#x60; events. Subsequent updates to these counters do not overwrite the original timestamp.
        """
        param_defs = [{"name": "id", "in": "path"}]
        extracted = extract_params({ "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/conversations/messages/email/{id}/status", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def export_messages_by_location(
        self,
        location_id: str,
        limit: Optional[float] = None,
        cursor: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        conversation_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        channel: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ExportMessagesResponseDto:
        """
        Export messages by location ID
        Export messages for a specific location with cursor-based pagination support. Response includes messageType (string), source, and subType fields. The channel parameter is optional - if not provided, all non-email message types will be returned including activity messages (opportunity updates, appointments, etc.).
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "cursor", "in": "query"}, {"name": "sortBy", "in": "query"}, {"name": "sortOrder", "in": "query"}, {"name": "conversationId", "in": "query"}, {"name": "contactId", "in": "query"}, {"name": "channel", "in": "query"}, {"name": "startDate", "in": "query"}, {"name": "endDate", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "limit": limit, "cursor": cursor, "sort_by": sort_by, "sort_order": sort_order, "conversation_id": conversation_id, "contact_id": contact_id, "channel": channel, "start_date": start_date, "end_date": end_date }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/conversations/messages/export", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def get_message(
        self,
        options: Optional[Dict[str, Any]] = None
    ) -> GetMessageResponseDto:
        """
        Get message by message id
        Get message by message id.
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/conversations/messages/{id}", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def get_messages(
        self,
        conversation_id: str,
        last_message_id: Optional[str] = None,
        limit: Optional[float] = None,
        type: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetMessagesByConversationResponseDto:
        """
        Get messages by conversation id
        Get messages by conversation id.
        """
        param_defs = [{"name": "conversationId", "in": "path"}, {"name": "lastMessageId", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "type", "in": "query"}]
        extracted = extract_params({ "conversation_id": conversation_id, "last_message_id": last_message_id, "limit": limit, "type": type }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/conversations/{conversationId}/messages", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def send_a_new_message(
        self,
        request_body: SendMessageBodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> SendMessageResponseDto:
        """
        Send a new message
        Post the necessary fields for the API to send a new message.
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/conversations/messages", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def add_an_inbound_message(
        self,
        request_body: ProcessMessageBodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> ProcessMessageResponseDto:
        """
        Add an inbound message
        Post the necessary fields for the API to add a new inbound message. &lt;br /&gt;
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/conversations/messages/inbound", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def add_an_outbound_message(
        self,
        request_body: ProcessOutboundMessageBodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> ProcessMessageResponseDto:
        """
        Add an external outbound call
        Post the necessary fields for the API to add a new outbound call.
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/conversations/messages/outbound", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def cancel_scheduled_message(
        self,
        message_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> CancelScheduledResponseDto:
        """
        Cancel a scheduled message.
        Post the messageId for the API to delete a scheduled message. &lt;br /&gt;
        """
        param_defs = [{"name": "messageId", "in": "path"}]
        extracted = extract_params({ "message_id": message_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/conversations/messages/{messageId}/schedule", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def upload_file_attachments(
        self,
        request_body: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None
    ) -> UploadFilesResponseDto:
        """
        Upload file attachments
        Post the necessary fields for the API to upload files. The files need to be a buffer with the key &quot;fileAttachment&quot;. &lt;br /&gt;&lt;br /&gt; The allowed file types are: &lt;br/&gt; &lt;ul&gt;&lt;li&gt;JPG&lt;/li&gt;&lt;li&gt;JPEG&lt;/li&gt;&lt;li&gt;PNG&lt;/li&gt;&lt;li&gt;MP4&lt;/li&gt;&lt;li&gt;MPEG&lt;/li&gt;&lt;li&gt;ZIP&lt;/li&gt;&lt;li&gt;RAR&lt;/li&gt;&lt;li&gt;PDF&lt;/li&gt;&lt;li&gt;DOC&lt;/li&gt;&lt;li&gt;DOCX&lt;/li&gt;&lt;li&gt;TXT&lt;/li&gt;&lt;li&gt;MP3&lt;/li&gt;&lt;li&gt;WAV&lt;/li&gt;&lt;/ul&gt; &lt;br /&gt;&lt;br /&gt; The API will return an object with the URLs
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/conversations/messages/upload", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def update_message_status(
        self,
        message_id: str,
        request_body: UpdateMessageStatusDto,
        options: Optional[Dict[str, Any]] = None
    ) -> SendMessageResponseDto:
        """
        Update message status
        Post the necessary fields for the API to update message status.
        """
        param_defs = [{"name": "messageId", "in": "path"}]
        extracted = extract_params({ "message_id": message_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/conversations/messages/{messageId}/status", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def add_message_attachments(
        self,
        message_id: str,
        request_body: AddMessageAttachmentsDto,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Add message attachments
        Set attachments on an existing message (replaces existing). Maximum 5 URLs. Supported for TYPE_CUSTOM_CALL (34) and TYPE_CALL (1) with subType EXTERNAL_CALL.
        """
        param_defs = [{"name": "messageId", "in": "path"}]
        extracted = extract_params({ "message_id": message_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/conversations/messages/{messageId}/attachments", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def get_message_recording(
        self,
        location_id: str,
        message_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Get Recording by Message ID
        Get the recording for a message by passing the message id
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "messageId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "message_id": message_id }, param_defs)
        requirements = ["bearer","Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/conversations/messages/{messageId}/locations/{locationId}/recording", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def get_message_transcription(
        self,
        location_id: str,
        message_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetMessageTranscriptionResponseDto:
        """
        Get transcription by Message ID
        Get the recording transcription for a message by passing the message id
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "messageId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "message_id": message_id }, param_defs)
        requirements = ["bearer","Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/conversations/locations/{locationId}/messages/{messageId}/transcription", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def download_message_transcription(
        self,
        location_id: str,
        message_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Download transcription by Message ID
        Download the recording transcription for a message by passing the message id
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "messageId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "message_id": message_id }, param_defs)
        requirements = ["bearer","Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/conversations/locations/{locationId}/messages/{messageId}/transcription/download", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {}
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def live_chat_agent_typing(
        self,
        request_body: UserTypingBody,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateLiveChatMessageFeedbackResponse:
        """
        Agent/Ai-Bot is typing a message indicator for live chat
        Agent/AI-Bot will call this when they are typing a message in live chat message
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/conversations/providers/live-chat/typing", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def create_conversation(
        self,
        request_body: CreateConversationDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateConversationSuccessResponse:
        """
        Create Conversation
        Creates a new conversation with the data provided
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/conversations/", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def send_review_reply(
        self,
        request_body: SendReviewReplyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> SendMessageResponseDto:
        """
        Send a review reply to Google My Business
        Post a reply to a customer review on Google My Business

This endpoint is internal-only and is not supported for OAuth or public API integrations. It will be removed from the public OpenAPI specification in a future release.
        
        .. deprecated::
           This method is deprecated
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/conversations/messages/review-reply", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def initiate_file_upload(
        self,
        request_body: InitiateFileUploadDto,
        options: Optional[Dict[str, Any]] = None
    ) -> InitiateFileUploadResponseDto:
        """
        Initiate file upload to GCS
        Generates a signed URL for direct file upload to Google Cloud Storage. Returns a signed URL valid for 15 minutes. Upload file via PUT request, then call /complete to finalize.

This endpoint is internal-only and is not supported for OAuth or public API integrations. It will be removed from the public OpenAPI specification in a future release.
        
        .. deprecated::
           This method is deprecated
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/conversations/messages/upload/initiate", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

    async def complete_file_upload(
        self,
        request_body: CompleteFileUploadDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CompleteFileUploadResponseDto:
        """
        Complete file upload
        Validates the uploaded file in GCS and returns the public URL. Call this endpoint after successfully uploading the file to the signed URL.

This endpoint is internal-only and is not supported for OAuth or public API integrations. It will be removed from the public OpenAPI specification in a future release.
        
        .. deprecated::
           This method is deprecated
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/conversations/messages/upload/complete", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})

        # Lock the Version header to the SDK's API version; user options cannot override it.
        config["headers"]["Version"] = self.ghl_instance.API_VERSION

        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body
        )
        
        if auth_token:
            config["headers"]["Authorization"] = auth_token
        
        try:
            request_kwargs = {
                "method": config["method"],
                "url": config["url"],
                "params": config["params"],
                "headers": config["headers"],
            }
            request_kwargs["json"] = config.get("data")

            request = self.client.build_request(**request_kwargs)
            setattr(request, "__security_requirements", requirements)
            setattr(request, "__path_params", config["__path_params"])
            
            request_kwargs_copy = {k: (dict(v) if isinstance(v, dict) else v) for k, v in request_kwargs.items()}
            setattr(request, "__request_kwargs", request_kwargs_copy)

            send_kwargs = {}
            for option_key in ["timeout", "follow_redirects", "stream", "auth"]:
                if option_key in config:
                    send_kwargs[option_key] = config[option_key]
            setattr(request, "__send_kwargs", dict(send_kwargs))

            response = await self.client.send(request, **send_kwargs)
            return response.json()

        except httpx.RequestError as e:
            # Handle network/request errors
            raise GHLError(
                f"Network error: {str(e)}",
                None,
                None,
                config
            ) from e

