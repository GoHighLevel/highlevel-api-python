from __future__ import annotations

# Conversations Models

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

class ForbiddenDTO(BaseModel):
    """ForbiddenDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None
    error: Optional[str] = None

class StartAfterNumberSchema(BaseModel):
    """StartAfterNumberSchema model"""
    startAfterDate: Optional[float] = None

class StartAfterArrayNumberSchema(BaseModel):
    """StartAfterArrayNumberSchema model"""
    startAfterDate: Optional[List[str]] = None

class ConversationSchema(BaseModel):
    """ConversationSchema model"""
    id: str
    contactId: str
    locationId: str
    lastMessageBody: str
    lastMessageType: str
    type: str
    unreadCount: float
    fullName: str
    contactName: str
    email: str
    phone: str

class SendConversationResponseDto(BaseModel):
    """SendConversationResponseDto model"""
    conversations: List[ConversationSchema]
    total: float

class CreateConversationDto(BaseModel):
    """CreateConversationDto model"""
    locationId: str
    contactId: str

class ConversationCreateResponseDto(BaseModel):
    """ConversationCreateResponseDto model"""
    id: str
    dateUpdated: str
    dateAdded: str
    deleted: bool
    contactId: str
    locationId: str
    lastMessageDate: str
    assignedTo: Optional[str] = None

class CreateConversationSuccessResponse(BaseModel):
    """CreateConversationSuccessResponse model"""
    success: bool
    conversation: Any

class GetConversationByIdResponse(BaseModel):
    """GetConversationByIdResponse model"""
    contactId: str
    locationId: str
    deleted: bool
    inbox: bool
    type: float
    unreadCount: float
    assignedTo: Optional[str] = None
    id: str
    starred: Optional[bool] = None

class UpdateConversationDto(BaseModel):
    """UpdateConversationDto model"""
    locationId: str
    unreadCount: Optional[float] = None
    starred: Optional[bool] = None
    feedback: Optional[Dict[str, Any]] = None

class ConversationDto(BaseModel):
    """ConversationDto model"""
    id: Optional[str] = None
    locationId: str
    contactId: str
    assignedTo: Optional[str] = None
    userId: Optional[str] = None
    lastMessageBody: Optional[str] = None
    lastMessageDate: Optional[str] = None
    lastMessageType: Optional[str] = None
    unreadCount: Optional[float] = None
    inbox: Optional[bool] = None
    starred: Optional[bool] = None
    deleted: bool

class GetConversationSuccessfulResponse(BaseModel):
    """GetConversationSuccessfulResponse model"""
    success: bool
    conversation: Any

class DeleteConversationSuccessfulResponse(BaseModel):
    """DeleteConversationSuccessfulResponse model"""
    success: bool

class GetEmailMessageResponseDto(BaseModel):
    """GetEmailMessageResponseDto model"""
    id: str
    altId: Optional[str] = None
    threadId: str
    locationId: str
    contactId: str
    conversationId: str
    dateAdded: str
    subject: Optional[str] = None
    body: str
    direction: str
    status: Optional[str] = None
    contentType: str
    attachments: Optional[List[str]] = None
    provider: Optional[str] = None
    from_: str
    to: List[str]
    cc: Optional[List[str]] = None
    bcc: Optional[List[str]] = None
    replyToMessageId: Optional[str] = None
    source: Optional[str] = None
    conversationProviderId: Optional[str] = None

class CancelScheduledResponseDto(BaseModel):
    """CancelScheduledResponseDto model"""
    status: float
    message: str

class MessageMeta(BaseModel):
    """MessageMeta model"""
    callDuration: Optional[str] = None
    callStatus: Optional[str] = None
    email: Optional[Dict[str, Any]] = None

class GetMessageResponseDto(BaseModel):
    """GetMessageResponseDto model"""
    id: str
    altId: Optional[str] = None
    type: float
    messageType: str
    locationId: str
    contactId: str
    conversationId: str
    dateAdded: str
    body: Optional[str] = None
    direction: str
    status: Optional[str] = None
    contentType: str
    attachments: Optional[List[str]] = None
    meta: Optional[MessageMeta] = None
    source: Optional[str] = None
    userId: Optional[str] = None
    conversationProviderId: Optional[str] = None
    chatWidgetId: Optional[str] = None

class GetMessagesByConversationResponseDto(BaseModel):
    """GetMessagesByConversationResponseDto model"""
    messages: Dict[str, Any]

class SendMessageBodyDto(BaseModel):
    """SendMessageBodyDto model"""
    type: str
    contactId: str
    appointmentId: Optional[str] = None
    attachments: Optional[List[str]] = None
    emailFrom: Optional[str] = None
    emailCc: Optional[List[str]] = None
    emailBcc: Optional[List[str]] = None
    html: Optional[str] = None
    message: Optional[str] = None
    subject: Optional[str] = None
    replyMessageId: Optional[str] = None
    templateId: Optional[str] = None
    threadId: Optional[str] = None
    scheduledTimestamp: Optional[float] = None
    conversationProviderId: Optional[str] = None
    emailTo: Optional[str] = None
    emailReplyMode: Optional[str] = None
    fromNumber: Optional[str] = None
    toNumber: Optional[str] = None

class SendMessageResponseDto(BaseModel):
    """SendMessageResponseDto model"""
    conversationId: str
    emailMessageId: Optional[str] = None
    messageId: str
    messageIds: Optional[List[str]] = None
    msg: Optional[str] = None

class CallDataDTO(BaseModel):
    """CallDataDTO model"""
    to: Optional[str] = None
    from_: Optional[str] = None
    status: Optional[str] = None

class ProcessMessageBodyDto(BaseModel):
    """ProcessMessageBodyDto model"""
    type: str
    attachments: Optional[List[str]] = None
    message: Optional[str] = None
    conversationId: str
    conversationProviderId: str
    html: Optional[str] = None
    subject: Optional[str] = None
    emailFrom: Optional[str] = None
    emailTo: Optional[str] = None
    emailCc: Optional[List[str]] = None
    emailBcc: Optional[List[str]] = None
    emailMessageId: Optional[str] = None
    altId: Optional[str] = None
    direction: Optional[Dict[str, Any]] = None
    date: Optional[str] = None
    call: Optional[Any] = None

class ProcessMessageResponseDto(BaseModel):
    """ProcessMessageResponseDto model"""
    success: bool
    conversationId: str
    messageId: str
    message: str
    contactId: Optional[str] = None
    dateAdded: Optional[str] = None
    emailMessageId: Optional[str] = None

class ProcessOutboundMessageBodyDto(BaseModel):
    """ProcessOutboundMessageBodyDto model"""
    type: str
    attachments: Optional[List[str]] = None
    conversationId: str
    conversationProviderId: str
    altId: Optional[str] = None
    date: Optional[str] = None
    call: Optional[Any] = None

class UploadFilesDto(BaseModel):
    """UploadFilesDto model"""
    conversationId: str
    locationId: str
    attachmentUrls: List[str]

class UploadFilesResponseDto(BaseModel):
    """UploadFilesResponseDto model"""
    uploadedFiles: Dict[str, Any]

class UploadFilesErrorResponseDto(BaseModel):
    """UploadFilesErrorResponseDto model"""
    status: float
    message: str

class ErrorDto(BaseModel):
    """ErrorDto model"""
    code: str
    type: str
    message: str

class UpdateMessageStatusDto(BaseModel):
    """UpdateMessageStatusDto model"""
    status: str
    error: Optional[Any] = None
    emailMessageId: Optional[str] = None
    recipients: Optional[List[str]] = None

class GetMessageTranscriptionResponseDto(BaseModel):
    """GetMessageTranscriptionResponseDto model"""
    mediaChannel: float
    sentenceIndex: float
    startTime: float
    endTime: float
    transcript: str
    confidence: float

class UserTypingBody(BaseModel):
    """UserTypingBody model"""
    locationId: str
    isTyping: str
    visitorId: str
    conversationId: str

class CreateLiveChatMessageFeedbackResponse(BaseModel):
    """CreateLiveChatMessageFeedbackResponse model"""
    success: bool

