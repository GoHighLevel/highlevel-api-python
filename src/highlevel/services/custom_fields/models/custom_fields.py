from __future__ import annotations

# CustomFields Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

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

class CustomFieldSuccessfulResponseDto(BaseModel):
    """CustomFieldSuccessfulResponseDto model"""
    field: Optional[ICustomField] = None

class CustomFieldsResponseDTO(BaseModel):
    """CustomFieldsResponseDTO model"""
    fields: Optional[List[ICustomField]] = None
    folders: Optional[List[ICustomField]] = None

class CreateCustomFieldsDTO(BaseModel):
    """CreateCustomFieldsDTO model"""
    locationId: str
    name: Optional[str] = None
    description: Optional[str] = None
    placeholder: Optional[str] = None
    showInForms: bool
    options: Optional[List[OptionDTO]] = None
    acceptedFormats: Optional[str] = None
    dataType: str
    fieldKey: str
    objectKey: str
    maxFileLimit: Optional[float] = None
    allowCustomOption: Optional[bool] = None
    parentId: str

class CreateFolder(BaseModel):
    """CreateFolder model"""
    objectKey: str
    name: str
    locationId: str

class ICustomFieldFolder(BaseModel):
    """ICustomFieldFolder model"""
    id: str
    objectKey: str
    locationId: str
    name: str

class UpdateFolder(BaseModel):
    """UpdateFolder model"""
    name: str
    locationId: str

class CustomFolderDeleteResponseDto(BaseModel):
    """CustomFolderDeleteResponseDto model"""
    succeded: bool
    id: str
    key: str

class UpdateCustomFieldsDTO(BaseModel):
    """UpdateCustomFieldsDTO model"""
    locationId: str
    name: Optional[str] = None
    description: Optional[str] = None
    placeholder: Optional[str] = None
    showInForms: bool
    options: Optional[List[OptionDTO]] = None
    acceptedFormats: Optional[str] = None
    maxFileLimit: Optional[float] = None

