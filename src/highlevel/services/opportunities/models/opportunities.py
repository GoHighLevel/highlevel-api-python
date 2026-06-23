# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# Opportunities Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class LostReasonResponseSchema(BaseModel):
    """LostReasonResponseSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    locationId: Optional[str] = None
    updatedAt: Optional[str] = None
    createdAt: Optional[str] = None

class LostReasonsResponseSchema(BaseModel):
    """LostReasonsResponseSchema model"""
    lostReasons: Optional[List[LostReasonResponseSchema]] = None
    total: Optional[float] = None

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
    forecastExpectedCloseDate: Optional[str] = None
    forecastOriginalCloseDate: Optional[str] = None
    forecastSlippageCount: Optional[float] = None
    forecastDaysSlipped: Optional[float] = None
    forecastLastSlippedAt: Optional[str] = None
    forecastProbability: Optional[float] = None
    effectiveProbability: Optional[float] = None
    contactId: Optional[str] = None
    locationId: Optional[str] = None
    contact: Optional[Any] = None
    notes: Optional[List[List[Any]]] = None
    tasks: Optional[List[List[Any]]] = None
    calendarEvents: Optional[List[List[Any]]] = None
    lostReasonId: Optional[str] = None
    customFields: Optional[List[CustomFieldResponseSchema]] = None
    followers: Optional[List[List[Any]]] = None
    externalObjectId: Optional[str] = None

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
    meta: Optional[Any] = None
    aggregations: Optional[Dict[str, Any]] = None

class AdditionalDetailsDTO(BaseModel):
    """AdditionalDetailsDTO model"""
    notes: bool
    tasks: bool
    calendarEvents: bool
    unReadConversations: bool

class OpportunitySearchBodyDTO(BaseModel):
    """OpportunitySearchBodyDTO model"""
    locationId: str
    query: str
    limit: float
    page: float
    searchAfter: List[str]
    additionalDetails: Any

class StageAggregationResponseDto(BaseModel):
    """StageAggregationResponseDto model"""
    pipelineStageId: str
    totalCount: float
    totalValue: float
    weightedValue: float
    openValue: float
    openWeightedValue: float
    wonValue: float

class PostSearchSuccessfulResponseDto(BaseModel):
    """PostSearchSuccessfulResponseDto model"""
    opportunities: Optional[List[SearchOpportunitiesResponseSchema]] = None
    total: float
    stageAggregations: Optional[List[StageAggregationResponseDto]] = None
    aggregations: Optional[Dict[str, Any]] = None

class PipelinesResponseSchema(BaseModel):
    """PipelinesResponseSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    stages: Optional[List[List[Any]]] = None
    showInFunnel: Optional[bool] = None
    showInPieChart: Optional[bool] = None
    locationId: Optional[str] = None
    useOpportunityProbability: Optional[bool] = None
    colorRenderMode: Optional[str] = None

class GetPipelinesSuccessfulResponseDto(BaseModel):
    """GetPipelinesSuccessfulResponseDto model"""
    pipelines: Optional[List[PipelinesResponseSchema]] = None

class GetPostOpportunitySuccessfulResponseDto(BaseModel):
    """GetPostOpportunitySuccessfulResponseDto model"""
    opportunity: Optional[Any] = None

class DeleteUpdateOpportunitySuccessfulResponseDto(BaseModel):
    """DeleteUpdateOpportunitySuccessfulResponseDto model"""
    succeded: Optional[bool] = None
    success: Optional[bool] = None

class UpdateStatusDto(BaseModel):
    """UpdateStatusDto model"""
    status: str
    lostReasonId: Optional[str] = None

class customFieldsInputStringSchemaV3(BaseModel):
    """customFieldsInputStringSchemaV3 model"""
    id: Optional[str] = None
    key: Optional[str] = None
    fieldValue: Optional[str] = None

class customFieldsInputArraySchemaV3(BaseModel):
    """customFieldsInputArraySchemaV3 model"""
    id: str
    key: Optional[str] = None
    fieldValue: Optional[List[str]] = None

class customFieldsInputObjectSchemaV3(BaseModel):
    """customFieldsInputObjectSchemaV3 model"""
    id: str
    key: Optional[str] = None
    fieldValue: Optional[Dict[str, Any]] = None

class CreateDtoV3(BaseModel):
    """CreateDtoV3 model"""
    pipelineId: str
    locationId: str
    name: str
    pipelineStageId: Optional[str] = None
    status: str
    contactId: str
    monetaryValue: Optional[float] = None
    forecastExpectedCloseDate: Optional[str] = None
    forecastProbability: Optional[float] = None
    assignedTo: Optional[str] = None
    customFields: Optional[List[Any]] = None

class UpdateOpportunityDtoV3(BaseModel):
    """UpdateOpportunityDtoV3 model"""
    pipelineId: Optional[str] = None
    name: Optional[str] = None
    pipelineStageId: Optional[str] = None
    status: Optional[str] = None
    monetaryValue: Optional[float] = None
    forecastExpectedCloseDate: Optional[str] = None
    forecastProbability: Optional[float] = None
    assignedTo: Optional[str] = None
    customFields: Optional[List[Any]] = None

class UpsertOpportunityDto(BaseModel):
    """UpsertOpportunityDto model"""
    id: Optional[str] = None
    pipelineId: str
    locationId: str
    followers: List[str]
    isRemoveAllFollowers: bool
    followersActionType: str
    name: Optional[str] = None
    status: Optional[str] = None
    pipelineStageId: Optional[str] = None
    monetaryValue: Optional[Dict[str, Any]] = None
    forecastExpectedCloseDate: Optional[str] = None
    forecastProbability: Optional[float] = None
    assignedTo: Optional[str] = None
    lostReasonId: Optional[str] = None

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

