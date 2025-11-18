from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class Surveys:
    """
    Surveys Service
    Documentation for surveys API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def get_surveys_submissions(
        self,
        location_id: str,
        page: Optional[float] = None,
        limit: Optional[float] = None,
        survey_id: Optional[str] = None,
        q: Optional[str] = None,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetSurveysSubmissionSuccessfulResponseDto:
        """
        Get Surveys Submissions
        Get Surveys Submissions
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "page", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "surveyId", "in": "query"}, {"name": "q", "in": "query"}, {"name": "startAt", "in": "query"}, {"name": "endAt", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "page": page, "limit": limit, "survey_id": survey_id, "q": q, "start_at": start_at, "end_at": end_at }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/surveys/submissions", extracted["path"]),
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

    async def get_surveys(
        self,
        location_id: str,
        skip: Optional[float] = None,
        limit: Optional[float] = None,
        type: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetSurveysSuccessfulResponseDto:
        """
        Get Surveys
        Get Surveys
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "skip", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "type", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "skip": skip, "limit": limit, "type": type }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/surveys/", extracted["path"]),
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

