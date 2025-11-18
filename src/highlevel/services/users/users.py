from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class Users:
    """
    Users Service
    Documentation for users API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def search_users(
        self,
        company_id: str,
        query: Optional[str] = None,
        skip: Optional[str] = None,
        limit: Optional[str] = None,
        location_id: Optional[str] = None,
        type: Optional[str] = None,
        role: Optional[str] = None,
        ids: Optional[str] = None,
        sort: Optional[str] = None,
        sort_direction: Optional[str] = None,
        enabled2way_sync: Optional[bool] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> SearchUserSuccessfulResponseDto:
        """
        Search Users
        Search Users
        """
        param_defs = [{"name": "companyId", "in": "query"}, {"name": "query", "in": "query"}, {"name": "skip", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "locationId", "in": "query"}, {"name": "type", "in": "query"}, {"name": "role", "in": "query"}, {"name": "ids", "in": "query"}, {"name": "sort", "in": "query"}, {"name": "sortDirection", "in": "query"}, {"name": "enabled2waySync", "in": "query"}]
        extracted = extract_params({ "company_id": company_id, "query": query, "skip": skip, "limit": limit, "location_id": location_id, "type": type, "role": role, "ids": ids, "sort": sort, "sort_direction": sort_direction, "enabled2way_sync": enabled2way_sync }, param_defs)
        requirements = ["Agency-Access","Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/users/search", extracted["path"]),
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

    async def filter_users_by_email(
        self,
        request_body: FilterByEmailDto,
        options: Optional[Dict[str, Any]] = None
    ) -> SearchUserSuccessfulResponseDto:
        """
        Filter Users by Email
        Filter users by company ID, deleted status, and email array
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Agency-Access","Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/users/search/filter-by-email", extracted["path"]),
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

    async def get_user(
        self,
        user_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> UserSuccessfulResponseDto:
        """
        Get User
        Get User
        """
        param_defs = [{"name": "userId", "in": "path"}]
        extracted = extract_params({ "user_id": user_id }, param_defs)
        requirements = ["Agency-Access","Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/users/{userId}", extracted["path"]),
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

    async def update_user(
        self,
        request_body: UpdateUserDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UserSuccessfulResponseDto:
        """
        Update User
        Update User
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Agency-Access","Location-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/users/{userId}", extracted["path"]),
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

    async def delete_user(
        self,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteUserSuccessfulResponseDto:
        """
        Delete User
        Delete User
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Agency-Access","Location-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/users/{userId}", extracted["path"]),
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

    async def get_user_by_location(
        self,
        location_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> LocationSuccessfulResponseDto:
        """
        Get User by Location
        Get User by Location
        """
        param_defs = [{"name": "locationId", "in": "query"}]
        extracted = extract_params({ "location_id": location_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/users/", extracted["path"]),
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

    async def create_user(
        self,
        request_body: CreateUserDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UserSuccessfulResponseDto:
        """
        Create User
        Create User
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Agency-Access","Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/users/", extracted["path"]),
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

