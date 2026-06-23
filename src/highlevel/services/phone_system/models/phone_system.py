# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# PhoneSystem Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class PurchasePhoneNumberBodyDto(BaseModel):
    """PurchasePhoneNumberBodyDto model"""
    phoneNumber: str
    addressSid: str
    bundleSid: str
    countryCode: str
    numberType: Dict[str, Any]
    paymentIntentId: str
    stripeAccountId: str
    paymentMethodId: str
    locality: str
    region: str
    fingerprintId: str
    skipLocationKYC: bool

class PurchaseNumberForLocationV3ResponseDto(BaseModel):
    """PurchaseNumberForLocationV3ResponseDto model"""
    number: str
    locationId: str
    id: str
    underLcAccount: bool

class PurchaseNumberForLocationV3Http201ResponseDto(BaseModel):
    """PurchaseNumberForLocationV3Http201ResponseDto model"""
    status: str
    data: Any
    message: str
    statusCode: float

class NumberCapabilitiesDto(BaseModel):
    """NumberCapabilitiesDto model"""
    voice: Optional[bool] = None
    sms: Optional[bool] = None
    mms: Optional[bool] = None
    fax: Optional[bool] = None

class ListNumberItemResponseDto(BaseModel):
    """ListNumberItemResponseDto model"""
    phoneNumber: str
    friendlyName: Optional[str] = None
    sid: Optional[str] = None
    countryCode: Optional[str] = None
    capabilities: Optional[Any] = None
    type: Optional[str] = None
    isDefaultNumber: Optional[bool] = None
    linkedUser: Optional[str] = None
    linkedRingAllUsers: Optional[List[str]] = None
    inboundCallService: Optional[Dict[str, Any]] = None
    forwardingNumber: Optional[str] = None
    isGroupConversationEnabled: Optional[bool] = None
    addressSid: Optional[str] = None
    bundleSid: Optional[str] = None
    dateAdded: Optional[Dict[str, Any]] = None
    dateUpdated: Optional[Dict[str, Any]] = None
    dateCreated: Optional[Dict[str, Any]] = None
    origin: Optional[str] = None

class RcsSenderIdResponseDto(BaseModel):
    """RcsSenderIdResponseDto model"""
    number: str
    numberType: str
    friendlyName: Optional[str] = None
    rcsMeta: Optional[Dict[str, Any]] = None

class ListNumbersV3ResponseDto(BaseModel):
    """ListNumbersV3ResponseDto model"""
    numbers: List[ListNumberItemResponseDto]
    isUnderLc: Optional[bool] = None
    pageSize: Optional[float] = None
    page: Optional[float] = None
    accountStatus: Optional[str] = None
    rcsSenderIds: Optional[List[RcsSenderIdResponseDto]] = None
    total: Optional[float] = None

class ListNumbersV3Http200ResponseDto(BaseModel):
    """ListNumbersV3Http200ResponseDto model"""
    status: str
    data: Any
    message: str
    statusCode: float

