from __future__ import annotations

# EmailIsv Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class EmailNotVerifiedResponseDto(BaseModel):
    """EmailNotVerifiedResponseDto model"""
    verified: bool
    message: Optional[str] = None
    address: Optional[str] = None

class LeadConnectorRecomandationDto(BaseModel):
    """LeadConnectorRecomandationDto model"""
    isEmailValid: Optional[bool] = None

class EmailVerifiedResponseDto(BaseModel):
    """EmailVerifiedResponseDto model"""
    reason: Optional[List[str]] = None
    result: str
    risk: str
    address: str
    leadconnectorRecomendation: Any

class VerificationBodyDto(BaseModel):
    """VerificationBodyDto model"""
    type: str
    verify: str

