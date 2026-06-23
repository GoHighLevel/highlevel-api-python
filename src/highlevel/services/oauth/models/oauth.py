# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# Oauth Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class GetAccessTokenBodyDto(BaseModel):
    """GetAccessTokenBodyDto model"""
    clientId: str
    clientSecret: str
    grantType: str
    code: Optional[str] = None
    refreshToken: Optional[str] = None
    userType: Optional[str] = None
    redirectUri: Optional[str] = None

class GetAccessTokenSuccessfulResponseDto(BaseModel):
    """GetAccessTokenSuccessfulResponseDto model"""
    accessToken: Optional[str] = None
    tokenType: Optional[str] = None
    expiresIn: Optional[float] = None
    refreshToken: Optional[str] = None
    scope: Optional[str] = None
    userType: Optional[str] = None
    locationId: Optional[str] = None
    companyId: Optional[str] = None
    approvedLocations: Optional[List[str]] = None
    userId: str
    planId: Optional[str] = None
    isBulkInstallation: Optional[bool] = None
    installToFutureLocations: Optional[bool] = None
    approveAllLocations: Optional[bool] = None

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
    appId: Optional[str] = None
    versionId: Optional[str] = None
    refresh_token: Optional[str] = None

class GetLocationAccessTokenV3SuccessfulResponseDto(BaseModel):
    """GetLocationAccessTokenV3SuccessfulResponseDto model"""
    accessToken: Optional[str] = None
    tokenType: Optional[str] = None
    expiresIn: Optional[float] = None
    scope: Optional[str] = None
    locationId: Optional[str] = None
    planId: Optional[str] = None
    userId: str
    appId: Optional[str] = None
    versionId: Optional[str] = None
    refreshToken: Optional[str] = None

class InstalledLocationSchema(BaseModel):
    """InstalledLocationSchema model"""
    _id: str
    name: str
    address: str
    isInstalled: Optional[bool] = None
    versionId: Optional[str] = None
    installedAt: Optional[str] = None

class GetInstalledLocationsSuccessfulResponseDto(BaseModel):
    """GetInstalledLocationsSuccessfulResponseDto model"""
    locations: Optional[List[InstalledLocationSchema]] = None
    count: Optional[float] = None
    installToFutureLocations: Optional[bool] = None

class V3PaginationMetaDto(BaseModel):
    """V3PaginationMetaDto model"""
    totalRecords: Optional[float] = None
    hasNextPage: bool
    hasPrevPage: bool
    nextPageToken: Optional[str] = None
    prevPageToken: Optional[str] = None
    currentPageSize: float
    estimatedTotalRecords: Optional[float] = None

class V3InstalledLocationsListMetadataDto(BaseModel):
    """V3InstalledLocationsListMetadataDto model"""
    filterApplied: Optional[Dict[str, Any]] = None
    sortApplied: Optional[Dict[str, Any]] = None

class GetInstalledLocationsV3SuccessfulResponseDto(BaseModel):
    """GetInstalledLocationsV3SuccessfulResponseDto model"""
    items: List[InstalledLocationSchema]
    pagination: Any
    metadata: Optional[Any] = None
    installToFutureLocations: Optional[bool] = None

class AipErrorBodyDto(BaseModel):
    """AipErrorBodyDto model"""
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None
    resolution: Optional[str] = None

class AipErrorResponseDto(BaseModel):
    """AipErrorResponseDto model"""
    error: Any

