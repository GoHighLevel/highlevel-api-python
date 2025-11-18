from __future__ import annotations

# Invoices Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class AddressDto(BaseModel):
    """AddressDto model"""
    addressLine1: Optional[str] = None
    addressLine2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    countryCode: Optional[str] = None
    postalCode: Optional[str] = None

class BusinessDetailsDto(BaseModel):
    """BusinessDetailsDto model"""
    logoUrl: Optional[str] = None
    name: Optional[str] = None
    phoneNo: Optional[str] = None
    address: Optional[Any] = None
    website: Optional[str] = None
    customValues: Optional[List[str]] = None

class ItemTaxDto(BaseModel):
    """ItemTaxDto model"""
    _id: str
    name: str
    rate: float
    calculation: Optional[str] = None
    description: Optional[str] = None
    taxId: Optional[str] = None

class InvoiceItemDto(BaseModel):
    """InvoiceItemDto model"""
    name: str
    description: Optional[str] = None
    productId: Optional[str] = None
    priceId: Optional[str] = None
    currency: str
    amount: float
    qty: float
    taxes: Optional[List[ItemTaxDto]] = None
    automaticTaxCategoryId: Optional[str] = None
    isSetupFeeItem: Optional[bool] = None
    type: Optional[str] = None
    taxInclusive: Optional[bool] = None

class DiscountDto(BaseModel):
    """DiscountDto model"""
    value: Optional[float] = None
    type: str
    validOnProductIds: Optional[List[str]] = None

class TipsConfigurationDto(BaseModel):
    """TipsConfigurationDto model"""
    tipsPercentage: List[str]
    tipsEnabled: bool

class LateFeesFrequencyDto(BaseModel):
    """LateFeesFrequencyDto model"""
    intervalCount: Optional[float] = None
    interval: str

class LateFeesGraceDto(BaseModel):
    """LateFeesGraceDto model"""
    intervalCount: float
    interval: str

class LateFeesMaxFeesDto(BaseModel):
    """LateFeesMaxFeesDto model"""
    type: str
    value: float

class LateFeesConfigurationDto(BaseModel):
    """LateFeesConfigurationDto model"""
    enable: bool
    value: float
    type: str
    frequency: Any
    grace: Optional[Any] = None
    maxLateFees: Optional[Any] = None

class StripePaymentMethodDto(BaseModel):
    """StripePaymentMethodDto model"""
    enableBankDebitOnly: bool

class PaymentMethodDto(BaseModel):
    """PaymentMethodDto model"""
    stripe: Any

class ProcessingFeePaidChargeDto(BaseModel):
    """ProcessingFeePaidChargeDto model"""
    name: str
    charge: float
    amount: float
    _id: str

class ProcessingFeeDto(BaseModel):
    """ProcessingFeeDto model"""
    charges: List[List[Any]]
    collectedMiscellaneousCharges: Optional[float] = None
    paidCharges: Optional[List[ProcessingFeePaidChargeDto]] = None

class CreateInvoiceTemplateDto(BaseModel):
    """CreateInvoiceTemplateDto model"""
    altId: str
    altType: str
    internal: Optional[bool] = None
    name: str
    businessDetails: BusinessDetailsDto
    currency: str
    items: List[InvoiceItemDto]
    automaticTaxesEnabled: Optional[bool] = None
    discount: Optional[DiscountDto] = None
    termsNotes: Optional[str] = None
    title: Optional[str] = None
    tipsConfiguration: Optional[Any] = None
    lateFeesConfiguration: Optional[Any] = None
    invoiceNumberPrefix: Optional[str] = None
    paymentMethods: Optional[Any] = None
    attachments: Optional[List[str]] = None
    miscellaneousCharges: Optional[Any] = None

class CreateInvoiceTemplateResponseDto(BaseModel):
    """CreateInvoiceTemplateResponseDto model"""
    _id: str
    altId: str
    altType: str
    name: str
    businessDetails: Any
    currency: str
    discount: Optional[Any] = None
    items: List[str]
    invoiceNumberPrefix: Optional[str] = None
    total: float
    createdAt: str
    updatedAt: str

