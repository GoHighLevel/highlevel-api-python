from __future__ import annotations

# Calendars Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class GroupDTO(BaseModel):
    """GroupDTO model"""
    locationId: str
    name: str
    description: str
    slug: str
    isActive: Optional[bool] = None
    id: Optional[str] = None

class AllGroupsSuccessfulResponseDTO(BaseModel):
    """AllGroupsSuccessfulResponseDTO model"""
    groups: Optional[List[GroupDTO]] = None

class ValidateGroupSlugPostBody(BaseModel):
    """ValidateGroupSlugPostBody model"""
    locationId: str
    slug: str

class ValidateGroupSlugSuccessResponseDTO(BaseModel):
    """ValidateGroupSlugSuccessResponseDTO model"""
    available: bool

class GroupCreateDTO(BaseModel):
    """GroupCreateDTO model"""
    locationId: str
    name: str
    description: str
    slug: str
    isActive: Optional[bool] = None

class GroupCreateSuccessfulResponseDTO(BaseModel):
    """GroupCreateSuccessfulResponseDTO model"""
    group: Optional[GroupDTO] = None

class GroupSuccessfulResponseDTO(BaseModel):
    """GroupSuccessfulResponseDTO model"""
    success: Optional[bool] = None

class GroupStatusUpdateParams(BaseModel):
    """GroupStatusUpdateParams model"""
    isActive: bool

class GroupUpdateDTO(BaseModel):
    """GroupUpdateDTO model"""
    name: str
    description: str
    slug: str

class AppointmentCreateSchema(BaseModel):
    """AppointmentCreateSchema model"""
    title: Optional[str] = None
    meetingLocationType: Optional[str] = None
    meetingLocationId: Optional[str] = None
    overrideLocationConfig: Optional[bool] = None
    appointmentStatus: Optional[str] = None
    assignedUserId: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    ignoreDateRange: Optional[bool] = None
    toNotify: Optional[bool] = None
    ignoreFreeSlotValidation: Optional[bool] = None
    rrule: Optional[str] = None
    calendarId: str
    locationId: str
    contactId: str
    startTime: str
    endTime: Optional[str] = None

class AppointmentSchemaResponse(BaseModel):
    """AppointmentSchemaResponse model"""
    calendarId: str
    locationId: str
    contactId: str
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    title: Optional[str] = None
    meetingLocationType: Optional[str] = None
    appointmentStatus: Optional[str] = None
    assignedUserId: Optional[str] = None
    address: Optional[str] = None
    isRecurring: Optional[bool] = None
    rrule: Optional[str] = None
    id: str

class AppointmentEditSchema(BaseModel):
    """AppointmentEditSchema model"""
    title: Optional[str] = None
    meetingLocationType: Optional[str] = None
    meetingLocationId: Optional[str] = None
    overrideLocationConfig: Optional[bool] = None
    appointmentStatus: Optional[str] = None
    assignedUserId: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    ignoreDateRange: Optional[bool] = None
    toNotify: Optional[bool] = None
    ignoreFreeSlotValidation: Optional[bool] = None
    rrule: Optional[str] = None
    calendarId: Optional[str] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None

class CreatedOrUpdatedBy(BaseModel):
    """CreatedOrUpdatedBy model"""
    userId: Optional[str] = None
    source: str

class CalendarEventDTO(BaseModel):
    """CalendarEventDTO model"""
    id: str
    address: Optional[str] = None
    title: str
    calendarId: str
    locationId: str
    contactId: str
    groupId: str
    appointmentStatus: str
    assignedUserId: str
    users: List[str]
    notes: Optional[str] = None
    description: Optional[str] = None
    isRecurring: Optional[bool] = None
    rrule: Optional[str] = None
    startTime: Dict[str, Any]
    endTime: Dict[str, Any]
    dateAdded: Dict[str, Any]
    dateUpdated: Dict[str, Any]
    assignedResources: Optional[List[str]] = None
    createdBy: Optional[Any] = None
    masterEventId: Optional[str] = None

class GetCalendarEventsSuccessfulResponseDTO(BaseModel):
    """GetCalendarEventsSuccessfulResponseDTO model"""
    events: Optional[List[CalendarEventDTO]] = None

