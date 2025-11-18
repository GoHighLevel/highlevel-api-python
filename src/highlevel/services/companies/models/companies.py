from __future__ import annotations

# Companies Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class IOnboardingDto(BaseModel):
    """IOnboardingDto model"""
    pending: bool
    haveWebsite: Optional[bool] = None
    websiteUrl: Optional[str] = None
    industryServed: Optional[str] = None
    customerCount: Optional[str] = None
    tools: Optional[List[str]] = None
    location: Optional[bool] = None
    conversationDemo: Optional[bool] = None
    locationId: Optional[str] = None
    snapshotId: Optional[str] = None
    planId: Optional[str] = None
    affiliateSignup: Optional[bool] = None
    hasJoinedKickoffCall: Optional[bool] = None
    kickoffActionTaken: Optional[bool] = None
    hasJoinedImplementationCall: Optional[bool] = None
    version: Optional[str] = None
    metaData: Optional[Dict[str, Any]] = None

class GetCompanyByIdSchema(BaseModel):
    """GetCompanyByIdSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    logoUrl: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    domain: Optional[str] = None
    spareDomain: Optional[str] = None
    privacyPolicy: Optional[str] = None
    termsConditions: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    postalCode: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    timezone: Optional[str] = None
    relationshipNumber: Optional[str] = None
    subdomain: Optional[str] = None
    plan: Optional[float] = None
    currency: Optional[str] = None
    customerType: Optional[str] = None
    termsOfServiceVersion: Optional[str] = None
    termsOfServiceAcceptedBy: Optional[str] = None
    twilioTrialMode: Optional[bool] = None
    twilioFreeCredits: Optional[float] = None
    termsOfServiceAcceptedDate: Optional[str] = None
    privacyPolicyVersion: Optional[str] = None
    privacyPolicyAcceptedBy: Optional[str] = None
    privacyPolicyAcceptedDate: Optional[str] = None
    affiliatePolicyVersion: Optional[str] = None
    affiliatePolicyAcceptedBy: Optional[str] = None
    affiliatePolicyAcceptedDate: Optional[str] = None
    isReselling: Optional[bool] = None
    onboardingInfo: Optional[Any] = None
    upgradeEnabledForClients: Optional[bool] = None
    cancelEnabledForClients: Optional[bool] = None
    autoSuspendEnabled: Optional[bool] = None
    saasSettings: Optional[Dict[str, Any]] = None
    stripeConnectId: Optional[str] = None
    enableDepreciatedFeatures: Optional[bool] = None
    premiumUpgraded: Optional[bool] = None
    status: Optional[str] = None
    locationCount: Optional[float] = None
    disableEmailService: Optional[bool] = None
    referralId: Optional[str] = None
    isEnterpriseAccount: Optional[bool] = None
    businessNiche: Optional[str] = None
    businessCategory: Optional[str] = None
    businessAffinityGroup: Optional[str] = None
    isSandboxAccount: Optional[bool] = None
    enableNewSubAccountDefaultData: Optional[bool] = None

class GetCompanyByIdSuccessfulResponseDto(BaseModel):
    """GetCompanyByIdSuccessfulResponseDto model"""
    company: Optional[GetCompanyByIdSchema] = None

