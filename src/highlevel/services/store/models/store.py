from __future__ import annotations

# Store Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class ShippingZoneCountryStateDto(BaseModel):
    """ShippingZoneCountryStateDto model"""
    code: str

class ShippingZoneCountryDto(BaseModel):
    """ShippingZoneCountryDto model"""
    code: float
    states: Optional[List[ShippingZoneCountryStateDto]] = None

class CreateShippingZoneDto(BaseModel):
    """CreateShippingZoneDto model"""
    altId: str
    altType: str
    name: str
    countries: List[ShippingZoneCountryDto]

class ShippingCarrierServiceDto(BaseModel):
    """ShippingCarrierServiceDto model"""
    name: str
    value: str

class ShippingRateSchema(BaseModel):
    """ShippingRateSchema model"""
    altId: str
    altType: str
    name: str
    description: Optional[str] = None
    currency: str
    amount: float
    conditionType: str
    minCondition: float
    maxCondition: float
    isCarrierRate: Optional[bool] = None
    shippingCarrierId: str
    percentageOfRateFee: Optional[float] = None
    shippingCarrierServices: Optional[List[ShippingCarrierServiceDto]] = None
    _id: str
    shippingZoneId: str
    createdAt: str
    updatedAt: str

class ShippingZoneSchema(BaseModel):
    """ShippingZoneSchema model"""
    altId: str
    altType: str
    name: str
    countries: List[ShippingZoneCountryDto]
    _id: str
    shippingRates: Optional[List[ShippingRateSchema]] = None
    createdAt: str
    updatedAt: str

class CreateShippingZoneResponseDto(BaseModel):
    """CreateShippingZoneResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class ListShippingZoneResponseDto(BaseModel):
    """ListShippingZoneResponseDto model"""
    total: float
    data: List[ShippingZoneSchema]

class GetShippingZoneResponseDto(BaseModel):
    """GetShippingZoneResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class UpdateShippingZoneDto(BaseModel):
    """UpdateShippingZoneDto model"""
    altId: Optional[str] = None
    altType: Optional[str] = None
    name: Optional[str] = None
    countries: Optional[List[ShippingZoneCountryDto]] = None

class UpdateShippingZoneResponseDto(BaseModel):
    """UpdateShippingZoneResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class DeleteShippingZoneResponseDto(BaseModel):
    """DeleteShippingZoneResponseDto model"""
    status: bool
    message: Optional[str] = None

class ContactAddress(BaseModel):
    """ContactAddress model"""
    name: Optional[str] = None
    companyName: Optional[str] = None
    addressLine1: Optional[str] = None
    country: str
    state: Optional[str] = None
    city: Optional[str] = None
    zip: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class OrderSource(BaseModel):
    """OrderSource model"""
    type: str
    subType: Optional[str] = None

class ProductItem(BaseModel):
    """ProductItem model"""
    id: str
    qty: float

class GetAvailableShippingRates(BaseModel):
    """GetAvailableShippingRates model"""
    altId: str
    altType: str
    country: str
    address: Optional[Any] = None
    amountAvailable: Optional[str] = None
    totalOrderAmount: float
    weightAvailable: Optional[bool] = None
    totalOrderWeight: float
    source: Any
    products: List[ProductItem]
    couponCode: Optional[str] = None

class AvailableShippingRate(BaseModel):
    """AvailableShippingRate model"""
    name: str
    description: Optional[str] = None
    currency: str
    amount: float
    isCarrierRate: Optional[bool] = None
    shippingCarrierId: str
    percentageOfRateFee: Optional[float] = None
    shippingCarrierServices: Optional[List[ShippingCarrierServiceDto]] = None
    _id: str
    shippingZoneId: str

class GetAvailableShippingRatesResponseDto(BaseModel):
    """GetAvailableShippingRatesResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: List[AvailableShippingRate]

class CreateShippingRateDto(BaseModel):
    """CreateShippingRateDto model"""
    altId: str
    altType: str
    name: str
    description: Optional[str] = None
    currency: str
    amount: float
    conditionType: str
    minCondition: float
    maxCondition: float
    isCarrierRate: Optional[bool] = None
    shippingCarrierId: str
    percentageOfRateFee: Optional[float] = None
    shippingCarrierServices: Optional[List[ShippingCarrierServiceDto]] = None

