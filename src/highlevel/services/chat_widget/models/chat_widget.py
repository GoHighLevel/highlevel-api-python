# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# ChatWidget Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class AcknowledgementDetailsDTO(BaseModel):
    """AcknowledgementDetailsDTO model"""
    icon: Optional[str] = None
    placeholderColor: Optional[str] = None
    liveChatIcon: Optional[str] = None
    liveChatPlaceholderColor: Optional[str] = None

class WidgetSettingsThemeCustomColorDTO(BaseModel):
    """WidgetSettingsThemeCustomColorDTO model"""
    chatBubbleColor: Optional[str] = None
    backgroundColor: Optional[str] = None
    headerColor: Optional[str] = None
    buttonColor: Optional[str] = None
    avatarBackgroundColor: Optional[str] = None
    avatarBorderColor: Optional[str] = None
    senderMessageColor: Optional[str] = None
    receivedMessageColor: Optional[str] = None

class WidgetSettingsThemeDTO(BaseModel):
    """WidgetSettingsThemeDTO model"""
    name: Optional[str] = None
    colors: Optional[Any] = None

class WidgetSettingsCustomizationSizeDTO(BaseModel):
    """WidgetSettingsCustomizationSizeDTO model"""
    width: Optional[float] = None
    height: Optional[float] = None

class WidgetSettingsCustomizationDTO(BaseModel):
    """WidgetSettingsCustomizationDTO model"""
    position: Optional[str] = None
    sizes: Optional[Any] = None

class RedirectDTO(BaseModel):
    """RedirectDTO model"""
    redirectAction: Optional[bool] = None
    redirectWebsite: Optional[str] = None
    redirectText: Optional[str] = None

class BusinessOfficeHoursDTO(BaseModel):
    """BusinessOfficeHoursDTO model"""
    enableBusinessHours: Optional[bool] = None
    openHours: Optional[List[str]] = None
    timezone: Optional[str] = None
    outsideOfficeHoursWelcomeMsg: Optional[str] = None

class FBPageDTO(BaseModel):
    """FBPageDTO model"""
    facebookPageId: Optional[str] = None
    facebookPageName: Optional[str] = None

class InstagramPageDTO(BaseModel):
    """InstagramPageDTO model"""
    facebookPageId: Optional[str] = None
    facebookPageName: Optional[str] = None
    instagramPageId: Optional[str] = None
    instagramUsername: Optional[str] = None

class A2PComplianceDTO(BaseModel):
    """A2PComplianceDTO model"""
    enableA2PCompliance: Optional[bool] = None
    a2pOptInForm1: Optional[str] = None
    a2pOptInForm1ShowCheckbox: Optional[bool] = None
    a2pOptInForm1PreChecked: Optional[bool] = None
    isA2POptInForm2: Optional[bool] = None
    a2pOptInForm2: Optional[str] = None
    a2pOptInForm2ShowCheckbox: Optional[bool] = None
    a2pOptInForm2PreChecked: Optional[bool] = None
    privacyPolicyLink: Optional[str] = None
    termsOfServiceLink: Optional[str] = None
    isA2POptInForm1: Optional[bool] = None
    messageType: Optional[str] = None

class AdvanceSettingsDTO(BaseModel):
    """AdvanceSettingsDTO model"""
    brandingTitle: Optional[str] = None
    redirect: Optional[Any] = None
    enableContactForm: Optional[bool] = None
    defaultConsentCheck: Optional[bool] = None
    businessOfficeHours: Optional[Any] = None
    contactFormOptions: Optional[List[str]] = None
    allInOneChatTypes: Optional[List[str]] = None
    allInOneInitialMsg: Optional[str] = None
    contactFormIntroMessage: Optional[str] = None
    contactFormSystemMessage: Optional[str] = None
    prefilledMessageText: Optional[str] = None
    voiceAiAgent: Optional[Dict[str, Any]] = None
    fbPage: Optional[Any] = None
    instagramPage: Optional[Any] = None
    playNotificationSound: Optional[bool] = None
    voiceAiSendActionText: Optional[str] = None
    aTwoPCompliance: Optional[Any] = None

class WidgetSettingsDTO(BaseModel):
    """WidgetSettingsDTO model"""
    acknowledgementDetails: Optional[Any] = None
    agencyName: Optional[str] = None
    agencyWebsite: Optional[str] = None
    allowAvatarImage: Optional[bool] = None
    autoCountryCode: Optional[bool] = None
    countryCode: Optional[str] = None
    chatType: str
    promptType: Optional[str] = None
    chatIcon: str
    enableRevisitMessage: Optional[bool] = None
    heading: Optional[str] = None
    legalMsg: Optional[str] = None
    liveChatAckMsg: Optional[str] = None
    liveChatEndedMsg: Optional[str] = None
    liveChatFeedbackMsg: Optional[str] = None
    liveChatFeedbackNote: Optional[str] = None
    liveChatIntroMsg: Optional[str] = None
    liveChatUserInactiveMsg: Optional[str] = None
    liveChatUserInactiveTime: Optional[str] = None
    liveChatVisitorInactiveMsg: Optional[str] = None
    liveChatVisitorInactiveTime: Optional[str] = None
    locale: Optional[str] = None
    promptAvatar: Optional[str] = None
    promptAvatarAltText: Optional[str] = None
    isPromptAvatarImageOptimize: Optional[bool] = None
    promptMsg: Optional[str] = None
    revisitPromptMsg: Optional[str] = None
    sendActionText: Optional[str] = None
    showAgencyBranding: Optional[bool] = None
    showConsentCheckbox: Optional[bool] = None
    showLiveChatWelcomeMsg: Optional[bool] = None
    showPrompt: Optional[bool] = None
    subHeading: Optional[str] = None
    successMsg: Optional[str] = None
    supportContact: Optional[str] = None
    thankYouMsg: Optional[str] = None
    theme: Optional[Any] = None
    useEmailField: Optional[bool] = None
    waNumber: Optional[str] = None
    widgetPrimaryColor: Optional[str] = None
    representativeAssignedMessage: Optional[str] = None
    dimensions: Optional[Any] = None
    advanceSettings: Optional[Any] = None
    locationCountryCode: Optional[str] = None
    widgetId: Optional[str] = None
    widgetPlacement: Optional[str] = None

class CreateWidgetDTO(BaseModel):
    """CreateWidgetDTO model"""
    version: float
    chatType: str
    name: str
    locationId: str
    deleted: Optional[bool] = None
    default: Optional[bool] = None
    settings: Optional[Any] = None

class UpdateWidgetDTO(BaseModel):
    """UpdateWidgetDTO model"""
    version: Optional[float] = None
    chatType: Optional[str] = None
    name: Optional[str] = None
    default: Optional[bool] = None
    settings: Optional[Any] = None

class CloneChatWidgetDTO(BaseModel):
    """CloneChatWidgetDTO model"""
    locationId: str
    chatWidgetId: str
    name: Optional[str] = None

