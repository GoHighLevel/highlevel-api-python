from __future__ import annotations

# CustomMenus Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class IconSchemaOptional(BaseModel):
    """IconSchemaOptional model"""
    name: Optional[str] = None
    fontFamily: Optional[str] = None

class CustomMenuSchema(BaseModel):
    """CustomMenuSchema model"""
    id: Optional[str] = None
    icon: Optional[Any] = None
    title: Optional[str] = None
    url: Optional[str] = None
    order: Optional[float] = None
    showOnCompany: Optional[bool] = None
    showOnLocation: Optional[bool] = None
    showToAllLocations: Optional[bool] = None
    locations: Optional[List[str]] = None
    openMode: Optional[str] = None
    userRole: Optional[str] = None
    allowCamera: Optional[bool] = None
    allowMicrophone: Optional[bool] = None

class GetCustomMenusResponseDTO(BaseModel):
    """GetCustomMenusResponseDTO model"""
    customMenus: Optional[List[CustomMenuSchema]] = None
    totalLinks: Optional[float] = None

class GetSingleCustomMenusSuccessfulResponseDTO(BaseModel):
    """GetSingleCustomMenusSuccessfulResponseDTO model"""
    customMenu: Optional[Any] = None

class DeleteCustomMenuSuccessfulResponseDTO(BaseModel):
    """DeleteCustomMenuSuccessfulResponseDTO model"""
    success: Optional[bool] = None
    message: Optional[str] = None
    deletedMenuId: Optional[str] = None
    deletedAt: Optional[str] = None

class IconSchema(BaseModel):
    """IconSchema model"""
    name: str
    fontFamily: str

class CreateCustomMenuDTO(BaseModel):
    """CreateCustomMenuDTO model"""
    title: str
    url: str
    icon: Any
    showOnCompany: bool
    showOnLocation: bool
    showToAllLocations: bool
    openMode: str
    locations: List[str]
    userRole: str
    allowCamera: Optional[bool] = None
    allowMicrophone: Optional[bool] = None

class UpdateCustomMenuDTO(BaseModel):
    """UpdateCustomMenuDTO model"""
    title: Optional[str] = None
    url: Optional[str] = None
    icon: Optional[Any] = None
    showOnCompany: Optional[bool] = None
    showOnLocation: Optional[bool] = None
    showToAllLocations: Optional[bool] = None
    openMode: Optional[str] = None
    locations: Optional[List[str]] = None
    userRole: Optional[str] = None
    allowCamera: Optional[bool] = None
    allowMicrophone: Optional[bool] = None

class UpdateCustomMenuLinkResponseDTO(BaseModel):
    """UpdateCustomMenuLinkResponseDTO model"""
    success: Optional[bool] = None
    customMenu: Optional[Any] = None

