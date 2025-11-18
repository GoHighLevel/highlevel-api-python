from __future__ import annotations

# Businesses Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class BusinessCreatedByOrUpdatedBy(BaseModel):
    """BusinessCreatedByOrUpdatedBy model"""

class BusinessDto(BaseModel):
    """BusinessDto model"""
    id: str
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    country: Optional[str] = None
    updatedBy: Optional[Any] = None
    locationId: str
    createdBy: Optional[Any] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class GetBusinessByLocationResponseDto(BaseModel):
    """GetBusinessByLocationResponseDto model"""
    businesses: List[BusinessDto]

class CreateBusinessDto(BaseModel):
    """CreateBusinessDto model"""
    name: str
    locationId: str
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    postalCode: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None

class UpdateBusinessResponseDto(BaseModel):
    """UpdateBusinessResponseDto model"""
    success: bool
    buiseness: Any

class UpdateBusinessDto(BaseModel):
    """UpdateBusinessDto model"""
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None

class DeleteBusinessResponseDto(BaseModel):
    """DeleteBusinessResponseDto model"""
    success: bool

class GetBusinessByIdResponseDto(BaseModel):
    """GetBusinessByIdResponseDto model"""
    business: Any

