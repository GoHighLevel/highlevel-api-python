from __future__ import annotations

# Locations Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class SettingsSchema(BaseModel):
    """SettingsSchema model"""
    allowDuplicateContact: Optional[bool] = None
    allowDuplicateOpportunity: Optional[bool] = None
    allowFacebookNameMerge: Optional[bool] = None
    disableContactTimezone: Optional[bool] = None

class SocialSchema(BaseModel):
    """SocialSchema model"""
    facebookUrl: Optional[str] = None
    googlePlus: Optional[str] = None
    linkedIn: Optional[str] = None
    foursquare: Optional[str] = None
    twitter: Optional[str] = None
    yelp: Optional[str] = None
    instagram: Optional[str] = None
    youtube: Optional[str] = None
    pinterest: Optional[str] = None
    blogRss: Optional[str] = None
    googlePlacesId: Optional[str] = None

class GetLocationSchema(BaseModel):
    """GetLocationSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    settings: Optional[Any] = None
    social: Optional[Any] = None

class SearchSuccessfulResponseDto(BaseModel):
    """SearchSuccessfulResponseDto model"""
    locations: Optional[List[GetLocationSchema]] = None

class BusinessSchema(BaseModel):
    """BusinessSchema model"""
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    logoUrl: Optional[str] = None

class GetLocationByIdSchema(BaseModel):
    """GetLocationByIdSchema model"""
    id: Optional[str] = None
    companyId: Optional[str] = None
    name: Optional[str] = None
    domain: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    logoUrl: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    business: Optional[BusinessSchema] = None
    social: Optional[SocialSchema] = None
    settings: Optional[SettingsSchema] = None
    reseller: Optional[Dict[str, Any]] = None

class GetLocationByIdSuccessfulResponseDto(BaseModel):
    """GetLocationByIdSuccessfulResponseDto model"""
    location: Optional[GetLocationByIdSchema] = None

class ProspectInfoDto(BaseModel):
    """ProspectInfoDto model"""
    firstName: str
    lastName: str
    email: str

class TwilioSchema(BaseModel):
    """TwilioSchema model"""
    sid: str
    authToken: str

class MailgunSchema(BaseModel):
    """MailgunSchema model"""
    apiKey: str
    domain: str

class CreateLocationDto(BaseModel):
    """CreateLocationDto model"""
    name: str
    phone: Optional[str] = None
    companyId: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    prospectInfo: Optional[Any] = None
    settings: Optional[Any] = None
    social: Optional[Any] = None
    twilio: Optional[Any] = None
    mailgun: Optional[Any] = None
    snapshotId: Optional[str] = None

class CreateLocationSuccessfulResponseDto(BaseModel):
    """CreateLocationSuccessfulResponseDto model"""
    id: Optional[str] = None
    companyId: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    domain: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    settings: Optional[Any] = None
    social: Optional[Any] = None

class SnapshotPutSchema(BaseModel):
    """SnapshotPutSchema model"""
    id: str
    override: Optional[bool] = None

class UpdateLocationDto(BaseModel):
    """UpdateLocationDto model"""
    name: Optional[str] = None
    phone: Optional[str] = None
    companyId: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    prospectInfo: Optional[Any] = None
    settings: Optional[Any] = None
    social: Optional[Any] = None
    twilio: Optional[Any] = None
    mailgun: Optional[Any] = None
    snapshot: Optional[Any] = None

class LocationDeletedSuccessfulResponseDto(BaseModel):
    """LocationDeletedSuccessfulResponseDto model"""
    success: bool
    message: str

class LocationTagsSchema(BaseModel):
    """LocationTagsSchema model"""
    name: Optional[str] = None
    locationId: Optional[str] = None
    id: Optional[str] = None

class LocationTagsSuccessfulResponseDto(BaseModel):
    """LocationTagsSuccessfulResponseDto model"""
    tags: Optional[List[LocationTagsSchema]] = None

class LocationTagSuccessfulResponseDto(BaseModel):
    """LocationTagSuccessfulResponseDto model"""
    tag: Optional[LocationTagsSchema] = None

class tagBody(BaseModel):
    """tagBody model"""
    name: str

class LocationTagDeleteSuccessfulResponseDto(BaseModel):
    """LocationTagDeleteSuccessfulResponseDto model"""
    succeded: Optional[bool] = None

class TaskSearchParamsDto(BaseModel):
    """TaskSearchParamsDto model"""
    contactId: Optional[List[str]] = None
    completed: Optional[bool] = None
    assignedTo: Optional[List[str]] = None
    query: Optional[str] = None
    limit: Optional[float] = None
    skip: Optional[float] = None
    businessId: Optional[str] = None

class LocationTaskListSuccessfulResponseDto(BaseModel):
    """LocationTaskListSuccessfulResponseDto model"""
    tasks: Optional[List[List[Any]]] = None

class CustomFieldSchema(BaseModel):
    """CustomFieldSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    fieldKey: Optional[str] = None
    placeholder: Optional[str] = None
    dataType: Optional[str] = None
    position: Optional[float] = None
    picklistOptions: Optional[List[str]] = None
    picklistImageOptions: Optional[List[str]] = None
    isAllowedCustomOption: Optional[bool] = None
    isMultiFileAllowed: Optional[bool] = None
    maxFileLimit: Optional[float] = None
    locationId: Optional[str] = None
    model: Optional[str] = None