class GetTemplateResponseDto(BaseModel):
    """GetTemplateResponseDto model"""
    _id: str
    altId: str
    altType: str
    name: str
    businessDetails: Any
    currency: str
    discount: Optional[Any] = None
    items: List[str]
    invoiceNumberPrefix: Optional[str] = None
    total: float
    createdAt: str
    updatedAt: str

class ListTemplatesResponseDto(BaseModel):
    """ListTemplatesResponseDto model"""
    data: List[GetTemplateResponseDto]
    totalCount: float

class UpdateInvoiceTemplateDto(BaseModel):
    """UpdateInvoiceTemplateDto model"""
    altId: str
    altType: str
    internal: Optional[bool] = None
    name: str
    businessDetails: BusinessDetailsDto
    currency: str
    items: List[InvoiceItemDto]
    discount: Optional[DiscountDto] = None
    termsNotes: Optional[str] = None
    title: Optional[str] = None
    miscellaneousCharges: Optional[Any] = None

class UpdateInvoiceTemplateResponseDto(BaseModel):
    """UpdateInvoiceTemplateResponseDto model"""
    _id: str
    altId: str
    altType: str
    name: str
    businessDetails: Any
    currency: str
    discount: Optional[Any] = None
    items: List[str]
    invoiceNumberPrefix: Optional[str] = None
    total: float
    createdAt: str
    updatedAt: str

class UpdateInvoiceLateFeesConfigurationDto(BaseModel):
    """UpdateInvoiceLateFeesConfigurationDto model"""
    altId: str
    altType: str
    lateFeesConfiguration: Any

class UpdatePaymentMethodsConfigurationDto(BaseModel):
    """UpdatePaymentMethodsConfigurationDto model"""
    altId: str
    altType: str
    paymentMethods: Optional[Any] = None

class DeleteInvoiceTemplateResponseDto(BaseModel):
    """DeleteInvoiceTemplateResponseDto model"""
    success: bool

class AdditionalEmailsDto(BaseModel):
    """AdditionalEmailsDto model"""
    email: str

class ContactDetailsDto(BaseModel):
    """ContactDetailsDto model"""
    id: str
    name: str
    phoneNo: str
    email: str
    additionalEmails: Optional[List[AdditionalEmailsDto]] = None
    companyName: Optional[str] = None
    address: Optional[AddressDto] = None
    customFields: Optional[List[str]] = None

class CustomRRuleOptionsDto(BaseModel):
    """CustomRRuleOptionsDto model"""
    intervalType: str
    interval: float
    startDate: str
    startTime: Optional[str] = None
    endDate: Optional[str] = None
    endTime: Optional[str] = None
    dayOfMonth: Optional[float] = None
    dayOfWeek: Optional[str] = None
    numOfWeek: Optional[float] = None
    monthOfYear: Optional[str] = None
    count: Optional[float] = None
    daysBefore: Optional[float] = None
    useStartAsPrimaryUserAccepted: Optional[bool] = None
    endType: Optional[str] = None

class ScheduleOptionsDto(BaseModel):
    """ScheduleOptionsDto model"""
    executeAt: Optional[str] = None
    rrule: Optional[CustomRRuleOptionsDto] = None

class AttachmentsDto(BaseModel):
    """AttachmentsDto model"""
    id: str
    name: str
    url: str
    type: str
    size: float

class CreateInvoiceScheduleDto(BaseModel):
    """CreateInvoiceScheduleDto model"""
    altId: str
    altType: str
    name: str
    contactDetails: ContactDetailsDto
    schedule: ScheduleOptionsDto
    liveMode: bool
    businessDetails: BusinessDetailsDto
    currency: str
    items: List[InvoiceItemDto]
    automaticTaxesEnabled: Optional[bool] = None
    discount: DiscountDto
    termsNotes: Optional[str] = None
    title: Optional[str] = None
    tipsConfiguration: Optional[Any] = None
    lateFeesConfiguration: Optional[Any] = None
    invoiceNumberPrefix: Optional[str] = None
    paymentMethods: Optional[Any] = None
    attachments: Optional[List[AttachmentsDto]] = None
    miscellaneousCharges: Optional[Any] = None

