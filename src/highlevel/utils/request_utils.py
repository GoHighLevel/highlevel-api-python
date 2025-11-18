"""
Request utility functions for the GHL SDK
"""

from typing import Any, Dict, List, Optional
from urllib.parse import quote
import httpx


RequestParams = Dict[str, Any]


class RequestConfig(Dict[str, Any]):
    """Request configuration dictionary with typed fields"""
    method: str
    url: str
    params: RequestParams
    headers: RequestParams
    data: Optional[Any]
    __security_requirements: Optional[List[str]]
    __preferred_token_type: Optional[str]
    __path_params: Optional[RequestParams]


def build_url(template: str, path_params: RequestParams) -> str:
    """
    Build URL from template and path parameters
    
    Args:
        template: URL template with {param} placeholders
        path_params: Dictionary of path parameters
    
    Returns:
        URL with parameters replaced
    """
    url = template
    for key, value in path_params.items():
        url = url.replace(f"{{{key}}}", quote(str(value)))
    return url


def extract_params(
    params: Optional[Dict[str, Any]],
    param_defs: List[Dict[str, str]]
) -> Dict[str, RequestParams]:
    """
    Extract and categorize parameters by their location (path, query, header)
    
    Args:
        params: Dictionary of parameters
        param_defs: List of parameter definitions with 'name' and 'in' fields
    
    Returns:
        Dictionary with 'path', 'query', 'header', and 'all' parameters
    """
    result: Dict[str, RequestParams] = {
        "path": {},
        "query": {},
        "header": {},
        "all": {}
    }
    
    if not params:
        return result
    
    for param_def in param_defs:
        if param_def["name"] in ["Authorization", "Version"]:
            continue
        
        # Convert name to snake_case for Python
        param_name = param_def["name"]
        snake_case_name = _to_snake_case(param_name)
        
        value = params.get(snake_case_name)
        if value is not None:
            result["all"][param_name] = value
            if param_def["in"] == "path":
                result["path"][param_name] = value
            elif param_def["in"] == "query":
                result["query"][param_name] = value
            elif param_def["in"] == "header":
                result["header"][param_name] = str(value)
    
    return result


def _to_snake_case(name: str) -> str:
    """Convert camelCase or PascalCase to snake_case"""
    result = []
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result.append("_")
        result.append(char.lower())
    return "".join(result)


async def get_auth_token(
    ghl_instance,
    requirements: List[str],
    headers: RequestParams,
    query: RequestParams,
    body: Any,
    preferred_type: Optional[str] = None
) -> Optional[str]:
    """
    Get authentication token from the HighLevel instance

    Args:
        ghl_instance: HighLevel SDK instance
        requirements: Security requirements
        headers: Request headers
        query: Query parameters
        body: Request body
        preferred_type: Preferred token type

    Returns:
        Authentication token or None
    """
    if not requirements:
        return None

    # Ensure we have a HighLevel instance with the required method
    if not ghl_instance or not hasattr(ghl_instance, "get_token_for_security"):
        return None

    return await ghl_instance.get_token_for_security(
        requirements,
        headers,
        query,
        body,
        preferred_type
    )