class CustomFieldsListSuccessfulResponseDto(BaseModel):
    """CustomFieldsListSuccessfulResponseDto model"""
    customFields: Optional[List[CustomFieldSchema]] = None

class CustomFieldSuccessfulResponseDto(BaseModel):
    """CustomFieldSuccessfulResponseDto model"""
    customField: Optional[CustomFieldSchema] = None

class textBoxListOptionsSchema(BaseModel):
    """textBoxListOptionsSchema model"""
    label: Optional[str] = None
    prefillValue: Optional[str] = None

class CreateCustomFieldsDTO(BaseModel):
    """CreateCustomFieldsDTO model"""
    name: str
    dataType: str
    placeholder: Optional[str] = None
    acceptedFormat: Optional[List[str]] = None
    isMultipleFile: Optional[bool] = None
    maxNumberOfFiles: Optional[float] = None
    textBoxListOptions: Optional[List[Any]] = None
    position: Optional[float] = None
    model: Optional[str] = None

class UpdateCustomFieldsDTO(BaseModel):
    """UpdateCustomFieldsDTO model"""
    name: str
    placeholder: Optional[str] = None
    acceptedFormat: Optional[List[str]] = None
    isMultipleFile: Optional[bool] = None
    maxNumberOfFiles: Optional[float] = None
    textBoxListOptions: Optional[List[Any]] = None
    position: Optional[float] = None
    model: Optional[str] = None

class CustomFieldDeleteSuccessfulResponseDto(BaseModel):
    """CustomFieldDeleteSuccessfulResponseDto model"""
    succeded: Optional[bool] = None

class FileUploadBody(BaseModel):
    """FileUploadBody model"""
    id: Optional[str] = None
    maxFiles: Optional[str] = None

class FileUploadResponseDto(BaseModel):
    """FileUploadResponseDto model"""
    uploadedFiles: Optional[Dict[str, Any]] = None
    meta: Optional[List[str]] = None

class CustomValueSchema(BaseModel):
    """CustomValueSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    fieldKey: Optional[str] = None
    value: Optional[str] = None
    locationId: Optional[str] = None

class CustomValuesListSuccessfulResponseDto(BaseModel):
    """CustomValuesListSuccessfulResponseDto model"""
    customValues: Optional[List[CustomValueSchema]] = None

class CustomValueIdSuccessfulResponseDto(BaseModel):
    """CustomValueIdSuccessfulResponseDto model"""
    customValue: Optional[CustomValueSchema] = None

class customValuesDTO(BaseModel):
    """customValuesDTO model"""
    name: str
    value: str

class CustomValueDeleteSuccessfulResponseDto(BaseModel):
    """CustomValueDeleteSuccessfulResponseDto model"""
    succeded: Optional[bool] = None

class SmsTemplateSchema(BaseModel):
    """SmsTemplateSchema model"""
    body: Optional[str] = None
    attachments: Optional[List[List[Any]]] = None

class GetSmsTemplateResponseSchema(BaseModel):
    """GetSmsTemplateResponseSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    template: Optional[SmsTemplateSchema] = None
    dateAdded: Optional[str] = None
    locationId: Optional[str] = None
    urlAttachments: Optional[List[str]] = None

class EmailTemplateSchema(BaseModel):
    """EmailTemplateSchema model"""
    subject: Optional[str] = None
    attachments: Optional[List[List[Any]]] = None
    html: Optional[str] = None

class GetEmailTemplateResponseSchema(BaseModel):
    """GetEmailTemplateResponseSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    dateAdded: Optional[str] = None
    template: Optional[EmailTemplateSchema] = None
    locationId: Optional[str] = None

class GetTemplatesSuccessfulResponseDto(BaseModel):
    """GetTemplatesSuccessfulResponseDto model"""
    templates: Optional[List[Any]] = None
    totalCount: Optional[float] = None

class CustomRRulesOptions(BaseModel):
    """CustomRRulesOptions model"""
    intervalType: str
    interval: float
    startDate: str
    endDate: Optional[str] = None
    dayOfMonth: Optional[float] = None
    dayOfWeek: Optional[str] = None
    monthOfYear: Optional[float] = None
    count: Optional[float] = None
    createTaskIfOverDue: Optional[bool] = None
    dueAfterSeconds: float

class RecurringTaskResponseDTO(BaseModel):
    """RecurringTaskResponseDTO model"""
    id: str
    title: str
    description: str
    locationId: str
    updatedAt: str
    createdAt: str
    rruleOptions: Any
    totalOccurrence: float
    deleted: bool
    assignedTo: Optional[str] = None
    contactId: Optional[str] = None

class RecurringTaskSingleResponseDTO(BaseModel):
    """RecurringTaskSingleResponseDTO model"""
    recurringTask: Any

class RecurringTaskCreateDTO(BaseModel):
    """RecurringTaskCreateDTO model"""
    title: str
    description: Optional[str] = None
    contactIds: Optional[List[str]] = None
    owners: Optional[List[str]] = None
    rruleOptions: Any
    ignoreTaskCreation: Optional[bool] = None

class RecurringTaskUpdateDTO(BaseModel):
    """RecurringTaskUpdateDTO model"""
    title: Optional[str] = None
    description: Optional[str] = None
    contactIds: Optional[List[str]] = None
    owners: Optional[List[str]] = None
    rruleOptions: Optional[Any] = None
    ignoreTaskCreation: Optional[bool] = None

class DeleteRecurringTaskResponseDTO(BaseModel):
    """DeleteRecurringTaskResponseDTO model"""
    id: str
    success: bool

