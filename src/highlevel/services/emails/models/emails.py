# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# Emails Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class ScheduleDto(BaseModel):
    """ScheduleDto model"""
    name: str
    repeatAfter: str
    id: str
    parentId: str
    childCount: float
    campaignType: str
    bulkActionVersion: str
    _id: str
    status: str
    sendDays: List[str]
    deleted: bool
    migrated: bool
    archived: bool
    hasTracking: bool
    isPlainText: bool
    hasUtmTracking: bool
    enableResendToUnopened: bool
    locationId: str
    templateId: str
    templateType: str
    createdAt: str
    updatedAt: str
    __v: float
    documentId: str
    downloadUrl: str
    templateDataDownloadUrl: str
    child: List[str]

class ScheduleFetchSuccessfulDTO(BaseModel):
    """ScheduleFetchSuccessfulDTO model"""
    schedules: List[ScheduleDto]
    total: List[str]
    traceId: str

class InvalidLocationDTO(BaseModel):
    """InvalidLocationDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class NotFoundDTO(BaseModel):
    """NotFoundDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None
    error: Optional[str] = None

class CreateBuilderDto(BaseModel):
    """CreateBuilderDto model"""
    locationId: str
    title: Optional[str] = None
    type: str
    updatedBy: Optional[str] = None
    builderVersion: Optional[str] = None
    name: Optional[str] = None
    parentId: Optional[str] = None
    templateDataUrl: Optional[str] = None
    importProvider: str
    importURL: Optional[str] = None
    templateSource: Optional[str] = None
    isPlainText: Optional[bool] = None
    subjectLine: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    previewText: Optional[str] = None

class CreateBuilderSuccesfulResponseDto(BaseModel):
    """CreateBuilderSuccesfulResponseDto model"""
    redirect: str
    traceId: str

class FetchBuilderSuccesfulResponseDto(BaseModel):
    """FetchBuilderSuccesfulResponseDto model"""
    name: Optional[str] = None
    updatedBy: Optional[str] = None
    isPlainText: Optional[bool] = None
    lastUpdated: Optional[str] = None
    dateAdded: Optional[str] = None
    previewUrl: Optional[str] = None
    id: Optional[str] = None
    version: Optional[str] = None
    templateType: Optional[str] = None

class DeleteBuilderSuccesfulResponseDto(BaseModel):
    """DeleteBuilderSuccesfulResponseDto model"""
    ok: Optional[str] = None
    traceId: Optional[str] = None

class TemplateSettings(BaseModel):
    """TemplateSettings model"""

class IBuilderJsonMapper(BaseModel):
    """IBuilderJsonMapper model"""
    elements: List[str]
    attrs: Dict[str, Any]
    templateSettings: Any

class SaveBuilderDataDto(BaseModel):
    """SaveBuilderDataDto model"""
    locationId: str
    templateId: str
    updatedBy: str
    dnd: Any
    html: str
    editorType: str
    previewText: Optional[str] = None
    isPlainText: Optional[bool] = None
    usedEmailAI: Optional[bool] = None

class BuilderUpdateSuccessfulDTO(BaseModel):
    """BuilderUpdateSuccessfulDTO model"""
    ok: Optional[str] = None
    traceId: Optional[str] = None
    previewUrl: Optional[str] = None
    templateDownloadUrl: Optional[str] = None
    versionId: Optional[str] = None

class UpdateEmailTemplateDto(BaseModel):
    """UpdateEmailTemplateDto model"""
    locationId: str
    updatedBy: Optional[str] = None
    editorContent: Optional[Any] = None
    editorType: Optional[str] = None
    previewText: Optional[str] = None
    subjectLine: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    name: Optional[str] = None
    archived: Optional[bool] = None
    fieldDefaults: Optional[Dict[str, Any]] = None

class UpdateEmailTemplateResponseDto(BaseModel):
    """UpdateEmailTemplateResponseDto model"""
    ok: bool
    id: str
    name: str
    archived: bool
    builderVersion: str
    fromName: str
    fromEmail: str
    subjectLine: str
    previewText: str
    previewUrl: str
    type: str
    lastUpdated: str
    createdAt: str
    isPlainText: bool
    fieldDefaults: Optional[Dict[str, Any]] = None

