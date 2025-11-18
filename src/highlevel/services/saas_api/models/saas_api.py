from __future__ import annotations

# SaasApi Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class BadRequestDTO(BaseModel):
    """BadRequestDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class UnauthorizedDTO(BaseModel):
    """UnauthorizedDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None
    error: Optional[str] = None

class ResourceNotFoundDTO(BaseModel):
    """ResourceNotFoundDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class InternalServerErrorDTO(BaseModel):
    """InternalServerErrorDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class UpdateSubscriptionDto(BaseModel):
    """UpdateSubscriptionDto model"""
    subscriptionId: str
    customerId: str
    companyId: str

class BulkDisableSaasDto(BaseModel):
    """BulkDisableSaasDto model"""
    locationIds: List[str]

class BulkDisableSaasResponseDto(BaseModel):
    """BulkDisableSaasResponseDto model"""
    data: Dict[str, Any]

class EnableSaasDto(BaseModel):
    """EnableSaasDto model"""
    stripeAccountId: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    stripeCustomerId: Optional[str] = None
    companyId: str
    isSaaSV2: bool
    contactId: Optional[str] = None
    providerLocationId: Optional[str] = None
    description: Optional[str] = None
    saasPlanId: Optional[str] = None
    priceId: Optional[str] = None

class EnableSaasResponseDto(BaseModel):
    """EnableSaasResponseDto model"""
    data: Dict[str, Any]

class PauseLocationDto(BaseModel):
    """PauseLocationDto model"""
    paused: bool
    companyId: str

class UpdateRebillingDto(BaseModel):
    """UpdateRebillingDto model"""
    product: str
    locationIds: List[str]
    config: Dict[str, Any]

class UpdateRebillingResponseDto(BaseModel):
    """UpdateRebillingResponseDto model"""
    success: bool

class AgencyPlanResponseDto(BaseModel):
    """AgencyPlanResponseDto model"""
    planId: str
    title: str
    description: str
    saasProducts: List[str]
    addOns: Optional[List[str]] = None
    planLevel: float
    trialPeriod: float
    userLimit: Optional[float] = None
    contactLimit: Optional[float] = None
    prices: List[Dict[str, Any]]
    categoryId: Optional[str] = None
    snapshotId: Optional[str] = None
    productId: Optional[str] = None
    isSaaSV2: bool
    providerLocationId: Optional[str] = None
    createdAt: str
    updatedAt: str

class LocationSubscriptionResponseDto(BaseModel):
    """LocationSubscriptionResponseDto model"""
    locationId: str
    isSaaSV2: bool
    companyId: str
    saasMode: Optional[str] = None
    subscriptionId: Optional[str] = None
    customerId: Optional[str] = None
    productId: Optional[str] = None
    priceId: Optional[str] = None
    saasPlanId: Optional[str] = None
    subscriptionStatus: Optional[str] = None

class BulkEnableSaasActionPayloadDto(BaseModel):
    """BulkEnableSaasActionPayloadDto model"""
    priceId: Optional[str] = None
    stripeAccountId: Optional[str] = None
    saasPlanId: str
    providerLocationId: Optional[str] = None

class BulkEnableSaasRequestDto(BaseModel):
    """BulkEnableSaasRequestDto model"""
    locationIds: List[str]
    isSaaSV2: bool
    actionPayload: Any

class BulkEnableSaasResponseDto(BaseModel):
    """BulkEnableSaasResponseDto model"""
    success: bool
    message: str
    bulkActionUrl: Optional[str] = None

class SaasLocationDto(BaseModel):
    """SaasLocationDto model"""
    locationId: str
    companyId: str
    saasMode: str
    subscriptionId: str
    customerId: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    providerLocationId: Optional[str] = None
    isSaaSV2: Optional[bool] = None
    subscriptionInfo: Optional[Dict[str, Any]] = None

class GetSaasLocationsResponseDto(BaseModel):
    """GetSaasLocationsResponseDto model"""
    locations: List[SaasLocationDto]
    pagination: Dict[str, Any]

class SaasPlanResponseDto(BaseModel):
    """SaasPlanResponseDto model"""
    planId: str
    companyId: str
    title: str
    description: str
    saasProducts: List[str]
    addOns: Optional[List[str]] = None
    planLevel: float
    trialPeriod: float
    setupFee: Optional[float] = None
    userLimit: Optional[float] = None
    contactLimit: Optional[float] = None
    prices: List[Dict[str, Any]]
    categoryId: Optional[str] = None
    snapshotId: Optional[str] = None
    providerLocationId: Optional[str] = None
    productId: Optional[str] = None
    isSaaSV2: bool
    createdAt: str
    updatedAt: str

