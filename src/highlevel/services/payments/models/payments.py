from __future__ import annotations

# Payments Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class CreateWhiteLabelIntegrationProviderDto(BaseModel):
    """CreateWhiteLabelIntegrationProviderDto model"""
    altId: str
    altType: str
    uniqueName: str
    title: str
    provider: str
    description: str
    imageUrl: str

class CreateWhitelabelIntegrationResponseDto(BaseModel):
    """CreateWhitelabelIntegrationResponseDto model"""
    _id: str
    altId: str
    altType: str
    title: str
    route: str
    provider: str
    description: str
    imageUrl: str
    createdAt: str
    updatedAt: str

class IntegrationProviderSchema(BaseModel):
    """IntegrationProviderSchema model"""
    _id: str
    altId: str
    altType: str
    title: str
    route: str
    provider: str
    description: str
    imageUrl: str
    createdAt: str
    updatedAt: str

class ListWhitelabelIntegrationProviderResponseDto(BaseModel):
    """ListWhitelabelIntegrationProviderResponseDto model"""
    providers: Any

class OrderResponseSchema(BaseModel):
    """OrderResponseSchema model"""
    _id: str
    altId: str
    altType: str
    contactId: Optional[str] = None
    contactName: Optional[str] = None
    contactEmail: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    subtotal: Optional[float] = None
    discount: Optional[float] = None
    status: str
    liveMode: Optional[bool] = None
    totalProducts: Optional[float] = None
    sourceType: str
    sourceName: Optional[str] = None
    sourceId: Optional[str] = None
    sourceMeta: Optional[Dict[str, Any]] = None
    couponCode: Optional[str] = None
    createdAt: str
    updatedAt: str
    sourceSubType: Optional[str] = None
    fulfillmentStatus: Optional[str] = None
    onetimeProducts: Optional[float] = None
    recurringProducts: Optional[float] = None

class ListOrdersResponseDto(BaseModel):
    """ListOrdersResponseDto model"""
    data: List[OrderResponseSchema]
    totalCount: float

class AmountSummary(BaseModel):
    """AmountSummary model"""
    subtotal: float
    discount: Optional[float] = None

class OrderSource(BaseModel):
    """OrderSource model"""
    type: str
    subType: Optional[str] = None
    id: str
    name: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None

class GetOrderResponseSchema(BaseModel):
    """GetOrderResponseSchema model"""
    _id: str
    altId: str
    altType: str
    contactId: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    status: str
    liveMode: Optional[bool] = None
    createdAt: str
    updatedAt: str
    fulfillmentStatus: Optional[str] = None
    contactSnapshot: Optional[Dict[str, Any]] = None
    amountSummary: Optional[Any] = None
    source: Optional[Any] = None
    items: Optional[List[str]] = None
    coupon: Optional[Dict[str, Any]] = None
    trackingId: Optional[str] = None
    fingerprint: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    markAsTest: Optional[bool] = None
    traceId: Optional[str] = None
    automaticTaxesCalculated: Optional[bool] = None
    taxCalculationProvider: Optional[Dict[str, Any]] = None

class CardDto(BaseModel):
    """CardDto model"""
    type: str
    last4: str

class ChequeDto(BaseModel):
    """ChequeDto model"""
    number: str

class PostRecordOrderPaymentBody(BaseModel):
    """PostRecordOrderPaymentBody model"""
    altId: str
    altType: str
    mode: str
    card: Optional[Any] = None
    cheque: Optional[Any] = None
    notes: Optional[str] = None
    amount: Optional[float] = None
    meta: Optional[Dict[str, Any]] = None
    isPartialPayment: Optional[bool] = None

class PostRecordOrderPaymentResponse(BaseModel):
    """PostRecordOrderPaymentResponse model"""
    success: bool

class FulfillmentTracking(BaseModel):
    """FulfillmentTracking model"""
    trackingNumber: Optional[str] = None
    shippingCarrier: Optional[str] = None
    trackingUrl: Optional[str] = None

class FulfillmentItems(BaseModel):
    """FulfillmentItems model"""
    priceId: str
    qty: float

class CreateFulfillmentDto(BaseModel):
    """CreateFulfillmentDto model"""
    altId: str
    altType: str
    trackings: List[FulfillmentTracking]
    items: List[FulfillmentItems]
    notifyCustomer: bool

class ProductVariantOptionDto(BaseModel):
    """ProductVariantOptionDto model"""
    id: str
    name: str

