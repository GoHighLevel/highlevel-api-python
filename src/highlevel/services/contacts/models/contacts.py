from __future__ import annotations

# Contacts Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class SearchBodyV2DTO(BaseModel):
    """SearchBodyV2DTO model"""

class CustomFieldSchema(BaseModel):
    """CustomFieldSchema model"""
    id: Optional[str] = None
    value: Optional[str] = None

class DndSettingSchema(BaseModel):
    """DndSettingSchema model"""
    status: str
    message: Optional[str] = None
    code: Optional[str] = None

class DndSettingsSchema(BaseModel):
    """DndSettingsSchema model"""
    Call: Optional[DndSettingSchema] = None
    Email: Optional[DndSettingSchema] = None
    SMS: Optional[DndSettingSchema] = None
    WhatsApp: Optional[DndSettingSchema] = None
    GMB: Optional[DndSettingSchema] = None
    FB: Optional[DndSettingSchema] = None

class ContactOpportunity(BaseModel):
    """ContactOpportunity model"""
    id: str
    pipeline_id: str
    pipeline_stage_id: str
    monetary_value: float
    status: str

class Contact(BaseModel):
    """Contact model"""
    id: Optional[str] = None
    phoneLabel: Optional[str] = None
    country: Optional[str] = None
    address: Optional[str] = None
    source: Optional[str] = None
    type: Optional[str] = None
    locationId: Optional[str] = None
    dnd: Optional[bool] = None
    state: Optional[str] = None
    businessName: Optional[str] = None
    customFields: Optional[List[CustomFieldSchema]] = None
    tags: Optional[List[str]] = None
    dateAdded: Optional[str] = None
    additionalEmails: Optional[List[str]] = None
    phone: Optional[str] = None
    companyName: Optional[str] = None
    additionalPhones: Optional[List[str]] = None
    dateUpdated: Optional[str] = None
    city: Optional[str] = None
    dateOfBirth: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    firstNameLowerCase: Optional[str] = None
    lastNameLowerCase: Optional[str] = None
    email: Optional[str] = None
    assignedTo: Optional[str] = None
    followers: Optional[List[str]] = None
    validEmail: Optional[bool] = None
    dndSettings: Optional[DndSettingsSchema] = None
    opportunities: Optional[List[ContactOpportunity]] = None
    postalCode: Optional[str] = None
    businessId: Optional[str] = None
    searchAfter: Optional[List[str]] = None

class SearchContactSuccessResponseDto(BaseModel):
    """SearchContactSuccessResponseDto model"""
    contacts: List[Contact]
    total: float

class TaskSchema(BaseModel):
    """TaskSchema model"""
    id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    assignedTo: Optional[str] = None
    dueDate: Optional[str] = None
    completed: Optional[bool] = None
    contactId: Optional[str] = None

class TasksListSuccessfulResponseDto(BaseModel):
    """TasksListSuccessfulResponseDto model"""
    tasks: Optional[List[TaskSchema]] = None

class TaskByIsSuccessfulResponseDto(BaseModel):
    """TaskByIsSuccessfulResponseDto model"""
    task: Optional[TaskSchema] = None

class CreateTaskParams(BaseModel):
    """CreateTaskParams model"""
    title: str
    body: Optional[str] = None
    dueDate: str
    completed: bool
    assignedTo: Optional[str] = None

class UpdateTaskBody(BaseModel):
    """UpdateTaskBody model"""
    title: Optional[str] = None
    body: Optional[str] = None
    dueDate: Optional[str] = None
    completed: Optional[bool] = None
    assignedTo: Optional[str] = None

class UpdateTaskStatusParams(BaseModel):
    """UpdateTaskStatusParams model"""
    completed: bool

class DeleteTaskSuccessfulResponseDto(BaseModel):
    """DeleteTaskSuccessfulResponseDto model"""
    succeded: Optional[bool] = None

