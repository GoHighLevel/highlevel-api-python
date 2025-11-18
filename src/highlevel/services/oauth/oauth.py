from typing import Any, Dict, Optional, List
from urllib.parse import urlencode
import httpx
from .models import *
from ...constants import UserType, UserTypeValue
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig


class Oauth:
    """
    Oauth Service
    Documentation for OAuth 2.0 API
    """
    
    MARKETPLACE_URL = "https://marketplace.gohighlevel.com"
    
    def __init__(self, ghl_instance, config: Optional[Dict[str, Any]] = None):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client
        self.config = config or {}
    
    def get_authorization_url(self, client_id: str, redirect_uri: str, scope: str) -> str:
        """Generate OAuth authorization URL for the authorization code flow"""
        params = {
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "scope": scope,
            "response_type": "code"
        }
        return f"{self.MARKETPLACE_URL}/oauth/chooselocation?{urlencode(params)}"
    
    async def refresh_token(
        self,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        grant_type: str,
        user_type: str
    ) -> Any:
        """
        Refresh access token using refresh token
        
        Args:
            refresh_token: The refresh token
            client_id: OAuth client ID
            client_secret: OAuth client secret
            grant_type: Grant type (must be 'refresh_token')
            user_type: User type (UserType.LOCATION or UserType.COMPANY)
        """
        if grant_type != "refresh_token":
            raise ValueError('grant_type must be "refresh_token"')
        
        if user_type not in [UserType.LOCATION, UserType.COMPANY]:
            raise ValueError(f'user_type must be "{UserType.LOCATION}" or "{UserType.COMPANY}"')
        
        return await self.get_access_token({
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
            "user_type": user_type
        })

    async def get_access_token(
        self,
        request_body: GetAccessCodebodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Get Access Token
        Use Access Tokens to access GoHighLevel resources on behalf of an authenticated location/company.
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = []
        
        is_form_data = True
        processed_body = urlencode(request_body) if request_body else None
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/oauth/token", extracted["path"]),
            "params": extracted["query"],
            "headers": {
                
                "Content-Type": "application/x-www-form-urlencoded",
                
                **extracted["header"],
                **(options.get("headers", {}) if options else {})
            },
            "data": processed_body,
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
        
        response = await self.client.request(
            method=config["method"],
            url=config["url"],
            params=config["params"],
            headers=config["headers"],
            data=config.get("data"),
        )
        
        await response.aread()
        return response.json()

    async def get_location_access_token(
        self,
        request_body: GetLocationAccessCodeBodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Get Location Access Token from Agency Token
        This API allows you to generate locationAccessToken from AgencyAccessToken
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Agency-Access-Only"]
        
        is_form_data = True
        processed_body = urlencode(request_body) if request_body else None
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/oauth/locationToken", extracted["path"]),
            "params": extracted["query"],
            "headers": {
                
                "Content-Type": "application/x-www-form-urlencoded",
                
                **extracted["header"],
                **(options.get("headers", {}) if options else {})
            },
            "data": processed_body,
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
        
        response = await self.client.request(
            method=config["method"],
            url=config["url"],
            params=config["params"],
            headers=config["headers"],
            data=config.get("data"),
        )
        
        await response.aread()
        return response.json()

    async def get_installed_location(
        self,
        company_id: str,
        app_id: str,
        skip: Optional[str] = None,
        limit: Optional[str] = None,
        query: Optional[str] = None,
        is_installed: Optional[bool] = None,
        version_id: Optional[str] = None,
        on_trial: Optional[bool] = None,
        plan_id: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Get Location where app is installed
        This API allows you fetch location where app is installed upon
        """
        param_defs = [{"name": "skip", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "query", "in": "query"}, {"name": "isInstalled", "in": "query"}, {"name": "companyId", "in": "query"}, {"name": "appId", "in": "query"}, {"name": "versionId", "in": "query"}, {"name": "onTrial", "in": "query"}, {"name": "planId", "in": "query"}, ]
        extracted = extract_params({ "skip": skip, "limit": limit, "query": query, "is_installed": is_installed, "company_id": company_id, "app_id": app_id, "version_id": version_id, "on_trial": on_trial, "plan_id": plan_id,  }, param_defs)
        requirements = ["Agency-Access"]
        
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/oauth/installedLocations", extracted["path"]),
            "params": extracted["query"],
            "headers": {
                
                **extracted["header"],
                **(options.get("headers", {}) if options else {})
            },
            
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
        
        response = await self.client.request(
            method=config["method"],
            url=config["url"],
            params=config["params"],
            headers=config["headers"],
            
        )
        
        await response.aread()
        return response.json()


