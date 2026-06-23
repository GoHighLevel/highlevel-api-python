# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# EmailIsv Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class LeadConnectorRecommendationDto(BaseModel):
    """LeadConnectorRecommendationDto model"""
    isEmailValid: Optional[bool] = None

class EmailNotVerifiedResponseDto(BaseModel):
    """EmailNotVerifiedResponseDto model"""
    verified: bool
    message: Optional[str] = None
    address: Optional[str] = None

class EmailVerifiedV3ResponseDto(BaseModel):
    """EmailVerifiedV3ResponseDto model"""
    reason: Optional[List[str]] = None
    result: str
    risk: str
    address: str
    leadConnectorRecommendation: Optional[Any] = None

class VerificationBodyDto(BaseModel):
    """VerificationBodyDto model"""
    type: str
    verify: str