class BlockSlotCreateRequestDTO(BaseModel):
    """BlockSlotCreateRequestDTO model"""
    title: Optional[str] = None
    calendarId: str
    assignedUserId: Optional[str] = None
    locationId: str
    startTime: Optional[str] = None
    endTime: Optional[str] = None

class BlockedSlotSuccessfulResponseDto(BaseModel):
    """BlockedSlotSuccessfulResponseDto model"""
    id: str
    locationId: str
    title: str
    startTime: Dict[str, Any]
    endTime: Dict[str, Any]
    calendarId: Optional[str] = None
    assignedUserId: Optional[str] = None

class BlockSlotEditRequestDTO(BaseModel):
    """BlockSlotEditRequestDTO model"""
    title: Optional[str] = None
    calendarId: str
    assignedUserId: Optional[str] = None
    locationId: str
    startTime: Optional[str] = None
    endTime: Optional[str] = None

class SlotsSchema(BaseModel):
    """SlotsSchema model"""
    slots: List[str]

class CalendarNotification(BaseModel):
    """CalendarNotification model"""
    type: Optional[str] = None
    shouldSendToContact: bool
    shouldSendToGuest: bool
    shouldSendToUser: bool
    shouldSendToSelectedUsers: bool
    selectedUsers: str

class LocationConfiguration(BaseModel):
    """LocationConfiguration model"""
    kind: str
    location: Optional[str] = None

class TeamMember(BaseModel):
    """TeamMember model"""
    userId: str
    priority: Optional[float] = None
    meetingLocationType: Optional[str] = None
    meetingLocation: Optional[str] = None
    isPrimary: Optional[bool] = None
    locationConfigurations: Optional[List[LocationConfiguration]] = None

class Hour(BaseModel):
    """Hour model"""
    openHour: float
    openMinute: float
    closeHour: float
    closeMinute: float

class OpenHour(BaseModel):
    """OpenHour model"""
    daysOfTheWeek: List[float]
    hours: List[Hour]

class Recurring(BaseModel):
    """Recurring model"""
    freq: Optional[str] = None
    count: Optional[float] = None
    bookingOption: Optional[str] = None
    bookingOverlapDefaultStatus: Optional[str] = None

class Availability(BaseModel):
    """Availability model"""
    date: str
    hours: List[Hour]
    deleted: Optional[bool] = None

class LookBusyConfiguration(BaseModel):
    """LookBusyConfiguration model"""
    enabled: bool
    LookBusyPercentage: float

class CalendarCreateDTO(BaseModel):
    """CalendarCreateDTO model"""
    isActive: Optional[bool] = None
    notifications: Optional[List[CalendarNotification]] = None
    locationId: str
    groupId: Optional[str] = None
    teamMembers: Optional[List[TeamMember]] = None
    eventType: Optional[str] = None
    name: str
    description: Optional[str] = None
    slug: Optional[str] = None
    widgetSlug: Optional[str] = None
    calendarType: Optional[str] = None
    widgetType: Optional[str] = None
    eventTitle: Optional[str] = None
    eventColor: Optional[str] = None
    meetingLocation: Optional[str] = None
    locationConfigurations: Optional[List[LocationConfiguration]] = None
    slotDuration: Optional[float] = None
    slotDurationUnit: Optional[str] = None
    slotInterval: Optional[float] = None
    slotIntervalUnit: Optional[str] = None
    slotBuffer: Optional[float] = None
    slotBufferUnit: Optional[str] = None
    preBuffer: Optional[float] = None
    preBufferUnit: Optional[str] = None
    appoinmentPerSlot: Optional[float] = None
    appoinmentPerDay: Optional[float] = None
    allowBookingAfter: Optional[float] = None
    allowBookingAfterUnit: Optional[str] = None
    allowBookingFor: Optional[float] = None
    allowBookingForUnit: Optional[str] = None
    openHours: Optional[List[OpenHour]] = None
    enableRecurring: Optional[bool] = None
    recurring: Optional[Recurring] = None
    formId: Optional[str] = None
    stickyContact: Optional[bool] = None
    isLivePaymentMode: Optional[bool] = None
    autoConfirm: Optional[bool] = None
    shouldSendAlertEmailsToAssignedMember: Optional[bool] = None
    alertEmail: Optional[str] = None
    googleInvitationEmails: Optional[bool] = None
    allowReschedule: Optional[bool] = None
    allowCancellation: Optional[bool] = None
    shouldAssignContactToTeamMember: Optional[bool] = None
    shouldSkipAssigningContactForExisting: Optional[bool] = None
    notes: Optional[str] = None
    pixelId: Optional[str] = None
    formSubmitType: Optional[str] = None
    formSubmitRedirectURL: Optional[str] = None
    formSubmitThanksMessage: Optional[str] = None
    availabilityType: Optional[float] = None
    availabilities: Optional[List[Availability]] = None
    guestType: Optional[str] = None
    consentLabel: Optional[str] = None
    calendarCoverImage: Optional[str] = None
    lookBusyConfig: Optional[Any] = None

