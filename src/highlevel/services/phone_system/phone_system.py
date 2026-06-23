# @generated
# File generated from our OpenAPI spec

from __future__ import annotations
from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class PhoneSystem:
    """
    PhoneSystem Service
    API Service for LC Phone - version v3
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def get_number_pool_list(
        self,
        location_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        List number pools
        Returns number pools for the location. Requires locationId as a query parameter.
        """
        param_defs = [{"name": "locationId", "in": "query"}]
        extracted = extract_params({ "location_id": location_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/phone-system/number-pools", extracted["path"]),
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

    async def list_available_numbers_for_a_country(
        self,
        first_part: str,
        last_part: str,
        anywhere: str,
        number_types: List[str],
        sms_enabled: bool,
        mms_enabled: bool,
        voice_enabled: bool,
        country_code: str,
        location_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        List available phone numbers
        Search Twilio inventory for purchasable phone numbers in a country for the given location.
        """
        param_defs = [{"name": "firstPart", "in": "query"}, {"name": "lastPart", "in": "query"}, {"name": "anywhere", "in": "query"}, {"name": "numberTypes", "in": "query"}, {"name": "smsEnabled", "in": "query"}, {"name": "mmsEnabled", "in": "query"}, {"name": "voiceEnabled", "in": "query"}, {"name": "countryCode", "in": "query"}, {"name": "locationId", "in": "path"}]
        extracted = extract_params({ "first_part": first_part, "last_part": last_part, "anywhere": anywhere, "number_types": number_types, "sms_enabled": sms_enabled, "mms_enabled": mms_enabled, "voice_enabled": voice_enabled, "country_code": country_code, "location_id": location_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/phone-system/numbers/location/{locationId}/available", extracted["path"]),
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

    async def purchase_number_for_location(
        self,
        location_id: str,
        version: str,
        request_body: PurchasePhoneNumberBodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> PurchaseNumberForLocationV3Http201ResponseDto:
        """
        Purchase number for location
        Purchase number for location. With &#x60;version: v3&#x60;, the HTTP 201 body is the standard success envelope (&#x60;status&#x60;, &#x60;data&#x60;, &#x60;message&#x60;, &#x60;statusCode&#x60;). The v3 purchase fields live under &#x60;data&#x60;: &#x60;number&#x60;, &#x60;locationId&#x60;, &#x60;id&#x60;, and &#x60;underLcAccount&#x60; (renamed from under_ghl_account).
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "version", "in": "header"}]
        extracted = extract_params({ "location_id": location_id, "version": version }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/phone-system/numbers/location/{locationId}/purchase", extracted["path"]),
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

    async def active_numbers(
        self,
        location_id: str,
        version: str,
        page_size: Optional[float] = None,
        page: Optional[float] = None,
        search_filter: Optional[str] = None,
        skip_number_pool: Optional[bool] = None,
        include_rcs_sender_ids: Optional[bool] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListNumbersV3Http200ResponseDto:
        """
        List active numbers
        List active numbers. With &#x60;version: v3&#x60;, the HTTP 200 body is the standard success envelope (&#x60;status&#x60;, &#x60;data&#x60;, &#x60;message&#x60;, &#x60;statusCode&#x60;). The v3 list payload is under &#x60;data&#x60;; &#x60;isUnderGhl&#x60; is renamed to &#x60;isUnderLc&#x60; per AIP naming convention.
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "pageSize", "in": "query"}, {"name": "page", "in": "query"}, {"name": "searchFilter", "in": "query"}, {"name": "skipNumberPool", "in": "query"}, {"name": "includeRcsSenderIds", "in": "query"}, {"name": "version", "in": "header"}]
        extracted = extract_params({ "location_id": location_id, "page_size": page_size, "page": page, "search_filter": search_filter, "skip_number_pool": skip_number_pool, "include_rcs_sender_ids": include_rcs_sender_ids, "version": version }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/phone-system/numbers/location/{locationId}", extracted["path"]),
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

