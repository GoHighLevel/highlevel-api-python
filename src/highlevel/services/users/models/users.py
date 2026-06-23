# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# Users Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class PermissionsDto(BaseModel):
    """PermissionsDto model"""
    campaignsEnabled: Optional[bool] = None
    campaignsReadOnly: Optional[bool] = None
    contactsEnabled: Optional[bool] = None
    workflowsEnabled: Optional[bool] = None
    workflowsReadOnly: Optional[bool] = None
    triggersEnabled: Optional[bool] = None
    funnelsEnabled: Optional[bool] = None
    websitesEnabled: Optional[bool] = None
    opportunitiesEnabled: Optional[bool] = None
    dashboardStatsEnabled: Optional[bool] = None
    bulkRequestsEnabled: Optional[bool] = None
    appointmentsEnabled: Optional[bool] = None
    reviewsEnabled: Optional[bool] = None
    onlineListingsEnabled: Optional[bool] = None
    phoneCallEnabled: Optional[bool] = None
    conversationsEnabled: Optional[bool] = None
    assignedDataOnly: Optional[bool] = None
    adwordsReportingEnabled: Optional[bool] = None
    membershipEnabled: Optional[bool] = None
    facebookAdsReportingEnabled: Optional[bool] = None
    attributionsReportingEnabled: Optional[bool] = None
    settingsEnabled: Optional[bool] = None
    tagsEnabled: Optional[bool] = None
    leadValueEnabled: Optional[bool] = None
    marketingEnabled: Optional[bool] = None
    agentReportingEnabled: Optional[bool] = None
    botService: Optional[bool] = None
    socialPlanner: Optional[bool] = None
    bloggingEnabled: Optional[bool] = None
    invoiceEnabled: Optional[bool] = None
    affiliateManagerEnabled: Optional[bool] = None
    contentAiEnabled: Optional[bool] = None
    refundsEnabled: Optional[bool] = None
    recordPaymentEnabled: Optional[bool] = None
    cancelSubscriptionEnabled: Optional[bool] = None
    paymentsEnabled: Optional[bool] = None
    communitiesEnabled: Optional[bool] = None
    exportPaymentsEnabled: Optional[bool] = None

class RoleSchema(BaseModel):
    """RoleSchema model"""
    type: Optional[str] = None
    role: Optional[str] = None
    locationIds: Optional[List[str]] = None
    restrictSubAccount: Optional[bool] = None

class UserSchema(BaseModel):
    """UserSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    extension: Optional[str] = None
    permissions: Optional[Any] = None
    scopes: Optional[str] = None
    roles: Optional[Any] = None
    deleted: Optional[bool] = None
    lcPhone: Optional[Dict[str, Any]] = None
    platformLanguage: Optional[str] = None

class SearchUserSuccessfulResponseDto(BaseModel):
    """SearchUserSuccessfulResponseDto model"""
    users: Optional[List[UserSchema]] = None
    count: Optional[float] = None

class FilterByEmailDto(BaseModel):
    """FilterByEmailDto model"""
    companyId: str
    emails: str
    deleted: Optional[bool] = None
    skip: Optional[str] = None
    limit: Optional[str] = None
    projection: Optional[str] = None

class UserSuccessfulResponseDto(BaseModel):
    """UserSuccessfulResponseDto model"""
    id: Optional[str] = None
    name: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    extension: Optional[str] = None
    permissions: Optional[Any] = None
    scopes: Optional[str] = None
    roles: Optional[Any] = None
    lcPhone: Optional[Dict[str, Any]] = None
    platformLanguage: Optional[str] = None

class CreateUserDto(BaseModel):
    """CreateUserDto model"""
    companyId: str
    email: str
    password: str
    phone: Optional[str] = None
    type: str
    role: str
    locationIds: List[str]
    permissions: Optional[Any] = None
    scopes: Optional[List[str]] = None
    scopesAssignedToOnly: Optional[List[str]] = None
    profilePhoto: Optional[str] = None
    twilioPhone: Optional[Dict[str, Any]] = None
    platformLanguage: Optional[str] = None
    firstName: str
    lastName: str

class UpdateUserDto(BaseModel):
    """UpdateUserDto model"""
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    type: Optional[str] = None
    role: Optional[str] = None
    companyId: Optional[str] = None
    locationIds: Optional[List[str]] = None
    permissions: Optional[Any] = None
    scopes: Optional[List[str]] = None
    scopesAssignedToOnly: Optional[List[str]] = None
    profilePhoto: Optional[str] = None
    twilioPhone: Optional[Dict[str, Any]] = None
    platformLanguage: Optional[str] = None

class DeleteUserSuccessfulResponseV3Dto(BaseModel):
    """DeleteUserSuccessfulResponseV3Dto model"""
    succeeded: Optional[bool] = None
    message: Optional[str] = None

