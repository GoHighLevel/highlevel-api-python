# @generated
# File generated from our OpenAPI spec

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

class ServiceResourceDTO(BaseModel):
    """ServiceResourceDTO model"""
    id: str

class ServiceAddOnResponseDTO(BaseModel):
    """ServiceAddOnResponseDTO model"""
    id: str
    quantity: Optional[float] = None

class ServiceDTO(BaseModel):
    """ServiceDTO model"""
    id: str
    serviceCategoryId: str
    serviceStaffId: str
    serviceStartTime: str
    serviceEndTime: str
    serviceResources: Optional[List[ServiceResourceDTO]] = None
    serviceAddOns: Optional[List[ServiceAddOnResponseDTO]] = None

class ServiceBookingResponseDTO(BaseModel):
    """ServiceBookingResponseDTO model"""
    bookingId: str
    locationId: str
    contactId: str
    serviceLocationId: str
    title: str
    startTime: str
    endTime: str
    services: List[ServiceDTO]
    timezone: str
    status: str
    deleted: bool
    dateAdded: str
    dateUpdated: str
    createdBy: Any
    meetingLocation: Optional[str] = None

class ServiceBookingsListResponseDTO(BaseModel):
    """ServiceBookingsListResponseDTO model"""
    bookings: List[ServiceBookingResponseDTO]

class ServiceBookingQueryDTO(BaseModel):
    """ServiceBookingQueryDTO model"""
    overrideAvailability: Optional[bool] = None
    skipSchedulingNotice: Optional[bool] = None

class ServiceAddOnDTO(BaseModel):
    """ServiceAddOnDTO model"""
    id: str
    quantity: Optional[float] = None
    duration: Optional[float] = None

class CreateBookingServiceDTO(BaseModel):
    """CreateBookingServiceDTO model"""
    id: str
    staffId: Optional[str] = None
    position: Optional[float] = None
    addOns: Optional[List[ServiceAddOnDTO]] = None

class CreatePublicServiceBookingDTO(BaseModel):
    """CreatePublicServiceBookingDTO model"""
    locationId: str
    contactId: str
    startTime: str
    endTime: str
    timezone: str
    services: List[CreateBookingServiceDTO]
    serviceLocationId: Optional[str] = None
    meetingLocation: Optional[str] = None
    title: Optional[str] = None
    status: Optional[str] = None

class CreateOrUpdateServiceBookingResponseDTO(BaseModel):
    """CreateOrUpdateServiceBookingResponseDTO model"""
    bookingId: str
    locationId: str
    contactId: str
    serviceLocationId: str
    title: str
    startTime: str
    endTime: str
    services: List[ServiceDTO]
    timezone: str
    status: str
    deleted: bool
    dateAdded: str
    dateUpdated: str
    createdBy: Any
    meetingLocation: Optional[str] = None
    messages: Optional[List[List[Any]]] = None

class UpdateServiceBookingDTO(BaseModel):
    """UpdateServiceBookingDTO model"""
    serviceLocationId: Optional[str] = None
    meetingLocation: Optional[str] = None
    title: Optional[str] = None
    status: Optional[str] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    timezone: Optional[str] = None
    services: Optional[List[CreateBookingServiceDTO]] = None

class DeleteServiceBookingResponseDTO(BaseModel):
    """DeleteServiceBookingResponseDTO model"""
    success: bool
    message: str

class PaymentDTO(BaseModel):
    """PaymentDTO model"""
    amount: Optional[float] = None
    deposit: Optional[float] = None
    depositType: Optional[str] = None

class ServiceVariationDTO(BaseModel):
    """ServiceVariationDTO model"""
    id: str
    name: str
    serviceDuration: Optional[float] = None
    serviceDurationUnit: Optional[str] = None
    payment: Optional[Any] = None
    preBuffer: Optional[float] = None
    preBufferUnit: Optional[str] = None
    postBuffer: Optional[float] = None
    postBufferUnit: Optional[str] = None

class StaffDTO(BaseModel):
    """StaffDTO model"""
    id: str

class ServiceResponseDTO(BaseModel):
    """ServiceResponseDTO model"""
    id: str
    locationId: str
    name: str
    description: Optional[str] = None
    slug: Optional[str] = None
    eventColor: Optional[str] = None
    coverImage: Optional[str] = None
    serviceCategoryId: Optional[str] = None
    payment: Optional[Any] = None
    serviceDuration: Optional[float] = None
    serviceDurationUnit: Optional[str] = None
    preBuffer: Optional[float] = None
    preBufferUnit: Optional[str] = None
    postBuffer: Optional[float] = None
    postBufferUnit: Optional[str] = None
    isPrivate: Optional[bool] = None
    formId: Optional[str] = None
    variations: Optional[List[ServiceVariationDTO]] = None
    staff: Optional[List[StaffDTO]] = None

class ServicesListResponseDTO(BaseModel):
    """ServicesListResponseDTO model"""
    services: List[ServiceResponseDTO]

class ServiceResponseWrapperDTO(BaseModel):
    """ServiceResponseWrapperDTO model"""
    service: Any

class CreateServiceVariationDTO(BaseModel):
    """CreateServiceVariationDTO model"""
    serviceDuration: Optional[float] = None
    serviceDurationUnit: Optional[str] = None
    preBuffer: Optional[float] = None
    preBufferUnit: Optional[str] = None
    postBuffer: Optional[float] = None
    postBufferUnit: Optional[str] = None
    payment: Optional[Any] = None
    name: str

