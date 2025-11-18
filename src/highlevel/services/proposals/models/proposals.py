from __future__ import annotations

# Proposals Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class EntityReference(BaseModel):
    """EntityReference model"""

class ELEMENTS_LOOKUP(BaseModel):
    """ELEMENTS_LOOKUP model"""

class FillableFieldsDTO(BaseModel):
    """FillableFieldsDTO model"""
    fieldId: str
    isRequired: bool
    hasCompleted: bool
    recipient: str
    entityType: EntityReference
    id: str
    type: ELEMENTS_LOOKUP
    value: str

class DiscountDto(BaseModel):
    """DiscountDto model"""
    id: str
    value: float
    type: str

class GrandTotalDto(BaseModel):
    """GrandTotalDto model"""
    amount: float
    currency: str
    discountPercentage: float
    discounts: List[DiscountDto]

class RecipientItem(BaseModel):
    """RecipientItem model"""
    id: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: str
    phoneNumber: Optional[str] = None
    phone: Optional[str] = None
    hasCompleted: bool
    role: str
    isPrimary: bool
    signingOrder: float
    imgUrl: Optional[str] = None
    ip: Optional[str] = None
    userAgent: Optional[str] = None
    signedDate: Optional[str] = None
    contactName: Optional[str] = None
    country: Optional[str] = None
    entityName: Optional[str] = None
    initialsImgUrl: Optional[str] = None
    lastViewedAt: Optional[str] = None
    shareLink: Optional[str] = None

class ProposalEstimateLinksDto(BaseModel):
    """ProposalEstimateLinksDto model"""
    referenceId: str
    documentId: str
    recipientId: str
    entityName: str
    recipientCategory: str
    documentRevision: float
    createdBy: str
    deleted: bool

class DocumentDto(BaseModel):
    """DocumentDto model"""
    locationId: str
    documentId: str
    _id: str
    name: str
    type: str
    deleted: bool
    isExpired: bool
    documentRevision: float
    fillableFields: List[FillableFieldsDTO]
    grandTotal: Any
    locale: str
    status: List[str]
    paymentStatus: List[str]
    recipients: List[RecipientItem]
    links: List[ProposalEstimateLinksDto]
    updatedAt: str
    createdAt: str

class DocumentListResponseDto(BaseModel):
    """DocumentListResponseDto model"""
    documents: List[DocumentDto]
    total: float
    whiteLabelBaseUrl: Optional[float] = None
    whiteLabelBaseUrlForInvoice: Optional[float] = None

class BadRequestDTO(BaseModel):
    """BadRequestDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class CCRecipientItem(BaseModel):
    """CCRecipientItem model"""
    email: str
    id: str
    imageUrl: str
    contactName: str
    firstName: str
    lastName: str

class NotificationSendSettingDto(BaseModel):
    """NotificationSendSettingDto model"""
    templateId: str
    subject: str

class NotificationSenderSettingDto(BaseModel):
    """NotificationSenderSettingDto model"""
    fromEmail: str
    fromName: str

class NotificationSettingsDto(BaseModel):
    """NotificationSettingsDto model"""
    receive: NotificationSendSettingDto
    sender: NotificationSenderSettingDto

class SendDocumentDto(BaseModel):
    """SendDocumentDto model"""
    locationId: str
    documentId: str
    documentName: Optional[str] = None
    medium: Optional[str] = None
    ccRecipients: Optional[List[CCRecipientItem]] = None
    notificationSettings: Optional[Any] = None
    sentBy: str

class SendDocumentResponseDto(BaseModel):
    """SendDocumentResponseDto model"""
    success: bool
    links: List[ProposalEstimateLinksDto]

class TemplateListResponseDTO(BaseModel):
    """TemplateListResponseDTO model"""
    _id: str
    deleted: bool
    version: float
    name: str
    locationId: str
    type: str
    updatedBy: str
    isPublicDocument: bool
    createdAt: str
    updatedAt: str
    id: str
    documentCount: Optional[float] = None
    docFormUrl: Optional[str] = None

class TemplateListPaginationResponseDTO(BaseModel):
    """TemplateListPaginationResponseDTO model"""
    data: List[TemplateListResponseDTO]
    total: float
    traceId: Optional[str] = None

class SendDocumentFromPublicApiBodyDto(BaseModel):
    """SendDocumentFromPublicApiBodyDto model"""
    templateId: str
    userId: str
    sendDocument: Optional[bool] = None
    locationId: str
    contactId: str
    opportunityId: Optional[str] = None

class SendTemplateResponseDto(BaseModel):
    """SendTemplateResponseDto model"""
    success: bool
    links: List[ProposalEstimateLinksDto]

class UnauthorizedDTO(BaseModel):
    """UnauthorizedDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None
    error: Optional[str] = None