class ProductVariantDto(BaseModel):
    """ProductVariantDto model"""
    id: str
    name: str
    options: List[ProductVariantOptionDto]

class ProductMediaDto(BaseModel):
    """ProductMediaDto model"""
    id: str
    title: Optional[str] = None
    url: str
    type: str
    isFeatured: Optional[bool] = None
    priceIds: Optional[List[List[Any]]] = None

class ProductLabelDto(BaseModel):
    """ProductLabelDto model"""
    title: str
    startDate: Optional[str] = None
    endDate: Optional[str] = None

class ProductSEODto(BaseModel):
    """ProductSEODto model"""
    title: Optional[str] = None
    description: Optional[str] = None

class DefaultProductResponseDto(BaseModel):
    """DefaultProductResponseDto model"""
    _id: str
    description: Optional[str] = None
    variants: Optional[List[ProductVariantDto]] = None
    medias: Optional[List[ProductMediaDto]] = None
    locationId: str
    name: str
    productType: str
    availableInStore: Optional[bool] = None
    userId: Optional[str] = None
    createdAt: str
    updatedAt: str
    statementDescriptor: Optional[str] = None
    image: Optional[str] = None
    collectionIds: Optional[List[str]] = None
    isTaxesEnabled: Optional[bool] = None
    taxes: Optional[List[str]] = None
    automaticTaxCategoryId: Optional[str] = None
    isLabelEnabled: Optional[bool] = None
    label: Optional[Any] = None
    slug: Optional[str] = None
    seo: Optional[Any] = None

class MembershipOfferDto(BaseModel):
    """MembershipOfferDto model"""
    label: str
    value: str
    _id: str

class RecurringDto(BaseModel):
    """RecurringDto model"""
    interval: str
    intervalCount: float

class DefaultPriceResponseDto(BaseModel):
    """DefaultPriceResponseDto model"""
    _id: str
    membershipOffers: Optional[List[MembershipOfferDto]] = None
    variantOptionIds: Optional[List[str]] = None
    locationId: Optional[str] = None
    product: Optional[str] = None
    userId: Optional[str] = None
    name: str
    type: str
    currency: str
    amount: float
    recurring: Optional[Any] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    compareAtPrice: Optional[float] = None
    trackInventory: Optional[bool] = None
    availableQuantity: Optional[float] = None
    allowOutOfStockPurchases: Optional[bool] = None

class FulfilledItem(BaseModel):
    """FulfilledItem model"""
    _id: str
    name: str
    product: Any
    price: Any
    qty: float

class FulfillmentSchema(BaseModel):
    """FulfillmentSchema model"""
    altId: str
    altType: str
    trackings: List[FulfillmentTracking]
    _id: str
    items: List[FulfilledItem]
    createdAt: str
    updatedAt: str

class CreateFulfillmentResponseDto(BaseModel):
    """CreateFulfillmentResponseDto model"""
    status: bool
    data: Any

class ListFulfillmentResponseDto(BaseModel):
    """ListFulfillmentResponseDto model"""
    status: bool
    data: List[FulfillmentSchema]

class TxnResponseSchema(BaseModel):
    """TxnResponseSchema model"""
    _id: str
    altId: str
    altType: str
    contactId: Optional[str] = None
    mergedFromContactId: Optional[str] = None
    contactName: Optional[str] = None
    contactEmail: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    status: Dict[str, Any]
    liveMode: Optional[bool] = None
    entityType: Optional[str] = None
    entityId: Optional[str] = None
    entitySourceType: str
    entitySourceSubType: Optional[str] = None
    entitySourceName: Optional[str] = None
    entitySourceId: Optional[str] = None
    entitySourceMeta: Optional[Dict[str, Any]] = None
    subscriptionId: Optional[str] = None
    chargeId: Optional[str] = None
    chargeSnapshot: Optional[Dict[str, Any]] = None
    paymentProviderType: Optional[str] = None
    paymentProviderConnectedAccount: Optional[str] = None
    ipAddress: Optional[str] = None
    createdAt: str
    updatedAt: str
    amountRefunded: Optional[float] = None
    paymentMethod: Optional[Dict[str, Any]] = None
    fulfilledAt: str

class ListTxnsResponseDto(BaseModel):
    """ListTxnsResponseDto model"""
    data: List[TxnResponseSchema]
    totalCount: float

