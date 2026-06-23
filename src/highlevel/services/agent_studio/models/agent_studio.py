# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# AgentStudio Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class InternalServerErrorDTO(BaseModel):
    """InternalServerErrorDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class CreatePublicAgentDTO(BaseModel):
    """CreatePublicAgentDTO model"""
    locationId: str
    name: Optional[str] = None
    description: Optional[str] = None
    agencyId: Optional[str] = None
    authorId: Optional[str] = None
    authorName: Optional[str] = None
    authorEmail: Optional[str] = None
    status: str
    version: Dict[str, Any]
    nodes: Optional[List[str]] = None
    edges: Optional[List[str]] = None

class CreatePublicAgentResponseDTO(BaseModel):
    """CreatePublicAgentResponseDTO model"""
    success: bool
    message: str
    agent: Dict[str, Any]
    versions: List[Any]

class UpdatePublicAgentVersionDTO(BaseModel):
    """UpdatePublicAgentVersionDTO model"""
    locationId: str
    versionName: Optional[str] = None
    description: Optional[str] = None
    nodes: Optional[List[Dict[str, Any]]] = None
    edges: Optional[List[Dict[str, Any]]] = None
    globalVariables: Optional[List[Dict[str, Any]]] = None
    inputVariables: Optional[List[Dict[str, Any]]] = None
    runtimeVariables: Optional[List[Dict[str, Any]]] = None
    globalConfig: Optional[Dict[str, Any]] = None
    userId: Optional[str] = None
    userName: Optional[str] = None

class UpdatePublicAgentResponseDTO(BaseModel):
    """UpdatePublicAgentResponseDTO model"""
    success: bool
    message: str
    data: Dict[str, Any]

class UpdatePublicAgentMetadataDTO(BaseModel):
    """UpdatePublicAgentMetadataDTO model"""
    locationId: str
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class DeletePublicAgentResponseDTO(BaseModel):
    """DeletePublicAgentResponseDTO model"""
    success: bool
    message: str
    agentId: Optional[str] = None

class PromoteAndPublishDTO(BaseModel):
    """PromoteAndPublishDTO model"""
    locationId: str
    userId: Optional[str] = None
    userName: Optional[str] = None
    userEmail: Optional[str] = None

class PromoteAndPublishResponseDTO(BaseModel):
    """PromoteAndPublishResponseDTO model"""
    success: bool
    message: str
    data: Dict[str, Any]

class GetPublishedAgentsResponseDTO(BaseModel):
    """GetPublishedAgentsResponseDTO model"""
    success: bool
    message: str
    agents: List[Dict[str, Any]]
    pagination: Dict[str, Any]

class GetAgentByIdResponseDTO(BaseModel):
    """GetAgentByIdResponseDTO model"""
    success: bool
    message: str
    agent: Dict[str, Any]
    traceId: Optional[str] = None

class PublicAttachmentSchema(BaseModel):
    """PublicAttachmentSchema model"""
    type: str
    imageUrl: str

class ExecutePublicAgentDTO(BaseModel):
    """ExecutePublicAgentDTO model"""
    message: str
    executionId: Optional[str] = None
    inputVariables: Optional[Dict[str, Any]] = None
    versionId: Optional[str] = None
    attachments: Optional[List[PublicAttachmentSchema]] = None
    locationId: str
    contactId: Optional[str] = None

class ExecutePublicAgentResponseDTO(BaseModel):
    """ExecutePublicAgentResponseDTO model"""
    success: bool
    executionId: str
    interactionId: str
    response: str
    type: str
    nextExpectedInput: str
    goalCompletion: bool
    executionStatus: str
    flowSwitch: bool
    attachments: List[Any]
    generativeOutputs: List[Any]

