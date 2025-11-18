from __future__ import annotations

# Funnels Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class CreateRedirectParams(BaseModel):
    """CreateRedirectParams model"""
    locationId: str
    domain: str
    path: str
    target: str
    action: str

class RedirectResponseDTO(BaseModel):
    """RedirectResponseDTO model"""
    id: str
    locationId: str
    domain: str
    path: str
    pathLowercase: str
    type: str
    target: str
    action: str

class CreateRedirectResponseDTO(BaseModel):
    """CreateRedirectResponseDTO model"""
    data: Any

class UpdateRedirectParams(BaseModel):
    """UpdateRedirectParams model"""
    target: str
    action: str
    locationId: str

class RedirectListResponseDTO(BaseModel):
    """RedirectListResponseDTO model"""
    data: Dict[str, Any]

class DeleteRedirectResponseDTO(BaseModel):
    """DeleteRedirectResponseDTO model"""
    data: Dict[str, Any]

class UpdateRedirectResponseDTO(BaseModel):
    """UpdateRedirectResponseDTO model"""
    data: Any

class FunnelPageResponseDTO(BaseModel):
    """FunnelPageResponseDTO model"""
    _id: str
    locationId: str
    funnelId: str
    name: str
    stepId: str
    deleted: str
    updatedAt: str

class FunnelPageCountResponseDTO(BaseModel):
    """FunnelPageCountResponseDTO model"""
    count: float

class FunnelListResponseDTO(BaseModel):
    """FunnelListResponseDTO model"""
    funnels: Dict[str, Any]
    count: float
    traceId: str

