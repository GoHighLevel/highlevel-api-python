from __future__ import annotations

# VoiceAi Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class VoiceAILanguage(BaseModel):
    """VoiceAILanguage model"""

class PatienceLevel(BaseModel):
    """PatienceLevel model"""

class SendPostCallNotificationDTO(BaseModel):
    """SendPostCallNotificationDTO model"""
    admins: bool
    allUsers: bool
    contactAssignedUser: bool
    specificUsers: List[str]
    customEmails: List[str]

class IntervalDTO(BaseModel):
    """IntervalDTO model"""
    startHour: float
    endHour: float
    startMinute: float
    endMinute: float

class AgentWorkingHoursDTO(BaseModel):
    """AgentWorkingHoursDTO model"""
    dayOfTheWeek: float
    intervals: List[IntervalDTO]

class TranslationDTO(BaseModel):
    """TranslationDTO model"""
    enabled: bool
    language: Optional[str] = None

class AgentCreationRequestDTO(BaseModel):
    """AgentCreationRequestDTO model"""
    locationId: Optional[str] = None
    agentName: Optional[str] = None
    businessName: Optional[str] = None
    welcomeMessage: Optional[str] = None
    agentPrompt: Optional[str] = None
    voiceId: Optional[str] = None
    language: Optional[VoiceAILanguage] = None
    patienceLevel: Optional[PatienceLevel] = None
    maxCallDuration: Optional[float] = None
    sendUserIdleReminders: Optional[bool] = None
    reminderAfterIdleTimeSeconds: Optional[float] = None
    inboundNumber: Optional[str] = None
    numberPoolId: Optional[str] = None
    callEndWorkflowIds: Optional[List[str]] = None
    sendPostCallNotificationTo: Optional[Any] = None
    agentWorkingHours: Optional[List[AgentWorkingHoursDTO]] = None
    timezone: Optional[str] = None
    isAgentAsBackupDisabled: Optional[bool] = None
    translation: Optional[Any] = None

class SendPostCallNotificationSchema(BaseModel):
    """SendPostCallNotificationSchema model"""
    admins: Optional[bool] = None
    allUsers: Optional[bool] = None
    contactAssignedUser: Optional[bool] = None
    specificUsers: Optional[List[str]] = None
    customEmails: Optional[List[str]] = None

class TranslationSchema(BaseModel):
    """TranslationSchema model"""
    enabled: Optional[bool] = None
    language: Optional[str] = None

class CreateAgentResponseDTO(BaseModel):
    """CreateAgentResponseDTO model"""
    id: str
    locationId: str
    agentName: str
    businessName: str
    welcomeMessage: str
    agentPrompt: str
    voiceId: str
    language: str
    patienceLevel: str
    maxCallDuration: float
    sendUserIdleReminders: bool
    reminderAfterIdleTimeSeconds: float
    inboundNumber: Optional[str] = None
    numberPoolId: Optional[str] = None
    callEndWorkflowIds: Optional[List[str]] = None
    sendPostCallNotificationTo: Optional[Any] = None
    agentWorkingHours: Optional[List[AgentWorkingHoursDTO]] = None
    timezone: str
    isAgentAsBackupDisabled: bool
    translation: Optional[Any] = None

class PatchAgentDTO(BaseModel):
    """PatchAgentDTO model"""
    agentName: Optional[str] = None
    businessName: Optional[str] = None
    welcomeMessage: Optional[str] = None
    agentPrompt: Optional[str] = None
    voiceId: Optional[str] = None
    language: Optional[VoiceAILanguage] = None
    patienceLevel: Optional[PatienceLevel] = None
    maxCallDuration: Optional[float] = None
    sendUserIdleReminders: Optional[bool] = None
    reminderAfterIdleTimeSeconds: Optional[float] = None
    inboundNumber: Optional[str] = None
    numberPoolId: Optional[str] = None
    callEndWorkflowIds: Optional[List[str]] = None
    sendPostCallNotificationTo: Optional[Any] = None
    agentWorkingHours: Optional[List[AgentWorkingHoursDTO]] = None
    timezone: Optional[str] = None
    isAgentAsBackupDisabled: Optional[bool] = None
    translation: Optional[Any] = None

class PatchAgentResponseDTO(BaseModel):
    """PatchAgentResponseDTO model"""
    id: str
    locationId: str
    agentName: str
    businessName: str
    welcomeMessage: str
    agentPrompt: str
    voiceId: str
    language: str
    patienceLevel: str
    maxCallDuration: float
    sendUserIdleReminders: bool
    reminderAfterIdleTimeSeconds: float
    inboundNumber: Optional[str] = None
    numberPoolId: Optional[str] = None
    callEndWorkflowIds: Optional[List[str]] = None
    sendPostCallNotificationTo: Optional[Any] = None
    agentWorkingHours: Optional[List[AgentWorkingHoursDTO]] = None
    timezone: str
    isAgentAsBackupDisabled: bool
    translation: Optional[Any] = None

class AgentActionResponseDTO(BaseModel):
    """AgentActionResponseDTO model"""
    id: str
    actionType: str
    name: str
    actionParameters: Any

