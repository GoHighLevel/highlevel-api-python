# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# ConversationAi Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class triggerWorkflowDto(BaseModel):
    """triggerWorkflowDto model"""
    workflowIds: List[str]
    triggerCondition: str
    triggerMessage: Optional[str] = None

class updateContactFieldDto(BaseModel):
    """updateContactFieldDto model"""
    contactFieldId: str
    description: str
    contactUpdateExamples: Optional[List[str]] = None

class appointmentBookingDto(BaseModel):
    """appointmentBookingDto model"""
    actionId: Optional[str] = None
    calendarId: str
    onlySendLink: bool
    triggerWorkflow: bool
    workflowIds: Optional[List[str]] = None
    sleepAfterBooking: bool
    sleepTimeUnit: Optional[str] = None
    sleepTime: Optional[float] = None
    transferBot: bool
    transferAgent: Optional[str] = None
    rescheduleEnabled: bool
    cancelEnabled: bool

class stopBotDto(BaseModel):
    """stopBotDto model"""
    stopBotDetectionType: str
    stopBotTriggerCondition: str
    reactivateEnabled: bool
    sleepTimeUnit: Optional[str] = None
    sleepTime: Optional[float] = None
    enabled: bool
    stopBotExamples: List[str]
    finalMessage: str
    tags: Optional[List[str]] = None

class humanHandOverDto(BaseModel):
    """humanHandOverDto model"""
    enabled: bool
    triggerCondition: str
    examples: Optional[List[str]] = None
    assignToUserId: Optional[str] = None
    skipAssignToUser: Optional[bool] = None
    createTask: Optional[bool] = None
    reactivateEnabled: bool
    sleepTimeUnit: Optional[str] = None
    sleepTime: Optional[float] = None
    finalMessage: str
    tags: Optional[List[str]] = None
    handoverType: str

class FollowupSequence(BaseModel):
    """FollowupSequence model"""
    id: float
    followupTimeUnit: str
    followupTime: float
    aiEnabledMessage: Optional[bool] = None
    triggerWorkflow: Optional[bool] = None
    customMessage: Optional[str] = None
    workflowId: Optional[str] = None
    contactRequested: Optional[bool] = None

class Interval(BaseModel):
    """Interval model"""
    startHour: float
    startMinute: float
    endHour: float
    endMinute: float

class WorkingHours(BaseModel):
    """WorkingHours model"""
    dayOfTheWeek: float
    intervals: Optional[List[Interval]] = None

class FollowupSettings(BaseModel):
    """FollowupSettings model"""
    dynamicChannelSwitching: bool
    followUpHours: Optional[bool] = None
    workingHours: Optional[List[WorkingHours]] = None
    timezoneToUse: Optional[str] = None

class advancedFollowupDto(BaseModel):
    """advancedFollowupDto model"""
    enabled: bool
    scenarioId: str
    followupSequence: List[FollowupSequence]
    followupSettings: Optional[Any] = None

class transferBotDto(BaseModel):
    """transferBotDto model"""
    transferBotType: str
    transferToBot: str
    enabled: bool
    transferBotTriggerCondition: Optional[str] = None
    transferBotExamples: Optional[List[str]] = None

class CreateActionDTO(BaseModel):
    """CreateActionDTO model"""
    type: str
    name: str
    details: Any

class ActionDataDTO(BaseModel):
    """ActionDataDTO model"""
    id: str
    name: str
    type: str
    agentId: Optional[str] = None
    details: Any

class createActionResponseDTO(BaseModel):
    """createActionResponseDTO model"""
    data: Any
    success: bool

class fetchActionsForEmployeeResponseDTO(BaseModel):
    """fetchActionsForEmployeeResponseDTO model"""
    data: List[ActionDataDTO]
    success: bool

class fetchActionDetailsResponseDTO(BaseModel):
    """fetchActionDetailsResponseDTO model"""
    data: Any
    success: bool

class updateActionResponseDTO(BaseModel):
    """updateActionResponseDTO model"""
    data: Any
    success: bool

class DeleteActionDataDTO(BaseModel):
    """DeleteActionDataDTO model"""
    id: str

class deleteActionResponseDTO(BaseModel):
    """deleteActionResponseDTO model"""
    data: Any
    success: bool

