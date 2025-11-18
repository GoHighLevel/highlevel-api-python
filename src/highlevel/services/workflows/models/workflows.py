from __future__ import annotations

# Workflows Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class WorkflowSchema(BaseModel):
    """WorkflowSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    version: Optional[float] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    locationId: Optional[str] = None

class GetWorkflowSuccessfulResponseDto(BaseModel):
    """GetWorkflowSuccessfulResponseDto model"""
    workflows: Optional[List[WorkflowSchema]] = None

