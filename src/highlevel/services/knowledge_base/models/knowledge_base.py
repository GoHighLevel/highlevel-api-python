# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# KnowledgeBase Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class BadRequestDTO(BaseModel):
    """BadRequestDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class UnauthorizedDTO(BaseModel):
    """UnauthorizedDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None
    error: Optional[str] = None

class UnprocessableDTO(BaseModel):
    """UnprocessableDTO model"""
    statusCode: Optional[float] = None
    message: Optional[List[str]] = None
    error: Optional[str] = None

class InternalServerErrorDTO(BaseModel):
    """InternalServerErrorDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class FaqResponseDTO(BaseModel):
    """FaqResponseDTO model"""
    id: str
    question: str
    questionLowerCase: str
    answer: str
    knowledgeBaseId: str
    locationId: str
    trainedUrlId: str
    deleted: bool
    createdAt: str
    updatedAt: str

class ListFaqsResponseDTO(BaseModel):
    """ListFaqsResponseDTO model"""
    count: float
    faqs: List[FaqResponseDTO]
    lastFaqId: Optional[str] = None
    hasMore: Optional[bool] = None

class AddFaqDTO(BaseModel):
    """AddFaqDTO model"""
    locationId: str
    question: str
    answer: str
    knowledgeBaseId: str

class CreateFaqResponseDTO(BaseModel):
    """CreateFaqResponseDTO model"""
    success: bool
    faq: Any

class UpdateFaqBodyDTO(BaseModel):
    """UpdateFaqBodyDTO model"""
    question: str
    answer: str

class UpdateFaqResponseDTO(BaseModel):
    """UpdateFaqResponseDTO model"""
    success: bool

class DeleteFaqResponseDTO(BaseModel):
    """DeleteFaqResponseDTO model"""
    success: bool

class CrawledUrlDTO(BaseModel):
    """CrawledUrlDTO model"""
    id: str
    url: str
    title: str
    status: str
    locationId: str
    knowledgeBaseId: str
    content: str
    contentEditedByUser: bool
    updatedAt: str

class GetAllUrlsByKnowledgeBaseResponseDTO(BaseModel):
    """GetAllUrlsByKnowledgeBaseResponseDTO model"""
    count: float
    urls: List[CrawledUrlDTO]

class ErrorDetailsDTO(BaseModel):
    """ErrorDetailsDTO model"""
    stack: str
    response: str
    status: float
    options: Optional[Dict[str, Any]] = None
    message: str
    name: str

class CrawlingRecordDTO(BaseModel):
    """CrawlingRecordDTO model"""
    url: str
    id: str
    title: Optional[str] = None
    error: Optional[Any] = None

class CrawlingAggregateDTO(BaseModel):
    """CrawlingAggregateDTO model"""
    _id: str
    records: List[CrawlingRecordDTO]

class OperationDetailsDTO(BaseModel):
    """OperationDetailsDTO model"""
    discoveredUrlsCount: float
    trainedUrlsCount: float
    _id: str
    locationId: str
    status: str
    url: str
    mode: str
    knowledgeBaseId: str
    createdAt: str
    updatedAt: str
    __v: float
    robotsFileData: Optional[str] = None

class CrawlingStatusDataDTO(BaseModel):
    """CrawlingStatusDataDTO model"""
    aggregate: List[CrawlingAggregateDTO]
    operationDetails: Any

class CrawlingStatusResponseDTO(BaseModel):
    """CrawlingStatusResponseDTO model"""
    success: bool
    data: Any

class DiscoverWebsiteRequestDTO(BaseModel):
    """DiscoverWebsiteRequestDTO model"""
    locationId: str
    url: str
    option: str
    knowledgeBaseId: str

class DiscoverWebsiteDataDTO(BaseModel):
    """DiscoverWebsiteDataDTO model"""
    operationId: str
    status: str
    url: str

class DiscoverWebsiteResponseDTO(BaseModel):
    """DiscoverWebsiteResponseDTO model"""
    success: bool
    data: Any

class TrainDiscoveredUrlsDTO(BaseModel):
    """TrainDiscoveredUrlsDTO model"""
    locationId: str
    urlIds: List[str]
    knowledgeBaseId: str
    operationId: str

class TrainDiscoveredUrlsResponseDTO(BaseModel):
    """TrainDiscoveredUrlsResponseDTO model"""
    success: bool

class DeleteWebsiteUrlRequestDTO(BaseModel):
    """DeleteWebsiteUrlRequestDTO model"""
    knowledgeBaseId: str
    locationId: str
    urlIds: List[str]

class DeleteWebsiteUrlResponseDTO(BaseModel):
    """DeleteWebsiteUrlResponseDTO model"""
    success: bool

class KnowledgeBaseListItemDTO(BaseModel):
    """KnowledgeBaseListItemDTO model"""
    id: str
    name: str
    createdAt: str

class GetAllKnowledgeBasesPaginatedDataDTO(BaseModel):
    """GetAllKnowledgeBasesPaginatedDataDTO model"""
    knowledgeBases: List[KnowledgeBaseListItemDTO]
    activeCount: float
    hasMore: bool
    lastKnowledgeBaseId: Optional[str] = None

class GetAllKnowledgeBasesPaginatedResponseDTO(BaseModel):
    """GetAllKnowledgeBasesPaginatedResponseDTO model"""
    success: bool
    data: Any

class KnowledgeBaseMetadataDTO(BaseModel):
    """KnowledgeBaseMetadataDTO model"""
    faqs: float
    urls: float
    richText: float
    files: float
    webSearches: float
    tables: float

class GetKnowledgeBaseByIdDataDTO(BaseModel):
    """GetKnowledgeBaseByIdDataDTO model"""
    id: str
    name: str
    nameLowerCase: str
    locationId: str
    deleted: bool
    createdAt: str
    updatedAt: str
    kbMetadata: Any
    isDefault: Optional[bool] = None

class GetKnowledgeBaseByIdResponseDTO(BaseModel):
    """GetKnowledgeBaseByIdResponseDTO model"""
    success: bool
    data: Any

class CreateKnowledgeBaseDTO(BaseModel):
    """CreateKnowledgeBaseDTO model"""
    name: str
    description: Optional[str] = None
    locationId: str

class KnowledgeBaseDataDTO(BaseModel):
    """KnowledgeBaseDataDTO model"""
    id: str
    name: str
    nameLowerCase: str
    locationId: str
    kbMetadata: Dict[str, Any]
    deleted: bool
    createdAt: str
    updatedAt: str

class CreateKnowledgeBaseResponseDTO(BaseModel):
    """CreateKnowledgeBaseResponseDTO model"""
    success: bool
    data: Any

class UpdateKnowledgeBaseDTO(BaseModel):
    """UpdateKnowledgeBaseDTO model"""
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateKnowledgeBaseResponseDTO(BaseModel):
    """UpdateKnowledgeBaseResponseDTO model"""
    success: bool

class DeleteKnowledgeBaseResponseDTO(BaseModel):
    """DeleteKnowledgeBaseResponseDTO model"""
    success: bool