class BuilderElementNodePublicV2Dto(BaseModel):
    """BuilderElementNodePublicV2Dto model"""
    id: str
    tagName: str
    children: Optional[List[BuilderElementNodePublicV2Dto]] = None

class BuilderEditorContentPublicV2Dto(BaseModel):
    """BuilderEditorContentPublicV2Dto model"""
    elements: Optional[List[BuilderElementNodePublicV2Dto]] = None
    attrs: Optional[Dict[str, Any]] = None
    templateSettings: Optional[Dict[str, Any]] = None

class BuilderAttributePublicV2Dto(BaseModel):
    """BuilderAttributePublicV2Dto model"""
    name: str
    default: Optional[Dict[str, Any]] = None
    unit: Optional[str] = None

class BuilderCustomFlagsPublicV2Dto(BaseModel):
    """BuilderCustomFlagsPublicV2Dto model"""
    layoutId: Optional[Dict[str, Any]] = None
    theme: Optional[str] = None
    socialElementType: Optional[str] = None

class BuilderNodeAttrsPublicV2Dto(BaseModel):
    """BuilderNodeAttrsPublicV2Dto model"""
    tagName: str
    attributes: List[BuilderAttributePublicV2Dto]
    content: Optional[str] = None
    customFlags: Optional[Any] = None

class CreateTemplatePublicV2BodyDto(BaseModel):
    """CreateTemplatePublicV2BodyDto model"""
    name: str
    editorType: str
    editorContent: Optional[str] = None
    parentFolderId: Optional[str] = None
    subjectLine: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    previewText: Optional[str] = None
    userId: Optional[str] = None

class CreateTemplatePublicV2ResponseDto(BaseModel):
    """CreateTemplatePublicV2ResponseDto model"""
    id: str
    name: str
    editorType: str
    isPlainText: bool
    parentFolderId: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    subjectLine: Optional[str] = None
    previewText: Optional[str] = None
    previewUrl: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    traceId: Optional[str] = None

class ImportTemplatePublicV2BodyDto(BaseModel):
    """ImportTemplatePublicV2BodyDto model"""
    importProvider: str
    importUrl: str
    name: Optional[str] = None
    parentFolderId: Optional[str] = None
    userId: Optional[str] = None

class ImportTemplatePublicV2ResponseDto(BaseModel):
    """ImportTemplatePublicV2ResponseDto model"""
    id: str
    name: str
    editorType: str
    isPlainText: bool
    parentFolderId: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    subjectLine: Optional[str] = None
    previewText: Optional[str] = None
    previewUrl: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    traceId: Optional[str] = None

class CreateTemplateFolderPublicV2BodyDto(BaseModel):
    """CreateTemplateFolderPublicV2BodyDto model"""
    name: str
    userId: Optional[str] = None

class CreateTemplateFolderPublicV2ResponseDto(BaseModel):
    """CreateTemplateFolderPublicV2ResponseDto model"""
    id: str
    name: str
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    traceId: Optional[str] = None

class TemplateListItemPublicV2Dto(BaseModel):
    """TemplateListItemPublicV2Dto model"""
    id: str
    name: str
    type: str
    isPlainText: Optional[bool] = None
    updatedAt: Optional[str] = None
    createdAt: Optional[str] = None
    previewUrl: Optional[str] = None
    editorType: Optional[str] = None
    childCount: Optional[float] = None
    hasChildren: Optional[bool] = None
    parentFolderId: Optional[str] = None

class ListTemplatesPublicV2ResponseDto(BaseModel):
    """ListTemplatesPublicV2ResponseDto model"""
    items: List[TemplateListItemPublicV2Dto]
    total: float
    traceId: Optional[str] = None

class GetTemplatePublicV2ResponseDto(BaseModel):
    """GetTemplatePublicV2ResponseDto model"""
    id: str
    name: str
    editorType: str
    isPlainText: bool
    parentFolderId: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    subject: Optional[str] = None
    previewText: Optional[str] = None
    editorContentUrl: Optional[str] = None
    deleted: bool
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    traceId: Optional[str] = None

class DeleteTemplatePublicV2ResponseDto(BaseModel):
    """DeleteTemplatePublicV2ResponseDto model"""
    deleted: bool
    traceId: Optional[str] = None