class GetAgentResponseDTO(BaseModel):
    """GetAgentResponseDTO model"""
    id: str
    locationId: str
    agentName: str
    businessName: str
    welcomeMessage: str
    agentPrompt: str
    voiceId: str
    language: str
    patienceLevel: str
    maxCallDuration: float
    sendUserIdleReminders: bool
    reminderAfterIdleTimeSeconds: float
    inboundNumber: Optional[str] = None
    numberPoolId: Optional[str] = None
    callEndWorkflowIds: Optional[List[str]] = None
    sendPostCallNotificationTo: Optional[Any] = None
    agentWorkingHours: Optional[List[AgentWorkingHoursDTO]] = None
    timezone: str
    isAgentAsBackupDisabled: bool
    translation: Optional[Any] = None
    actions: List[AgentActionResponseDTO]

class GetAgentsResponseDTO(BaseModel):
    """GetAgentsResponseDTO model"""
    total: float
    page: float
    pageSize: float
    agents: List[GetAgentResponseDTO]

class CallTransferActionParameters(BaseModel):
    """CallTransferActionParameters model"""
    triggerPrompt: str
    transferToType: str
    transferToValue: str
    triggerMessage: Optional[str] = None
    hearWhisperMessage: Optional[bool] = None

class DataExtractionActionParameters(BaseModel):
    """DataExtractionActionParameters model"""
    contactFieldId: str
    description: str
    examples: List[str]
    overwriteExistingValue: Optional[bool] = None

class InCallDataExtractionActionParameters(BaseModel):
    """InCallDataExtractionActionParameters model"""
    contactFieldId: str
    description: str
    examples: List[str]
    overwriteExistingValue: Optional[bool] = None

class WorkflowTriggerParameters(BaseModel):
    """WorkflowTriggerParameters model"""
    triggerPrompt: str
    triggerMessage: str
    workflowId: str

class SMSParameters(BaseModel):
    """SMSParameters model"""
    triggerPrompt: str
    triggerMessage: str
    messageBody: str

class AppointmentBookingActionParameters(BaseModel):
    """AppointmentBookingActionParameters model"""
    calendarId: str
    daysOfOfferingDates: float
    slotsPerDay: float
    hoursBetweenSlots: float

class CustomActionHeaderDTO(BaseModel):
    """CustomActionHeaderDTO model"""
    key: str
    value: str

class CustomActionParameterDTO(BaseModel):
    """CustomActionParameterDTO model"""
    name: str
    description: Optional[str] = None
    type: Optional[str] = None
    example: Optional[str] = None

class CustomActionApiDetailsDTO(BaseModel):
    """CustomActionApiDetailsDTO model"""
    url: str
    method: str
    authenticationRequired: Optional[bool] = None
    authenticationValue: Optional[str] = None
    headers: Optional[List[CustomActionHeaderDTO]] = None
    parameters: Optional[List[CustomActionParameterDTO]] = None

class CustomActionParameters(BaseModel):
    """CustomActionParameters model"""
    triggerPrompt: str
    triggerMessage: Optional[str] = None
    apiDetails: Any
    selectedPaths: Optional[List[str]] = None

class KnowledgeBaseParameters(BaseModel):
    """KnowledgeBaseParameters model"""
    triggerPrompt: Optional[str] = None
    triggerMessage: str
    knowledgeBaseId: str
    parameters: Optional[List[CustomActionParameterDTO]] = None

class CallActionSchema(BaseModel):
    """CallActionSchema model"""
    actionId: Optional[str] = None
    actionType: str
    actionName: str
    description: Optional[str] = None
    actionParameters: Optional[Any] = None
    executedAt: Optional[str] = None
    triggerReceivedAt: Optional[str] = None

class ExtractedDataSchema(BaseModel):
    """ExtractedDataSchema model"""

class CallLogDTO(BaseModel):
    """CallLogDTO model"""
    id: str
    contactId: Optional[str] = None
    agentId: str
    isAgentDeleted: bool
    fromNumber: Optional[str] = None
    createdAt: str
    duration: float
    trialCall: bool
    executedCallActions: List[CallActionSchema]
    summary: str
    transcript: str
    translation: Optional[Any] = None
    extractedData: Optional[Any] = None
    messageId: Optional[str] = None

class CallLogsResponseDTO(BaseModel):
    """CallLogsResponseDTO model"""
    total: float
    page: float
    pageSize: float
    callLogs: List[CallLogDTO]

class CreateSingleActionDTO(BaseModel):
    """CreateSingleActionDTO model"""
    agentId: str
    locationId: str
    actionType: str
    name: str
    actionParameters: Any

class CreateActionResponseDTO(BaseModel):
    """CreateActionResponseDTO model"""
    id: str
    actionType: str
    name: str
    actionParameters: Any

class UpdateSingleActionDTO(BaseModel):
    """UpdateSingleActionDTO model"""
    agentId: str
    locationId: str
    actionType: str
    name: str
    actionParameters: Any

class UpdateActionResponseDTO(BaseModel):
    """UpdateActionResponseDTO model"""
    id: str
    actionType: str
    name: str
    actionParameters: Any

class GetActionResponseDTO(BaseModel):
    """GetActionResponseDTO model"""
    id: str
    actionType: str
    name: str
    actionParameters: Any

