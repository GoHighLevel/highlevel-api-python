from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class CustomFields:
    """
    CustomFields Service
    Custom fields are data points that allow you to capture and store specific information tailored to your business requirements. You can create fields across field types like text, numeric, selection options and special fields like date/time or signature
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def get_custom_field_by_id(
        self,
        id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> CustomFieldSuccessfulResponseDto:
        """
        Get Custom Field / Folder By Id
        &lt;div&gt;
                  &lt;p&gt; Get Custom Field / Folder By Id.&lt;/p&gt; 
                  &lt;div&gt;
                    &lt;span style&#x3D; &quot;display: inline-block;
                                width: 25px; height: 25px;
                                background-color: yellow;
                                color: black;
                                font-weight: bold;
                                font-size: 24px;
                                text-align: center;
                                line-height: 22px;
                                border: 2px solid black;
                                border-radius: 10%;
                                margin-right: 10px;&quot;&gt;
                                !
                      &lt;/span&gt;
                      &lt;span&gt;
                        &lt;strong&gt;
                        Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
                        &lt;/strong&gt;
                      &lt;/span&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
        """
        param_defs = [{"name": "id", "in": "path"}]
        extracted = extract_params({ "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/custom-fields/{id}", extracted["path"]),
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

    async def update_custom_field(
        self,
        id: str,
        request_body: UpdateCustomFieldsDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> CustomFieldSuccessfulResponseDto:
        """
        Update Custom Field By Id
        &lt;div&gt;
    &lt;p&gt; Update Custom Field By Id &lt;/p&gt; 
    &lt;div&gt;
      &lt;span style&#x3D; &quot;display: inline-block;
                  width: 25px; height: 25px;
                  background-color: yellow;
                  color: black;
                  font-weight: bold;
                  font-size: 24px;
                  text-align: center;
                  line-height: 22px;
                  border: 2px solid black;
                  border-radius: 10%;
                  margin-right: 10px;&quot;&gt;
                  !
        &lt;/span&gt;
        &lt;span&gt;
          &lt;strong&gt;
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          &lt;/strong&gt;
        &lt;/span&gt;
    &lt;/div&gt;
  &lt;/div&gt;
        """
        param_defs = [{"name": "id", "in": "path"}]
        extracted = extract_params({ "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/custom-fields/{id}", extracted["path"]),
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

    async def delete_custom_field(
        self,
        id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> CustomFolderDeleteResponseDto:
        """
        Delete Custom Field By Id
        &lt;div&gt;
    &lt;p&gt; Delete Custom Field By Id &lt;/p&gt; 
    &lt;div&gt;
      &lt;span style&#x3D; &quot;display: inline-block;
                  width: 25px; height: 25px;
                  background-color: yellow;
                  color: black;
                  font-weight: bold;
                  font-size: 24px;
                  text-align: center;
                  line-height: 22px;
                  border: 2px solid black;
                  border-radius: 10%;
                  margin-right: 10px;&quot;&gt;
                  !
        &lt;/span&gt;
        &lt;span&gt;
          &lt;strong&gt;
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          &lt;/strong&gt;
        &lt;/span&gt;
    &lt;/div&gt;
  &lt;/div&gt;
        """
        param_defs = [{"name": "id", "in": "path"}]
        extracted = extract_params({ "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/custom-fields/{id}", extracted["path"]),
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

    async def get_custom_fields_by_object_key(
        self,
        object_key: str,
        location_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> CustomFieldsResponseDTO:
        """
        Get Custom Fields By Object Key
        &lt;div&gt;
                  &lt;p&gt; Get Custom Fields By Object Key&lt;/p&gt; 
                  &lt;div&gt;
                    &lt;span style&#x3D; &quot;display: inline-block;
                                width: 25px; height: 25px;
                                background-color: yellow;
                                color: black;
                                font-weight: bold;
                                font-size: 24px;
                                text-align: center;
                                line-height: 22px;
                                border: 2px solid black;
                                border-radius: 10%;
                                margin-right: 10px;&quot;&gt;
                                !
                      &lt;/span&gt;
                      &lt;span&gt;
                        &lt;strong&gt;
                        Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
                        &lt;/strong&gt;
                      &lt;/span&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
        """
        param_defs = [{"name": "objectKey", "in": "path"}, {"name": "locationId", "in": "query"}]
        extracted = extract_params({ "object_key": object_key, "location_id": location_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/custom-fields/object-key/{objectKey}", extracted["path"]),
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

    async def create_custom_field_folder(
        self,
        request_body: CreateFolder,
        options: Optional[Dict[str, Any]] = None
    ) -> ICustomFieldFolder:
        """
        Create Custom Field Folder
        &lt;div&gt;
    &lt;p&gt; Create Custom Field Folder &lt;/p&gt; 
    &lt;div&gt;
      &lt;span style&#x3D; &quot;display: inline-block;
                  width: 25px; height: 25px;
                  background-color: yellow;
                  color: black;
                  font-weight: bold;
                  font-size: 24px;
                  text-align: center;
                  line-height: 22px;
                  border: 2px solid black;
                  border-radius: 10%;
                  margin-right: 10px;&quot;&gt;
                  !
        &lt;/span&gt;
        &lt;span&gt;
          &lt;strong&gt;
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          &lt;/strong&gt;
        &lt;/span&gt;
    &lt;/div&gt;
  &lt;/div&gt;
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/custom-fields/folder", extracted["path"]),
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

    async def update_custom_field_folder(
        self,
        id: str,
        request_body: UpdateFolder,
        options: Optional[Dict[str, Any]] = None
    ) -> ICustomFieldFolder:
        """
        Update Custom Field Folder Name
        &lt;div&gt;
    &lt;p&gt; Create Custom Field Folder &lt;/p&gt; 
    &lt;div&gt;
      &lt;span style&#x3D; &quot;display: inline-block;
                  width: 25px; height: 25px;
                  background-color: yellow;
                  color: black;
                  font-weight: bold;
                  font-size: 24px;
                  text-align: center;
                  line-height: 22px;
                  border: 2px solid black;
                  border-radius: 10%;
                  margin-right: 10px;&quot;&gt;
                  !
        &lt;/span&gt;
        &lt;span&gt;
          &lt;strong&gt;
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          &lt;/strong&gt;
        &lt;/span&gt;
    &lt;/div&gt;
  &lt;/div&gt;
        """
        param_defs = [{"name": "id", "in": "path"}]
        extracted = extract_params({ "id": id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/custom-fields/folder/{id}", extracted["path"]),
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

    async def delete_custom_field_folder(
        self,
        id: str,
        location_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> CustomFolderDeleteResponseDto:
        """
        Delete Custom Field Folder
        &lt;div&gt;
    &lt;p&gt; Create Custom Field Folder &lt;/p&gt; 
    &lt;div&gt;
      &lt;span style&#x3D; &quot;display: inline-block;
                  width: 25px; height: 25px;
                  background-color: yellow;
                  color: black;
                  font-weight: bold;
                  font-size: 24px;
                  text-align: center;
                  line-height: 22px;
                  border: 2px solid black;
                  border-radius: 10%;
                  margin-right: 10px;&quot;&gt;
                  !
        &lt;/span&gt;
        &lt;span&gt;
          &lt;strong&gt;
          Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
          &lt;/strong&gt;
        &lt;/span&gt;
    &lt;/div&gt;
  &lt;/div&gt;
        """
        param_defs = [{"name": "id", "in": "path"}, {"name": "locationId", "in": "query"}]
        extracted = extract_params({ "id": id, "location_id": location_id }, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/custom-fields/folder/{id}", extracted["path"]),
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

    async def create_custom_field(
        self,
        request_body: CreateCustomFieldsDTO,
        options: Optional[Dict[str, Any]] = None
    ) -> CustomFieldSuccessfulResponseDto:
        """
        Create Custom Field
        &lt;div&gt;
                  &lt;p&gt; Create Custom Field &lt;/p&gt; 
                  &lt;div&gt;
                    &lt;span style&#x3D; &quot;display: inline-block;
                                width: 25px; height: 25px;
                                background-color: yellow;
                                color: black;
                                font-weight: bold;
                                font-size: 24px;
                                text-align: center;
                                line-height: 22px;
                                border: 2px solid black;
                                border-radius: 10%;
                                margin-right: 10px;&quot;&gt;
                                !
                      &lt;/span&gt;
                      &lt;span&gt;
                        &lt;strong&gt;
                        Only supports Custom Objects and Company (Business) today. Will be extended to other Standard Objects in the future.
                        &lt;/strong&gt;
                      &lt;/span&gt;
                  &lt;/div&gt;
                &lt;/div&gt;
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["bearer"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/custom-fields/", extracted["path"]),
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

