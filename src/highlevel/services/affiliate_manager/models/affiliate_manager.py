# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# AffiliateManager Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class OAuthAffiliateListItemResponseDto(BaseModel):
    """OAuthAffiliateListItemResponseDto model"""
    _id: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    phone: Optional[str] = None
    deleted: Optional[bool] = None
    locationId: str
    active: Optional[bool] = None
    address: Optional[str] = None
    avatar: Optional[str] = None
    createdAt: Optional[str] = None
    createdBy: Optional[Dict[str, Any]] = None
    facebookUrl: Optional[str] = None
    instagramUrl: Optional[str] = None
    linkedInUrl: Optional[str] = None
    twitterUrl: Optional[str] = None
    youtubeUrl: Optional[str] = None
    websiteUrl: Optional[str] = None
    contactId: Optional[str] = None
    campaignIds: Optional[List[str]] = None
    vatId: Optional[str] = None
    updatedAt: Optional[str] = None
    w8Form: Optional[str] = None
    w9Form: Optional[str] = None
    lastUpdatedBy: Optional[Dict[str, Any]] = None
    email: str
    revenue: Optional[float] = None
    customer: Optional[float] = None
    lead: Optional[float] = None
    droppedCustomer: Optional[float] = None
    clickCount: Optional[float] = None
    paid: Optional[float] = None
    currency: Optional[str] = None
    owned: Optional[float] = None

class AffiliateListMetaResponseDto(BaseModel):
    """AffiliateListMetaResponseDto model"""
    count: float

class ListAffiliatesResponseDto(BaseModel):
    """ListAffiliatesResponseDto model"""
    affiliates: List[OAuthAffiliateListItemResponseDto]
    meta: Any

class GetAffiliateResponseDto(BaseModel):
    """GetAffiliateResponseDto model"""
    _id: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    phone: Optional[str] = None
    deleted: Optional[bool] = None
    locationId: str
    active: Optional[bool] = None
    address: Optional[str] = None
    avatar: Optional[str] = None
    createdAt: Optional[str] = None
    createdBy: Optional[Dict[str, Any]] = None
    facebookUrl: Optional[str] = None
    instagramUrl: Optional[str] = None
    linkedInUrl: Optional[str] = None
    twitterUrl: Optional[str] = None
    youtubeUrl: Optional[str] = None
    websiteUrl: Optional[str] = None
    contactId: Optional[str] = None
    campaignIds: Optional[List[str]] = None
    vatId: Optional[str] = None
    updatedAt: Optional[str] = None
    w8Form: Optional[str] = None
    w9Form: Optional[str] = None
    lastUpdatedBy: Optional[Dict[str, Any]] = None
    email: str
    revenue: Optional[float] = None
    customer: Optional[float] = None
    lead: Optional[float] = None
    droppedCustomer: Optional[float] = None
    clickCount: Optional[float] = None
    paid: Optional[float] = None
    currency: Optional[str] = None
    owned: Optional[float] = None

class PayoutListItemResponseDto(BaseModel):
    """PayoutListItemResponseDto model"""
    _id: str
    locationId: str
    affiliateId: str
    campaignId: Optional[str] = None
    currency: str
    amount: float
    status: Optional[str] = None
    payoutMonth: Optional[str] = None
    dueAt: Optional[str] = None
    paidAt: Optional[str] = None
    paidMeta: Optional[Dict[str, Any]] = None
    paidMethod: Optional[str] = None
    altId: Optional[str] = None
    deleted: Optional[bool] = None
    isMigrated: Optional[bool] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    campaign: Optional[str] = None
    affiliateName: Optional[str] = None
    affiliateEmail: Optional[str] = None
    payoutMethod: Optional[str] = None
    affiliate: Optional[Any] = None

class PayoutListMetaResponseDto(BaseModel):
    """PayoutListMetaResponseDto model"""
    count: float

class GetPayoutListResponseDto(BaseModel):
    """GetPayoutListResponseDto model"""
    payouts: List[PayoutListItemResponseDto]
    meta: Optional[Any] = None

class CommissionCustomerResponseDto(BaseModel):
    """CommissionCustomerResponseDto model"""
    _id: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    type: Optional[str] = None

class CommissionCampaignResponseDto(BaseModel):
    """CommissionCampaignResponseDto model"""
    id: Optional[str] = None
    name: Optional[str] = None
    liveMode: Optional[bool] = None

class CommissionAffiliateResponseDto(BaseModel):
    """CommissionAffiliateResponseDto model"""
    _id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None

class CommissionListItemResponseDto(BaseModel):
    """CommissionListItemResponseDto model"""
    _id: str
    productId: Optional[str] = None
    productName: Optional[str] = None
    qty: Optional[float] = None
    productCommission: Optional[float] = None
    commissionAmount: Optional[float] = None
    amount: Optional[float] = None
    unitDiscount: Optional[float] = None
    campaignName: Optional[str] = None
    commission: Optional[float] = None
    commissionType: Optional[str] = None
    transactionAt: Optional[str] = None
    transactionId: Optional[str] = None
    affiliateId: Optional[str] = None
    payoutId: Optional[str] = None
    status: Optional[str] = None
    currency: Optional[str] = None
    isTrial: Optional[bool] = None
    customer: Optional[Any] = None
    createdAt: Optional[str] = None
    eventId: Optional[str] = None
    campaign: Optional[Any] = None
    affiliate: Optional[Any] = None
    dueAt: Optional[str] = None
    liveMode: Optional[bool] = None
    tier: Optional[float] = None

class CommissionListMetaResponseDto(BaseModel):
    """CommissionListMetaResponseDto model"""
    count: float

class GetCommissionListResponseDto(BaseModel):
    """GetCommissionListResponseDto model"""
    commissions: List[CommissionListItemResponseDto]
    meta: Optional[Any] = None

