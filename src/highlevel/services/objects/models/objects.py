from __future__ import annotations

# Objects Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class CustomObjectLabelDto(BaseModel):
    """CustomObjectLabelDto model"""
    singular: str
    plural: str

class ICustomObjectSchema(BaseModel):
    """ICustomObjectSchema model"""
    id: str
    standard: bool
    key: str
    labels: Any
    description: Optional[str] = None
    locationId: str
    primaryDisplayProperty: str
    dateAdded: str
    dateUpdated: str
    type: Optional[Dict[str, Any]] = None

class OptionDTO(BaseModel):
    """OptionDTO model"""
    key: str
    label: str
    url: Optional[str] = None

class ICustomField(BaseModel):
    """ICustomField model"""
    locationId: str
    name: Optional[str] = None
    description: Optional[str] = None
    placeholder: Optional[str] = None
    showInForms: bool
    options: Optional[List[OptionDTO]] = None
    acceptedFormats: Optional[str] = None
    id: str
    objectKey: str
    dataType: str
    parentId: str
    fieldKey: str
    allowCustomOption: Optional[bool] = None
    maxFileLimit: Optional[float] = None
    dateAdded: str
    dateUpdated: str

class CustomObjectByIdResponseDTO(BaseModel):
    """CustomObjectByIdResponseDTO model"""
    object: Optional[ICustomObjectSchema] = None
    cache: bool
    fields: Optional[List[ICustomField]] = None

class CustomObjectListResponseDTO(BaseModel):
    """CustomObjectListResponseDTO model"""
    objects: Optional[List[ICustomObjectSchema]] = None

class CustomObjectDisplayPropertyDetails(BaseModel):
    """CustomObjectDisplayPropertyDetails model"""
    key: str
    name: str
    dataType: str

class CreateCustomObjectSchemaDTO(BaseModel):
    """CreateCustomObjectSchemaDTO model"""
    labels: Any
    key: str
    description: Optional[str] = None
    locationId: str
    primaryDisplayPropertyDetails: Any

class CustomObjectResponseDTO(BaseModel):
    """CustomObjectResponseDTO model"""
    object: Optional[ICustomObjectSchema] = None

class CustomObjectLabelUpdateDto(BaseModel):
    """CustomObjectLabelUpdateDto model"""
    singular: Optional[str] = None
    plural: Optional[str] = None

class UpdateCustomObjectSchemaDTO(BaseModel):
    """UpdateCustomObjectSchemaDTO model"""
    labels: Optional[Any] = None
    description: Optional[str] = None
    locationId: str
    searchableProperties: List[str]

class IRecordSchema(BaseModel):
    """IRecordSchema model"""
    id: str
    owner: List[str]
    followers: List[str]
    properties: str
    dateAdded: str
    dateUpdated: str

class RecordByIdResponseDTO(BaseModel):
    """RecordByIdResponseDTO model"""
    record: Optional[IRecordSchema] = None

class CreateCustomObjectRecordDto(BaseModel):
    """CreateCustomObjectRecordDto model"""

class UpdateCustomObjectRecordDto(BaseModel):
    """UpdateCustomObjectRecordDto model"""

class ObjectRecordDeleteResponseDTO(BaseModel):
    """ObjectRecordDeleteResponseDTO model"""
    id: Optional[str] = None
    success: Optional[bool] = None

class SearchRecordsBody(BaseModel):
    """SearchRecordsBody model"""
    locationId: str
    page: float
    pageLimit: float
    query: str
    searchAfter: List[str]

class CreatedByResponseDTO(BaseModel):
    """CreatedByResponseDTO model"""
    channel: str
    createdAt: str
    source: str
    sourceId: str

class RecordResponseDTO(BaseModel):
    """RecordResponseDTO model"""
    id: str
    owner: List[str]
    followers: List[str]
    properties: str
    createdAt: str
    updatedAt: str
    locationId: str
    objectId: str
    objectKey: str
    createdBy: Any
    lastUpdatedBy: Any
    searchAfter: List[float]

class SearchRecordResponseDTO(BaseModel):
    """SearchRecordResponseDTO model"""
    records: Optional[List[RecordResponseDTO]] = None
    total: float