class DefaultInvoiceResponseDto(BaseModel):
    """DefaultInvoiceResponseDto model"""
    _id: str
    status: str
    liveMode: bool
    amountPaid: float
    altId: str
    altType: str
    name: str
    businessDetails: Dict[str, Any]
    invoiceNumber: float
    currency: str
    contactDetails: Dict[str, Any]
    issueDate: str
    dueDate: str
    discount: Optional[Dict[str, Any]] = None
    invoiceItems: List[str]
    total: float
    title: str
    amountDue: float
    createdAt: str
    updatedAt: str
    automaticTaxesEnabled: Optional[bool] = None
    automaticTaxesCalculated: Optional[bool] = None
    paymentSchedule: Optional[Dict[str, Any]] = None

class CreateInvoiceScheduleResponseDto(BaseModel):
    """CreateInvoiceScheduleResponseDto model"""
    _id: str
    status: Dict[str, Any]
    liveMode: bool
    altId: str
    altType: str
    name: str
    schedule: Optional[ScheduleOptionsDto] = None
    invoices: List[DefaultInvoiceResponseDto]
    businessDetails: Any
    currency: str
    contactDetails: Any
    discount: Optional[Any] = None
    items: List[str]
    total: float
    title: str
    termsNotes: str
    compiledTermsNotes: str
    createdAt: str
    updatedAt: str

class GetScheduleResponseDto(BaseModel):
    """GetScheduleResponseDto model"""
    _id: str
    status: Dict[str, Any]
    liveMode: bool
    altId: str
    altType: str
    name: str
    schedule: Optional[ScheduleOptionsDto] = None
    invoices: List[DefaultInvoiceResponseDto]
    businessDetails: Any
    currency: str
    contactDetails: Any
    discount: Optional[Any] = None
    items: List[str]
    total: float
    title: str
    termsNotes: str
    compiledTermsNotes: str
    createdAt: str
    updatedAt: str

class ListSchedulesResponseDto(BaseModel):
    """ListSchedulesResponseDto model"""
    schedules: List[GetScheduleResponseDto]
    total: float

class UpdateInvoiceScheduleDto(BaseModel):
    """UpdateInvoiceScheduleDto model"""
    altId: str
    altType: str
    name: str
    contactDetails: ContactDetailsDto
    schedule: ScheduleOptionsDto
    liveMode: bool
    businessDetails: BusinessDetailsDto
    currency: str
    items: List[InvoiceItemDto]
    discount: DiscountDto
    termsNotes: Optional[str] = None
    title: Optional[str] = None
    attachments: Optional[List[AttachmentsDto]] = None
    miscellaneousCharges: Optional[Any] = None

class UpdateInvoiceScheduleResponseDto(BaseModel):
    """UpdateInvoiceScheduleResponseDto model"""
    _id: str
    status: Dict[str, Any]
    liveMode: bool
    altId: str
    altType: str
    name: str
    schedule: Optional[ScheduleOptionsDto] = None
    invoices: List[DefaultInvoiceResponseDto]
    businessDetails: Any
    currency: str
    contactDetails: Any
    discount: Optional[Any] = None
    items: List[str]
    total: float
    title: str
    termsNotes: str
    compiledTermsNotes: str
    createdAt: str
    updatedAt: str

class DeleteInvoiceScheduleResponseDto(BaseModel):
    """DeleteInvoiceScheduleResponseDto model"""
    success: bool

class UpdateAndScheduleInvoiceScheduleResponseDto(BaseModel):
    """UpdateAndScheduleInvoiceScheduleResponseDto model"""
    _id: str
    status: Dict[str, Any]
    liveMode: bool
    altId: str
    altType: str
    name: str
    schedule: Optional[ScheduleOptionsDto] = None
    invoices: List[DefaultInvoiceResponseDto]
    businessDetails: Any
    currency: str
    contactDetails: Any
    discount: Optional[Any] = None
    items: List[str]
    total: float
    title: str
    termsNotes: str
    compiledTermsNotes: str
    createdAt: str
    updatedAt: str

