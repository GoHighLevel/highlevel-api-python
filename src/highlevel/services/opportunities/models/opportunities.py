from __future__ import annotations

# Opportunities Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class SearchOpportunitiesContactResponseSchema(BaseModel):
    """SearchOpportunitiesContactResponseSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    companyName: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    tags: Optional[List[str]] = None

class CustomFieldResponseSchema(BaseModel):
    """CustomFieldResponseSchema model"""
    id: str
    fieldValue: Any

class SearchOpportunitiesResponseSchema(BaseModel):
    """SearchOpportunitiesResponseSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    monetaryValue: Optional[float] = None
    pipelineId: Optional[str] = None
    pipelineStageId: Optional[str] = None
    assignedTo: Optional[str] = None
    status: Optional[str] = None
    source: Optional[str] = None
    lastStatusChangeAt: Optional[str] = None
    lastStageChangeAt: Optional[str] = None
    lastActionDate: Optional[str] = None
    indexVersion: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    contactId: Optional[str] = None
    locationId: Optional[str] = None
    contact: Optional[SearchOpportunitiesContactResponseSchema] = None
    notes: Optional[List[str]] = None
    tasks: Optional[List[str]] = None
    calendarEvents: Optional[List[str]] = None
    customFields: Optional[List[CustomFieldResponseSchema]] = None
    followers: Optional[List[List[Any]]] = None

class SearchMetaResponseSchema(BaseModel):
    """SearchMetaResponseSchema model"""
    total: Optional[float] = None
    nextPageUrl: Optional[str] = None
    startAfterId: Optional[str] = None
    startAfter: Optional[float] = None
    currentPage: Optional[float] = None
    nextPage: Optional[float] = None
    prevPage: Optional[float] = None

class SearchSuccessfulResponseDto(BaseModel):
    """SearchSuccessfulResponseDto model"""
    opportunities: Optional[List[SearchOpportunitiesResponseSchema]] = None
    meta: Optional[SearchMetaResponseSchema] = None
    aggregations: Optional[Dict[str, Any]] = None

class PipelinesResponseSchema(BaseModel):
    """PipelinesResponseSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    stages: Optional[List[List[Any]]] = None
    showInFunnel: Optional[bool] = None
    showInPieChart: Optional[bool] = None
    locationId: Optional[str] = None

class GetPipelinesSuccessfulResponseDto(BaseModel):
    """GetPipelinesSuccessfulResponseDto model"""
    pipelines: Optional[List[PipelinesResponseSchema]] = None

class GetPostOpportunitySuccessfulResponseDto(BaseModel):
    """GetPostOpportunitySuccessfulResponseDto model"""
    opportunity: Optional[SearchOpportunitiesResponseSchema] = None

class DeleteUpdateOpportunitySuccessfulResponseDto(BaseModel):
    """DeleteUpdateOpportunitySuccessfulResponseDto model"""
    succeded: Optional[bool] = None

class UpdateStatusDto(BaseModel):
    """UpdateStatusDto model"""
    status: str

class customFieldsInputArraySchema(BaseModel):
    """customFieldsInputArraySchema model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[List[str]] = None

class customFieldsInputObjectSchema(BaseModel):
    """customFieldsInputObjectSchema model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[Dict[str, Any]] = None

class customFieldsInputStringSchema(BaseModel):
    """customFieldsInputStringSchema model"""
    id: Optional[str] = None
    key: Optional[str] = None
    field_value: Optional[str] = None

class CreateDto(BaseModel):
    """CreateDto model"""
    pipelineId: str
    locationId: str
    name: str
    pipelineStageId: Optional[str] = None
    status: str
    contactId: str
    monetaryValue: Optional[float] = None
    assignedTo: Optional[str] = None
    customFields: Optional[List[Any]] = None

class UpdateOpportunityDto(BaseModel):
    """UpdateOpportunityDto model"""
    pipelineId: Optional[str] = None
    name: Optional[str] = None
    pipelineStageId: Optional[str] = None
    status: Optional[str] = None
    monetaryValue: Optional[float] = None
    assignedTo: Optional[str] = None
    customFields: Optional[List[Any]] = None

class UpsertOpportunityDto(BaseModel):
    """UpsertOpportunityDto model"""
    pipelineId: str
    locationId: str
    contactId: str
    name: Optional[str] = None
    status: Optional[str] = None
    pipelineStageId: Optional[str] = None
    monetaryValue: Optional[float] = None
    assignedTo: Optional[str] = None

class UpsertOpportunitySuccessfulResponseDto(BaseModel):
    """UpsertOpportunitySuccessfulResponseDto model"""
    opportunity: Dict[str, Any]
    new: bool

class FollowersDTO(BaseModel):
    """FollowersDTO model"""
    followers: List[str]

class CreateAddFollowersSuccessfulResponseDto(BaseModel):
    """CreateAddFollowersSuccessfulResponseDto model"""
    followers: Optional[List[str]] = None
    followersAdded: Optional[List[str]] = None

class DeleteFollowersSuccessfulResponseDto(BaseModel):
    """DeleteFollowersSuccessfulResponseDto model"""
    followers: Optional[List[str]] = None
    followersRemoved: Optional[List[str]] = None

