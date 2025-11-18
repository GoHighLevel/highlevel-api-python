from __future__ import annotations

# PhoneSystem Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class DetailedPhoneNumberDto(BaseModel):
    """DetailedPhoneNumberDto model"""
    phoneNumber: str
    friendlyName: Optional[str] = None
    sid: str
    countryCode: str
    capabilities: Dict[str, Any]
    type: str
    isDefaultNumber: bool
    linkedUser: Optional[str] = None
    linkedRingAllUsers: List[str]
    inboundCallService: Optional[Dict[str, Any]] = None
    forwardingNumber: Optional[str] = None
    isGroupConversationEnabled: bool
    addressSid: Optional[str] = None
    bundleSid: Optional[str] = None
    dateAdded: Optional[str] = None
    dateUpdated: Optional[str] = None
    origin: Optional[str] = None

class NumberPoolDto(BaseModel):
    """NumberPoolDto model"""
    id: Optional[str] = None
    name: Optional[str] = None
    locationId: Optional[str] = None
    numbers: Optional[List[Dict[str, Any]]] = None
    forwardingNumber: Optional[str] = None
    whisper: Optional[bool] = None
    whisperMessage: Optional[str] = None
    callRecording: Optional[bool] = None
    isActive: Optional[bool] = None
    inboundCallService: Optional[Dict[str, Any]] = None

