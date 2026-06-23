# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# Marketplace Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class RaiseChargeBodyDTO(BaseModel):
    """RaiseChargeBodyDTO model"""
    appId: str
    meterId: str
    eventId: str
    userId: Optional[str] = None
    locationId: str
    companyId: str
    description: str
    price: Optional[float] = None
    units: float
    eventTime: Optional[str] = None

class DeleteIntegrationBodyDto(BaseModel):
    """DeleteIntegrationBodyDto model"""
    companyId: Optional[str] = None
    locationId: Optional[str] = None
    reason: Optional[str] = None

class DeleteIntegrationResponse(BaseModel):
    """DeleteIntegrationResponse model"""
    success: bool

class WhitelabelDetailsDTO(BaseModel):
    """WhitelabelDetailsDTO model"""
    domain: str
    logoUrl: str

class InstallerDetailsDTO(BaseModel):
    """InstallerDetailsDTO model"""
    companyId: str
    locationId: Optional[str] = None
    companyName: str
    relationshipNumber: str
    companyEmail: Optional[str] = None
    companyOwnerFullName: Optional[str] = None
    userId: str
    isWhitelabelCompany: bool
    companyPlan: Optional[str] = None
    companyHighLevelPlan: Optional[str] = None
    marketplaceAppPlanId: Optional[str] = None
    whitelabelDetails: Optional[Any] = None

class GetInstallerDetailsResponseDTO(BaseModel):
    """GetInstallerDetailsResponseDTO model"""
    installationDetails: Any

class SubscriptionPlanDTO(BaseModel):
    """SubscriptionPlanDTO model"""
    resellingAmount: float
    baseAmount: float
    planId: str
    features: List[str]
    paymentType: str
    name: str
    paymentTime: str

class UsagePlanDTO(BaseModel):
    """UsagePlanDTO model"""
    productType: str
    productName: str
    usageUnit: str
    meterId: str
    meterName: str
    fixedPricePerUnit: float
    priceType: str
    minPricePerUnit: str
    maxPricePerUnit: str
    executionLimitPerCycle: float

class PlansDTO(BaseModel):
    """PlansDTO model"""
    subscription: List[SubscriptionPlanDTO]
    usage: List[UsagePlanDTO]

class GetRebillingConfigResponseDTO(BaseModel):
    """GetRebillingConfigResponseDTO model"""
    plans: Any

class MigrateConnectionDto(BaseModel):
    """MigrateConnectionDto model"""
    type: str
    locationId: str
    appId: str
    appVersionId: str
    accountId: str
    apiKey: Optional[str] = None
    basicCredentials: Optional[Dict[str, Any]] = None
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    expiryIn: Optional[float] = None
    expiryAt: Optional[float] = None
    scopes: Optional[List[str]] = None
    displayName: Optional[str] = None
    isDefault: Optional[bool] = None

class MigrateConnectionResponseDto(BaseModel):
    """MigrateConnectionResponseDto model"""
    success: bool
    identifier: str
    message: Optional[str] = None

class InternalServerErrorDTO(BaseModel):
    """InternalServerErrorDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