class UpdateTemplatePublicV2BodyDto(BaseModel):
    """UpdateTemplatePublicV2BodyDto model"""
    name: Optional[str] = None
    editorContent: Optional[str] = None
    editorType: Optional[str] = None
    previewText: Optional[str] = None
    subjectLine: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    archived: Optional[bool] = None
    parentFolderId: Optional[str] = None
    userId: Optional[str] = None

class UpdateTemplatePublicV2ResponseDto(BaseModel):
    """UpdateTemplatePublicV2ResponseDto model"""
    id: str
    name: str
    archived: bool
    fromName: str
    fromEmail: str
    subjectLine: str
    previewText: str
    previewUrl: str
    editorType: Optional[str] = None
    isPlainText: Optional[bool] = None
    parentFolderId: Optional[str] = None
    updatedAt: Optional[str] = None
    createdAt: Optional[str] = None
    traceId: Optional[str] = None

class EmailStatsNumbersDto(BaseModel):
    """EmailStatsNumbersDto model"""
    delivered: float
    opened: float
    clicked: float
    unsubscribed: float
    complained: float
    permanentFail: float
    temporaryFail: float
    rejected: float
    failed: float
    replied: float

class GetCampaignStatsResponseDto(BaseModel):
    """GetCampaignStatsResponseDto model"""
    locationId: str
    source: str
    sourceId: str
    subSourceId: Optional[str] = None
    stats: Any

class EmailStatsNumbersPublicV2Dto(BaseModel):
    """EmailStatsNumbersPublicV2Dto model"""
    sent: float
    accepted: float
    delivered: float
    opened: float
    clicked: float
    unsubscribed: float
    complained: float
    permanentFail: float
    temporaryFail: float
    rejected: float
    failed: float
    replied: float
    openRate: float
    clickRate: float
    unsubscribeRate: float
    complaintRate: float
    bounceRate: float
    replyRate: float

class GetCampaignStatsPublicV2ResponseDto(BaseModel):
    """GetCampaignStatsPublicV2ResponseDto model"""
    locationId: str
    source: str
    sourceId: str
    subSourceId: Optional[str] = None
    stats: Any
    traceId: Optional[str] = None

class WorkflowCampaignPublicDto(BaseModel):
    """WorkflowCampaignPublicDto model"""
    id: str
    name: str
    status: str
    sourceId: str
    deleted: bool
    createdAt: str
    updatedAt: str

class GetWorkflowCampaignsPublicResponseDto(BaseModel):
    """GetWorkflowCampaignsPublicResponseDto model"""
    campaigns: List[WorkflowCampaignPublicDto]
    total: float

class BulkActionCampaignEmailDetailsDto(BaseModel):
    """BulkActionCampaignEmailDetailsDto model"""
    subject: Optional[str] = None
    from_: Optional[str] = None
    name: Optional[str] = None
    templateId: Optional[str] = None

class BulkActionCampaignDto(BaseModel):
    """BulkActionCampaignDto model"""
    id: str
    name: str
    status: str
    scheduleType: str
    createdBy: str
    deleted: bool
    createdAt: str
    updatedAt: str
    completedAt: Optional[str] = None
    emailMetadata: Optional[Any] = None

class GetBulkActionCampaignsResponseDto(BaseModel):
    """GetBulkActionCampaignsResponseDto model"""
    campaigns: List[BulkActionCampaignDto]
    total: float

class CreateEmailCampaignPublicV2BodyDto(BaseModel):
    """CreateEmailCampaignPublicV2BodyDto model"""
    name: str
    editorType: str
    templateId: Optional[str] = None
    editorContent: Optional[str] = None
    parentFolderId: Optional[str] = None
    timeZone: str
    userId: str
    userName: Optional[str] = None

class EmailCampaignVariationPublicV2Dto(BaseModel):
    """EmailCampaignVariationPublicV2Dto model"""
    sourceId: str
    isWinner: bool

class CreateEmailCampaignPublicV2ResponseDto(BaseModel):
    """CreateEmailCampaignPublicV2ResponseDto model"""
    id: str
    source: Optional[str] = None
    sourceId: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    campaignType: Optional[str] = None
    campaignCategory: Optional[str] = None
    variations: Optional[List[EmailCampaignVariationPublicV2Dto]] = None
    deleted: bool
    createdAt: str
    updatedAt: str
    traceId: Optional[str] = None

