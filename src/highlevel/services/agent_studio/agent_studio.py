# @generated
# File generated from our OpenAPI spec

from __future__ import annotations
from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class AgentStudio:
    """
    AgentStudio Service
    Documentation for Agent Studio APIs
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def create_agent(
        self,
        request_body: CreatePublicAgentDTO,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> CreatePublicAgentResponseDTO:
        """
        Create Agent
        Creates a new agent with staging version. The agent will be created with an initial staging version that can later be promoted to production. 
        """
        param_defs = [{"name": "source", "in": "query"}]
        extracted = extract_params({ "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/agent-studio/agent", extracted["path"]),
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

    async def get_agents(
        self,
        location_id: str,
        limit: str,
        offset: str,
        is_published: Optional[str] = None,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetPublishedAgentsResponseDTO:
        """
        List Agents
        Lists all active agents for the specified location. locationId is required parameter to ensure optimal performance. Supports pagination using limit and offset. Optionally filter by isPublished&#x3D;true to return only agents with a published production version.
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "isPublished", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "is_published": is_published, "limit": limit, "offset": offset, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/agent-studio/agent", extracted["path"]),
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

    async def update_agent_version(
        self,
        version_id: str,
        request_body: UpdatePublicAgentVersionDTO,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdatePublicAgentResponseDTO:
        """
        Update Agent
        Updates a specific agent version by versionId. Supports updating nodes, edges, variables, and configuration. 
        """
        param_defs = [{"name": "versionId", "in": "path"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "version_id": version_id, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/agent-studio/agent/versions/{versionId}", extracted["path"]),
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

    async def update_agent_metadata(
        self,
        agent_id: str,
        request_body: UpdatePublicAgentMetadataDTO,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdatePublicAgentResponseDTO:
        """
        Update Agent Metadata
        Updates agent metadata such as name, description, and status. 
        """
        param_defs = [{"name": "agentId", "in": "path"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "agent_id": agent_id, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/agent-studio/agent/{agentId}", extracted["path"]),
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

    async def delete_agent(
        self,
        agent_id: str,
        location_id: str,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> DeletePublicAgentResponseDTO:
        """
        Delete Agent
        Deletes an agent and all its versions. 
        """
        param_defs = [{"name": "agentId", "in": "path"}, {"name": "locationId", "in": "query"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "agent_id": agent_id, "location_id": location_id, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/agent-studio/agent/{agentId}", extracted["path"]),
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

    async def get_agent_by_id(
        self,
        agent_id: str,
        location_id: str,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetAgentByIdResponseDTO:
        """
        Get Agent
        Gets a specific agent by its ID for the specified location with all its versions. Returns complete agent metadata and all non-deleted versions (draft, staging, production). locationId is required parameter. The agent must have active status.
        """
        param_defs = [{"name": "agentId", "in": "path"}, {"name": "locationId", "in": "query"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "agent_id": agent_id, "location_id": location_id, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/agent-studio/agent/{agentId}", extracted["path"]),
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

    async def promote_and_publish(
        self,
        version_id: str,
        request_body: PromoteAndPublishDTO,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> PromoteAndPublishResponseDTO:
        """
        Promote to Production
        Promotes a draft version to production.
        """
        param_defs = [{"name": "versionId", "in": "path"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "version_id": version_id, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/agent-studio/agent/versions/{versionId}/publish", extracted["path"]),
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

    async def execute_agent(
        self,
        agent_id: str,
        request_body: ExecutePublicAgentDTO,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ExecutePublicAgentResponseDTO:
        """
        Execute Agent
        Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body. 

**Session Management:**
- For the first message in a new session, do not include the &#x60;executionId&#x60; in the request payload.
- The API will return an &#x60;executionId&#x60; along with the agent response, which uniquely identifies this conversation session.
- To continue the conversation within the same session, include the &#x60;executionId&#x60; from the previous response in subsequent requests. This allows the agent to maintain conversation context and history across multiple interactions.
        """
        param_defs = [{"name": "agentId", "in": "path"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "agent_id": agent_id, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/agent-studio/agent/{agentId}/execute", extracted["path"]),
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

    async def get_agents_deprecated(
        self,
        location_id: str,
        limit: str,
        offset: str,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetPublishedAgentsResponseDTO:
        """
        List Agents (Deprecated)
        **Deprecated endpoint - use GET /agent instead.**

Lists all active agents that have a published production version for the specified location. locationId is required parameter. Supports pagination using limit and offset.
        
        .. deprecated::
           Deprecated endpoint - use GET /agent instead. Use GET /agent instead instead.
        """
        param_defs = [{"name": "locationId", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "location_id": location_id, "limit": limit, "offset": offset, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/agent-studio/public-api/agents", extracted["path"]),
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

    async def get_agent_by_id_deprecated(
        self,
        agent_id: str,
        location_id: str,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetAgentByIdResponseDTO:
        """
        Get Agent (Deprecated)
        **Deprecated endpoint - use GET /agent/:agentId instead.**

Gets a specific agent by its ID for the specified location with all its versions. locationId is required parameter. The agent must have active status.
        
        .. deprecated::
           Deprecated endpoint - use GET /agent/:agentId instead. Use GET /agent/:agentId instead instead.
        """
        param_defs = [{"name": "agentId", "in": "path"}, {"name": "locationId", "in": "query"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "agent_id": agent_id, "location_id": location_id, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/agent-studio/public-api/agents/{agentId}", extracted["path"]),
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

    async def execute_agent_deprecated(
        self,
        agent_id: str,
        request_body: ExecutePublicAgentDTO,
        source: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ExecutePublicAgentResponseDTO:
        """
        Execute Agent (Deprecated)
        **Deprecated endpoint - use POST /agent/:agentId/execute instead.**

Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body. 

**Session Management:**
- For the first message in a new session, do not include the &#x60;executionId&#x60; in the request payload.
- The API will return an &#x60;executionId&#x60; along with the agent response, which uniquely identifies this conversation session.
- To continue the conversation within the same session, include the &#x60;executionId&#x60; from the previous response in subsequent requests.
        
        .. deprecated::
           Deprecated endpoint - use POST /agent/:agentId/execute instead. Use POST /agent/:agentId/execute instead instead.
        """
        param_defs = [{"name": "agentId", "in": "path"}, {"name": "source", "in": "query"}]
        extracted = extract_params({ "agent_id": agent_id, "source": source }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/agent-studio/public-api/agents/{agentId}/execute", extracted["path"]),
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

