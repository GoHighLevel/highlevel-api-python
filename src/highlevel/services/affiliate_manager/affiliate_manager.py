# @generated
# File generated from our OpenAPI spec

from __future__ import annotations
from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class AffiliateManager:
    """
    AffiliateManager Service
    Documentation for Affiliate Manager API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def list_affiliates(
        self,
        location_id: str,
        query: Optional[str] = None,
        active: Optional[str] = None,
        campaign_id: Optional[str] = None,
        skip: Optional[float] = None,
        limit: Optional[float] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListAffiliatesResponseDto:
        """
        List Affiliates
        Retrieve the list of affiliates for a location.
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "query", "in": "query"}, {"name": "active", "in": "query"}, {"name": "campaignId", "in": "query"}, {"name": "skip", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "fromDate", "in": "query"}, {"name": "toDate", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "query": query, "active": active, "campaign_id": campaign_id, "skip": skip, "limit": limit, "from_date": from_date, "to_date": to_date }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/affiliate-manager/{locationId}/affiliates", extracted["path"]),
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

    async def get_affiliate(
        self,
        location_id: str,
        affiliate_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetAffiliateResponseDto:
        """
        Get Affiliate
        Retrieve a single affiliate by id for a location.
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "affiliateId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "affiliate_id": affiliate_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/affiliate-manager/{locationId}/affiliates/{affiliateId}", extracted["path"]),
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

    async def list_payouts(
        self,
        location_id: str,
        status: Optional[str] = None,
        query: Optional[str] = None,
        affiliate_id: Optional[str] = None,
        campaign_id: Optional[str] = None,
        skip: Optional[float] = None,
        limit: Optional[float] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetPayoutListResponseDto:
        """
        List Payouts
        Retrieve the list of payouts for a location.
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "status", "in": "query"}, {"name": "query", "in": "query"}, {"name": "affiliateId", "in": "query"}, {"name": "campaignId", "in": "query"}, {"name": "skip", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "start", "in": "query"}, {"name": "end", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "status": status, "query": query, "affiliate_id": affiliate_id, "campaign_id": campaign_id, "skip": skip, "limit": limit, "start": start, "end": end }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/affiliate-manager/{locationId}/payouts", extracted["path"]),
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

    async def list_commissions(
        self,
        location_id: str,
        campaign_id: Optional[str] = None,
        affiliate_id: Optional[str] = None,
        status: Optional[str] = None,
        query: Optional[str] = None,
        skip: Optional[float] = None,
        limit: Optional[float] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetCommissionListResponseDto:
        """
        List Commissions
        Retrieve the list of commissions for a location.
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "campaignId", "in": "query"}, {"name": "affiliateId", "in": "query"}, {"name": "status", "in": "query"}, {"name": "query", "in": "query"}, {"name": "skip", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "fromDate", "in": "query"}, {"name": "toDate", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "campaign_id": campaign_id, "affiliate_id": affiliate_id, "status": status, "query": query, "skip": skip, "limit": limit, "from_date": from_date, "to_date": to_date }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/affiliate-manager/{locationId}/commissions", extracted["path"]),
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