class UpdateFollowupSettingsDTO(BaseModel):
    """UpdateFollowupSettingsDTO model"""
    actionIds: List[str]
    followupSettings: FollowupSettings

class CreateEmployeeDto(BaseModel):
    """CreateEmployeeDto model"""
    name: str
    businessName: Optional[str] = None
    mode: Optional[str] = None
    channels: Optional[List[str]] = None
    isPrimary: Optional[bool] = None
    waitTime: Optional[float] = None
    waitTimeUnit: Optional[str] = None
    sleepEnabled: Optional[bool] = None
    sleepTime: Optional[float] = None
    sleepTimeUnit: Optional[str] = None
    personality: str
    goal: str
    instructions: str
    autoPilotMaxMessages: Optional[float] = None
    knowledgeBaseIds: Optional[List[str]] = None
    respondToImages: Optional[bool] = None
    respondToAudio: Optional[bool] = None
    sleepOnManualMessage: Optional[bool] = None
    sleepOnWorkflowMessage: Optional[bool] = None

class ActionsIdDto(BaseModel):
    """ActionsIdDto model"""
    id: str
    type: str

class EmployeeResponseDTO(BaseModel):
    """EmployeeResponseDTO model"""
    id: str
    name: str
    businessName: Optional[str] = None
    mode: str
    channels: List[str]
    waitTime: float
    waitTimeUnit: str
    sleepEnabled: bool
    sleepTime: Optional[float] = None
    sleepTimeUnit: Optional[str] = None
    actions: List[ActionsIdDto]
    isPrimary: bool
    autoPilotMaxMessages: float
    goal: Optional[str] = None
    personality: Optional[str] = None
    instructions: Optional[str] = None
    knowledgeBaseIds: Optional[List[str]] = None
    sleepOnManualMessage: Optional[bool] = None
    sleepOnWorkflowMessage: Optional[bool] = None

class EmployeeListItemDTO(BaseModel):
    """EmployeeListItemDTO model"""
    id: str
    name: str
    businessName: Optional[str] = None
    mode: str
    channels: List[str]
    waitTime: float
    waitTimeUnit: str
    sleepEnabled: bool
    sleepTime: Optional[float] = None
    sleepTimeUnit: Optional[str] = None
    actions: List[Dict[str, Any]]
    isPrimary: bool
    autoPilotMaxMessages: float
    goal: Optional[Dict[str, Any]] = None
    knowledgeBaseIds: Optional[List[str]] = None
    createdAt: str
    updatedAt: str
    sleepOnManualMessage: Optional[bool] = None
    sleepOnWorkflowMessage: Optional[bool] = None

class SearchEmployeeResponseDTO(BaseModel):
    """SearchEmployeeResponseDTO model"""
    agents: List[EmployeeListItemDTO]
    totalCount: float
    count: float

class UpdateEmployeeDto(BaseModel):
    """UpdateEmployeeDto model"""
    name: Optional[str] = None
    businessName: Optional[str] = None
    mode: Optional[str] = None
    channels: Optional[List[str]] = None
    isPrimary: Optional[bool] = None
    waitTime: Optional[float] = None
    waitTimeUnit: Optional[str] = None
    sleepEnabled: Optional[bool] = None
    sleepTime: Optional[float] = None
    sleepTimeUnit: Optional[str] = None
    personality: Optional[str] = None
    goal: Optional[str] = None
    instructions: Optional[str] = None
    autoPilotMaxMessages: float
    knowledgeBaseIds: Optional[List[str]] = None
    respondToImages: Optional[bool] = None
    respondToAudio: Optional[bool] = None
    sleepOnManualMessage: Optional[bool] = None
    sleepOnWorkflowMessage: Optional[bool] = None

class DeleteEmployeeResponseDTO(BaseModel):
    """DeleteEmployeeResponseDTO model"""
    success: bool
    id: str

class FetchAIResponseDetailsResponseDTO(BaseModel):
    """FetchAIResponseDetailsResponseDTO model"""
    prompt: str
    intent: Optional[str] = None
    responseMessage: str
    faqs: Optional[List[Any]] = None
    website: Optional[List[Any]] = None
    agentId: Optional[str] = None
    input: Optional[str] = None
    actionLogs: List[Any]
    history: List[Any]
    mode: Optional[str] = None