class EmailCampaignPublicV2Dto(BaseModel):
    """EmailCampaignPublicV2Dto model"""
    id: str
    source: Optional[str] = None
    sourceId: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    campaignType: Optional[str] = None
    campaignCategory: Optional[str] = None
    variations: Optional[List[EmailCampaignVariationPublicV2Dto]] = None
    deleted: bool
    createdAt: str
    updatedAt: str

class ListEmailCampaignsPublicV2ResponseDto(BaseModel):
    """ListEmailCampaignsPublicV2ResponseDto model"""
    campaigns: List[EmailCampaignPublicV2Dto]
    total: float
    traceId: Optional[str] = None

class UpdateEmailCampaignPublicV2BodyDto(BaseModel):
    """UpdateEmailCampaignPublicV2BodyDto model"""
    name: Optional[str] = None
    editorContent: Optional[str] = None
    editorType: Optional[str] = None
    userId: Optional[str] = None

class UpdateEmailCampaignPublicV2ResponseDto(BaseModel):
    """UpdateEmailCampaignPublicV2ResponseDto model"""
    id: str
    source: Optional[str] = None
    sourceId: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    campaignType: Optional[str] = None
    campaignCategory: Optional[str] = None
    variations: Optional[List[EmailCampaignVariationPublicV2Dto]] = None
    deleted: bool
    createdAt: str
    updatedAt: str
    traceId: Optional[str] = None

class GetEmailCampaignPublicV2ResponseDto(BaseModel):
    """GetEmailCampaignPublicV2ResponseDto model"""
    id: str
    source: Optional[str] = None
    sourceId: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    campaignType: Optional[str] = None
    campaignCategory: Optional[str] = None
    variations: Optional[List[EmailCampaignVariationPublicV2Dto]] = None
    editorType: Optional[str] = None
    isPlainText: Optional[bool] = None
    editorContentUrl: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    subject: Optional[str] = None
    replyToAddress: Optional[str] = None
    previewText: Optional[str] = None
    deleted: bool
    createdAt: str
    updatedAt: str
    traceId: Optional[str] = None

class WorkflowCampaignPublicV2Dto(BaseModel):
    """WorkflowCampaignPublicV2Dto model"""
    id: str
    name: Optional[str] = None
    status: Optional[str] = None
    source: Optional[str] = None
    sourceId: Optional[str] = None
    deleted: Optional[bool] = None
    createdAt: str
    updatedAt: str

class ListWorkflowCampaignsPublicV2ResponseDto(BaseModel):
    """ListWorkflowCampaignsPublicV2ResponseDto model"""
    campaigns: List[WorkflowCampaignPublicV2Dto]
    total: float
    traceId: Optional[str] = None

class WorkflowCampaignSubSourcePublicV2Dto(BaseModel):
    """WorkflowCampaignSubSourcePublicV2Dto model"""
    id: str
    name: Optional[str] = None
    subject: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    previewText: Optional[str] = None
    editorType: Optional[str] = None
    isPlainText: Optional[bool] = None
    editorContentUrl: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class GetWorkflowCampaignPublicV2ResponseDto(BaseModel):
    """GetWorkflowCampaignPublicV2ResponseDto model"""
    id: str
    name: Optional[str] = None
    status: Optional[str] = None
    source: Optional[str] = None
    sourceId: Optional[str] = None
    subSources: Optional[List[WorkflowCampaignSubSourcePublicV2Dto]] = None
    deleted: Optional[bool] = None
    createdAt: str
    updatedAt: str
    traceId: Optional[str] = None

class BulkActionCampaignPublicV2Dto(BaseModel):
    """BulkActionCampaignPublicV2Dto model"""
    id: str
    source: Optional[str] = None
    sourceId: Optional[str] = None
    name: Optional[str] = None
    status: str
    scheduleType: Optional[str] = None
    deleted: bool
    createdAt: str
    updatedAt: str
    completedAt: Optional[str] = None
    emailMetadata: Optional[Any] = None

class ListBulkActionCampaignsPublicV2ResponseDto(BaseModel):
    """ListBulkActionCampaignsPublicV2ResponseDto model"""
    campaigns: List[BulkActionCampaignPublicV2Dto]
    total: float
    traceId: Optional[str] = None

