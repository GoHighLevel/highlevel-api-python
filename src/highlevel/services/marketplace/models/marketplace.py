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
    units: str
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
    companyEmail: str
    companyOwnerFullName: Optional[str] = None
    userId: str
    isWhitelabelCompany: bool
    companyHighLevelPlan: Optional[str] = None
    marketplaceAppPlanId: Optional[str] = None
    whitelabelDetails: Optional[Any] = None

class GetInstallerDetailsResponseDTO(BaseModel):
    """GetInstallerDetailsResponseDTO model"""
    installationDetails: Any

