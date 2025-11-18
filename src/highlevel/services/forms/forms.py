from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class Forms:
    """
    Forms Service
    Documentation for forms API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def get_forms_submissions(
        self,
        location_id: str,
        page: Optional[float] = None,
        limit: Optional[float] = None,
        form_id: Optional[str] = None,
        q: Optional[str] = None,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> FormsSubmissionsSuccessfulResponseDto:
        """
        Get Forms Submissions
        Get Forms Submissions
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "page", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "formId", "in": "query"}, {"name": "q", "in": "query"}, {"name": "startAt", "in": "query"}, {"name": "endAt", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "page": page, "limit": limit, "form_id": form_id, "q": q, "start_at": start_at, "end_at": end_at }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/forms/submissions", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})
        
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

    async def upload_to_custom_fields(
        self,
        contact_id: str,
        location_id: str,
        request_body: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Upload files to custom fields
        Post the necessary fields for the API to upload files. The files need to be a buffer with the key &quot;&lt; custom_field_id &gt;_&lt; file_id &gt;&quot;. &lt;br /&gt; Here custom field id is the ID of your custom field and file id is a randomly generated id (or uuid) &lt;br /&gt; There is support for multiple file uploads as well. Have multiple fields in the format mentioned.&lt;br /&gt;File size is limited to 50 MB.&lt;br /&gt;&lt;br /&gt; The allowed file types are: &lt;br/&gt; &lt;ul&gt;&lt;li&gt;PDF&lt;/li&gt;&lt;li&gt;DOCX&lt;/li&gt;&lt;li&gt;DOC&lt;/li&gt;&lt;li&gt;JPG&lt;/li&gt;&lt;li&gt;JPEG&lt;/li&gt;&lt;li&gt;PNG&lt;/li&gt;&lt;li&gt;GIF&lt;/li&gt;&lt;li&gt;CSV&lt;/li&gt;&lt;li&gt;XLSX&lt;/li&gt;&lt;li&gt;XLS&lt;/li&gt;&lt;li&gt;MP4&lt;/li&gt;&lt;li&gt;MPEG&lt;/li&gt;&lt;li&gt;ZIP&lt;/li&gt;&lt;li&gt;RAR&lt;/li&gt;&lt;li&gt;TXT&lt;/li&gt;&lt;li&gt;SVG&lt;/li&gt;&lt;/ul&gt; &lt;br /&gt;&lt;br /&gt; The API will return the updated contact object.
        """
        param_defs = [{"name": "contactId", "in": "query"}, {"name": "locationId", "in": "query"}]
        extracted = extract_params({ "contact_id": contact_id, "location_id": location_id }, param_defs)
        requirements = ["bearer","Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/forms/upload-custom-files", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})
        
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

    async def get_forms(
        self,
        location_id: str,
        skip: Optional[float] = None,
        limit: Optional[float] = None,
        type: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> FormsSuccessfulResponseDto:
        """
        Get Forms
        Get Forms
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "skip", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "type", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "skip": skip, "limit": limit, "type": type }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/forms/", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})
        
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