class CreateShippingRateResponseDto(BaseModel):
    """CreateShippingRateResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class ListShippingRateResponseDto(BaseModel):
    """ListShippingRateResponseDto model"""
    total: float
    data: List[ShippingRateSchema]

class GetShippingRateResponseDto(BaseModel):
    """GetShippingRateResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class UpdateShippingRateDto(BaseModel):
    """UpdateShippingRateDto model"""
    altId: Optional[str] = None
    altType: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    conditionType: Optional[str] = None
    minCondition: Optional[float] = None
    maxCondition: Optional[float] = None
    isCarrierRate: Optional[bool] = None
    shippingCarrierId: Optional[str] = None
    percentageOfRateFee: Optional[float] = None
    shippingCarrierServices: Optional[List[ShippingCarrierServiceDto]] = None

class UpdateShippingRateResponseDto(BaseModel):
    """UpdateShippingRateResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class DeleteShippingRateResponseDto(BaseModel):
    """DeleteShippingRateResponseDto model"""
    status: bool
    message: Optional[str] = None

class CreateShippingCarrierDto(BaseModel):
    """CreateShippingCarrierDto model"""
    altId: str
    altType: str
    name: str
    callbackUrl: str
    services: Optional[List[ShippingCarrierServiceDto]] = None
    allowsMultipleServiceSelection: Optional[bool] = None

class ShippingCarrierSchema(BaseModel):
    """ShippingCarrierSchema model"""
    altId: str
    altType: str
    name: str
    callbackUrl: str
    services: Optional[List[ShippingCarrierServiceDto]] = None
    allowsMultipleServiceSelection: Optional[bool] = None
    _id: str
    marketplaceAppId: str
    createdAt: str
    updatedAt: str

class CreateShippingCarrierResponseDto(BaseModel):
    """CreateShippingCarrierResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class ListShippingCarrierResponseDto(BaseModel):
    """ListShippingCarrierResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: List[ShippingCarrierSchema]

class GetShippingCarrierResponseDto(BaseModel):
    """GetShippingCarrierResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class UpdateShippingCarrierDto(BaseModel):
    """UpdateShippingCarrierDto model"""
    altId: Optional[str] = None
    altType: Optional[str] = None
    name: Optional[str] = None
    callbackUrl: Optional[str] = None
    services: Optional[List[ShippingCarrierServiceDto]] = None
    allowsMultipleServiceSelection: Optional[bool] = None

class UpdateShippingCarrierResponseDto(BaseModel):
    """UpdateShippingCarrierResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class DeleteShippingCarrierResponseDto(BaseModel):
    """DeleteShippingCarrierResponseDto model"""
    status: bool
    message: Optional[str] = None

class StoreShippingOriginDto(BaseModel):
    """StoreShippingOriginDto model"""
    name: str
    country: float
    state: Optional[str] = None
    city: str
    street1: str
    street2: Optional[str] = None
    zip: str
    phone: Optional[str] = None
    email: Optional[str] = None

class StoreOrderNotificationDto(BaseModel):
    """StoreOrderNotificationDto model"""
    enabled: bool
    subject: str
    emailTemplateId: str
    defaultEmailTemplateId: str

class StoreOrderFulfillmentNotificationDto(BaseModel):
    """StoreOrderFulfillmentNotificationDto model"""
    enabled: bool
    subject: str
    emailTemplateId: str
    defaultEmailTemplateId: str

class CreateStoreSettingDto(BaseModel):
    """CreateStoreSettingDto model"""
    altId: str
    altType: str
    shippingOrigin: Any
    storeOrderNotification: Optional[Any] = None
    storeOrderFulfillmentNotification: Optional[Any] = None

class StoreSettingSchema(BaseModel):
    """StoreSettingSchema model"""
    altId: str
    altType: str
    shippingOrigin: Any
    storeOrderNotification: Optional[Any] = None
    storeOrderFulfillmentNotification: Optional[Any] = None
    _id: str
    createdAt: str
    updatedAt: str

class CreateStoreSettingResponseDto(BaseModel):
    """CreateStoreSettingResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

class GetStoreSettingResponseDto(BaseModel):
    """GetStoreSettingResponseDto model"""
    status: bool
    message: Optional[str] = None
    data: Any

