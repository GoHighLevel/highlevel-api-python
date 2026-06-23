# @generated
# File generated from our OpenAPI spec

from __future__ import annotations
from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class Emails:
    """
    Emails Service
    Documentation for emails API

## API Version v3

All APIs available via &#x60;/v3&#x60; route prefix with AIP-compliant responses.
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def create_email_template(
        self,
        location_id: str,
        request_body: CreateTemplatePublicV2BodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateTemplatePublicV2ResponseDto:
        """
        Create an email template
        Create a new email template
        """
        param_defs = [{"name": "locationId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/emails/locations/{locationId}/templates", extracted["path"]),
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

    async def list_email_templates(
        self,
        location_id: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        search: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        archived: Optional[bool] = None,
        folder_id: Optional[str] = None,
        include: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListTemplatesPublicV2ResponseDto:
        """
        List templates
        Get list of templates by location
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "search", "in": "query"}, {"name": "sortBy", "in": "query"}, {"name": "sortOrder", "in": "query"}, {"name": "archived", "in": "query"}, {"name": "folderId", "in": "query"}, {"name": "include", "in": "query"}, ]
        extracted = extract_params({ "location_id": location_id, "limit": limit, "offset": offset, "search": search, "sort_by": sort_by, "sort_order": sort_order, "archived": archived, "folder_id": folder_id, "include": include,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/locations/{locationId}/templates", extracted["path"]),
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

    async def import_email_template(
        self,
        location_id: str,
        request_body: ImportTemplatePublicV2BodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> ImportTemplatePublicV2ResponseDto:
        """
        Import an email template
        Import a template from a provider URL
        """
        param_defs = [{"name": "locationId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/emails/locations/{locationId}/templates/import", extracted["path"]),
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

    async def create_template_folder(
        self,
        location_id: str,
        request_body: CreateTemplateFolderPublicV2BodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateTemplateFolderPublicV2ResponseDto:
        """
        Create a template folder
        Create a new template folder
        """
        param_defs = [{"name": "locationId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/emails/locations/{locationId}/templates/folders", extracted["path"]),
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

    async def get_email_template(
        self,
        location_id: str,
        template_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetTemplatePublicV2ResponseDto:
        """
        Get Email Template by ID
        Get a single email template by its ID
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "templateId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "template_id": template_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/locations/{locationId}/templates/{templateId}", extracted["path"]),
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

    async def delete_email_template(
        self,
        location_id: str,
        template_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteTemplatePublicV2ResponseDto:
        """
        Delete a template
        Delete a template
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "templateId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "template_id": template_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/emails/locations/{locationId}/templates/{templateId}", extracted["path"]),
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

    async def update_email_template(
        self,
        location_id: str,
        template_id: str,
        request_body: UpdateTemplatePublicV2BodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateTemplatePublicV2ResponseDto:
        """
        Update an email template
        Update email template
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "templateId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "template_id": template_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/emails/locations/{locationId}/templates/{templateId}", extracted["path"]),
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

    async def get_campaign_stats(
        self,
        location_id: str,
        source: str,
        source_id: str,
        sub_source_id: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetCampaignStatsPublicV2ResponseDto:
        """
        Get Campaign Statistics
        Get statistics for email campaigns, workflows, or bulk actions
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "source", "in": "path"}, {"name": "sourceId", "in": "path"}, {"name": "subSourceId", "in": "query"}, ]
        extracted = extract_params({ "location_id": location_id, "source": source, "source_id": source_id, "sub_source_id": sub_source_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/locations/{locationId}/campaigns/stats/{source}/{sourceId}", extracted["path"]),
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

    async def create_email_campaign(
        self,
        location_id: str,
        request_body: CreateEmailCampaignPublicV2BodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateEmailCampaignPublicV2ResponseDto:
        """
        Create Email Campaign
        Create a new email campaign
        """
        param_defs = [{"name": "locationId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/emails/locations/{locationId}/campaigns/emails", extracted["path"]),
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

    async def list_email_campaigns(
        self,
        location_id: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        search: Optional[str] = None,
        status: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListEmailCampaignsPublicV2ResponseDto:
        """
        List Email Campaigns
        Get list of email campaigns for a location
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "search", "in": "query"}, {"name": "status", "in": "query"}, ]
        extracted = extract_params({ "location_id": location_id, "limit": limit, "offset": offset, "search": search, "status": status,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/locations/{locationId}/campaigns/emails", extracted["path"]),
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

    async def update_email_campaign(
        self,
        location_id: str,
        campaign_id: str,
        request_body: UpdateEmailCampaignPublicV2BodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateEmailCampaignPublicV2ResponseDto:
        """
        Update Email Campaign
        Update an email campaign draft
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "campaignId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "campaign_id": campaign_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/emails/locations/{locationId}/campaigns/emails/{campaignId}", extracted["path"]),
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

    async def get_email_campaign(
        self,
        location_id: str,
        campaign_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetEmailCampaignPublicV2ResponseDto:
        """
        Get Email Campaign by ID
        Get a single email campaign by its ID
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "campaignId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "campaign_id": campaign_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/locations/{locationId}/campaigns/emails/{campaignId}", extracted["path"]),
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

    async def delete_campaign(
        self,
        location_id: str,
        campaign_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteCampaignPublicV2ResponseDto:
        """
        Delete Campaign
        Delete a campaign
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "campaignId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "campaign_id": campaign_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/emails/locations/{locationId}/campaigns/emails/{campaignId}", extracted["path"]),
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

    async def list_workflow_campaigns(
        self,
        location_id: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        search: Optional[str] = None,
        status: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListWorkflowCampaignsPublicV2ResponseDto:
        """
        List Workflow Campaigns
        Get list of workflow campaigns for a location
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "search", "in": "query"}, {"name": "status", "in": "query"}, ]
        extracted = extract_params({ "location_id": location_id, "limit": limit, "offset": offset, "search": search, "status": status,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/locations/{locationId}/campaigns/workflows", extracted["path"]),
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

    async def get_workflow_campaign(
        self,
        location_id: str,
        campaign_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetWorkflowCampaignPublicV2ResponseDto:
        """
        Get Workflow Campaign by ID
        Get a single workflow campaign by its ID
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "campaignId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "campaign_id": campaign_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/locations/{locationId}/campaigns/workflows/{campaignId}", extracted["path"]),
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

    async def list_bulk_action_campaigns(
        self,
        location_id: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        search: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        status: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListBulkActionCampaignsPublicV2ResponseDto:
        """
        List Bulk Action Campaigns
        Get list of bulk action campaigns for a location
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "search", "in": "query"}, {"name": "dateFrom", "in": "query"}, {"name": "dateTo", "in": "query"}, {"name": "status", "in": "query"}, ]
        extracted = extract_params({ "location_id": location_id, "limit": limit, "offset": offset, "search": search, "date_from": date_from, "date_to": date_to, "status": status,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/locations/{locationId}/campaigns/bulk-actions", extracted["path"]),
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

    async def get_bulk_action_campaign(
        self,
        location_id: str,
        campaign_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetBulkActionCampaignPublicV2ResponseDto:
        """
        Get Bulk Action Campaign by ID
        Get a single bulk action campaign by its ID
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "campaignId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "campaign_id": campaign_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/emails/locations/{locationId}/campaigns/bulk-actions/{campaignId}", extracted["path"]),
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

    async def schedule_campaign(
        self,
        location_id: str,
        campaign_id: str,
        request_body: ScheduleCampaignPublicV2BodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> ScheduleCampaignPublicV2ResponseDto:
        """
        Schedule Campaign
        Schedule or start an email campaign. The campaign must be in draft, cancelled, or paused status.
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "campaignId", "in": "path"}, ]
        extracted = extract_params({ "location_id": location_id, "campaign_id": campaign_id,  }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/emails/locations/{locationId}/campaigns/emails/{campaignId}/schedule", extracted["path"]),
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