class CardDto(BaseModel):
    """CardDto model"""
    brand: str
    last4: str

class USBankAccountDto(BaseModel):
    """USBankAccountDto model"""
    bank_name: str
    last4: str

class SepaDirectDebitDTO(BaseModel):
    """SepaDirectDebitDTO model"""
    bank_code: str
    last4: str
    branch_code: str

class BacsDirectDebitDTO(BaseModel):
    """BacsDirectDebitDTO model"""
    sort_code: str
    last4: str

class BecsDirectDebitDTO(BaseModel):
    """BecsDirectDebitDTO model"""
    bsb_number: str
    last4: str

class AutoPaymentDetailsDto(BaseModel):
    """AutoPaymentDetailsDto model"""
    enable: bool
    type: Optional[str] = None
    paymentMethodId: Optional[str] = None
    customerId: Optional[str] = None
    card: Optional[CardDto] = None
    usBankAccount: Optional[USBankAccountDto] = None
    sepaDirectDebit: Optional[SepaDirectDebitDTO] = None
    bacsDirectDebit: Optional[BacsDirectDebitDTO] = None
    becsDirectDebit: Optional[BecsDirectDebitDTO] = None
    cardId: Optional[str] = None

class ScheduleInvoiceScheduleDto(BaseModel):
    """ScheduleInvoiceScheduleDto model"""
    altId: str
    altType: str
    liveMode: bool
    autoPayment: Optional[Any] = None

class ScheduleInvoiceScheduleResponseDto(BaseModel):
    """ScheduleInvoiceScheduleResponseDto model"""
    _id: str
    status: Dict[str, Any]
    liveMode: bool
    altId: str
    altType: str
    name: str
    schedule: Optional[ScheduleOptionsDto] = None
    invoices: List[DefaultInvoiceResponseDto]
    businessDetails: Any
    currency: str
    contactDetails: Any
    discount: Optional[Any] = None
    items: List[str]
    total: float
    title: str
    termsNotes: str
    compiledTermsNotes: str
    createdAt: str
    updatedAt: str

class AutoPaymentScheduleDto(BaseModel):
    """AutoPaymentScheduleDto model"""
    altId: str
    altType: str
    id: str
    autoPayment: Any

class AutoPaymentInvoiceScheduleResponseDto(BaseModel):
    """AutoPaymentInvoiceScheduleResponseDto model"""
    _id: str
    status: Dict[str, Any]
    liveMode: bool
    altId: str
    altType: str
    name: str
    schedule: Optional[ScheduleOptionsDto] = None
    invoices: List[DefaultInvoiceResponseDto]
    businessDetails: Any
    currency: str
    contactDetails: Any
    discount: Optional[Any] = None
    items: List[str]
    total: float
    title: str
    termsNotes: str
    compiledTermsNotes: str
    createdAt: str
    updatedAt: str

class CancelInvoiceScheduleDto(BaseModel):
    """CancelInvoiceScheduleDto model"""
    altId: str
    altType: str

class CancelInvoiceScheduleResponseDto(BaseModel):
    """CancelInvoiceScheduleResponseDto model"""
    _id: str
    status: Dict[str, Any]
    liveMode: bool
    altId: str
    altType: str
    name: str
    schedule: Optional[ScheduleOptionsDto] = None
    invoices: List[DefaultInvoiceResponseDto]
    businessDetails: Any
    currency: str
    contactDetails: Any
    discount: Optional[Any] = None
    items: List[str]
    total: float
    title: str
    termsNotes: str
    compiledTermsNotes: str
    createdAt: str
    updatedAt: str

class SentToDto(BaseModel):
    """SentToDto model"""
    email: List[str]
    emailCc: Optional[List[str]] = None
    emailBcc: Optional[List[str]] = None
    phoneNo: Optional[List[str]] = None

class PaymentScheduleDto(BaseModel):
    """PaymentScheduleDto model"""
    type: str
    schedules: List[str]

