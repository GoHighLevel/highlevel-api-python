from __future__ import annotations

# Medias Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class GetFilesResponseDTO(BaseModel):
    """GetFilesResponseDTO model"""
    files: List[str]

class UploadFileResponseDTO(BaseModel):
    """UploadFileResponseDTO model"""
    fileId: str
    url: str

class FolderDTO(BaseModel):
    """FolderDTO model"""
    altId: str
    altType: str
    name: str
    parentId: Optional[str] = None
    type: str
    deleted: Optional[bool] = None
    pendingUpload: Optional[bool] = None
    category: Optional[str] = None
    subCategory: Optional[str] = None
    isPrivate: Optional[bool] = None
    relocatedFolder: Optional[bool] = None
    migrationCompleted: Optional[bool] = None
    appFolder: Optional[bool] = None
    isEssential: Optional[bool] = None
    status: Optional[str] = None
    lastUpdatedBy: Optional[str] = None

class CreateFolderParams(BaseModel):
    """CreateFolderParams model"""
    altId: str
    altType: str
    name: str
    parentId: Optional[str] = None

class UpdateObject(BaseModel):
    """UpdateObject model"""
    name: str
    altType: str
    altId: str

class UpdateMediaObjects(BaseModel):
    """UpdateMediaObjects model"""
    altId: str
    altType: str
    filesToBeUpdated: List[UpdateMediaObject]

class DeleteMediaObjectItem(BaseModel):
    """DeleteMediaObjectItem model"""
    _id: str

class UpdateMediaObject(BaseModel):
    """UpdateMediaObject model"""
    id: str
    name: Optional[str] = None

class DeleteMediaObjectsBodyParams(BaseModel):
    """DeleteMediaObjectsBodyParams model"""
    filesToBeDeleted: List[DeleteMediaObjectItem]
    altType: str
    altId: str
    status: str

class MoveOrDeleteObjectParams(BaseModel):
    """MoveOrDeleteObjectParams model"""
    altType: str
    altId: str
    _id: str

