from __future__ import annotations

# Links Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class LinkSchema(BaseModel):
    """LinkSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    redirectTo: Optional[str] = None
    fieldKey: Optional[str] = None
    locationId: Optional[str] = None

class GetLinksSuccessfulResponseDto(BaseModel):
    """GetLinksSuccessfulResponseDto model"""
    links: Optional[List[LinkSchema]] = None

class LinksDto(BaseModel):
    """LinksDto model"""
    locationId: str
    name: str
    redirectTo: str

class GetLinkSuccessfulResponseDto(BaseModel):
    """GetLinkSuccessfulResponseDto model"""
    link: Optional[LinkSchema] = None

class LinkUpdateDto(BaseModel):
    """LinkUpdateDto model"""
    name: str
    redirectTo: str

class DeleteLinksSuccessfulResponseDto(BaseModel):
    """DeleteLinksSuccessfulResponseDto model"""
    succeded: Optional[bool] = None