class GetEventSchema(BaseModel):
    """GetEventSchema model"""
    id: Optional[str] = None
    calendarId: Optional[str] = None
    status: Optional[str] = None
    title: Optional[str] = None
    assignedUserId: Optional[str] = None
    notes: Optional[str] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    address: Optional[str] = None
    locationId: Optional[str] = None
    contactId: Optional[str] = None
    groupId: Optional[str] = None
    appointmentStatus: Optional[str] = None
    users: Optional[List[str]] = None
    dateAdded: Optional[str] = None
    dateUpdated: Optional[str] = None
    assignedResources: Optional[List[str]] = None

class GetEventsSuccessfulResponseDto(BaseModel):
    """GetEventsSuccessfulResponseDto model"""
    events: Optional[List[GetEventSchema]] = None

class TagsDTO(BaseModel):
    """TagsDTO model"""
    tags: List[str]

class CreateAddTagSuccessfulResponseDto(BaseModel):
    """CreateAddTagSuccessfulResponseDto model"""
    tags: Optional[List[str]] = None

class CreateDeleteTagSuccessfulResponseDto(BaseModel):
    """CreateDeleteTagSuccessfulResponseDto model"""
    tags: Optional[List[str]] = None

class GetNoteSchema(BaseModel):
    """GetNoteSchema model"""
    id: Optional[str] = None
    body: Optional[str] = None
    userId: Optional[str] = None
    dateAdded: Optional[str] = None
    contactId: Optional[str] = None

class GetNotesListSuccessfulResponseDto(BaseModel):
    """GetNotesListSuccessfulResponseDto model"""
    notes: Optional[List[GetNoteSchema]] = None

class NotesDTO(BaseModel):
    """NotesDTO model"""
    userId: Optional[str] = None
    body: str

class GetCreateUpdateNoteSuccessfulResponseDto(BaseModel):
    """GetCreateUpdateNoteSuccessfulResponseDto model"""
    note: Optional[GetNoteSchema] = None

class DeleteNoteSuccessfulResponseDto(BaseModel):
    """DeleteNoteSuccessfulResponseDto model"""
    succeded: Optional[bool] = None

class UpdateTagsDTO(BaseModel):
    """UpdateTagsDTO model"""
    contacts: List[str]
    tags: List[str]
    locationId: str
    removeAllTags: Optional[bool] = None

class UpdateTagsResponseDTO(BaseModel):
    """UpdateTagsResponseDTO model"""
    succeded: bool
    errorCount: float
    responses: List[str]

class ContactsBusinessUpdate(BaseModel):
    """ContactsBusinessUpdate model"""
    locationId: str
    ids: List[str]
    businessId: str

class ContactsBulkUpateResponse(BaseModel):
    """ContactsBulkUpateResponse model"""
    success: bool
    ids: List[str]

class AttributionSource(BaseModel):
    """AttributionSource model"""
    url: str
    campaign: Optional[str] = None
    utmSource: Optional[str] = None
    utmMedium: Optional[str] = None
    utmContent: Optional[str] = None
    referrer: Optional[str] = None
    campaignId: Optional[str] = None
    fbclid: Optional[str] = None
    gclid: Optional[str] = None
    msclikid: Optional[str] = None
    dclid: Optional[str] = None
    fbc: Optional[str] = None
    fbp: Optional[str] = None
    fbEventId: Optional[str] = None
    userAgent: Optional[str] = None
    ip: Optional[str] = None
    medium: Optional[str] = None
    mediumId: Optional[str] = None

class GetContectByIdSchema(BaseModel):
    """GetContectByIdSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    locationId: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    emailLowerCase: Optional[str] = None
    timezone: Optional[str] = None
    companyName: Optional[str] = None
    phone: Optional[str] = None
    dnd: Optional[bool] = None
    dndSettings: Optional[DndSettingsSchema] = None
    type: Optional[str] = None
    source: Optional[str] = None
    assignedTo: Optional[str] = None
    address1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    tags: Optional[List[str]] = None
    dateOfBirth: Optional[str] = None
    dateAdded: Optional[str] = None
    dateUpdated: Optional[str] = None
    attachments: Optional[str] = None
    ssn: Optional[str] = None
    keyword: Optional[str] = None
    firstNameLowerCase: Optional[str] = None
    fullNameLowerCase: Optional[str] = None
    lastNameLowerCase: Optional[str] = None
    lastActivity: Optional[str] = None
    customFields: Optional[List[CustomFieldSchema]] = None
    businessId: Optional[str] = None
    attributionSource: Optional[AttributionSource] = None
    lastAttributionSource: Optional[AttributionSource] = None
    visitorId: Optional[str] = None

class ContactsByIdSuccessfulResponseDto(BaseModel):
    """ContactsByIdSuccessfulResponseDto model"""
    contact: Optional[GetContectByIdSchema] = None

class customFieldsInputArraySchema(BaseModel):
    """customFieldsInputArraySchema model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[List[str]] = None

