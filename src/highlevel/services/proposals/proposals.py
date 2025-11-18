from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class Proposals:
    """
    Proposals Service
    Documentation for Documents and Contracts API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def list_documents_contracts(
        self,
        location_id: str,
        status: Optional[str] = None,
        payment_status: Optional[str] = None,
        limit: Optional[float] = None,
        skip: Optional[float] = None,
        query: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> DocumentListResponseDto:
        """
        List documents
        List documents for a location
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "status", "in": "query"}, {"name": "paymentStatus", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "skip", "in": "query"}, {"name": "query", "in": "query"}, {"name": "dateFrom", "in": "query"}, {"name": "dateTo", "in": "query"}, ]
        extracted = extract_params({ "location_id": location_id, "status": status, "payment_status": payment_status, "limit": limit, "skip": skip, "query": query, "date_from": date_from, "date_to": date_to,  }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/proposals/document", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            "__preferred_token_type": options.get("preferred_token_type") if options else None,
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})
        
        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {},
            config.get("__preferred_token_type")
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
            setattr(request, "__preferred_token_type", config.get("__preferred_token_type"))
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

    async def send_documents_contracts(
        self,
        request_body: SendDocumentDto,
        options: Optional[Dict[str, Any]] = None
    ) -> SendDocumentResponseDto:
        """
        Send document
        Send document to a client
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/proposals/document/send", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            "__preferred_token_type": options.get("preferred_token_type") if options else None,
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})
        
        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body,
            config.get("__preferred_token_type")
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
            setattr(request, "__preferred_token_type", config.get("__preferred_token_type"))
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

    async def list_documents_contracts_templates(
        self,
        location_id: str,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        type: Optional[str] = None,
        name: Optional[str] = None,
        is_public_document: Optional[bool] = None,
        user_id: Optional[str] = None,
        limit: Optional[str] = None,
        skip: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> TemplateListPaginationResponseDTO:
        """
        List templates
        List document contract templates for a location
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "dateFrom", "in": "query"}, {"name": "dateTo", "in": "query"}, {"name": "type", "in": "query"}, {"name": "name", "in": "query"}, {"name": "isPublicDocument", "in": "query"}, {"name": "userId", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "skip", "in": "query"}, ]
        extracted = extract_params({ "location_id": location_id, "date_from": date_from, "date_to": date_to, "type": type, "name": name, "is_public_document": is_public_document, "user_id": user_id, "limit": limit, "skip": skip,  }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/proposals/templates", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            
            "__security_requirements": requirements,
            "__preferred_token_type": options.get("preferred_token_type") if options else None,
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})
        
        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            {},
            config.get("__preferred_token_type")
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
            setattr(request, "__preferred_token_type", config.get("__preferred_token_type"))
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

    async def send_documents_contracts_template(
        self,
        request_body: SendDocumentFromPublicApiBodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> SendTemplateResponseDto:
        """
        Send template
        Send template to a client
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/proposals/templates/send", extracted["path"]),
            "params": extracted["query"],
            "headers": {**extracted["header"], **(options.get("headers", {}) if options else {})},
            "data": request_body,
            "__security_requirements": requirements,
            "__preferred_token_type": options.get("preferred_token_type") if options else None,
            "__path_params": extracted["path"],
        }
        
        if options:
            config.update({k: v for k, v in options.items() if k not in ["headers", "preferred_token_type"]})
        
        auth_token = await get_auth_token(
            self.ghl_instance,
            requirements,
            config["headers"],
            {**config["params"], **config["__path_params"]},
            request_body,
            config.get("__preferred_token_type")
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
            setattr(request, "__preferred_token_type", config.get("__preferred_token_type"))
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

