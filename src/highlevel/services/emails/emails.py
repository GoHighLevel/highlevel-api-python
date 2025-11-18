from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class Emails:
    """
    Emails Service
    Documentation for emails API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def fetch_campaigns(
        self,
        location_id: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        status: Optional[str] = None,
        email_status: Optional[str] = None,
        name: Optional[str] = None,
        parent_id: Optional[str] = None,
        limited_fields: Optional[bool] = None,
        archived: Optional[bool] = None,
        campaigns_only: Optional[bool] = None,
        show_stats: Optional[bool] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ScheduleFetchSuccessfulDTO:
        """
        Get Campaigns
        Get Campaigns
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "status", "in": "query"}, {"name": "emailStatus", "in": "query"}, {"name": "name", "in": "query"}, {"name": "parentId", "in": "query"}, {"name": "limitedFields", "in": "query"}, {"name": "archived", "in": "query"}, {"name": "campaignsOnly", "in": "query"}, {"name": "showStats", "in": "query"}, ]
        extracted = extract_params({ "location_id": location_id, "limit": limit, "offset": offset, "status": status, "email_status": email_status, "name": name, "parent_id": parent_id, "limited_fields": limited_fields, "archived": archived, "campaigns_only": campaigns_only, "show_stats": show_stats,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/schedule", extracted["path"]),
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

    async def create_template(
        self,
        request_body: CreateBuilderDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateBuilderSuccesfulResponseDto:
        """
        Create a new template
        Create a new template
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/emails/builder", extracted["path"]),
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

    async def fetch_template(
        self,
        location_id: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        search: Optional[str] = None,
        sort_by_date: Optional[str] = None,
        archived: Optional[str] = None,
        builder_version: Optional[str] = None,
        name: Optional[str] = None,
        parent_id: Optional[str] = None,
        origin_id: Optional[str] = None,
        templates_only: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> FetchBuilderSuccesfulResponseDto:
        """
        Fetch email templates
        Fetch email templates by location id
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "search", "in": "query"}, {"name": "sortByDate", "in": "query"}, {"name": "archived", "in": "query"}, {"name": "builderVersion", "in": "query"}, {"name": "name", "in": "query"}, {"name": "parentId", "in": "query"}, {"name": "originId", "in": "query"}, {"name": "templatesOnly", "in": "query"}, ]
        extracted = extract_params({ "location_id": location_id, "limit": limit, "offset": offset, "search": search, "sort_by_date": sort_by_date, "archived": archived, "builder_version": builder_version, "name": name, "parent_id": parent_id, "origin_id": origin_id, "templates_only": templates_only,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/builder", extracted["path"]),
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

    async def delete_template(
        self,
        location_id: str,
        template_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteBuilderSuccesfulResponseDto:
        """
        Delete a template
        Delete a template
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "templateId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "template_id": template_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/emails/builder/{locationId}/{templateId}", extracted["path"]),
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

    async def update_template(
        self,
        request_body: SaveBuilderDataDto,
        options: Optional[Dict[str, Any]] = None
    ) -> BuilderUpdateSuccessfulDTO:
        """
        Update a template
        Update a template
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/emails/builder/data", extracted["path"]),
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

