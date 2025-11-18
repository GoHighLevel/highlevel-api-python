from typing import Any, Dict, Optional, List
import httpx
from .models import *
from ...utils.request_utils import build_url, extract_params, get_auth_token, RequestConfig
from ...error import GHLError


class Invoices:
    """
    Invoices Service
    Documentation for invoice API
    """

    def __init__(self, ghl_instance):
        self.ghl_instance = ghl_instance
        self.client = ghl_instance.http_client

    async def create_invoice_template(
        self,
        request_body: CreateInvoiceTemplateDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateInvoiceTemplateResponseDto:
        """
        Create template
        API to create a template
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/template", extracted["path"]),
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

    async def list_invoice_templates(
        self,
        alt_id: str,
        alt_type: str,
        limit: str,
        offset: str,
        status: Optional[str] = None,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None,
        search: Optional[str] = None,
        payment_mode: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListTemplatesResponseDto:
        """
        List templates
        API to get list of templates
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "status", "in": "query"}, {"name": "startAt", "in": "query"}, {"name": "endAt", "in": "query"}, {"name": "search", "in": "query"}, {"name": "paymentMode", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type, "status": status, "start_at": start_at, "end_at": end_at, "search": search, "payment_mode": payment_mode, "limit": limit, "offset": offset }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/template", extracted["path"]),
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

    async def get_invoice_template(
        self,
        template_id: str,
        alt_id: str,
        alt_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetTemplateResponseDto:
        """
        Get an template
        API to get an template by template id
        """
        param_defs = [{"name": "templateId", "in": "path"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}]
        extracted = extract_params({ "template_id": template_id, "alt_id": alt_id, "alt_type": alt_type }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/template/{templateId}", extracted["path"]),
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

    async def update_invoice_template(
        self,
        template_id: str,
        request_body: UpdateInvoiceTemplateDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateInvoiceTemplateResponseDto:
        """
        Update template
        API to update an template by template id
        """
        param_defs = [{"name": "templateId", "in": "path"}]
        extracted = extract_params({ "template_id": template_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/invoices/template/{templateId}", extracted["path"]),
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

    async def delete_invoice_template(
        self,
        template_id: str,
        alt_id: str,
        alt_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteInvoiceTemplateResponseDto:
        """
        Delete template
        API to update an template by template id
        """
        param_defs = [{"name": "templateId", "in": "path"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}]
        extracted = extract_params({ "template_id": template_id, "alt_id": alt_id, "alt_type": alt_type }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/invoices/template/{templateId}", extracted["path"]),
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

    async def update_invoice_template_late_fees_configuration(
        self,
        template_id: str,
        request_body: UpdateInvoiceLateFeesConfigurationDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateInvoiceTemplateResponseDto:
        """
        Update template late fees configuration
        API to update template late fees configuration by template id
        """
        param_defs = [{"name": "templateId", "in": "path"}]
        extracted = extract_params({ "template_id": template_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/invoices/template/{templateId}/late-fees-configuration", extracted["path"]),
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

    async def update_invoice_payment_methods_configuration(
        self,
        template_id: str,
        request_body: UpdatePaymentMethodsConfigurationDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateInvoiceTemplateResponseDto:
        """
        Update template late fees configuration
        API to update template late fees configuration by template id
        """
        param_defs = [{"name": "templateId", "in": "path"}]
        extracted = extract_params({ "template_id": template_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/invoices/template/{templateId}/payment-methods-configuration", extracted["path"]),
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

    async def create_invoice_schedule(
        self,
        request_body: CreateInvoiceScheduleDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateInvoiceScheduleResponseDto:
        """
        Create Invoice Schedule
        API to create an invoice Schedule
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/schedule", extracted["path"]),
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

    async def list_invoice_schedules(
        self,
        alt_id: str,
        alt_type: str,
        limit: str,
        offset: str,
        status: Optional[str] = None,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None,
        search: Optional[str] = None,
        payment_mode: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListSchedulesResponseDto:
        """
        List schedules
        API to get list of schedules
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "status", "in": "query"}, {"name": "startAt", "in": "query"}, {"name": "endAt", "in": "query"}, {"name": "search", "in": "query"}, {"name": "paymentMode", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type, "status": status, "start_at": start_at, "end_at": end_at, "search": search, "payment_mode": payment_mode, "limit": limit, "offset": offset }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/schedule", extracted["path"]),
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

    async def get_invoice_schedule(
        self,
        schedule_id: str,
        alt_id: str,
        alt_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetScheduleResponseDto:
        """
        Get an schedule
        API to get an schedule by schedule id
        """
        param_defs = [{"name": "scheduleId", "in": "path"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}]
        extracted = extract_params({ "schedule_id": schedule_id, "alt_id": alt_id, "alt_type": alt_type }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/schedule/{scheduleId}", extracted["path"]),
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

    async def update_invoice_schedule(
        self,
        schedule_id: str,
        request_body: UpdateInvoiceScheduleDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateInvoiceScheduleResponseDto:
        """
        Update schedule
        API to update an schedule by schedule id
        """
        param_defs = [{"name": "scheduleId", "in": "path"}]
        extracted = extract_params({ "schedule_id": schedule_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/invoices/schedule/{scheduleId}", extracted["path"]),
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

    async def delete_invoice_schedule(
        self,
        schedule_id: str,
        alt_id: str,
        alt_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteInvoiceScheduleResponseDto:
        """
        Delete schedule
        API to delete an schedule by schedule id
        """
        param_defs = [{"name": "scheduleId", "in": "path"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}]
        extracted = extract_params({ "schedule_id": schedule_id, "alt_id": alt_id, "alt_type": alt_type }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/invoices/schedule/{scheduleId}", extracted["path"]),
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

    async def update_and_schedule_invoice_schedule(
        self,
        schedule_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateAndScheduleInvoiceScheduleResponseDto:
        """
        Update scheduled recurring invoice
        API to update scheduled recurring invoice
        """
        param_defs = [{"name": "scheduleId", "in": "path"}]
        extracted = extract_params({ "schedule_id": schedule_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/schedule/{scheduleId}/updateAndSchedule", extracted["path"]),
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

    async def schedule_invoice_schedule(
        self,
        schedule_id: str,
        request_body: ScheduleInvoiceScheduleDto,
        options: Optional[Dict[str, Any]] = None
    ) -> ScheduleInvoiceScheduleResponseDto:
        """
        Schedule an schedule invoice
        API to schedule an schedule invoice to start sending to the customer
        """
        param_defs = [{"name": "scheduleId", "in": "path"}]
        extracted = extract_params({ "schedule_id": schedule_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/schedule/{scheduleId}/schedule", extracted["path"]),
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

    async def auto_payment_invoice_schedule(
        self,
        schedule_id: str,
        request_body: AutoPaymentScheduleDto,
        options: Optional[Dict[str, Any]] = None
    ) -> AutoPaymentInvoiceScheduleResponseDto:
        """
        Manage Auto payment for an schedule invoice
        API to manage auto payment for a schedule
        """
        param_defs = [{"name": "scheduleId", "in": "path"}]
        extracted = extract_params({ "schedule_id": schedule_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/schedule/{scheduleId}/auto-payment", extracted["path"]),
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

    async def cancel_invoice_schedule(
        self,
        schedule_id: str,
        request_body: CancelInvoiceScheduleDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CancelInvoiceScheduleResponseDto:
        """
        Cancel an scheduled invoice
        API to cancel a scheduled invoice by schedule id
        """
        param_defs = [{"name": "scheduleId", "in": "path"}]
        extracted = extract_params({ "schedule_id": schedule_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/schedule/{scheduleId}/cancel", extracted["path"]),
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

    async def text2pay_invoice(
        self,
        request_body: Text2PayDto,
        options: Optional[Dict[str, Any]] = None
    ) -> Text2PayInvoiceResponseDto:
        """
        Create &amp; Send
        API to create or update a text2pay invoice
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/text2pay", extracted["path"]),
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

    async def generate_invoice_number(
        self,
        alt_id: str,
        alt_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GenerateInvoiceNumberResponseDto:
        """
        Generate Invoice Number
        Get the next invoice number for the given location
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/generate-invoice-number", extracted["path"]),
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

    async def get_invoice(
        self,
        invoice_id: str,
        alt_id: str,
        alt_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GetInvoiceResponseDto:
        """
        Get invoice
        API to get invoice by invoice id
        """
        param_defs = [{"name": "invoiceId", "in": "path"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}]
        extracted = extract_params({ "invoice_id": invoice_id, "alt_id": alt_id, "alt_type": alt_type }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/{invoiceId}", extracted["path"]),
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

    async def update_invoice(
        self,
        invoice_id: str,
        request_body: UpdateInvoiceDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateInvoiceResponseDto:
        """
        Update invoice
        API to update invoice by invoice id
        """
        param_defs = [{"name": "invoiceId", "in": "path"}]
        extracted = extract_params({ "invoice_id": invoice_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/invoices/{invoiceId}", extracted["path"]),
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

    async def delete_invoice(
        self,
        invoice_id: str,
        alt_id: str,
        alt_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> DeleteInvoiceResponseDto:
        """
        Delete invoice
        API to delete invoice by invoice id
        """
        param_defs = [{"name": "invoiceId", "in": "path"}, {"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}]
        extracted = extract_params({ "invoice_id": invoice_id, "alt_id": alt_id, "alt_type": alt_type }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/invoices/{invoiceId}", extracted["path"]),
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

    async def update_invoice_late_fees_configuration(
        self,
        invoice_id: str,
        request_body: UpdateInvoiceLateFeesConfigurationDto,
        options: Optional[Dict[str, Any]] = None
    ) -> UpdateInvoiceResponseDto:
        """
        Update invoice late fees configuration
        API to update invoice late fees configuration by invoice id
        """
        param_defs = [{"name": "invoiceId", "in": "path"}]
        extracted = extract_params({ "invoice_id": invoice_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/invoices/{invoiceId}/late-fees-configuration", extracted["path"]),
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

    async def void_invoice(
        self,
        invoice_id: str,
        request_body: VoidInvoiceDto,
        options: Optional[Dict[str, Any]] = None
    ) -> VoidInvoiceResponseDto:
        """
        Void invoice
        API to delete invoice by invoice id
        """
        param_defs = [{"name": "invoiceId", "in": "path"}]
        extracted = extract_params({ "invoice_id": invoice_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/{invoiceId}/void", extracted["path"]),
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

    async def send_invoice(
        self,
        invoice_id: str,
        request_body: SendInvoiceDto,
        options: Optional[Dict[str, Any]] = None
    ) -> SendInvoicesResponseDto:
        """
        Send invoice
        API to send invoice by invoice id
        """
        param_defs = [{"name": "invoiceId", "in": "path"}]
        extracted = extract_params({ "invoice_id": invoice_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/{invoiceId}/send", extracted["path"]),
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

    async def record_invoice(
        self,
        invoice_id: str,
        request_body: RecordPaymentDto,
        options: Optional[Dict[str, Any]] = None
    ) -> RecordPaymentResponseDto:
        """
        Record a manual payment for an invoice
        API to record manual payment for an invoice by invoice id
        """
        param_defs = [{"name": "invoiceId", "in": "path"}]
        extracted = extract_params({ "invoice_id": invoice_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/{invoiceId}/record-payment", extracted["path"]),
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

    async def update_invoice_last_visited_at(
        self,
        request_body: PatchInvoiceStatsLastViewedDto,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Update invoice last visited at
        API to update invoice last visited at by invoice id
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/invoices/stats/last-visited-at", extracted["path"]),
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

    async def create_new_estimate(
        self,
        request_body: CreateEstimatesDto,
        options: Optional[Dict[str, Any]] = None
    ) -> EstimateResponseDto:
        """
        Create New Estimate
        Create a new estimate with the provided details
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/estimate", extracted["path"]),
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

    async def update_estimate(
        self,
        estimate_id: str,
        request_body: UpdateEstimateDto,
        options: Optional[Dict[str, Any]] = None
    ) -> EstimateResponseDto:
        """
        Update Estimate
        Update an existing estimate with new details
        """
        param_defs = [{"name": "estimateId", "in": "path"}]
        extracted = extract_params({ "estimate_id": estimate_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/invoices/estimate/{estimateId}", extracted["path"]),
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

    async def delete_estimate(
        self,
        estimate_id: str,
        request_body: AltDto,
        options: Optional[Dict[str, Any]] = None
    ) -> EstimateResponseDto:
        """
        Delete Estimate
        Delete an existing estimate
        """
        param_defs = [{"name": "estimateId", "in": "path"}]
        extracted = extract_params({ "estimate_id": estimate_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/invoices/estimate/{estimateId}", extracted["path"]),
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

    async def generate_estimate_number(
        self,
        alt_id: str,
        alt_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> GenerateEstimateNumberResponse:
        """
        Generate Estimate Number
        Get the next estimate number for the given location
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/estimate/number/generate", extracted["path"]),
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

    async def send_estimate(
        self,
        estimate_id: str,
        request_body: SendEstimateDto,
        options: Optional[Dict[str, Any]] = None
    ) -> EstimateResponseDto:
        """
        Send Estimate
        API to send estimate by estimate id
        """
        param_defs = [{"name": "estimateId", "in": "path"}]
        extracted = extract_params({ "estimate_id": estimate_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/estimate/{estimateId}/send", extracted["path"]),
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

    async def create_invoice_from_estimate(
        self,
        estimate_id: str,
        request_body: CreateInvoiceFromEstimateDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateInvoiceFromEstimateResponseDTO:
        """
        Create Invoice from Estimate
        Create a new invoice from an existing estimate
        """
        param_defs = [{"name": "estimateId", "in": "path"}]
        extracted = extract_params({ "estimate_id": estimate_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/estimate/{estimateId}/invoice", extracted["path"]),
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

    async def list_estimates(
        self,
        alt_id: str,
        alt_type: str,
        limit: str,
        offset: str,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None,
        search: Optional[str] = None,
        status: Optional[str] = None,
        contact_id: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListEstimatesResponseDTO:
        """
        List Estimates
        Get a paginated list of estimates
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "startAt", "in": "query"}, {"name": "endAt", "in": "query"}, {"name": "search", "in": "query"}, {"name": "status", "in": "query"}, {"name": "contactId", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type, "start_at": start_at, "end_at": end_at, "search": search, "status": status, "contact_id": contact_id, "limit": limit, "offset": offset }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/estimate/list", extracted["path"]),
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

    async def update_estimate_last_visited_at(
        self,
        request_body: EstimateIdParam,
        options: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Update estimate last visited at
        API to update estimate last visited at by estimate id
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PATCH",
            "url": build_url("/invoices/estimate/stats/last-visited-at", extracted["path"]),
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

    async def list_estimate_templates(
        self,
        alt_id: str,
        alt_type: str,
        limit: str,
        offset: str,
        search: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListEstimateTemplateResponseDTO:
        """
        List Estimate Templates
        Get a list of estimate templates or a specific template by ID
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "search", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type, "search": search, "limit": limit, "offset": offset }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/estimate/template", extracted["path"]),
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

    async def create_estimate_template(
        self,
        request_body: EstimateTemplatesDto,
        options: Optional[Dict[str, Any]] = None
    ) -> EstimateTemplateResponseDTO:
        """
        Create Estimate Template
        Create a new estimate template
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/estimate/template", extracted["path"]),
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

    async def update_estimate_template(
        self,
        template_id: str,
        request_body: EstimateTemplatesDto,
        options: Optional[Dict[str, Any]] = None
    ) -> EstimateTemplateResponseDTO:
        """
        Update Estimate Template
        Update an existing estimate template
        """
        param_defs = [{"name": "templateId", "in": "path"}]
        extracted = extract_params({ "template_id": template_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "PUT",
            "url": build_url("/invoices/estimate/template/{templateId}", extracted["path"]),
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

    async def delete_estimate_template(
        self,
        template_id: str,
        request_body: AltDto,
        options: Optional[Dict[str, Any]] = None
    ) -> EstimateTemplateResponseDTO:
        """
        Delete Estimate Template
        Delete an existing estimate template
        """
        param_defs = [{"name": "templateId", "in": "path"}]
        extracted = extract_params({ "template_id": template_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "DELETE",
            "url": build_url("/invoices/estimate/template/{templateId}", extracted["path"]),
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

    async def preview_estimate_template(
        self,
        alt_id: str,
        alt_type: str,
        template_id: str,
        options: Optional[Dict[str, Any]] = None
    ) -> EstimateTemplateResponseDTO:
        """
        Preview Estimate Template
        Get a preview of an estimate template
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "templateId", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type, "template_id": template_id }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/estimate/template/preview", extracted["path"]),
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

    async def create_invoice(
        self,
        request_body: CreateInvoiceDto,
        options: Optional[Dict[str, Any]] = None
    ) -> CreateInvoiceResponseDto:
        """
        Create Invoice
        API to create an invoice
        """
        param_defs = []
        extracted = extract_params(None, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "POST",
            "url": build_url("/invoices/", extracted["path"]),
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
        alt_id: str,
        alt_type: str,
        limit: str,
        offset: str,
        status: Optional[str] = None,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None,
        search: Optional[str] = None,
        payment_mode: Optional[str] = None,
        contact_id: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ListInvoicesResponseDto:
        """
        List invoices
        API to get list of invoices
        """
        param_defs = [{"name": "altId", "in": "query"}, {"name": "altType", "in": "query"}, {"name": "status", "in": "query"}, {"name": "startAt", "in": "query"}, {"name": "endAt", "in": "query"}, {"name": "search", "in": "query"}, {"name": "paymentMode", "in": "query"}, {"name": "contactId", "in": "query"}, {"name": "limit", "in": "query"}, {"name": "offset", "in": "query"}, {"name": "sortField", "in": "query"}, {"name": "sortOrder", "in": "query"}]
        extracted = extract_params({ "alt_id": alt_id, "alt_type": alt_type, "status": status, "start_at": start_at, "end_at": end_at, "search": search, "payment_mode": payment_mode, "contact_id": contact_id, "limit": limit, "offset": offset, "sort_field": sort_field, "sort_order": sort_order }, param_defs)
        requirements = ["Location-Access","Agency-Access"]
        
        config: RequestConfig = {
            "method": "GET",
            "url": build_url("/invoices/", extracted["path"]),
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

