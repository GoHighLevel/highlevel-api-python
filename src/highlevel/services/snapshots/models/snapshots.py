from __future__ import annotations

# Snapshots Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class SnapshotsSchema(BaseModel):
    """SnapshotsSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None

class GetSnapshotsSuccessfulResponseDto(BaseModel):
    """GetSnapshotsSuccessfulResponseDto model"""
    snapshots: Optional[List[SnapshotsSchema]] = None

class CreateSnapshotShareLinkRequestDTO(BaseModel):
    """CreateSnapshotShareLinkRequestDTO model"""
    snapshot_id: str
    share_type: str
    relationship_number: Optional[str] = None
    share_location_id: Optional[str] = None

class CreateSnapshotShareLinkSuccessfulResponseDTO(BaseModel):
    """CreateSnapshotShareLinkSuccessfulResponseDTO model"""
    id: Optional[str] = None
    shareLink: Optional[str] = None

class SnapshotStatusSchema(BaseModel):
    """SnapshotStatusSchema model"""
    id: Optional[str] = None
    locationId: Optional[str] = None
    status: Optional[str] = None
    dateAdded: Optional[str] = None

class GetSnapshotPushStatusSuccessfulResponseDTO(BaseModel):
    """GetSnapshotPushStatusSuccessfulResponseDTO model"""
    data: Optional[List[SnapshotStatusSchema]] = None

class SnapshotStatusSchemaWithAssets(BaseModel):
    """SnapshotStatusSchemaWithAssets model"""
    id: Optional[str] = None
    locationId: Optional[str] = None
    status: Optional[str] = None
    completed: Optional[List[str]] = None
    pending: Optional[List[str]] = None

class GetLatestSnapshotPushStatusSuccessfulResponseDTO(BaseModel):
    """GetLatestSnapshotPushStatusSuccessfulResponseDTO model"""
    data: Optional[SnapshotStatusSchemaWithAssets] = None

