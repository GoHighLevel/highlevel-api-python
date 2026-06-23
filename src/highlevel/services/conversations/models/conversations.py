# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# Conversations Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

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
    feedback: Optional[str] = None

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

class ExportMessagesResponseDto(BaseModel):
    """ExportMessagesResponseDto model"""
    messages: List[GetMessageResponseDto]
    nextCursor: Optional[str] = None
    total: float

class GetMessagesByConversationResponseDto(BaseModel):
    """GetMessagesByConversationResponseDto model"""
    lastMessageId: str
    nextPage: bool
    messages: List[GetMessageResponseDto]

class ForwardConfigDto(BaseModel):
    """ForwardConfigDto model"""
    isForwarded: bool
    forwardWholeThread: Optional[bool] = None
    messageId: Optional[str] = None
    emailMessageId: Optional[str] = None
    sourceContactId: Optional[str] = None
    sourceConversationId: Optional[str] = None
    toEmail: Optional[str] = None
    recipientContactId: Optional[str] = None
    recipientConversationId: Optional[str] = None

class SendMessageBodyDto(BaseModel):
    """SendMessageBodyDto model"""
    type: str
    subType: Dict[str, Any]
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
    customSubtypeId: Optional[str] = None
    emailReplyMode: Optional[str] = None
    fromNumber: Optional[str] = None
    toNumber: Optional[str] = None
    forward: Optional[Any] = None
    status: str
    usesNativeSchedulingAi: Optional[bool] = None
    optimizationPeriod: Optional[str] = None

class ForwardResponseDto(BaseModel):
    """ForwardResponseDto model"""
    forwardWholeThread: Optional[bool] = None
    messageId: Optional[str] = None
    emailMessageId: Optional[str] = None
    sourceContactId: Optional[str] = None
    sourceConversationId: Optional[str] = None
    forwardToEmail: Optional[str] = None
    recipientContactId: Optional[str] = None
    recipientConversationId: Optional[str] = None

class SendMessageResponseDto(BaseModel):
    """SendMessageResponseDto model"""
    conversationId: str
    emailMessageId: Optional[str] = None
    messageId: str
    messageIds: Optional[List[str]] = None
    msg: Optional[str] = None
    forwardData: Optional[Any] = None
    status: str

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
    contactId: str
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
    contactId: str
    locationId: str
    attachmentUrls: List[str]
    chatServiceSid: Optional[str] = None
    isGroupSms: Optional[str] = None

class UploadFilesResponseDto(BaseModel):
    """UploadFilesResponseDto model"""
    uploadedFiles: Dict[str, Any]
    twilioMediaSids: Optional[List[str]] = None

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

class AddMessageAttachmentsDto(BaseModel):
    """AddMessageAttachmentsDto model"""
    attachments: List[str]

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

class EmailEventsDto(BaseModel):
    """EmailEventsDto model"""
    delivered: Optional[int] = None
    opened: Optional[int] = None
    clicked: Optional[int] = None
    replied: Optional[int] = None
    failed: Optional[int] = None
    accepted: Optional[int] = None
    rejected: Optional[int] = None
    unsubscribed: Optional[int] = None
    complained: Optional[int] = None
    stored: Optional[int] = None

class UpdateRecipientMessageStatusDto(BaseModel):
    """UpdateRecipientMessageStatusDto model"""
    emailId: str
    status: str
    failReason: Optional[str] = None

class UpdateEmailMessageStatusDto(BaseModel):
    """UpdateEmailMessageStatusDto model"""
    events: Optional[Any] = None
    recipients: Optional[List[UpdateRecipientMessageStatusDto]] = None
    status: str

class UpdateEmailMessageStatusResponseDto(BaseModel):
    """UpdateEmailMessageStatusResponseDto model"""
    success: bool
    message: str

class SendReviewReplyDto(BaseModel):
    """SendReviewReplyDto model"""
    conversationId: str
    locationId: str
    message: str

class InitiateFileUploadDto(BaseModel):
    """InitiateFileUploadDto model"""
    locationId: str
    conversationId: str
    filename: str
    contentType: str
    fileSize: Optional[float] = None
    channel: str

class InitiateFileUploadResponseDto(BaseModel):
    """InitiateFileUploadResponseDto model"""
    uploadUrl: str
    uploadId: str
    filePath: str
    expiresAt: float
    maxFileSize: float

class CompleteFileUploadDto(BaseModel):
    """CompleteFileUploadDto model"""
    uploadId: str
    filePath: str
    locationId: str
    conversationId: str
    filename: str

class CompleteFileUploadResponseDto(BaseModel):
    """CompleteFileUploadResponseDto model"""
    uploadedFiles: Dict[str, Any]
    metadata: Dict[str, Any]

