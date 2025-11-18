from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class SocialMediaPosting:
    """
    SocialMediaPosting Service
    Documentation for Social Media Posting API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def start_google_oauth(
        self,
        location_id: str,
        user_id: str,
        page: Optional[str] = None,
        reconnect: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Starts OAuth For Google Account
        Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Google login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener(&#x27;message&#x27;, 
      function(e) {
        if (e.data &amp;&amp; e.data.page &#x3D;&#x3D;&#x3D; &#x27;social_media_posting&#x27;) {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } &#x3D; e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: &quot;close&quot; 
      page: string,                  Ex: &quot;social-media-posting&quot; 
      platform: string,              Ex: &quot;google&quot; 
      placement: string,             Ex: &quot;placement&quot; 
      accountId: string,             Ex: &quot;658a9b6833b91e0ecb8f3958&quot; 
      reconnectAccounts: string[]]   Ex: [&quot;658a9b6833b91e0ecb834acd&quot;, &quot;efd2daa9b6833b91e0ecb8f3511&quot;] 
    }
  ### The accountId retrieved from above data can be used to fetch Google account details using below API -
  API: &#x27;/social-media-posting/oauth/google/accounts/:accountId&#x27; 

  Method: GET
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "userId", "in": "query"}, {"name": "page", "in": "query"}, {"name": "reconnect", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "user_id": user_id, "page": page, "reconnect": reconnect }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/google/start", extracted["path"]),
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

    async def get_google_locations(
        self,
        location_id: str,
        account_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetGoogleLocationResponseDTO:
        """
        Get google business locations
        Get google business locations
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/{locationId}/google/locations/{accountId}", extracted["path"]),
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

    async def set_google_locations(
        self,
        location_id: str,
        account_id: str,
        request_body: AttachGMBLocationDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> SocialMediaGmbAccountResponseDTO:
        """
        Set google business locations
        Set google business locations
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/oauth/{locationId}/google/locations/{accountId}", extracted["path"]),
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

    async def get_posts(
        self,
        location_id: str,
        request_body: SearchPostDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> PostSuccessfulResponseDTO:
        """
        Get posts
        Get Posts
        """
        param_defs = [{"name": "locationId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/{locationId}/posts/list", extracted["path"]),
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

    async def create_post(
        self,
        location_id: str,
        request_body: CreatePostDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> CreatePostSuccessfulResponseDTO:
        """
        Create post
        Create posts for all supported platforms. It is possible to create customized posts per channel by using the same platform account IDs in a request and hitting the create post API multiple times with different summaries and account IDs per platform.

The content and media limitations, as well as platform rate limiters corresponding to the respective platforms, are provided in the following reference link:

  Link: [Platform Limitations](https://help.leadconnectorhq.com/support/solutions/articles/48001240003-social-planner-image-video-content-and-api-limitations &quot;Social Planner Help&quot;)
        """
        param_defs = [{"name": "locationId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/{locationId}/posts", extracted["path"]),
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

    async def get_post(
        self,
        location_id: str,
        id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetPostSuccessfulResponseDTO:
        """
        Get post
        Get post
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "id", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/{locationId}/posts/{id}", extracted["path"]),
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

    async def edit_post(
        self,
        location_id: str,
        id: str,
        request_body: PostCreateRequest,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdatePostSuccessfulResponseDTO:
        """
        Edit post
        Create posts for all supported platforms. It is possible to create customized posts per channel by using the same platform account IDs in a request and hitting the create post API multiple times with different summaries and account IDs per platform.

The content and media limitations, as well as platform rate limiters corresponding to the respective platforms, are provided in the following reference link:

  Link: [Platform Limitations](https://help.leadconnectorhq.com/support/solutions/articles/48001240003-social-planner-image-video-content-and-api-limitations &quot;Social Planner Help&quot;)
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "id", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/social-media-posting/{locationId}/posts/{id}", extracted["path"]),
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

    async def delete_post(
        self,
        location_id: str,
        id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeletePostSuccessfulResponseDTO:
        """
        Delete Post
        Delete Post
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "id", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/social-media-posting/{locationId}/posts/{id}", extracted["path"]),
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

    async def bulk_delete_social_planner_posts(
        self,
        request_body: DeletePostsDto,
        options: Optional[Dict[str, Any]] = None
    ) -> BulkDeleteResponseDto:
        """
        Bulk Delete Social Planner Posts
        Deletes multiple posts based on the provided list of post IDs. 
                  This operation is useful for clearing up large numbers of posts efficiently. 
                  
Note: 
                  
1.The maximum number of posts that can be deleted in a single request is &#x27;50&#x27;.
                  
2.However, It will only get deleted in Highlevel database but still
                   it is recommended to be cautious of this operation.
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = []
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/{locationId}/posts/bulk-delete", extracted["path"]),
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

    async def get_account(
        self,
        location_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> AccountsListResponseDTO:
        """
        Get Accounts
        Get list of accounts and groups
        """
        param_defs = [{"name": "locationId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/{locationId}/accounts", extracted["path"]),
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

    async def delete_account(
        self,
        location_id: str,
        id: str,
        company_id: Optional[str] = None,
        user_id: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> LocationAndAccountDeleteResponseDTO:
        """
        Delete Account
        Delete account and account from group
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "id", "in": "path"}, {"name": "companyId", "in": "query"}, {"name": "userId", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "id": id, "company_id": company_id, "user_id": user_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/social-media-posting/{locationId}/accounts/{id}", extracted["path"]),
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

    async def start_facebook_oauth(
        self,
        location_id: str,
        user_id: str,
        page: Optional[str] = None,
        reconnect: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Starts OAuth For Facebook Account
        Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Facebook login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener(&#x27;message&#x27;, 
      function(e) {
        if (e.data &amp;&amp; e.data.page &#x3D;&#x3D;&#x3D; &#x27;social_media_posting&#x27;) {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } &#x3D; e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: &quot;close&quot; 
      page: string,                  Ex: &quot;social-media-posting&quot; 
      platform: string,              Ex: &quot;facebook&quot; 
      placement: string,             Ex: &quot;placement&quot; 
      accountId: string,             Ex: &quot;658a9b6833b91e0ecb8f3958&quot; 
      reconnectAccounts: string[]]   Ex: [&quot;658a9b6833b91e0ecb834acd&quot;, &quot;efd2daa9b6833b91e0ecb8f3511&quot;] 
    }
  ### The accountId retrieved from above data can be used to fetch Facebook account details using below API -
  API: &#x27;/social-media-posting/oauth/facebook/accounts/:accountId&#x27; 

  Method: GET
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "userId", "in": "query"}, {"name": "page", "in": "query"}, {"name": "reconnect", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "user_id": user_id, "page": page, "reconnect": reconnect }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/facebook/start", extracted["path"]),
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

    async def get_facebook_page_group(
        self,
        location_id: str,
        account_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetFacebookAccountsResponseDTO:
        """
        Get facebook pages
        Get facebook pages
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/{locationId}/facebook/accounts/{accountId}", extracted["path"]),
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

    async def attach_facebook_page_group(
        self,
        location_id: str,
        account_id: str,
        request_body: AttachFBAccountDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> SocialMediaFBAccountResponseDTO:
        """
        Attach facebook pages
        Attach facebook pages
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/oauth/{locationId}/facebook/accounts/{accountId}", extracted["path"]),
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

    async def start_instagram_oauth(
        self,
        location_id: str,
        user_id: str,
        page: Optional[str] = None,
        reconnect: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Starts OAuth For Instagram Account
        Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Instagram login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener(&#x27;message&#x27;, 
      function(e) {
        if (e.data &amp;&amp; e.data.page &#x3D;&#x3D;&#x3D; &#x27;social_media_posting&#x27;) {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } &#x3D; e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: &quot;close&quot; 
      page: string,                  Ex: &quot;social-media-posting&quot; 
      platform: string,              Ex: &quot;instagram&quot; 
      placement: string,             Ex: &quot;placement&quot; 
      accountId: string,             Ex: &quot;658a9b6833b91e0ecb8f3958&quot; 
      reconnectAccounts: string[]]   Ex: [&quot;658a9b6833b91e0ecb834acd&quot;, &quot;efd2daa9b6833b91e0ecb8f3511&quot;] 
    }
  ### The accountId retrieved from above data can be used to fetch Instagram account details using below API -
  API: &#x27;/social-media-posting/oauth/instagram/accounts/:accountId&#x27; 

  Method: GET
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "userId", "in": "query"}, {"name": "page", "in": "query"}, {"name": "reconnect", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "user_id": user_id, "page": page, "reconnect": reconnect }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/instagram/start", extracted["path"]),
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

    async def get_instagram_page_group(
        self,
        location_id: str,
        account_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetInstagramAccountsResponseDTO:
        """
        Get Instagram Professional Accounts
        Get Instagram Professional Accounts
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/{locationId}/instagram/accounts/{accountId}", extracted["path"]),
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

    async def attach_instagram_page_group(
        self,
        location_id: str,
        account_id: str,
        request_body: AttachIGAccountDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> SocialMediaInstagramAccountResponseDTO:
        """
        Attach Instagram Professional Accounts
        Attach Instagram Professional Accounts
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/oauth/{locationId}/instagram/accounts/{accountId}", extracted["path"]),
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

    async def start_linkedin_oauth(
        self,
        location_id: str,
        user_id: str,
        page: Optional[str] = None,
        reconnect: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Starts OAuth For LinkedIn Account
        Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to LinkedIn login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener(&#x27;message&#x27;, 
      function(e) {
        if (e.data &amp;&amp; e.data.page &#x3D;&#x3D;&#x3D; &#x27;social_media_posting&#x27;) {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } &#x3D; e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: &quot;close&quot; 
      page: string,                  Ex: &quot;social-media-posting&quot; 
      platform: string,              Ex: &quot;linkedin&quot; 
      placement: string,             Ex: &quot;placement&quot; 
      accountId: string,             Ex: &quot;658a9b6833b91e0ecb8f3958&quot; 
      reconnectAccounts: string[]]   Ex: [&quot;658a9b6833b91e0ecb834acd&quot;, &quot;efd2daa9b6833b91e0ecb8f3511&quot;] 
    }
  ### The accountId retrieved from above data can be used to fetch LinkedIn account details using below API -
  API: &#x27;/social-media-posting/oauth/linkedin/accounts/:accountId&#x27; 

  Method: GET
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "userId", "in": "query"}, {"name": "page", "in": "query"}, {"name": "reconnect", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "user_id": user_id, "page": page, "reconnect": reconnect }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/linkedin/start", extracted["path"]),
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

    async def get_linkedin_page_profile(
        self,
        location_id: str,
        account_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetLinkedInAccountsResponseDTO:
        """
        Get Linkedin pages and profile
        Get Linkedin pages and profile
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/{locationId}/linkedin/accounts/{accountId}", extracted["path"]),
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

    async def attach_linkedin_page_profile(
        self,
        location_id: str,
        account_id: str,
        request_body: AttachLinkedinAccountDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> SocialMediaLinkedInAccountResponseDTO:
        """
        Attach linkedin pages and profile
        Attach linkedin pages and profile
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/oauth/{locationId}/linkedin/accounts/{accountId}", extracted["path"]),
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

    async def start_twitter_oauth(
        self,
        location_id: str,
        user_id: str,
        page: Optional[str] = None,
        reconnect: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Starts OAuth For Twitter Account
        &lt;div&gt;&lt;div&gt;
  &lt;span style&#x3D; &quot;display: inline-block;
    width: 25px; height: 25px;
    background-color: red;
    color: black;
    font-weight: bold;
    font-size: 24px;
    text-align: center;
    line-height: 20px;
    border: 2px solid black;
    border-radius: 20%;
    margin-right: 10px;&quot;&gt;
    !
  &lt;/span&gt;
  &lt;span&gt;&lt;strong&gt;As of December 4, 2024, X (formerly Twitter) is no longer supported. We apologise for any inconvenience.&lt;/strong&gt;&lt;/span&gt;
&lt;/div&gt;&lt;/div&gt;
        
        .. deprecated::
           This method is deprecated
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "userId", "in": "query"}, {"name": "page", "in": "query"}, {"name": "reconnect", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "user_id": user_id, "page": page, "reconnect": reconnect }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/twitter/start", extracted["path"]),
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

    async def get_twitter_profile(
        self,
        location_id: str,
        account_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetTwitterAccountsResponseDTO:
        """
        Get Twitter profile
        &lt;div&gt;&lt;div&gt;
  &lt;span style&#x3D; &quot;display: inline-block;
    width: 25px; height: 25px;
    background-color: red;
    color: black;
    font-weight: bold;
    font-size: 24px;
    text-align: center;
    line-height: 20px;
    border: 2px solid black;
    border-radius: 20%;
    margin-right: 10px;&quot;&gt;
    !
  &lt;/span&gt;
  &lt;span&gt;&lt;strong&gt;As of December 4, 2024, X (formerly Twitter) is no longer supported. We apologise for any inconvenience.&lt;/strong&gt;&lt;/span&gt;
&lt;/div&gt;&lt;/div&gt;
        
        .. deprecated::
           This method is deprecated
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = []
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/{locationId}/twitter/accounts/{accountId}", extracted["path"]),
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

    async def attach_twitter_profile(
        self,
        location_id: str,
        account_id: str,
        request_body: AttachTwitterAccountDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> SocialMediaTwitterAccountResponseDTO:
        """
        Attach Twitter profile
        &lt;div&gt;&lt;div&gt;
  &lt;span style&#x3D; &quot;display: inline-block;
    width: 25px; height: 25px;
    background-color: red;
    color: black;
    font-weight: bold;
    font-size: 24px;
    text-align: center;
    line-height: 20px;
    border: 2px solid black;
    border-radius: 20%;
    margin-right: 10px;&quot;&gt;
    !
  &lt;/span&gt;
  &lt;span&gt;&lt;strong&gt;As of December 4, 2024, X (formerly Twitter) is no longer supported. We apologise for any inconvenience.&lt;/strong&gt;&lt;/span&gt;
&lt;/div&gt;&lt;/div&gt;
        
        .. deprecated::
           This method is deprecated
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = []
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/oauth/{locationId}/twitter/accounts/{accountId}", extracted["path"]),
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

    async def upload_csv(
        self,
        location_id: str,
        request_body: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None
    ) -> UploadFileResponseDTO:
        """
        Upload CSV
        
        """
        param_defs = [{"name": "locationId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/{locationId}/csv", extracted["path"]),
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

    async def get_upload_status(
        self,
        location_id: str,
        skip: Optional[str] = None,
        limit: Optional[str] = None,
        include_users: Optional[str] = None,
        user_id: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetUploadStatusResponseDTO:
        """
        Get Upload Status
        
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "skip", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "includeUsers", "in": "query"}, {"name": "userId", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "skip": skip, "limit": limit, "include_users": include_users, "user_id": user_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/{locationId}/csv", extracted["path"]),
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

    async def set_accounts(
        self,
        location_id: str,
        request_body: SetAccountsDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> SetAccountsResponseDTO:
        """
        Set Accounts
        
        """
        param_defs = [{"name": "locationId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/{locationId}/set-accounts", extracted["path"]),
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

    async def get_csv_post(
        self,
        location_id: str,
        id: str,
        skip: Optional[str] = None,
        limit: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetCsvPostResponseDTO:
        """
        Get CSV Post
        
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "id", "in": "path"}, {"name": "skip", "in": "query"}, {"name": "limit", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "id": id, "skip": skip, "limit": limit }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/{locationId}/csv/{id}", extracted["path"]),
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

    async def start_csv_finalize(
        self,
        location_id: str,
        id: str,
        request_body: CSVDefaultDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> CsvPostStatusResponseDTO:
        """
        Start CSV Finalize
        
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "id", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/social-media-posting/{locationId}/csv/{id}", extracted["path"]),
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

    async def delete_csv(
        self,
        location_id: str,
        id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteCsvResponseDTO:
        """
        Delete CSV
        
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "id", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/social-media-posting/{locationId}/csv/{id}", extracted["path"]),
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

    async def delete_csv_post(
        self,
        location_id: str,
        post_id: str,
        csv_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeletePostResponseDTO:
        """
        Delete CSV Post
        
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "postId", "in": "path"}, {"name": "csvId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "post_id": post_id, "csv_id": csv_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/social-media-posting/{locationId}/csv/{csvId}/post/{postId}", extracted["path"]),
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

    async def start_tiktok_oauth(
        self,
        location_id: str,
        user_id: str,
        page: Optional[str] = None,
        reconnect: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Starts OAuth For Tiktok Account
        Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Tiktok login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener(&#x27;message&#x27;, 
      function(e) {
        if (e.data &amp;&amp; e.data.page &#x3D;&#x3D;&#x3D; &#x27;social_media_posting&#x27;) {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } &#x3D; e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: &quot;close&quot; 
      page: string,                  Ex: &quot;social-media-posting&quot; 
      platform: string,              Ex: &quot;tiktok&quot; 
      placement: string,             Ex: &quot;placement&quot; 
      accountId: string,             Ex: &quot;658a9b6833b91e0ecb8f3958&quot; 
      reconnectAccounts: string[]]   Ex: [&quot;658a9b6833b91e0ecb834acd&quot;, &quot;efd2daa9b6833b91e0ecb8f3511&quot;] 
    }
  ### The accountId retrieved from above data can be used to fetch Tiktok account details using below API -
  API: &#x27;/social-media-posting/oauth/tiktok/accounts/:accountId&#x27; 

  Method: GET
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "userId", "in": "query"}, {"name": "page", "in": "query"}, {"name": "reconnect", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "user_id": user_id, "page": page, "reconnect": reconnect }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/tiktok/start", extracted["path"]),
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

    async def get_tiktok_profile(
        self,
        location_id: str,
        account_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetTiktokAccountResponseDTO:
        """
        Get Tiktok profile
        Get Tiktok profile
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/{locationId}/tiktok/accounts/{accountId}", extracted["path"]),
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

    async def attach_tiktok_profile(
        self,
        location_id: str,
        account_id: str,
        request_body: AttachTiktokAccountDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> SocialMediaTiktokAccountResponseDTO:
        """
        Attach Tiktok profile
        Attach Tiktok profile
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/oauth/{locationId}/tiktok/accounts/{accountId}", extracted["path"]),
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

    async def start_tiktok_business_oauth(
        self,
        location_id: str,
        user_id: str,
        page: Optional[str] = None,
        reconnect: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Starts OAuth For Tiktok Business Account
        Open the API in a window with appropriate params and headers instead of using the Curl. User is navigated to Tiktok-Business login OAuth screen. On successful login, listen on window object for message where event listener returns data in its callback function. 
  ### Sample code to listen to event data:
    window.addEventListener(&#x27;message&#x27;, 
      function(e) {
        if (e.data &amp;&amp; e.data.page &#x3D;&#x3D;&#x3D; &#x27;social_media_posting&#x27;) {
        const { actionType, page, platform, placement, accountId, reconnectAccounts } &#x3D; e.data
        }
      },
    false)
  ### Event Data Response:
    {
      actionType: string,            Ex: &quot;close&quot; 
      page: string,                  Ex: &quot;social-media-posting&quot; 
      platform: string,              Ex: &quot;tiktok-business&quot; 
      placement: string,             Ex: &quot;placement&quot; 
      accountId: string,             Ex: &quot;658a9b6833b91e0ecb8f3958&quot; 
      reconnectAccounts: string[]]   Ex: [&quot;658a9b6833b91e0ecb834acd&quot;, &quot;efd2daa9b6833b91e0ecb8f3511&quot;] 
    }
  ### The accountId retrieved from above data can be used to fetch Tiktok-Business account details using below API -
  API: &#x27;/social-media-posting/oauth/tiktok-business/accounts/:accountId&#x27; 

  Method: GET
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "userId", "in": "query"}, {"name": "page", "in": "query"}, {"name": "reconnect", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "user_id": user_id, "page": page, "reconnect": reconnect }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/tiktok-business/start", extracted["path"]),
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

    async def get_tiktok_business_profile(
        self,
        location_id: str,
        account_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetTiktokBusinessAccountResponseDTO:
        """
        Get Tiktok Business profile
        Get Tiktok Business profile
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "accountId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id, "account_id": account_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/oauth/{locationId}/tiktok-business/accounts/{accountId}", extracted["path"]),
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

    async def get_categories_location_id(
        self,
        location_id: str,
        search_text: Optional[str] = None,
        limit: Optional[str] = None,
        skip: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetByLocationIdResponseDTO:
        """
        Get categories by location id
        
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "searchText", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "skip", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "search_text": search_text, "limit": limit, "skip": skip }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/{locationId}/categories", extracted["path"]),
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

    async def get_categories_id(
        self,
        id: str,
        location_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetByIdResponseDTO:
        """
        Get categories by id
        
        """
        param_defs = [{"name": "id", "in": "path"}, {"name": "locationId", "in": "path"}]
        extracted = extract_params({ "id": id, "location_id": location_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/{locationId}/categories/{id}", extracted["path"]),
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

    async def get_tags_location_id(
        self,
        location_id: str,
        search_text: Optional[str] = None,
        limit: Optional[str] = None,
        skip: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetTagsByLocationIdResponseDTO:
        """
        Get tags by location id
        
        """
        param_defs = [{"name": "locationId", "in": "path"}, {"name": "searchText", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "skip", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "search_text": search_text, "limit": limit, "skip": skip }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/social-media-posting/{locationId}/tags", extracted["path"]),
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

    async def get_tags_by_ids(
        self,
        location_id: str,
        request_body: UpdateTagDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> GetTagsByIdResponseDTO:
        """
        Get tags by ids
        
        """
        param_defs = [{"name": "locationId", "in": "path"}]
        extracted = extract_params({ "location_id": location_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/{locationId}/tags/details", extracted["path"]),
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

    async def get_social_media_statistics(
        self,
        location_id: str,
        request_body: Optional[Dict[str, Any]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Get Social Media Statistics
        Retrieve analytics data for multiple social media accounts. Provides metrics for the last 7 days with comparison to the previous 7 days. Supports filtering by platforms and specific connected accounts.
        """
        param_defs = [{"name": "locationId", "in": "query"}]
        extracted = extract_params({ "location_id": location_id }, param_defs)
        requirements = []
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/social-media-posting/statistics", extracted["path"]),
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