class LocationConfigurationResponse(BaseModel):
    """LocationConfigurationResponse model"""
    kind: str
    location: Optional[str] = None
    meetingId: Optional[str] = None

class TeamMemberResponse(BaseModel):
    """TeamMemberResponse model"""
    userId: str
    priority: Optional[float] = None
    meetingLocationType: Optional[str] = None
    meetingLocation: Optional[str] = None
    isPrimary: Optional[bool] = None
    locationConfigurations: Optional[List[LocationConfigurationResponse]] = None

class CalendarDTO(BaseModel):
    """CalendarDTO model"""
    isActive: Optional[bool] = None
    notifications: Optional[List[CalendarNotification]] = None
    locationId: str
    groupId: Optional[str] = None
    teamMembers: Optional[List[TeamMemberResponse]] = None
    eventType: Optional[str] = None
    name: str
    description: Optional[str] = None
    slug: Optional[str] = None
    widgetSlug: Optional[str] = None
    calendarType: Optional[str] = None
    widgetType: Optional[str] = None
    eventTitle: Optional[str] = None
    eventColor: Optional[str] = None
    meetingLocation: Optional[str] = None
    locationConfigurations: Optional[List[LocationConfigurationResponse]] = None
    slotDuration: Optional[float] = None
    slotDurationUnit: Optional[str] = None
    slotInterval: Optional[float] = None
    slotIntervalUnit: Optional[str] = None
    slotBuffer: Optional[float] = None
    slotBufferUnit: Optional[str] = None
    preBuffer: Optional[float] = None
    preBufferUnit: Optional[str] = None
    appoinmentPerSlot: Optional[float] = None
    appoinmentPerDay: Optional[float] = None
    allowBookingAfter: Optional[float] = None
    allowBookingAfterUnit: Optional[str] = None
    allowBookingFor: Optional[float] = None
    allowBookingForUnit: Optional[str] = None
    openHours: Optional[List[OpenHour]] = None
    enableRecurring: Optional[bool] = None
    recurring: Optional[Recurring] = None
    formId: Optional[str] = None
    stickyContact: Optional[bool] = None
    isLivePaymentMode: Optional[bool] = None
    autoConfirm: Optional[bool] = None
    shouldSendAlertEmailsToAssignedMember: Optional[bool] = None
    alertEmail: Optional[str] = None
    googleInvitationEmails: Optional[bool] = None
    allowReschedule: Optional[bool] = None
    allowCancellation: Optional[bool] = None
    shouldAssignContactToTeamMember: Optional[bool] = None
    shouldSkipAssigningContactForExisting: Optional[bool] = None
    notes: Optional[str] = None
    pixelId: Optional[str] = None
    formSubmitType: Optional[str] = None
    formSubmitRedirectURL: Optional[str] = None
    formSubmitThanksMessage: Optional[str] = None
    availabilityType: Optional[float] = None
    availabilities: Optional[List[Availability]] = None
    guestType: Optional[str] = None
    consentLabel: Optional[str] = None
    calendarCoverImage: Optional[str] = None
    lookBusyConfig: Optional[Any] = None
    id: str

class CalendarsGetSuccessfulResponseDTO(BaseModel):
    """CalendarsGetSuccessfulResponseDTO model"""
    calendars: Optional[List[CalendarDTO]] = None

