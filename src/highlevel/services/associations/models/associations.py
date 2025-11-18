from __future__ import annotations

# Associations Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class createRelationReqDto(BaseModel):
    """createRelationReqDto model"""
    locationId: str
    associationId: str
    firstRecordId: str
    secondRecordId: str

class GetPostSuccessfulResponseDto(BaseModel):
    """GetPostSuccessfulResponseDto model"""
    locationId: str
    id: str
    key: str
    firstObjectLabel: Dict[str, Any]
    firstObjectKey: Dict[str, Any]
    secondObjectLabel: Dict[str, Any]
    secondObjectKey: Dict[str, Any]
    associationType: Dict[str, Any]

class createAssociationReqDto(BaseModel):
    """createAssociationReqDto model"""
    locationId: str
    key: str
    firstObjectLabel: Dict[str, Any]
    firstObjectKey: Dict[str, Any]
    secondObjectLabel: Dict[str, Any]
    secondObjectKey: Dict[str, Any]

class UpdateAssociationReqDto(BaseModel):
    """UpdateAssociationReqDto model"""
    firstObjectLabel: Dict[str, Any]
    secondObjectLabel: Dict[str, Any]

class DeleteAssociationsResponseDTO(BaseModel):
    """DeleteAssociationsResponseDTO model"""
    deleted: bool
    id: str
    message: str