class CreateServiceDTO(BaseModel):
    """CreateServiceDTO model"""
    locationId: str
    name: str
    slug: str
    staff: List[StaffDTO]
    description: Optional[str] = None
    eventColor: Optional[str] = None
    coverImage: Optional[str] = None
    serviceCategoryId: Optional[str] = None
    payment: Optional[Any] = None
    serviceDuration: Optional[float] = None
    serviceDurationUnit: Optional[str] = None
    preBuffer: Optional[float] = None
    preBufferUnit: Optional[str] = None
    postBuffer: Optional[float] = None
    postBufferUnit: Optional[str] = None
    isPrivate: Optional[bool] = None
    formId: Optional[str] = None
    variations: Optional[List[CreateServiceVariationDTO]] = None

class UpdateServiceVariationDTO(BaseModel):
    """UpdateServiceVariationDTO model"""
    serviceDuration: Optional[float] = None
    serviceDurationUnit: Optional[str] = None
    preBuffer: Optional[float] = None
    preBufferUnit: Optional[str] = None
    postBuffer: Optional[float] = None
    postBufferUnit: Optional[str] = None
    payment: Optional[Any] = None
    id: Optional[str] = None
    name: Optional[str] = None

class UpdateServiceDTO(BaseModel):
    """UpdateServiceDTO model"""
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
    eventColor: Optional[str] = None
    coverImage: Optional[str] = None
    serviceCategoryId: Optional[str] = None
    payment: Optional[Any] = None
    serviceDuration: Optional[float] = None
    serviceDurationUnit: Optional[str] = None
    preBuffer: Optional[float] = None
    preBufferUnit: Optional[str] = None
    postBuffer: Optional[float] = None
    postBufferUnit: Optional[str] = None
    isPrivate: Optional[bool] = None
    formId: Optional[str] = None
    staff: Optional[List[StaffDTO]] = None
    variations: Optional[List[UpdateServiceVariationDTO]] = None

class DeleteServiceResponseDTO(BaseModel):
    """DeleteServiceResponseDTO model"""
    success: bool
    message: Optional[str] = None

class ServiceLocationResponseDTO(BaseModel):
    """ServiceLocationResponseDTO model"""
    id: str
    locationId: str
    name: str
    slug: str
    isActive: Optional[bool] = None
    isPrivate: Optional[bool] = None
    coverImage: Optional[str] = None
    locationType: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None

class ServiceLocationListResponseDTO(BaseModel):
    """ServiceLocationListResponseDTO model"""
    serviceLocations: List[ServiceLocationResponseDTO]

class CreateServiceLocationDTO(BaseModel):
    """CreateServiceLocationDTO model"""
    locationId: str
    name: str
    slug: str
    phone: Optional[str] = None
    address: Optional[str] = None
    coverImage: Optional[str] = None
    locationType: Optional[str] = None

class UpdateServiceLocationDTO(BaseModel):
    """UpdateServiceLocationDTO model"""
    name: Optional[str] = None
    slug: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    coverImage: Optional[str] = None
    locationType: Optional[str] = None

class DeleteServiceLocationResponseDTO(BaseModel):
    """DeleteServiceLocationResponseDTO model"""
    success: bool
    message: Optional[str] = None

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
    dateAdded: str
    dateUpdated: str
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
    deleted: Optional[bool] = None
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

class ScheduleIntervalDTO(BaseModel):
    """ScheduleIntervalDTO model"""
    from_: str
    to: str

class ScheduleRuleDTO(BaseModel):
    """ScheduleRuleDTO model"""
    type: str
    intervals: List[ScheduleIntervalDTO]
    date: Optional[str] = None
    day: Optional[str] = None

class ScheduleObjectResponseDTO(BaseModel):
    """ScheduleObjectResponseDTO model"""
    id: str
    name: str
    locationId: str
    rules: List[ScheduleRuleDTO]
    timezone: str
    dateAdded: str
    dateUpdated: str
    userId: str
    calendarIds: Optional[List[str]] = None
    deleted: bool

class GetAllSchedulesResponseDTO(BaseModel):
    """GetAllSchedulesResponseDTO model"""
    schedules: List[ScheduleObjectResponseDTO]

class ScheduleResponseDTO(BaseModel):
    """ScheduleResponseDTO model"""
    schedule: Any

class CreateScheduleDTO(BaseModel):
    """CreateScheduleDTO model"""
    rules: Optional[List[ScheduleRuleDTO]] = None
    timezone: str
    locationId: str
    name: str
    userId: str
    calendarIds: Optional[List[str]] = None

class UpdateScheduleDTO(BaseModel):
    """UpdateScheduleDTO model"""
    name: Optional[str] = None
    rules: Optional[List[ScheduleRuleDTO]] = None
    timezone: Optional[str] = None

class CreateEventCalendarScheduleDTO(BaseModel):
    """CreateEventCalendarScheduleDTO model"""
    rules: List[ScheduleRuleDTO]
    timezone: str

class EventCalendarScheduleResponseDTO(BaseModel):
    """EventCalendarScheduleResponseDTO model"""
    timezone: str
    rules: List[ScheduleRuleDTO]
    calendarId: str
    dateAdded: Optional[str] = None
    dateUpdated: Optional[str] = None

class EventCalendarScheduleWrapperDTO(BaseModel):
    """EventCalendarScheduleWrapperDTO model"""
    schedule: Any

class UpdateEventCalendarScheduleDTO(BaseModel):
    """UpdateEventCalendarScheduleDTO model"""
    rules: Optional[List[ScheduleRuleDTO]] = None
    timezone: Optional[str] = None

