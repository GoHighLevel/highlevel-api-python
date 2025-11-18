from __future__ import annotations

# Oauth Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class GetAccessCodebodyDto(BaseModel):
    """GetAccessCodebodyDto model"""
    client_id: str
    client_secret: str
    grant_type: str
    code: Optional[str] = None
    refresh_token: Optional[str] = None
    user_type: Optional[str] = None
    redirect_uri: Optional[str] = None

class GetAccessCodeSuccessfulResponseDto(BaseModel):
    """GetAccessCodeSuccessfulResponseDto model"""
    access_token: Optional[str] = None
    token_type: Optional[str] = None
    expires_in: Optional[float] = None
    refresh_token: Optional[str] = None
    scope: Optional[str] = None
    userType: Optional[str] = None
    locationId: Optional[str] = None
    companyId: Optional[str] = None
    approvedLocations: Optional[List[str]] = None
    userId: str
    planId: Optional[str] = None
    isBulkInstallation: Optional[bool] = None

class GetLocationAccessCodeBodyDto(BaseModel):
    """GetLocationAccessCodeBodyDto model"""
    companyId: str
    locationId: str

class GetLocationAccessTokenSuccessfulResponseDto(BaseModel):
    """GetLocationAccessTokenSuccessfulResponseDto model"""
    access_token: Optional[str] = None
    token_type: Optional[str] = None
    expires_in: Optional[float] = None
    scope: Optional[str] = None
    locationId: Optional[str] = None
    planId: Optional[str] = None
    userId: str

class InstalledLocationSchema(BaseModel):
    """InstalledLocationSchema model"""
    _id: str
    name: str
    address: str
    isInstalled: Optional[bool] = None

class GetInstalledLocationsSuccessfulResponseDto(BaseModel):
    """GetInstalledLocationsSuccessfulResponseDto model"""
    locations: Optional[List[InstalledLocationSchema]] = None
    count: Optional[float] = None
    installToFutureLocations: Optional[bool] = None