class GetBulkActionCampaignPublicV2ResponseDto(BaseModel):
    """GetBulkActionCampaignPublicV2ResponseDto model"""
    id: str
    source: Optional[str] = None
    sourceId: Optional[str] = None
    name: Optional[str] = None
    status: str
    scheduleType: Optional[str] = None
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None
    subject: Optional[str] = None
    replyToAddress: Optional[str] = None
    previewText: Optional[str] = None
    editorType: Optional[str] = None
    isPlainText: Optional[bool] = None
    editorContentUrl: Optional[str] = None
    deleted: bool
    createdAt: str
    updatedAt: str
    completedAt: Optional[str] = None
    traceId: Optional[str] = None

class ScheduleCampaignEmailMetaPublicV2Dto(BaseModel):
    """ScheduleCampaignEmailMetaPublicV2Dto model"""
    subject: str
    fromName: str
    fromEmail: str
    replyToAddress: Optional[str] = None
    previewText: Optional[str] = None
    attachments: Optional[List[str]] = None

class ScheduleCampaignRecipientsPublicV2Dto(BaseModel):
    """ScheduleCampaignRecipientsPublicV2Dto model"""
    type: str
    contactIds: Optional[List[str]] = None
    tagIds: Optional[List[str]] = None
    segment: Optional[str] = None
    freezeList: Optional[bool] = None

class ScheduleCampaignBatchConfigPublicV2Dto(BaseModel):
    """ScheduleCampaignBatchConfigPublicV2Dto model"""
    batchSize: float
    interval: float
    intervalUnit: str
    skipDays: Optional[List[str]] = None
    windowStart: Optional[str] = None
    windowEnd: Optional[str] = None

class ScheduleCampaignTrackingPublicV2Dto(BaseModel):
    """ScheduleCampaignTrackingPublicV2Dto model"""
    clickTracking: Optional[bool] = None
    utmTracking: Optional[bool] = None

class ScheduleCampaignResendPublicV2Dto(BaseModel):
    """ScheduleCampaignResendPublicV2Dto model"""
    enabled: Optional[bool] = None
    waitHours: Optional[float] = None
    subject: Optional[str] = None

class ScheduleCampaignScheduleConfigPublicV2Dto(BaseModel):
    """ScheduleCampaignScheduleConfigPublicV2Dto model"""
    sendAt: Optional[str] = None
    batch: Optional[Any] = None
    tracking: Optional[Any] = None
    resend: Optional[Any] = None
    emailPreferenceId: Optional[str] = None

class ScheduleCampaignRssConfigPublicV2Dto(BaseModel):
    """ScheduleCampaignRssConfigPublicV2Dto model"""
    name: str
    rssFeedURL: str
    repeatAfter: str
    repeatAfterTime: str
    rssFeedLimit: Optional[float] = None
    startAtDay: Optional[str] = None
    startAtMonthDay: Optional[str] = None
    firstExecutionDate: Optional[str] = None

class ScheduleCampaignABTestVariationPublicV2Dto(BaseModel):
    """ScheduleCampaignABTestVariationPublicV2Dto model"""
    subject: Optional[str] = None
    documentId: Optional[str] = None

class ScheduleCampaignABTestConfigPublicV2Dto(BaseModel):
    """ScheduleCampaignABTestConfigPublicV2Dto model"""
    testType: str
    testDuration: float
    variationCount: float
    testSize: float
    winningCriteria: str
    variations: List[ScheduleCampaignABTestVariationPublicV2Dto]

class ScheduleCampaignPublicV2BodyDto(BaseModel):
    """ScheduleCampaignPublicV2BodyDto model"""
    scheduleType: str
    timeZone: str
    userId: str
    userName: Optional[str] = None
    emailMeta: Any
    recipients: Any
    sendDays: Optional[List[str]] = None
    scheduleConfig: Optional[Any] = None
    rssConfig: Optional[Any] = None
    abTestConfig: Optional[Any] = None

class ScheduleCampaignPublicV2ResponseDto(BaseModel):
    """ScheduleCampaignPublicV2ResponseDto model"""
    campaignId: str
    sourceId: str
    traceId: Optional[str] = None

class DeleteCampaignPublicV2ResponseDto(BaseModel):
    """DeleteCampaignPublicV2ResponseDto model"""
    deleted: bool
    traceId: Optional[str] = None