class Text2PayDto(BaseModel):
    """Text2PayDto model"""
    altId: str
    altType: str
    name: str
    currency: str
    items: List[InvoiceItemDto]
    termsNotes: Optional[str] = None
    title: Optional[str] = None
    contactDetails: Any
    invoiceNumber: Optional[str] = None
    issueDate: str
    dueDate: Optional[str] = None
    sentTo: SentToDto
    liveMode: bool
    automaticTaxesEnabled: Optional[bool] = None
    paymentSchedule: Optional[Any] = None
    lateFeesConfiguration: Optional[Any] = None
    tipsConfiguration: Optional[Any] = None
    invoiceNumberPrefix: Optional[str] = None
    paymentMethods: Optional[Any] = None
    attachments: Optional[List[AttachmentsDto]] = None
    miscellaneousCharges: Optional[Any] = None
    id: Optional[str] = None
    includeTermsNote: Optional[bool] = None
    action: str
    userId: str
    discount: Optional[DiscountDto] = None
    businessDetails: Optional[BusinessDetailsDto] = None

class Text2PayInvoiceResponseDto(BaseModel):
    """Text2PayInvoiceResponseDto model"""
    invoice: DefaultInvoiceResponseDto
    invoiceUrl: str

class GenerateInvoiceNumberResponseDto(BaseModel):
    """GenerateInvoiceNumberResponseDto model"""
    invoiceNumber: Optional[float] = None

class CreateInvoiceDto(BaseModel):
    """CreateInvoiceDto model"""
    altId: str
    altType: str
    name: str
    businessDetails: BusinessDetailsDto
    currency: str
    items: List[InvoiceItemDto]
    discount: DiscountDto
    termsNotes: Optional[str] = None
    title: Optional[str] = None
    contactDetails: Any
    invoiceNumber: Optional[str] = None
    issueDate: str
    dueDate: Optional[str] = None
    sentTo: SentToDto
    liveMode: bool
    automaticTaxesEnabled: Optional[bool] = None
    paymentSchedule: Optional[Any] = None
    lateFeesConfiguration: Optional[Any] = None
    tipsConfiguration: Optional[Any] = None
    invoiceNumberPrefix: Optional[str] = None
    paymentMethods: Optional[Any] = None
    attachments: Optional[List[AttachmentsDto]] = None
    miscellaneousCharges: Optional[Any] = None

class OldCreateInvoiceDTO(BaseModel):
    """OldCreateInvoiceDTO model"""

class CreateInvoiceResponseDto(BaseModel):
    """CreateInvoiceResponseDto model"""
    _id: str
    status: str
    liveMode: bool
    amountPaid: float
    altId: str
    altType: str
    name: str
    businessDetails: Dict[str, Any]
    invoiceNumber: float
    currency: str
    contactDetails: Dict[str, Any]
    issueDate: str
    dueDate: str
    discount: Optional[Dict[str, Any]] = None
    invoiceItems: List[str]
    total: float
    title: str
    amountDue: float
    createdAt: str
    updatedAt: str
    automaticTaxesEnabled: Optional[bool] = None
    automaticTaxesCalculated: Optional[bool] = None
    paymentSchedule: Optional[Dict[str, Any]] = None

class TotalSummaryDto(BaseModel):
    """TotalSummaryDto model"""
    subTotal: float
    discount: float
    tax: float

class ReminderExecutionDetailsList(BaseModel):
    """ReminderExecutionDetailsList model"""

class ReminderDto(BaseModel):
    """ReminderDto model"""
    enabled: bool
    emailTemplate: str
    smsTemplate: str
    emailSubject: str
    reminderId: str
    reminderName: str
    reminderTime: str
    intervalType: str
    maxReminders: float
    reminderInvoiceCondition: str
    reminderNumber: float
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    timezone: Optional[str] = None

class ReminderSettingsDto(BaseModel):
    """ReminderSettingsDto model"""
    defaultEmailTemplateId: str
    reminders: List[ReminderDto]

class RemindersConfigurationDto(BaseModel):
    """RemindersConfigurationDto model"""
    reminderExecutionDetailsList: Any
    reminderSettings: Any

