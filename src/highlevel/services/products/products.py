from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class Products:
    """
    Products Service
    Documentation for products API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def bulk_update(
        self,
        request_body: BulkUpdateDto,
        options: Optional[Dict[str, Any]] = None
    ) -> BulkUpdateResponseDto:
        """
        Bulk Update Products
        API to bulk update products (price, availability, collections, delete)
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/products/bulk-update", extracted["path"]),
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

    async def bulk_edit(
        self,
        request_body: BulkEditRequestDto,
        options: Optional[Dict[str, Any]] = None
    ) -> BulkEditResponseDto:
        """
        Bulk Edit Products and Prices
        API to bulk edit products and their associated prices (max 30 entities)
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = []
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/products/bulk-update/edit", extracted["path"]),
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

    async def create_price_for_product(
        self,
        product_id: str,
        request_body: CreatePriceDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreatePriceResponseDto:
        """
        Create Price for a Product
        The &quot;Create Price for a Product&quot; API allows adding a new price associated with a specific product to the system. Use this endpoint to create a price with the specified details for a particular product. Ensure that the required information is provided in the request payload.
        """
        param_defs = [{"name": "productId", "in": "path"}]
        extracted = extract_params({ "product_id": product_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/products/{productId}/price", extracted["path"]),
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

    async def list_prices_for_product(
        self,
        product_id: str,
        location_id: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        ids: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListPricesResponseDto:
        """
        List Prices for a Product
        The &quot;List Prices for a Product&quot; API allows retrieving a paginated list of prices associated with a specific product. Customize your results by filtering prices or paginate through the list using the provided query parameters.
        """
        param_defs = [{"name": "productId", "in": "path"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "locationId", "in": "query"}, {"name": "ids", "in": "query"}]
        extracted = extract_params({ "product_id": product_id, "limit": limit, "offset": offset, "location_id": location_id, "ids": ids }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/{productId}/price", extracted["path"]),
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

    async def get_list_inventory(
        self,
        alt_id: str,
        alt_type: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        search: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetInventoryResponseDto:
        """
        List Inventory
        The &quot;List Inventory API allows the user to retrieve a paginated list of inventory items. Use this endpoint to fetch details for multiple items in the inventory based on the provided query parameters.
        """
        param_defs = [{"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "search", "in": "query"}]
        extracted = extract_params({ "limit": limit, "offset": offset, "alt_id": alt_id, "alt_type": alt_type, "search": search }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/inventory", extracted["path"]),
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

    async def update_inventory(
        self,
        request_body: UpdateInventoryDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateInventoryResponseDto:
        """
        Update Inventory
        The Update Inventory API allows the user to bulk update the inventory for multiple items. Use this endpoint to update the available quantity and out-of-stock purchase settings for multiple items in the inventory.
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/products/inventory", extracted["path"]),
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

    async def get_price_by_id_for_product(
        self,
        product_id: str,
        price_id: str,
        location_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetPriceResponseDto:
        """
        Get Price by ID for a Product
        The &quot;Get Price by ID for a Product&quot; API allows retrieving information for a specific price associated with a particular product using its unique identifier. Use this endpoint to fetch details for a single price based on the provided price ID and product ID.
        """
        param_defs = [{"name": "productId", "in": "path"}, {"name": "priceId", "in": "path"}, {"name": "locationId", "in": "query"}]
        extracted = extract_params({ "product_id": product_id, "price_id": price_id, "location_id": location_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/{productId}/price/{priceId}", extracted["path"]),
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

    async def update_price_by_id_for_product(
        self,
        product_id: str,
        price_id: str,
        request_body: UpdatePriceDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdatePriceResponseDto:
        """
        Update Price by ID for a Product
        The &quot;Update Price by ID for a Product&quot; API allows modifying information for a specific price associated with a particular product using its unique identifier. Use this endpoint to update details for a single price based on the provided price ID and product ID.
        """
        param_defs = [{"name": "productId", "in": "path"}, {"name": "priceId", "in": "path"}]
        extracted = extract_params({ "product_id": product_id, "price_id": price_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/products/{productId}/price/{priceId}", extracted["path"]),
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

    async def delete_price_by_id_for_product(
        self,
        product_id: str,
        price_id: str,
        location_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeletePriceResponseDto:
        """
        Delete Price by ID for a Product
        The &quot;Delete Price by ID for a Product&quot; API allows deleting a specific price associated with a particular product using its unique identifier. Use this endpoint to remove a price from the system.
        """
        param_defs = [{"name": "productId", "in": "path"}, {"name": "priceId", "in": "path"}, {"name": "locationId", "in": "query"}]
        extracted = extract_params({ "product_id": product_id, "price_id": price_id, "location_id": location_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/products/{productId}/price/{priceId}", extracted["path"]),
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

    async def get_product_store_stats(
        self,
        store_id: str,
        alt_id: str,
        alt_type: str,
        search: Optional[str] = None,
        collection_ids: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetProductStatsResponseDto:
        """
        Fetch Product Store Stats
        API to fetch the total number of products, included in the store, and excluded from the store and other stats
        """
        param_defs = [{"name": "storeId", "in": "path"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "search", "in": "query"}, {"name": "collectionIds", "in": "query"}]
        extracted = extract_params({ "store_id": store_id, "alt_id": alt_id, "alt_type": alt_type, "search": search, "collection_ids": collection_ids }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/store/{storeId}/stats", extracted["path"]),
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

    async def update_store_status(
        self,
        store_id: str,
        request_body: UpdateProductStoreDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateProductStoreResponseDto:
        """
        Action to include/exclude the product in store
        API to update the status of products in a particular store
        """
        param_defs = [{"name": "storeId", "in": "path"}]
        extracted = extract_params({ "store_id": store_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/products/store/{storeId}", extracted["path"]),
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

    async def update_display_priority(
        self,
        store_id: str,
        request_body: UpdateDisplayPriorityBodyDto,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Update product display priorities in store
        API to set the display priority of products in a store
        """
        param_defs = [{"name": "storeId", "in": "path"}]
        extracted = extract_params({ "store_id": store_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/products/store/{storeId}/priority", extracted["path"]),
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

    async def get_product_collection(
        self,
        alt_id: str,
        alt_type: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        collection_ids: Optional[str] = None,
        name: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListCollectionResponseDto:
        """
        Fetch Product Collections
        Internal API to fetch the Product Collections
        """
        param_defs = [{"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "collectionIds", "in": "query"}, {"name": "name", "in": "query"}]
        extracted = extract_params({ "limit": limit, "offset": offset, "alt_id": alt_id, "alt_type": alt_type, "collection_ids": collection_ids, "name": name }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/collections", extracted["path"]),
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

    async def create_product_collection(
        self,
        request_body: CreateProductCollectionsDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateCollectionResponseDto:
        """
        Create Product Collection
        Create a new Product Collection for a specific location
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/products/collections", extracted["path"]),
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

    async def get_product_collection_id(
        self,
        collection_id: str,
        alt_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DefaultCollectionResponseDto:
        """
        Get Details about individual product collection
        Get Details about individual product collection
        """
        param_defs = [{"name": "collectionId", "in": "path"}, {"name": "altId", "in": "query"}]
        extracted = extract_params({ "collection_id": collection_id, "alt_id": alt_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/collections/{collectionId}", extracted["path"]),
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

    async def update_product_collection(
        self,
        collection_id: str,
        request_body: UpdateProductCollectionsDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateProductCollectionResponseDto:
        """
        Update Product Collection
        Update a specific product collection with Id :collectionId
        """
        param_defs = [{"name": "collectionId", "in": "path"}]
        extracted = extract_params({ "collection_id": collection_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/products/collections/{collectionId}", extracted["path"]),
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

    async def delete_product_collection(
        self,
        collection_id: str,
        alt_id: str,
        alt_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteProductCollectionResponseDto:
        """
        Delete Product Collection
        Delete specific product collection with Id :collectionId
        """
        param_defs = [{"name": "collectionId", "in": "path"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}]
        extracted = extract_params({ "collection_id": collection_id, "alt_id": alt_id, "alt_type": alt_type }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/products/collections/{collectionId}", extracted["path"]),
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

    async def get_product_reviews(
        self,
        alt_id: str,
        alt_type: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = None,
        rating: Optional[float] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        product_id: Optional[str] = None,
        store_id: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListProductReviewsResponseDto:
        """
        Fetch Product Reviews
        API to fetch the Product Reviews
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "sortField", "in": "query"}, {"name": "sortOrder", "in": "query"}, {"name": "rating", "in": "query"}, {"name": "startDate", "in": "query"}, {"name": "endDate", "in": "query"}, {"name": "productId", "in": "query"}, {"name": "storeId", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type, "limit": limit, "offset": offset, "sort_field": sort_field, "sort_order": sort_order, "rating": rating, "start_date": start_date, "end_date": end_date, "product_id": product_id, "store_id": store_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/reviews", extracted["path"]),
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

    async def get_reviews_count(
        self,
        alt_id: str,
        alt_type: str,
        rating: Optional[float] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        product_id: Optional[str] = None,
        store_id: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> CountReviewsByStatusResponseDto:
        """
        Fetch Review Count as per status
        API to fetch the Review Count as per status
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "rating", "in": "query"}, {"name": "startDate", "in": "query"}, {"name": "endDate", "in": "query"}, {"name": "productId", "in": "query"}, {"name": "storeId", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type, "rating": rating, "start_date": start_date, "end_date": end_date, "product_id": product_id, "store_id": store_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/reviews/count", extracted["path"]),
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

    async def update_product_review(
        self,
        review_id: str,
        request_body: UpdateProductReviewDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateProductReviewsResponseDto:
        """
        Update Product Reviews
        Update status, reply, etc of a particular review
        """
        param_defs = [{"name": "reviewId", "in": "path"}]
        extracted = extract_params({ "review_id": review_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/products/reviews/{reviewId}", extracted["path"]),
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

    async def delete_product_review(
        self,
        review_id: str,
        alt_id: str,
        alt_type: str,
        product_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteProductReviewResponseDto:
        """
        Delete Product Review
        Delete specific product review
        """
        param_defs = [{"name": "reviewId", "in": "path"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "productId", "in": "query"}]
        extracted = extract_params({ "review_id": review_id, "alt_id": alt_id, "alt_type": alt_type, "product_id": product_id }, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/products/reviews/{reviewId}", extracted["path"]),
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

    async def bulk_update_product_review(
        self,
        request_body: UpdateProductReviewsDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateProductReviewsResponseDto:
        """
        Update Product Reviews
        Update one or multiple product reviews: status, reply, etc.
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/products/reviews/bulk-update", extracted["path"]),
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

    async def get_product_by_id(
        self,
        product_id: str,
        location_id: str,
        send_wishlist_status: Optional[bool] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> GetProductResponseDto:
        """
        Get Product by ID
        The &quot;Get Product by ID&quot; API allows to retrieve information for a specific product using its unique identifier. Use this endpoint to fetch details for a single product based on the provided product ID.
        """
        param_defs = [{"name": "productId", "in": "path"}, {"name": "locationId", "in": "query"}, {"name": "sendWishlistStatus", "in": "query"}]
        extracted = extract_params({ "product_id": product_id, "location_id": location_id, "send_wishlist_status": send_wishlist_status }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/{productId}", extracted["path"]),
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

    async def delete_product_by_id(
        self,
        product_id: str,
        location_id: str,
        send_wishlist_status: Optional[bool] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteProductResponseDto:
        """
        Delete Product by ID
        The &quot;Delete Product by ID&quot; API allows deleting a specific product using its unique identifier. Use this endpoint to remove a product from the system.
        """
        param_defs = [{"name": "productId", "in": "path"}, {"name": "locationId", "in": "query"}, {"name": "sendWishlistStatus", "in": "query"}]
        extracted = extract_params({ "product_id": product_id, "location_id": location_id, "send_wishlist_status": send_wishlist_status }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/products/{productId}", extracted["path"]),
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

    async def update_product_by_id(
        self,
        product_id: str,
        request_body: UpdateProductDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateProductResponseDto:
        """
        Update Product by ID
        The &quot;Update Product by ID&quot; API allows modifying information for a specific product using its unique identifier. Use this endpoint to update details for a single product based on the provided product ID.
        """
        param_defs = [{"name": "productId", "in": "path"}]
        extracted = extract_params({ "product_id": product_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/products/{productId}", extracted["path"]),
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

    async def create_product(
        self,
        request_body: CreateProductDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateProductResponseDto:
        """
        Create Product
        The &quot;Create Product&quot; API allows adding a new product to the system. Use this endpoint to create a product with the specified details. Ensure that the required information is provided in the request payload.
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/products/", extracted["path"]),
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

    async def list_invoices(
        self,
        location_id: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        search: Optional[str] = None,
        collection_ids: Optional[str] = None,
        collection_slug: Optional[str] = None,
        expand: Optional[List[str]] = None,
        product_ids: Optional[List[str]] = None,
        store_id: Optional[str] = None,
        included_in_store: Optional[bool] = None,
        available_in_store: Optional[bool] = None,
        sort_order: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListProductsResponseDto:
        """
        List Products
        The &quot;List Products&quot; API allows to retrieve a paginated list of products. Customize your results by filtering products based on name or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve product information.
        """
        param_defs = [{"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "locationId", "in": "query"}, {"name": "search", "in": "query"}, {"name": "collectionIds", "in": "query"}, {"name": "collectionSlug", "in": "query"}, {"name": "expand", "in": "query"}, {"name": "productIds", "in": "query"}, {"name": "storeId", "in": "query"}, {"name": "includedInStore", "in": "query"}, {"name": "availableInStore", "in": "query"}, {"name": "sortOrder", "in": "query"}]
        extracted = extract_params({ "limit": limit, "offset": offset, "location_id": location_id, "search": search, "collection_ids": collection_ids, "collection_slug": collection_slug, "expand": expand, "product_ids": product_ids, "store_id": store_id, "included_in_store": included_in_store, "available_in_store": available_in_store, "sort_order": sort_order }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/products/", extracted["path"]),
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