class GetTxnResponseSchema(BaseModel):
    """GetTxnResponseSchema model"""
    _id: str
    altType: str
    altId: str
    contactId: Optional[str] = None
    contactSnapshot: Optional[Dict[str, Any]] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    status: Optional[Dict[str, Any]] = None
    liveMode: Optional[bool] = None
    createdAt: str
    updatedAt: str
    entityType: Optional[str] = None
    entityId: Optional[str] = None
    entitySource: Optional[Any] = None
    chargeId: Optional[str] = None
    chargeSnapshot: Optional[Dict[str, Any]] = None
    invoiceId: Optional[str] = None
    subscriptionId: Optional[str] = None
    paymentProvider: Optional[Dict[str, Any]] = None
    ipAddress: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    markAsTest: Optional[bool] = None
    isParent: Optional[bool] = None
    amountRefunded: Optional[float] = None
    receiptId: Optional[str] = None
    qboSynced: Optional[bool] = None
    qboResponse: Optional[Dict[str, Any]] = None
    traceId: Optional[str] = None
    mergedFromContactId: Optional[str] = None

class SubscriptionResponseSchema(BaseModel):
    """SubscriptionResponseSchema model"""
    _id: str
    altId: str
    altType: str
    contactId: Optional[str] = None
    contactName: Optional[str] = None
    contactEmail: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    status: Dict[str, Any]
    liveMode: Optional[bool] = None
    entityType: Optional[str] = None
    entityId: Optional[str] = None
    entitySourceType: str
    entitySourceName: Optional[str] = None
    entitySourceId: Optional[str] = None
    entitySourceMeta: Optional[Dict[str, Any]] = None
    subscriptionId: Optional[str] = None
    subscriptionSnapshot: Optional[Dict[str, Any]] = None
    paymentProviderType: Optional[str] = None
    paymentProviderConnectedAccount: Optional[str] = None
    ipAddress: Optional[str] = None
    createdAt: str
    updatedAt: str

class ListSubscriptionResponseDto(BaseModel):
    """ListSubscriptionResponseDto model"""
    data: List[SubscriptionResponseSchema]
    totalCount: float

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

class ScheduleOptionsDto(BaseModel):
    """ScheduleOptionsDto model"""
    executeAt: Optional[str] = None
    rrule: Optional[CustomRRuleOptionsDto] = None

class GetSubscriptionResponseSchema(BaseModel):
    """GetSubscriptionResponseSchema model"""
    _id: str
    altType: Dict[str, Any]
    altId: str
    contactId: Optional[str] = None
    contactSnapshot: Optional[Dict[str, Any]] = None
    coupon: Optional[Dict[str, Any]] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    status: Optional[Dict[str, Any]] = None
    liveMode: Optional[bool] = None
    entityType: Optional[str] = None
    entityId: Optional[str] = None
    entitySource: Optional[Any] = None
    subscriptionId: Optional[str] = None
    subscriptionSnapshot: Optional[Dict[str, Any]] = None
    paymentProvider: Optional[Dict[str, Any]] = None
    ipAddress: Optional[str] = None
    createdAt: str
    updatedAt: str
    meta: Optional[Dict[str, Any]] = None
    markAsTest: Optional[bool] = None
    schedule: Optional[Any] = None
    autoPayment: Optional[Dict[str, Any]] = None
    recurringProduct: Optional[Dict[str, Any]] = None
    canceledAt: Optional[str] = None
    canceledBy: Optional[str] = None
    traceId: Optional[str] = None

class ApplyToFuturePaymentsConfigDto(BaseModel):
    """ApplyToFuturePaymentsConfigDto model"""
    type: str
    duration: Optional[float] = None
    durationType: Optional[str] = None

class CouponDto(BaseModel):
    """CouponDto model"""
    _id: str
    usageCount: float
    limitPerCustomer: float
    altId: str
    altType: str
    name: str
    code: str
    discountType: str
    discountValue: float
    status: str
    startDate: str
    endDate: Optional[str] = None
    applyToFuturePayments: bool
    applyToFuturePaymentsConfig: Any
    userId: Optional[str] = None
    createdAt: str
    updatedAt: str

class ListCouponsResponseDto(BaseModel):
    """ListCouponsResponseDto model"""
    data: List[CouponDto]
    totalCount: float
    traceId: str

class ApplyToFuturePaymentsConfig(BaseModel):
    """ApplyToFuturePaymentsConfig model"""
    type: str
    duration: float
    durationType: str

