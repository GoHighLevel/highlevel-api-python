from __future__ import annotations

# Emails Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class ScheduleDto(BaseModel):
    """ScheduleDto model"""
    name: str
    repeatAfter: str
    id: str
    parentId: str
    childCount: float
    campaignType: str
    bulkActionVersion: str
    _id: str
    status: str
    sendDays: List[str]
    deleted: bool
    migrated: bool
    archived: bool
    hasTracking: bool
    isPlainText: bool
    hasUtmTracking: bool
    enableResendToUnopened: bool
    locationId: str
    templateId: str
    templateType: str
    createdAt: str
    updatedAt: str
    __v: float
    documentId: str
    downloadUrl: str
    templateDataDownloadUrl: str
    child: List[str]

class ScheduleFetchSuccessfulDTO(BaseModel):
    """ScheduleFetchSuccessfulDTO model"""
    schedules: List[ScheduleDto]
    total: List[str]
    traceId: str

class InvalidLocationDTO(BaseModel):
    """InvalidLocationDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class NotFoundDTO(BaseModel):
    """NotFoundDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None
    error: Optional[str] = None

class CreateBuilderDto(BaseModel):
    """CreateBuilderDto model"""
    locationId: str
    title: Optional[str] = None
    type: str
    updatedBy: Optional[str] = None
    builderVersion: Optional[str] = None
    name: Optional[str] = None
    parentId: Optional[str] = None
    templateDataUrl: Optional[str] = None
    importProvider: str
    importURL: Optional[str] = None
    templateSource: Optional[str] = None
    isPlainText: Optional[bool] = None

class CreateBuilderSuccesfulResponseDto(BaseModel):
    """CreateBuilderSuccesfulResponseDto model"""
    redirect: str
    traceId: str

class FetchBuilderSuccesfulResponseDto(BaseModel):
    """FetchBuilderSuccesfulResponseDto model"""
    name: Optional[str] = None
    updatedBy: Optional[str] = None
    isPlainText: Optional[bool] = None
    lastUpdated: Optional[str] = None
    dateAdded: Optional[str] = None
    previewUrl: Optional[str] = None
    id: Optional[str] = None
    version: Optional[str] = None
    templateType: Optional[str] = None

class DeleteBuilderSuccesfulResponseDto(BaseModel):
    """DeleteBuilderSuccesfulResponseDto model"""
    ok: Optional[str] = None
    traceId: Optional[str] = None

class TemplateSettings(BaseModel):
    """TemplateSettings model"""

class IBuilderJsonMapper(BaseModel):
    """IBuilderJsonMapper model"""
    elements: List[str]
    attrs: Dict[str, Any]
    templateSettings: TemplateSettings

class SaveBuilderDataDto(BaseModel):
    """SaveBuilderDataDto model"""
    locationId: str
    templateId: str
    updatedBy: str
    dnd: Any
    html: str
    editorType: str
    previewText: Optional[str] = None
    isPlainText: Optional[bool] = None

class BuilderUpdateSuccessfulDTO(BaseModel):
    """BuilderUpdateSuccessfulDTO model"""
    ok: Optional[str] = None
    traceId: Optional[str] = None
    previewUrl: Optional[str] = None
    templateDownloadUrl: Optional[str] = None