class CalendarByIdSuccessfulResponseDTO(BaseModel):
    """CalendarByIdSuccessfulResponseDTO model"""
    calendar: CalendarDTO

class UpdateAvailability(BaseModel):
    """UpdateAvailability model"""
    date: str
    hours: List[Hour]
    deleted: Optional[bool] = None
    id: Optional[str] = None

class CalendarUpdateDTO(BaseModel):
    """CalendarUpdateDTO model"""
    notifications: Optional[List[CalendarNotification]] = None
    groupId: Optional[str] = None
    teamMembers: Optional[List[TeamMember]] = None
    eventType: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
    widgetSlug: Optional[str] = None
    widgetType: Optional[str] = None
    eventTitle: Optional[str] = None
    eventColor: Optional[str] = None
    locationConfigurations: Optional[List[LocationConfiguration]] = None
    meetingLocation: Optional[str] = None
    slotDuration: Optional[float] = None
    slotDurationUnit: Optional[str] = None
    preBufferUnit: Optional[str] = None
    slotInterval: Optional[float] = None
    slotIntervalUnit: Optional[str] = None
    slotBuffer: Optional[float] = None
    preBuffer: Optional[float] = None
    appoinmentPerSlot: Optional[float] = None
    appoinmentPerDay: Optional[float] = None
    allowBookingAfter: Optional[float] = None
    allowBookingAfterUnit: Optional[str] = None
    allowBookingFor: Optional[float] = None
    allowBookingForUnit: Optional[str] = None
    openHours: Optional[List[OpenHour]] = None
    enableRecurring: Optional[bool] = None
    recurring: Optional[Recurring] = None
    formId: Optional[str] = None
    stickyContact: Optional[bool] = None
    isLivePaymentMode: Optional[bool] = None
    autoConfirm: Optional[bool] = None
    shouldSendAlertEmailsToAssignedMember: Optional[bool] = None
    alertEmail: Optional[str] = None
    googleInvitationEmails: Optional[bool] = None
    allowReschedule: Optional[bool] = None
    allowCancellation: Optional[bool] = None
    shouldAssignContactToTeamMember: Optional[bool] = None
    shouldSkipAssigningContactForExisting: Optional[bool] = None
    notes: Optional[str] = None
    pixelId: Optional[str] = None
    formSubmitType: Optional[str] = None
    formSubmitRedirectURL: Optional[str] = None
    formSubmitThanksMessage: Optional[str] = None
    availabilityType: Optional[float] = None
    availabilities: Optional[List[UpdateAvailability]] = None
    guestType: Optional[str] = None
    consentLabel: Optional[str] = None
    calendarCoverImage: Optional[str] = None
    lookBusyConfig: Optional[Any] = None
    isActive: Optional[bool] = None

class CalendarDeleteSuccessfulResponseDTO(BaseModel):
    """CalendarDeleteSuccessfulResponseDTO model"""
    success: bool

class GetCalendarEventSuccessfulResponseDTO(BaseModel):
    """GetCalendarEventSuccessfulResponseDTO model"""
    event: Optional[CalendarEventDTO] = None

class DeleteAppointmentSchema(BaseModel):
    """DeleteAppointmentSchema model"""

class DeleteEventSuccessfulResponseDto(BaseModel):
    """DeleteEventSuccessfulResponseDto model"""
    succeeded: Optional[bool] = None

class NoteCreatedBySchema(BaseModel):
    """NoteCreatedBySchema model"""
    id: Optional[str] = None
    name: Optional[str] = None

class GetNoteSchema(BaseModel):
    """GetNoteSchema model"""
    id: Optional[str] = None
    body: Optional[str] = None
    userId: Optional[str] = None
    dateAdded: Optional[str] = None
    contactId: Optional[str] = None
    createdBy: Optional[NoteCreatedBySchema] = None

class GetNotesListSuccessfulResponseDto(BaseModel):
    """GetNotesListSuccessfulResponseDto model"""
    notes: Optional[List[GetNoteSchema]] = None
    hasMore: Optional[bool] = None

class NotesDTO(BaseModel):
    """NotesDTO model"""
    userId: Optional[str] = None
    body: str

class GetCreateUpdateNoteSuccessfulResponseDto(BaseModel):
    """GetCreateUpdateNoteSuccessfulResponseDto model"""
    note: Optional[GetNoteSchema] = None