class CreateCouponParams(BaseModel):
    """CreateCouponParams model"""
    altId: str
    altType: str
    name: str
    code: str
    discountType: str
    discountValue: float
    startDate: str
    endDate: Optional[str] = None
    usageLimit: Optional[float] = None
    productIds: Optional[List[str]] = None
    applyToFuturePayments: Optional[bool] = None
    applyToFuturePaymentsConfig: Optional[Any] = None
    limitPerCustomer: Optional[bool] = None

class CreateCouponResponseDto(BaseModel):
    """CreateCouponResponseDto model"""
    _id: str
    usageCount: float
    limitPerCustomer: float
    altId: str
    altType: str
    name: str
    code: str
    discountType: str
    discountValue: float
    status: str
    startDate: str
    endDate: Optional[str] = None
    applyToFuturePayments: bool
    applyToFuturePaymentsConfig: Any
    userId: Optional[str] = None
    createdAt: str
    updatedAt: str
    traceId: str

class UpdateCouponParams(BaseModel):
    """UpdateCouponParams model"""
    altId: str
    altType: str
    name: str
    code: str
    discountType: str
    discountValue: float
    startDate: str
    endDate: Optional[str] = None
    usageLimit: Optional[float] = None
    productIds: Optional[List[str]] = None
    applyToFuturePayments: Optional[bool] = None
    applyToFuturePaymentsConfig: Optional[Any] = None
    limitPerCustomer: Optional[bool] = None
    id: str

class DeleteCouponParams(BaseModel):
    """DeleteCouponParams model"""
    altId: str
    altType: str
    id: str

class DeleteCouponResponseDto(BaseModel):
    """DeleteCouponResponseDto model"""
    success: bool
    traceId: str

class CreateCustomProvidersDto(BaseModel):
    """CreateCustomProvidersDto model"""
    name: str
    description: str
    paymentsUrl: str
    queryUrl: str
    imageUrl: str
    supportsSubscriptionSchedule: bool

class CreateCustomProvidersResponseSchema(BaseModel):
    """CreateCustomProvidersResponseSchema model"""
    name: str
    description: str
    paymentsUrl: str
    queryUrl: str
    imageUrl: str
    _id: str
    locationId: str
    marketplaceAppId: str
    paymentProvider: Optional[Dict[str, Any]] = None
    deleted: bool
    createdAt: str
    updatedAt: str
    traceId: Optional[str] = None

class DeleteCustomProvidersResponseSchema(BaseModel):
    """DeleteCustomProvidersResponseSchema model"""
    success: bool

class GetCustomProvidersResponseSchema(BaseModel):
    """GetCustomProvidersResponseSchema model"""
    name: str
    description: str
    paymentsUrl: str
    queryUrl: str
    imageUrl: str
    _id: str
    locationId: str
    marketplaceAppId: str
    paymentProvider: Optional[Dict[str, Any]] = None
    deleted: bool
    createdAt: str
    updatedAt: str
    traceId: Optional[str] = None

class CustomProviderKeys(BaseModel):
    """CustomProviderKeys model"""
    apiKey: str
    publishableKey: str

class ConnectCustomProvidersConfigDto(BaseModel):
    """ConnectCustomProvidersConfigDto model"""
    live: Any
    test: Any

class ConnectCustomProvidersResponseSchema(BaseModel):
    """ConnectCustomProvidersResponseSchema model"""
    name: str
    description: str
    paymentsUrl: str
    queryUrl: str
    imageUrl: str
    _id: str
    locationId: str
    marketplaceAppId: str
    paymentProvider: Optional[Dict[str, Any]] = None
    deleted: bool
    createdAt: str
    updatedAt: str
    traceId: Optional[str] = None

class DeleteCustomProvidersConfigDto(BaseModel):
    """DeleteCustomProvidersConfigDto model"""
    liveMode: bool

class DisconnectCustomProvidersResponseSchema(BaseModel):
    """DisconnectCustomProvidersResponseSchema model"""
    success: bool

class UpdateCustomProviderCapabilitiesDto(BaseModel):
    """UpdateCustomProviderCapabilitiesDto model"""
    supportsSubscriptionSchedules: bool
    companyId: Optional[str] = None
    locationId: Optional[str] = None

class UpdateCustomProviderCapabilitiesResponseSchema(BaseModel):
    """UpdateCustomProviderCapabilitiesResponseSchema model"""
    success: bool

