from __future__ import annotations

# Surveys Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class GetSurveysSchema(BaseModel):
    """GetSurveysSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    locationId: Optional[str] = None

class GetSurveysSuccessfulResponseDto(BaseModel):
    """GetSurveysSuccessfulResponseDto model"""
    surveys: Optional[List[GetSurveysSchema]] = None
    total: Optional[float] = None

class PageDetailsSchema(BaseModel):
    """PageDetailsSchema model"""
    url: Optional[str] = None
    title: Optional[str] = None

class ContactSessionIds(BaseModel):
    """ContactSessionIds model"""
    ids: Optional[List[str]] = None

class EventDataSchema(BaseModel):
    """EventDataSchema model"""
    fbc: Optional[str] = None
    fbp: Optional[str] = None
    page: Optional[PageDetailsSchema] = None
    type: Optional[str] = None
    domain: Optional[str] = None
    medium: Optional[str] = None
    source: Optional[str] = None
    version: Optional[str] = None
    adSource: Optional[str] = None
    mediumId: Optional[str] = None
    parentId: Optional[str] = None
    referrer: Optional[str] = None
    fbEventId: Optional[str] = None
    timestamp: Optional[float] = None
    parentName: Optional[str] = None
    fingerprint: Optional[str] = None
    pageVisitType: Optional[str] = None
    contactSessionIds: Optional[Any] = None

class othersSchema(BaseModel):
    """othersSchema model"""
    __submissions_other_field__: Optional[str] = None
    __custom_field_id__: Optional[str] = None
    eventData: Optional[EventDataSchema] = None
    fieldsOriSequance: Optional[List[str]] = None

class SubmissionSchema(BaseModel):
    """SubmissionSchema model"""
    id: Optional[str] = None
    contactId: Optional[str] = None
    createdAt: Optional[str] = None
    surveyId: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    others: Optional[othersSchema] = None

class metaSchema(BaseModel):
    """metaSchema model"""
    total: Optional[float] = None
    currentPage: Optional[float] = None
    nextPage: Optional[float] = None
    prevPage: Optional[float] = None

class GetSurveysSubmissionSuccessfulResponseDto(BaseModel):
    """GetSurveysSubmissionSuccessfulResponseDto model"""
    submissions: Optional[List[SubmissionSchema]] = None
    meta: Optional[metaSchema] = None