class customFieldsInputObjectSchema(BaseModel):
    """customFieldsInputObjectSchema model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[Dict[str, Any]] = None

class customFieldsInputStringSchema(BaseModel):
    """customFieldsInputStringSchema model"""
    id: Optional[str] = None
    key: Optional[str] = None
    field_value: Optional[str] = None

class TextField(BaseModel):
    """TextField model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[str] = None

class LargeTextField(BaseModel):
    """LargeTextField model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[str] = None

class SingleSelectField(BaseModel):
    """SingleSelectField model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[str] = None

class RadioField(BaseModel):
    """RadioField model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[str] = None

class NumericField(BaseModel):
    """NumericField model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[Dict[str, Any]] = None

class MonetoryField(BaseModel):
    """MonetoryField model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[Dict[str, Any]] = None

class CheckboxField(BaseModel):
    """CheckboxField model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[List[str]] = None

class MultiSelectField(BaseModel):
    """MultiSelectField model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[List[str]] = None

class FileField(BaseModel):
    """FileField model"""
    id: str
    key: Optional[str] = None
    field_value: Optional[Dict[str, Any]] = None

class InboundDndSettingSchema(BaseModel):
    """InboundDndSettingSchema model"""
    status: str
    message: Optional[str] = None

class InboundDndSettingsSchema(BaseModel):
    """InboundDndSettingsSchema model"""
    all: Optional[InboundDndSettingSchema] = None

class CreateContactDto(BaseModel):
    """CreateContactDto model"""
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    locationId: str
    gender: Optional[str] = None
    phone: Optional[str] = None
    address1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    dnd: Optional[bool] = None
    dndSettings: Optional[DndSettingsSchema] = None
    inboundDndSettings: Optional[InboundDndSettingsSchema] = None
    tags: Optional[List[str]] = None
    customFields: Optional[List[Any]] = None
    source: Optional[str] = None
    country: Optional[str] = None
    companyName: Optional[str] = None
    assignedTo: Optional[str] = None

class CreateContactSchema(BaseModel):
    """CreateContactSchema model"""
    id: Optional[str] = None
    dateAdded: Optional[str] = None
    dateUpdated: Optional[str] = None
    deleted: Optional[bool] = None
    tags: Optional[List[str]] = None
    type: Optional[str] = None
    customFields: Optional[List[CustomFieldSchema]] = None
    locationId: Optional[str] = None
    firstName: Optional[str] = None
    firstNameLowerCase: Optional[str] = None
    fullNameLowerCase: Optional[str] = None
    lastName: Optional[str] = None
    lastNameLowerCase: Optional[str] = None
    email: Optional[str] = None
    emailLowerCase: Optional[str] = None
    bounceEmail: Optional[bool] = None
    unsubscribeEmail: Optional[bool] = None
    dnd: Optional[bool] = None
    dndSettings: Optional[DndSettingsSchema] = None
    phone: Optional[str] = None
    address1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    source: Optional[str] = None
    companyName: Optional[str] = None
    dateOfBirth: Optional[str] = None
    birthMonth: Optional[float] = None
    birthDay: Optional[float] = None
    lastSessionActivityAt: Optional[str] = None
    offers: Optional[List[str]] = None
    products: Optional[List[str]] = None
    businessId: Optional[str] = None
    assignedTo: Optional[str] = None

class CreateContactsSuccessfulResponseDto(BaseModel):
    """CreateContactsSuccessfulResponseDto model"""
    contact: Optional[CreateContactSchema] = None

class UpdateContactDto(BaseModel):
    """UpdateContactDto model"""
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    dnd: Optional[bool] = None
    dndSettings: Optional[DndSettingsSchema] = None
    inboundDndSettings: Optional[InboundDndSettingsSchema] = None
    tags: Optional[List[str]] = None
    customFields: Optional[List[Any]] = None
    source: Optional[str] = None
    country: Optional[str] = None
    assignedTo: Optional[str] = None

class UpdateContactsSuccessfulResponseDto(BaseModel):
    """UpdateContactsSuccessfulResponseDto model"""
    succeded: Optional[bool] = None
    contact: Optional[GetContectByIdSchema] = None

class UpsertContactDto(BaseModel):
    """UpsertContactDto model"""
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    locationId: str
    gender: Optional[str] = None
    phone: Optional[str] = None
    address1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    dnd: Optional[bool] = None
    dndSettings: Optional[DndSettingsSchema] = None
    inboundDndSettings: Optional[InboundDndSettingsSchema] = None
    tags: Optional[List[str]] = None
    customFields: Optional[List[Any]] = None
    source: Optional[str] = None
    country: Optional[str] = None
    companyName: Optional[str] = None
    assignedTo: Optional[str] = None

class UpsertContactsSuccessfulResponseDto(BaseModel):
    """UpsertContactsSuccessfulResponseDto model"""
    new: Optional[bool] = None
    contact: Optional[GetContectByIdSchema] = None
    traceId: Optional[str] = None

class DeleteContactsSuccessfulResponseDto(BaseModel):
    """DeleteContactsSuccessfulResponseDto model"""
    succeded: Optional[bool] = None

class ContactsSearchSchema(BaseModel):
    """ContactsSearchSchema model"""
    id: Optional[str] = None
    locationId: Optional[str] = None
    email: Optional[str] = None
    timezone: Optional[str] = None
    country: Optional[str] = None
    source: Optional[str] = None
    dateAdded: Optional[str] = None
    customFields: Optional[List[CustomFieldSchema]] = None
    tags: Optional[List[str]] = None
    businessId: Optional[str] = None
    attributions: Optional[List[AttributionSource]] = None
    followers: Optional[List[str]] = None

class ContactsMetaSchema(BaseModel):
    """ContactsMetaSchema model"""
    total: Optional[float] = None
    nextPageUrl: Optional[str] = None
    startAfterId: Optional[str] = None
    startAfter: Optional[float] = None
    currentPage: Optional[float] = None
    nextPage: Optional[float] = None
    prevPage: Optional[float] = None

class ContactsSearchSuccessfulResponseDto(BaseModel):
    """ContactsSearchSuccessfulResponseDto model"""
    contacts: Optional[List[ContactsSearchSchema]] = None
    count: Optional[float] = None

class FollowersDTO(BaseModel):
    """FollowersDTO model"""
    followers: List[str]

class CreateAddFollowersSuccessfulResponseDto(BaseModel):
    """CreateAddFollowersSuccessfulResponseDto model"""
    followers: Optional[List[str]] = None
    followersAdded: Optional[List[str]] = None

class DeleteFollowersSuccessfulResponseDto(BaseModel):
    """DeleteFollowersSuccessfulResponseDto model"""
    followers: Optional[List[str]] = None
    followersRemoved: Optional[List[str]] = None

class AddContactToCampaignDto(BaseModel):
    """AddContactToCampaignDto model"""

class CreateDeleteCantactsCampaignsSuccessfulResponseDto(BaseModel):
    """CreateDeleteCantactsCampaignsSuccessfulResponseDto model"""
    succeded: Optional[bool] = None

class CreateWorkflowDto(BaseModel):
    """CreateWorkflowDto model"""
    eventStartTime: Optional[str] = None

class ContactsWorkflowSuccessfulResponseDto(BaseModel):
    """ContactsWorkflowSuccessfulResponseDto model"""
    succeded: Optional[bool] = None

