from __future__ import annotations

# Campaigns Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class campaignsSchema(BaseModel):
    """campaignsSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    locationId: Optional[str] = None

class CampaignsSuccessfulResponseDto(BaseModel):
    """CampaignsSuccessfulResponseDto model"""
    campaigns: Optional[List[campaignsSchema]] = None