class GetInvoiceResponseDto(BaseModel):
    """GetInvoiceResponseDto model"""
    _id: str
    status: str
    liveMode: bool
    amountPaid: float
    altId: str
    altType: str
    name: str
    businessDetails: Dict[str, Any]
    invoiceNumber: float
    currency: str
    contactDetails: Dict[str, Any]
    issueDate: str
    dueDate: str
    discount: Optional[Dict[str, Any]] = None
    invoiceItems: List[str]
    total: float
    title: str
    amountDue: float
    createdAt: str
    updatedAt: str
    automaticTaxesEnabled: Optional[bool] = None
    automaticTaxesCalculated: Optional[bool] = None
    paymentSchedule: Optional[Dict[str, Any]] = None
    totalSummary: TotalSummaryDto
    remindersConfiguration: Optional[Any] = None

class ListInvoicesResponseDto(BaseModel):
    """ListInvoicesResponseDto model"""
    invoices: List[GetInvoiceResponseDto]
    total: float

class UpdateInvoiceDto(BaseModel):
    """UpdateInvoiceDto model"""
    altId: str
    altType: str
    name: str
    title: Optional[str] = None
    currency: str
    description: Optional[str] = None
    businessDetails: Optional[Any] = None
    invoiceNumber: Optional[str] = None
    contactId: Optional[str] = None
    contactDetails: Optional[ContactDetailsDto] = None
    termsNotes: Optional[str] = None
    discount: Optional[DiscountDto] = None
    invoiceItems: List[InvoiceItemDto]
    automaticTaxesEnabled: Optional[bool] = None
    liveMode: Optional[bool] = None
    issueDate: str
    dueDate: str
    paymentSchedule: Optional[Any] = None
    tipsConfiguration: Optional[Any] = None
    xeroDetails: Optional[Dict[str, Any]] = None
    invoiceNumberPrefix: Optional[str] = None
    paymentMethods: Optional[Any] = None
    attachments: Optional[List[AttachmentsDto]] = None
    miscellaneousCharges: Optional[Any] = None

class UpdateInvoiceResponseDto(BaseModel):
    """UpdateInvoiceResponseDto model"""
    _id: str
    status: str
    liveMode: bool
    amountPaid: float
    altId: str
    altType: str
    name: str
    businessDetails: Dict[str, Any]
    invoiceNumber: float
    currency: str
    contactDetails: Dict[str, Any]
    issueDate: str
    dueDate: str
    discount: Optional[Dict[str, Any]] = None
    invoiceItems: List[str]
    total: float
    title: str
    amountDue: float
    createdAt: str
    updatedAt: str
    automaticTaxesEnabled: Optional[bool] = None
    automaticTaxesCalculated: Optional[bool] = None
    paymentSchedule: Optional[Dict[str, Any]] = None

class DeleteInvoiceResponseDto(BaseModel):
    """DeleteInvoiceResponseDto model"""
    _id: str
    status: str
    liveMode: bool
    amountPaid: float
    altId: str
    altType: str
    name: str
    businessDetails: Dict[str, Any]
    invoiceNumber: float
    currency: str
    contactDetails: Dict[str, Any]
    issueDate: str
    dueDate: str
    discount: Optional[Dict[str, Any]] = None
    invoiceItems: List[str]
    total: float
    title: str
    amountDue: float
    createdAt: str
    updatedAt: str
    automaticTaxesEnabled: Optional[bool] = None
    automaticTaxesCalculated: Optional[bool] = None
    paymentSchedule: Optional[Dict[str, Any]] = None

class VoidInvoiceDto(BaseModel):
    """VoidInvoiceDto model"""
    altId: str
    altType: str

class VoidInvoiceResponseDto(BaseModel):
    """VoidInvoiceResponseDto model"""
    _id: str
    status: str
    liveMode: bool
    amountPaid: float
    altId: str
    altType: str
    name: str
    businessDetails: Dict[str, Any]
    invoiceNumber: float
    currency: str
    contactDetails: Dict[str, Any]
    issueDate: str
    dueDate: str
    discount: Optional[Dict[str, Any]] = None
    invoiceItems: List[str]
    total: float
    title: str
    amountDue: float
    createdAt: str
    updatedAt: str
    automaticTaxesEnabled: Optional[bool] = None
    automaticTaxesCalculated: Optional[bool] = None
    paymentSchedule: Optional[Dict[str, Any]] = None