class DeleteNoteSuccessfulResponseDto(BaseModel):
    """DeleteNoteSuccessfulResponseDto model"""
    success: Optional[bool] = None

class CalendarResourceByIdResponseDTO(BaseModel):
    """CalendarResourceByIdResponseDTO model"""
    locationId: str
    name: str
    resourceType: str
    isActive: bool
    description: Optional[str] = None
    quantity: Optional[float] = None
    outOfService: Optional[float] = None
    capacity: Optional[float] = None
    calendarIds: List[str]

class UpdateCalendarResourceDTO(BaseModel):
    """UpdateCalendarResourceDTO model"""
    locationId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[float] = None
    outOfService: Optional[float] = None
    capacity: Optional[float] = None
    calendarIds: Optional[List[str]] = None
    isActive: Optional[bool] = None

class CalendarResourceResponseDTO(BaseModel):
    """CalendarResourceResponseDTO model"""
    locationId: str
    name: str
    resourceType: str
    isActive: bool
    description: Optional[str] = None
    quantity: Optional[float] = None
    outOfService: Optional[float] = None
    capacity: Optional[float] = None

class ResourceDeleteResponseDTO(BaseModel):
    """ResourceDeleteResponseDTO model"""
    success: Optional[bool] = None

class CreateCalendarResourceDTO(BaseModel):
    """CreateCalendarResourceDTO model"""
    locationId: str
    name: str
    description: str
    quantity: float
    outOfService: float
    capacity: float
    calendarIds: List[str]

class SchedulesDTO(BaseModel):
    """SchedulesDTO model"""
    timeOffset: Optional[float] = None
    unit: Optional[str] = None

class CalendarNotificationResponseDTO(BaseModel):
    """CalendarNotificationResponseDTO model"""
    _id: Optional[str] = None
    receiverType: Optional[str] = None
    additionalEmailIds: Optional[List[str]] = None
    additionalPhoneNumbers: Optional[List[str]] = None
    channel: Optional[str] = None
    notificationType: Optional[str] = None
    isActive: Optional[bool] = None
    additionalWhatsappNumbers: Optional[List[str]] = None
    templateId: Optional[str] = None
    body: Optional[str] = None
    subject: Optional[str] = None
    afterTime: Optional[List[SchedulesDTO]] = None
    beforeTime: Optional[List[SchedulesDTO]] = None
    selectedUsers: Optional[List[str]] = None
    deleted: Optional[bool] = None

class CreateCalendarNotificationDTO(BaseModel):
    """CreateCalendarNotificationDTO model"""
    receiverType: str
    channel: str
    notificationType: str
    isActive: Optional[bool] = None
    templateId: Optional[str] = None
    body: Optional[str] = None
    subject: Optional[str] = None
    afterTime: Optional[List[SchedulesDTO]] = None
    beforeTime: Optional[List[SchedulesDTO]] = None
    additionalEmailIds: Optional[List[str]] = None
    additionalPhoneNumbers: Optional[List[str]] = None
    selectedUsers: Optional[List[str]] = None
    fromAddress: Optional[str] = None
    fromName: Optional[str] = None
    fromNumber: Optional[str] = None

class UpdateCalendarNotificationsDTO(BaseModel):
    """UpdateCalendarNotificationsDTO model"""
    receiverType: Optional[str] = None
    additionalEmailIds: Optional[List[str]] = None
    additionalPhoneNumbers: Optional[List[str]] = None
    selectedUsers: Optional[List[str]] = None
    channel: Optional[str] = None
    notificationType: Optional[str] = None
    isActive: Optional[bool] = None
    deleted: Optional[bool] = None
    templateId: Optional[str] = None
    body: Optional[str] = None
    subject: Optional[str] = None
    afterTime: Optional[List[SchedulesDTO]] = None
    beforeTime: Optional[List[SchedulesDTO]] = None
    fromAddress: Optional[str] = None
    fromNumber: Optional[str] = None
    fromName: Optional[str] = None

class CalendarNotificationDeleteResponseDTO(BaseModel):
    """CalendarNotificationDeleteResponseDTO model"""
    message: str

