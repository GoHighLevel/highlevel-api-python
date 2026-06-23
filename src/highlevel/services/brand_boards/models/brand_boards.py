# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# BrandBoards Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class BrandVoicePublicV1Dto(BaseModel):
    """BrandVoicePublicV1Dto model"""
    id: str
    name: str
    isDefault: bool
    createdAt: str
    updatedAt: str

class ListBrandVoicesPublicV1ResponseDto(BaseModel):
    """ListBrandVoicesPublicV1ResponseDto model"""
    items: List[BrandVoicePublicV1Dto]
    total: float
    traceId: Optional[str] = None

class InvalidLocationDTO(BaseModel):
    """InvalidLocationDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None

class NotFoundDTO(BaseModel):
    """NotFoundDTO model"""
    statusCode: Optional[float] = None
    message: Optional[str] = None
    error: Optional[str] = None

class BrandVoiceAnswersDto(BaseModel):
    """BrandVoiceAnswersDto model"""
    brandName: str
    toneOfVoice: str
    targetAudience: str
    customerPainPoints: str
    businessType: Optional[str] = None
    companyWebsite: Optional[str] = None
    companyEmail: Optional[str] = None
    companyAddress: Optional[str] = None
    phone: Optional[Dict[str, Any]] = None
    businessHours: Optional[str] = None
    brandPromise: Optional[str] = None
    brandValues: Optional[str] = None
    brandPurpose: Optional[str] = None
    competitiveAdvantage: Optional[str] = None
    risksOfInaction: Optional[str] = None
    uniqueSellingProposition: Optional[str] = None
    callToAction: Optional[str] = None

class CreateBrandVoicePublicV1BodyDto(BaseModel):
    """CreateBrandVoicePublicV1BodyDto model"""
    name: Optional[str] = None
    type: str
    url: Optional[str] = None
    description: Optional[str] = None
    answers: Optional[Any] = None

class BrandVoiceAnswersPublicV1Dto(BaseModel):
    """BrandVoiceAnswersPublicV1Dto model"""
    brandName: Optional[str] = None
    toneOfVoice: Optional[str] = None
    targetAudience: Optional[str] = None
    customerPainPoints: Optional[str] = None
    businessType: Optional[str] = None
    companyWebsite: Optional[str] = None
    companyEmail: Optional[str] = None
    companyAddress: Optional[str] = None
    phone: Optional[Dict[str, Any]] = None
    businessHours: Optional[str] = None
    brandPromise: Optional[str] = None
    brandValues: Optional[str] = None
    brandPurpose: Optional[str] = None
    competitiveAdvantage: Optional[str] = None
    risksOfInaction: Optional[str] = None
    uniqueSellingProposition: Optional[str] = None
    callToAction: Optional[str] = None

class CreateBrandVoicePublicV1ResponseDto(BaseModel):
    """CreateBrandVoicePublicV1ResponseDto model"""
    id: str
    name: str
    isDefault: bool
    createdAt: str
    updatedAt: str
    locationId: str
    deleted: bool
    answers: Optional[Any] = None
    traceId: Optional[str] = None

class GetBrandVoicePublicV1ResponseDto(BaseModel):
    """GetBrandVoicePublicV1ResponseDto model"""
    id: str
    name: str
    isDefault: bool
    createdAt: str
    updatedAt: str
    locationId: str
    deleted: bool
    answers: Optional[Any] = None
    traceId: Optional[str] = None

class UpdateBrandVoiceAnswersDto(BaseModel):
    """UpdateBrandVoiceAnswersDto model"""
    brandName: Optional[str] = None
    toneOfVoice: Optional[str] = None
    targetAudience: Optional[str] = None
    customerPainPoints: Optional[str] = None
    businessType: Optional[str] = None
    companyWebsite: Optional[str] = None
    companyEmail: Optional[str] = None
    companyAddress: Optional[str] = None
    phone: Optional[Dict[str, Any]] = None
    businessHours: Optional[str] = None
    brandPromise: Optional[str] = None
    brandValues: Optional[str] = None
    brandPurpose: Optional[str] = None
    competitiveAdvantage: Optional[str] = None
    risksOfInaction: Optional[str] = None
    uniqueSellingProposition: Optional[str] = None
    callToAction: Optional[str] = None

class UpdateBrandVoicePublicV1BodyDto(BaseModel):
    """UpdateBrandVoicePublicV1BodyDto model"""
    name: Optional[str] = None
    answers: Optional[Any] = None

class UpdateBrandVoicePublicV1ResponseDto(BaseModel):
    """UpdateBrandVoicePublicV1ResponseDto model"""
    id: str
    name: str
    isDefault: bool
    createdAt: str
    updatedAt: str
    locationId: str
    deleted: bool
    answers: Optional[Any] = None
    traceId: Optional[str] = None

class DeleteBrandVoicePublicV1ResponseDto(BaseModel):
    """DeleteBrandVoicePublicV1ResponseDto model"""
    deleted: bool
    traceId: Optional[str] = None

class SetDefaultBrandVoicePublicV1ResponseDto(BaseModel):
    """SetDefaultBrandVoicePublicV1ResponseDto model"""
    success: bool
    brandVoiceId: str
    traceId: Optional[str] = None

class Logo(BaseModel):
    """Logo model"""
    id: Optional[str] = None
    url: str
    label: str
    path: str

class Color(BaseModel):
    """Color model"""
    id: Optional[str] = None
    hexa: str
    rgba: str
    hex: str
    rgb: str
    label: str

class Font(BaseModel):
    """Font model"""
    id: Optional[str] = None
    font: str
    fallback: str
    label: str

class CreateBrandBoardParam(BaseModel):
    """CreateBrandBoardParam model"""
    locationId: str
    name: str
    logos: Optional[List[Logo]] = None
    colors: Optional[List[Color]] = None
    fonts: Optional[List[Font]] = None
    default: Optional[bool] = None
    brandBoardId: Optional[str] = None
    parentId: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None

class MetaData(BaseModel):
    """MetaData model"""
    updatedBy: Optional[str] = None
    lastAction: Optional[str] = None
    sourceId: Optional[str] = None
    sourceType: Optional[str] = None

class MissingAssets(BaseModel):
    """MissingAssets model"""
    logos: List[str]
    fonts: List[str]
    colors: List[str]

class GetBrandBoardSuccessDTO(BaseModel):
    """GetBrandBoardSuccessDTO model"""
    _id: str
    locationId: str
    name: str
    logos: Optional[List[Logo]] = None
    colors: Optional[List[Color]] = None
    fonts: Optional[List[Font]] = None
    default: bool
    deleted: bool
    parentId: Optional[str] = None
    folderId: Optional[str] = None
    originId: Optional[str] = None
    meta: Optional[Any] = None
    missingAssets: Optional[Any] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class BrandBoardListItemDTO(BaseModel):
    """BrandBoardListItemDTO model"""
    _id: str
    name: str
    updatedAt: str
    default: Optional[bool] = None
    meta: Optional[Any] = None

class GetBrandBoardsByLocationSuccessDTO(BaseModel):
    """GetBrandBoardsByLocationSuccessDTO model"""
    brandBoards: List[BrandBoardListItemDTO]
    totalCount: float

class UpdateBrandBoardBody(BaseModel):
    """UpdateBrandBoardBody model"""
    name: Optional[str] = None
    logos: Optional[List[Logo]] = None
    colors: Optional[List[Color]] = None
    fonts: Optional[List[Font]] = None
    default: Optional[bool] = None
    parentId: Optional[str] = None