class InvoiceSettingsSenderConfigurationDto(BaseModel):
    """InvoiceSettingsSenderConfigurationDto model"""
    fromName: Optional[str] = None
    fromEmail: Optional[str] = None

class SendInvoiceDto(BaseModel):
    """SendInvoiceDto model"""
    altId: str
    altType: str
    userId: str
    action: str
    liveMode: bool
    sentFrom: Optional[Any] = None
    autoPayment: Optional[Any] = None

class SendInvoicesResponseDto(BaseModel):
    """SendInvoicesResponseDto model"""
    invoice: DefaultInvoiceResponseDto
    smsData: Dict[str, Any]
    emailData: Dict[str, Any]

class ChequeDto(BaseModel):
    """ChequeDto model"""
    number: str

class RecordPaymentDto(BaseModel):
    """RecordPaymentDto model"""
    altId: str
    altType: str
    mode: str
    card: CardDto
    cheque: ChequeDto
    notes: str
    amount: Optional[float] = None
    meta: Optional[Dict[str, Any]] = None
    paymentScheduleIds: Optional[List[str]] = None
    fulfilledAt: Optional[str] = None

class RecordPaymentResponseDto(BaseModel):
    """RecordPaymentResponseDto model"""
    success: bool
    invoice: DefaultInvoiceResponseDto

class PatchInvoiceStatsLastViewedDto(BaseModel):
    """PatchInvoiceStatsLastViewedDto model"""
    invoiceId: str

class SendEstimateDto(BaseModel):
    """SendEstimateDto model"""
    altId: str
    altType: str
    action: str
    liveMode: bool
    userId: str
    sentFrom: Optional[Any] = None
    estimateName: Optional[str] = None

class FrequencySettingsDto(BaseModel):
    """FrequencySettingsDto model"""
    enabled: bool
    schedule: Any

class AutoInvoicingDto(BaseModel):
    """AutoInvoicingDto model"""
    enabled: bool
    directPayments: Optional[bool] = None

class PaymentScheduleDateConfigDto(BaseModel):
    """PaymentScheduleDateConfigDto model"""
    depositDateType: str
    scheduleDateType: str

class PaymentScheduleConfigDto(BaseModel):
    """PaymentScheduleConfigDto model"""
    type: str
    dateConfig: Any
    schedules: List[List[Any]]

class CreateEstimatesDto(BaseModel):
    """CreateEstimatesDto model"""
    altId: str
    altType: str
    name: str
    businessDetails: BusinessDetailsDto
    currency: str
    items: List[InvoiceItemDto]
    liveMode: Optional[bool] = None
    discount: DiscountDto
    termsNotes: Optional[str] = None
    title: Optional[str] = None
    contactDetails: Any
    estimateNumber: Optional[float] = None
    issueDate: Optional[str] = None
    expiryDate: Optional[str] = None
    sentTo: Optional[Any] = None
    automaticTaxesEnabled: Optional[bool] = None
    meta: Optional[Dict[str, Any]] = None
    sendEstimateDetails: Optional[Any] = None
    frequencySettings: Any
    estimateNumberPrefix: Optional[str] = None
    userId: Optional[str] = None
    attachments: Optional[List[AttachmentsDto]] = None
    autoInvoice: Optional[Any] = None
    miscellaneousCharges: Optional[Any] = None
    paymentScheduleConfig: Optional[Any] = None

class BusinessDetails(BaseModel):
    """BusinessDetails model"""

class ContactDetails(BaseModel):
    """ContactDetails model"""

class SentTo(BaseModel):
    """SentTo model"""

class AutoInvoice(BaseModel):
    """AutoInvoice model"""

class EstimateResponseDto(BaseModel):
    """EstimateResponseDto model"""
    altId: str
    altType: str
    _id: str
    liveMode: bool
    deleted: bool
    name: str
    currency: str
    businessDetails: Any
    items: List[List[Any]]
    discount: Any
    title: Optional[str] = None
    estimateNumberPrefix: Optional[str] = None
    attachments: Optional[List[AttachmentsDto]] = None
    updatedBy: Optional[str] = None
    total: float
    createdAt: str
    updatedAt: str
    __v: float
    automaticTaxesEnabled: bool
    termsNotes: Optional[str] = None
    companyId: str
    contactDetails: Any
    issueDate: str
    expiryDate: str
    sentBy: Optional[str] = None
    automaticTaxesCalculated: bool
    meta: Dict[str, Any]
    estimateActionHistory: List[str]
    sentTo: Any
    frequencySettings: Any
    lastVisitedAt: str
    totalamountInUSD: float
    autoInvoice: Optional[Any] = None
    traceId: str

class UpdateEstimateDto(BaseModel):
    """UpdateEstimateDto model"""
    altId: str
    altType: str
    name: str
    businessDetails: BusinessDetailsDto
    currency: str
    items: List[InvoiceItemDto]
    liveMode: Optional[bool] = None
    discount: DiscountDto
    termsNotes: Optional[str] = None
    title: Optional[str] = None
    contactDetails: Any
    estimateNumber: Optional[float] = None
    issueDate: Optional[str] = None
    expiryDate: Optional[str] = None
    sentTo: Optional[Any] = None
    automaticTaxesEnabled: Optional[bool] = None
    meta: Optional[Dict[str, Any]] = None
    sendEstimateDetails: Optional[Any] = None
    frequencySettings: Any
    estimateNumberPrefix: Optional[str] = None
    userId: Optional[str] = None
    attachments: Optional[List[AttachmentsDto]] = None
    autoInvoice: Optional[Any] = None
    miscellaneousCharges: Optional[Any] = None
    paymentScheduleConfig: Optional[Any] = None
    estimateStatus: Optional[str] = None

class GenerateEstimateNumberResponse(BaseModel):
    """GenerateEstimateNumberResponse model"""
    estimateNumber: float
    traceId: str

class AltDto(BaseModel):
    """AltDto model"""
    altId: str
    altType: str

class CreateInvoiceFromEstimateDto(BaseModel):
    """CreateInvoiceFromEstimateDto model"""
    altId: str
    altType: str
    markAsInvoiced: bool
    version: Optional[str] = None

class CreateInvoiceFromEstimateResponseDTO(BaseModel):
    """CreateInvoiceFromEstimateResponseDTO model"""
    estimate: Any
    invoice: Any

class ListEstimatesResponseDTO(BaseModel):
    """ListEstimatesResponseDTO model"""
    estimates: List[str]
    total: float
    traceId: str

class EstimateIdParam(BaseModel):
    """EstimateIdParam model"""
    estimateId: str

class ListEstimateTemplateResponseDTO(BaseModel):
    """ListEstimateTemplateResponseDTO model"""
    data: List[str]
    totalCount: float
    traceId: str

class EstimateTemplatesDto(BaseModel):
    """EstimateTemplatesDto model"""
    altId: str
    altType: str
    name: str
    businessDetails: BusinessDetailsDto
    currency: str
    items: List[List[Any]]
    liveMode: Optional[bool] = None
    discount: DiscountDto
    termsNotes: Optional[str] = None
    title: Optional[str] = None
    automaticTaxesEnabled: Optional[bool] = None
    meta: Optional[Dict[str, Any]] = None
    sendEstimateDetails: Optional[Any] = None
    estimateNumberPrefix: Optional[str] = None
    attachments: Optional[List[AttachmentsDto]] = None
    miscellaneousCharges: Optional[Any] = None

class EstimateTemplateResponseDTO(BaseModel):
    """EstimateTemplateResponseDTO model"""
    altId: str
    altType: str
    _id: str
    liveMode: bool
    deleted: bool
    name: str
    currency: str
    businessDetails: Any
    items: List[List[Any]]
    discount: Any
    title: Optional[str] = None
    estimateNumberPrefix: Optional[str] = None
    attachments: Optional[List[AttachmentsDto]] = None
    updatedBy: Optional[str] = None
    total: float
    createdAt: str
    updatedAt: str
    __v: float
    automaticTaxesEnabled: bool
    termsNotes: Optional[str] = None

