# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# AdPublishing Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class GreetingCard(BaseModel):
    """GreetingCard model"""
    title: str
    style: str
    content: List[str]

class FormQuestionOption(BaseModel):
    """FormQuestionOption model"""
    key: str
    value: str

class FormQuestion(BaseModel):
    """FormQuestion model"""
    label: Optional[str] = None
    key: str
    type: str
    options: Optional[List[FormQuestionOption]] = None

class CustomDisclaimerCheckbox(BaseModel):
    """CustomDisclaimerCheckbox model"""
    isRequired: bool
    text: str
    key: str

class CustomDisclaimer(BaseModel):
    """CustomDisclaimer model"""
    title: str
    body: str
    checkboxes: Optional[List[CustomDisclaimerCheckbox]] = None

class ThankYouPage(BaseModel):
    """ThankYouPage model"""
    title: str
    body: str
    buttonText: str
    buttonType: str
    buttonLink: Optional[str] = None
    businessPhone: Optional[str] = None
    countryCode: Optional[str] = None

class CreateLeadFormDTO(BaseModel):
    """CreateLeadFormDTO model"""
    type: str
    name: str
    locationId: str
    greetingCard: Optional[Any] = None
    questions: List[FormQuestion]
    questionPageHeadline: Optional[str] = None
    privacyPolicyLink: str
    privacyPolicyText: Optional[str] = None
    customDisclaimer: Optional[Any] = None
    thankYouPage: Any
    isDraft: Optional[bool] = None
    draftFormId: Optional[str] = None
    locale: Optional[str] = None

class LocationIdBodyDTO(BaseModel):
    """LocationIdBodyDTO model"""
    locationId: str

class WelcomeMessageQuestion(BaseModel):
    """WelcomeMessageQuestion model"""
    question: str
    response: Optional[str] = None

class CreateConversationFormDTO(BaseModel):
    """CreateConversationFormDTO model"""
    locationId: str
    name: str
    text: str
    questions: List[WelcomeMessageQuestion]

class CreateIntegrationDTO(BaseModel):
    """CreateIntegrationDTO model"""
    locationId: str
    pageId: str
    adAccountId: Optional[str] = None

class PublishAdDTO(BaseModel):
    """PublishAdDTO model"""
    locationId: str

class UpsertConversionPixelDTO(BaseModel):
    """UpsertConversionPixelDTO model"""
    locationId: str
    conversionPixelId: Optional[str] = None
    name: Optional[str] = None
    igUserId: Optional[str] = None
    type: str

class FbUpdateAudienceBodyDTO(BaseModel):
    """FbUpdateAudienceBodyDTO model"""
    locationId: str
    name: str
    description: Optional[str] = None

class UpdateCustomAudienceDTO(BaseModel):
    """UpdateCustomAudienceDTO model"""
    locationId: str
    contactId: str
    fbAdAccountId: Optional[str] = None

class UpdateCustomAudienceBatchDTO(BaseModel):
    """UpdateCustomAudienceBatchDTO model"""
    locationId: str
    csvPath: Optional[str] = None
    operationType: str
    smartlistIds: Optional[List[str]] = None
    dynamicAudience: Optional[str] = None

class FbSetDefaultPageBodyDTO(BaseModel):
    """FbSetDefaultPageBodyDTO model"""
    pageId: str

class UpsertCampaignDTO(BaseModel):
    """UpsertCampaignDTO model"""
    id: Optional[str] = None
    locationId: str
    name: Optional[str] = None
    objective: Optional[str] = None
    specialAdCategories: Optional[List[str]] = None
    source: Optional[str] = None

class AudienceLocationGeometry(BaseModel):
    """AudienceLocationGeometry model"""
    location: Dict[str, Any]
    locationType: str

class AudienceLocationDTO(BaseModel):
    """AudienceLocationDTO model"""
    key: str
    name: str
    type: str
    selectionType: str
    radius: Optional[float] = None
    radiusUnit: Optional[str] = None
    geometry: Optional[Any] = None

class AudienceLocaleDTO(BaseModel):
    """AudienceLocaleDTO model"""
    name: str
    key: float

class AudiencePlacementsDTO(BaseModel):
    """AudiencePlacementsDTO model"""
    facebook: Optional[List[str]] = None
    instagram: Optional[List[str]] = None
    messenger: Optional[List[str]] = None

class AudienceCustomAudienceItemDTO(BaseModel):
    """AudienceCustomAudienceItemDTO model"""
    id: str
    name: str

class AudienceInterestDTO(BaseModel):
    """AudienceInterestDTO model"""
    id: str
    name: str
    type: Optional[str] = None

class FacebookAudienceDTO(BaseModel):
    """FacebookAudienceDTO model"""
    geoLocations: List[AudienceLocationDTO]
    locales: Optional[List[AudienceLocaleDTO]] = None
    placements: Optional[Any] = None
    placementType: Optional[str] = None
    lookalike: Optional[List[AudienceCustomAudienceItemDTO]] = None
    retargeting: Optional[List[AudienceCustomAudienceItemDTO]] = None
    interests: Optional[List[AudienceInterestDTO]] = None
    ageMin: Optional[float] = None
    ageMax: Optional[float] = None
    genders: Optional[List[float]] = None

class Budget(BaseModel):
    """Budget model"""
    budgetType: str
    amount: float
    scheduleStartDate: Optional[str] = None
    scheduleEndDate: Optional[str] = None

class UpsertAdsetDTO(BaseModel):
    """UpsertAdsetDTO model"""
    id: Optional[str] = None
    locationId: str
    name: Optional[str] = None
    pageId: Optional[str] = None
    instagramActorId: Optional[str] = None
    messagingPlatforms: Optional[List[str]] = None
    whatsappNumber: Optional[str] = None
    audience: Optional[Any] = None
    budget: Optional[Any] = None
    conversionLocation: Optional[str] = None
    customEventType: Optional[str] = None
    pixelId: Optional[str] = None
    campaignId: str

class MediaDTO(BaseModel):
    """MediaDTO model"""
    src: str
    thumbnailUrl: Optional[str] = None
    selectedPoster: Optional[float] = None
    type: str
    name: Optional[str] = None
    headline: Optional[str] = None
    description: Optional[str] = None
    link: Optional[str] = None

class UpsertAdDTO(BaseModel):
    """UpsertAdDTO model"""
    id: Optional[str] = None
    locationId: str
    name: Optional[str] = None
    primaryText: Optional[str] = None
    headline: Optional[str] = None
    description: Optional[str] = None
    imageUrl: Optional[str] = None
    mediaType: Optional[str] = None
    media: Optional[List[MediaDTO]] = None
    multiAdvertiserAds: Optional[bool] = None
    campaignId: str
    adsetId: str
    cta: Optional[str] = None
    conversationFormId: Optional[str] = None
    destinationLink: Optional[str] = None
    destinationFormId: Optional[str] = None

class PublishingProgressResponseDTO(BaseModel):
    """PublishingProgressResponseDTO model"""
    campaignId: str
    publishingStatus: str
    total: float
    processed: float
    isComplete: bool
    hasFailed: bool

class AdScheduleTargetDTO(BaseModel):
    """AdScheduleTargetDTO model"""
    startMinute: str
    endMinute: str
    dayOfWeek: str
    startHour: float
    endHour: float

class CallAssetPayloadDTO(BaseModel):
    """CallAssetPayloadDTO model"""
    phoneNumber: str
    countryCode: str
    callConversionAction: Optional[str] = None
    adScheduleTargets: Optional[List[AdScheduleTargetDTO]] = None
    resourceName: Optional[str] = None

class SitelinkAssetPayloadDTO(BaseModel):
    """SitelinkAssetPayloadDTO model"""
    resourceName: Optional[str] = None
    linkText: str
    finalUrls: str
    description1: Optional[str] = None
    description2: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    adScheduleTargets: Optional[List[AdScheduleTargetDTO]] = None

class LeadFormFieldDTO(BaseModel):
    """LeadFormFieldDTO model"""
    inputType: str
    singleChoiceAnswers: Optional[List[str]] = None

class CustomQuestionFieldDTO(BaseModel):
    """CustomQuestionFieldDTO model"""
    customQuestionText: str
    singleChoiceAnswers: List[str]

class LeadFormAssetPayloadDTO(BaseModel):
    """LeadFormAssetPayloadDTO model"""
    resourceName: Optional[str] = None
    headline: str
    description: str
    businessName: str
    privacyPolicyUrl: str
    fields: List[LeadFormFieldDTO]
    callToActionType: str
    callToActionDescription: Optional[str] = None
    backgroundImageAsset: Optional[str] = None
    desiredIntent: Optional[str] = None
    customQuestionFields: Optional[List[CustomQuestionFieldDTO]] = None
    postSubmitHeadline: Optional[str] = None
    postSubmitDescription: Optional[str] = None
    postSubmitCallToActionType: Optional[str] = None
    finalUrls: Optional[str] = None

class ConversionValueSettings(BaseModel):
    """ConversionValueSettings model"""
    defaultValue: float
    defaultCurrencyCode: str
    alwaysUseDefaultValue: bool

class UpsertConversionDTO(BaseModel):
    """UpsertConversionDTO model"""
    locationId: str
    conversionId: Optional[str] = None
    name: str
    type: str
    category: str
    valueSettings: Any
    countingType: str
    attributionModel: str
    clickThroughWindow: float

class CreateGoogleIntegrationDTO(BaseModel):
    """CreateGoogleIntegrationDTO model"""
    locationId: str
    adAccountId: str
    mccId: str

class KeywordSuggestionDTO(BaseModel):
    """KeywordSuggestionDTO model"""
    url: str
    languageCode: Optional[str] = None
    locations: Optional[List[str]] = None
    keywords: Optional[List[str]] = None

class UpsertAssetsDTO(BaseModel):
    """UpsertAssetsDTO model"""
    locationId: str
    type: str
    payload: Any

class MemberDTO(BaseModel):
    """MemberDTO model"""
    memberType: str
    keyword: Optional[str] = None
    url: Optional[str] = None
    app: Optional[str] = None

class StringRuleItemDTO(BaseModel):
    """StringRuleItemDTO model"""
    operator: str
    value: str

class RuleItemDTO(BaseModel):
    """RuleItemDTO model"""
    name: str
    stringRuleItem: Any

class RuleItemGroupDTO(BaseModel):
    """RuleItemGroupDTO model"""
    ruleItems: List[RuleItemDTO]

class RuleDTO(BaseModel):
    """RuleDTO model"""
    ruleItemGroups: List[RuleItemGroupDTO]

class RuleOperandDTO(BaseModel):
    """RuleOperandDTO model"""
    lookbackWindowDays: float
    rule: Any

class FlexibleRuleUserListDTO(BaseModel):
    """FlexibleRuleUserListDTO model"""
    inclusiveRuleOperator: Optional[str] = None
    inclusiveOperands: List[RuleOperandDTO]
    exclusiveOperands: List[RuleOperandDTO]

class RuleBasedUserListDTO(BaseModel):
    """RuleBasedUserListDTO model"""
    prepopulationStatus: Optional[str] = None
    flexibleRuleUserList: Any

class UpsertSegmentDTO(BaseModel):
    """UpsertSegmentDTO model"""
    name: str
    description: Optional[str] = None
    members: Optional[List[MemberDTO]] = None
    status: Optional[str] = None
    type: Optional[str] = None
    id: Optional[str] = None
    membershipStatus: Optional[str] = None
    ruleBasedUserList: Optional[Any] = None
    membershipLifeSpan: Optional[float] = None
    seedUserListIds: Optional[List[str]] = None
    countryCodes: Optional[List[str]] = None
    expansionLevel: Optional[str] = None

class CreateOfflineUserListJobDTO(BaseModel):
    """CreateOfflineUserListJobDTO model"""
    locationId: str
    smartListIds: Optional[List[str]] = None
    csvPath: Optional[str] = None
    userListId: Optional[str] = None
    isDynamic: Optional[bool] = None

class AudienceSegmentsDTO(BaseModel):
    """AudienceSegmentsDTO model"""
    customAudiences: Optional[List[str]] = None
    userLists: Optional[List[str]] = None
    userInterests: Optional[List[str]] = None

class AudienceDimensionDTO(BaseModel):
    """AudienceDimensionDTO model"""
    isAgeUnknown: Optional[bool] = None
    ageRanges: Optional[List[str]] = None
    genders: Optional[List[str]] = None
    parentalStatuses: Optional[List[str]] = None
    audienceSegments: Optional[Any] = None

class UpsertAudienceDTO(BaseModel):
    """UpsertAudienceDTO model"""
    locationId: str
    resourceName: Optional[str] = None
    name: str
    dimensions: Optional[Any] = None
    exclusionDimension: Optional[Any] = None

class GoogleBudgetDTO(BaseModel):
    """GoogleBudgetDTO model"""
    budgetType: Optional[str] = None
    amount: Optional[float] = None
    scheduleStartDate: Optional[str] = None
    scheduleEndDate: Optional[str] = None

class GeoLatLngDTO(BaseModel):
    """GeoLatLngDTO model"""
    lat: Optional[float] = None
    lng: Optional[float] = None

class GeoViewportDTO(BaseModel):
    """GeoViewportDTO model"""
    northeast: Optional[Any] = None
    southwest: Optional[Any] = None

class GeoGeometryDTO(BaseModel):
    """GeoGeometryDTO model"""
    location: Optional[Any] = None
    locationType: Optional[str] = None
    viewport: Optional[Any] = None

class GeoAddressComponentDTO(BaseModel):
    """GeoAddressComponentDTO model"""
    longName: Optional[str] = None
    shortName: Optional[str] = None
    types: Optional[List[str]] = None

class GoogleGeoLocationDTO(BaseModel):
    """GoogleGeoLocationDTO model"""
    key: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    countryName: Optional[str] = None
    type: Optional[str] = None
    radius: Optional[float] = None
    radiusUnit: Optional[str] = None
    selectionType: Optional[str] = None
    resourceName: Optional[str] = None
    placeId: Optional[str] = None
    formattedAddress: Optional[str] = None
    geometry: Optional[Any] = None
    addressComponents: Optional[List[GeoAddressComponentDTO]] = None

class GoogleLocaleDTO(BaseModel):
    """GoogleLocaleDTO model"""
    name: Optional[str] = None
    key: Optional[str] = None
    id: Optional[str] = None
    resourceName: Optional[str] = None

class GoogleDemographicTargetDTO(BaseModel):
    """GoogleDemographicTargetDTO model"""
    enum: str
    negative: bool

class GoogleSegmentTargetDTO(BaseModel):
    """GoogleSegmentTargetDTO model"""
    type: str
    id: str

class GoogleTargetInterestsDTO(BaseModel):
    """GoogleTargetInterestsDTO model"""
    affinity: Optional[List[str]] = None
    inMarket: Optional[List[str]] = None

class GoogleCampaignAudienceDTO(BaseModel):
    """GoogleCampaignAudienceDTO model"""
    geoLocations: Optional[List[GoogleGeoLocationDTO]] = None
    locales: Optional[List[GoogleLocaleDTO]] = None
    gender: Optional[List[GoogleDemographicTargetDTO]] = None
    ageRange: Optional[List[GoogleDemographicTargetDTO]] = None
    segments: Optional[List[GoogleSegmentTargetDTO]] = None
    targetInterests: Optional[Any] = None

class GoogleNetworkSettingsDTO(BaseModel):
    """GoogleNetworkSettingsDTO model"""
    targetSearchNetwork: bool
    targetContentNetwork: bool

class GoogleBiddingStrategyDTO(BaseModel):
    """GoogleBiddingStrategyDTO model"""
    type: Optional[str] = None
    value: Optional[float] = None

class GoogleAssetImageDTO(BaseModel):
    """GoogleAssetImageDTO model"""
    url: str
    resourceName: Optional[str] = None
    name: Optional[str] = None
    error: Optional[str] = None

class GoogleAssetsDTO(BaseModel):
    """GoogleAssetsDTO model"""
    calls: Optional[List[str]] = None
    sitelinks: Optional[List[str]] = None
    leadForm: Optional[str] = None
    images: Optional[List[GoogleAssetImageDTO]] = None
    businessLogo: Optional[Any] = None

class GoogleMediaDTO(BaseModel):
    """GoogleMediaDTO model"""
    type: Optional[str] = None
    src: Optional[str] = None
    isLogo: Optional[bool] = None
    error: Optional[str] = None
    url: Optional[str] = None
    imageType: Optional[str] = None

class GoogleYouTubeVideoLinkDTO(BaseModel):
    """GoogleYouTubeVideoLinkDTO model"""
    youtubeVideoId: str

class GoogleCarouselCardDTO(BaseModel):
    """GoogleCarouselCardDTO model"""
    headline: Optional[str] = None
    finalUrl: Optional[str] = None
    callToActionLabel: Optional[str] = None
    media: Optional[List[GoogleMediaDTO]] = None

class GoogleAdContentDTO(BaseModel):
    """GoogleAdContentDTO model"""
    id: Optional[str] = None
    name: Optional[str] = None
    mediaType: Optional[str] = None
    headlines: Optional[List[str]] = None
    longHeadlines: Optional[List[str]] = None
    descriptions: Optional[List[str]] = None
    finalUrl: Optional[str] = None
    path1: Optional[str] = None
    path2: Optional[str] = None
    isDeleted: Optional[bool] = None
    adError: Optional[str] = None
    publishingStatus: Optional[str] = None
    adId: Optional[str] = None
    adCampaignId: Optional[str] = None
    adGroupId: Optional[str] = None
    googleAdId: Optional[str] = None
    media: Optional[List[GoogleMediaDTO]] = None
    callToActionLabel: Optional[str] = None
    businessName: Optional[str] = None
    youtubeVideoLinks: Optional[List[GoogleYouTubeVideoLinkDTO]] = None
    carouselCards: Optional[List[GoogleCarouselCardDTO]] = None
    placements: Optional[List[str]] = None
    customChannels: Optional[bool] = None

class GoogleKeywordItemDTO(BaseModel):
    """GoogleKeywordItemDTO model"""
    keyword: str
    matchType: str

class GoogleKeywordsDTO(BaseModel):
    """GoogleKeywordsDTO model"""
    positives: Optional[List[GoogleKeywordItemDTO]] = None
    negatives: Optional[List[GoogleKeywordItemDTO]] = None

class GoogleAdGroupAudienceDTO(BaseModel):
    """GoogleAdGroupAudienceDTO model"""
    geoLocations: Optional[List[GoogleGeoLocationDTO]] = None
    locales: Optional[List[GoogleLocaleDTO]] = None

class GoogleAdGroupDTO(BaseModel):
    """GoogleAdGroupDTO model"""
    id: Optional[str] = None
    adGroupId: Optional[str] = None
    name: Optional[str] = None
    adCampaignId: Optional[str] = None
    adContent: Optional[List[GoogleAdContentDTO]] = None
    keywords: Optional[Any] = None
    publishingStatus: Optional[str] = None
    adGroupError: Optional[str] = None
    googleAdGroupId: Optional[str] = None
    customChannels: Optional[bool] = None
    selectedChannels: Optional[List[str]] = None
    googleAudienceId: Optional[str] = None
    audience: Optional[Any] = None

class GoogleCampaignGoalDTO(BaseModel):
    """GoogleCampaignGoalDTO model"""
    type: str
    value: Optional[str] = None
    isCustomConversionGoal: Optional[bool] = None

class GoogleAdScheduleDTO(BaseModel):
    """GoogleAdScheduleDTO model"""
    dayOfWeek: str
    from_: str
    to: str

class CampaignDTO(BaseModel):
    """CampaignDTO model"""
    id: Optional[str] = None
    name: str
    locationId: str
    advertisingChannelType: str
    advertisingChannelSubType: Optional[str] = None
    goalType: Optional[str] = None
    budget: Optional[Any] = None
    audience: Optional[Any] = None
    networkSettings: Optional[Any] = None
    biddingStrategy: Optional[Any] = None
    assets: Optional[Any] = None
    isEuPoliticalAds: Optional[bool] = None
    adGroups: Optional[List[GoogleAdGroupDTO]] = None
    campaignGoal: Optional[Any] = None
    adSchedule: Optional[List[GoogleAdScheduleDTO]] = None
    publishingStatus: Optional[str] = None
    googleAdAccountId: Optional[str] = None
    unpublishedChanges: Optional[bool] = None
    maximumCpc: Optional[float] = None
    googleCampaignId: Optional[str] = None
    source: Optional[str] = None
    advancedOptions: Optional[Dict[str, Any]] = None

class CreateLinkedinIntegrationDTO(BaseModel):
    """CreateLinkedinIntegrationDTO model"""
    locationId: str
    adAccountId: str
    adAccountName: str
    currencyCode: str
    organizationId: str

class LinkedInBudgetDTO(BaseModel):
    """LinkedInBudgetDTO model"""
    budgetType: Optional[str] = None
    amount: Optional[float] = None
    scheduleStartDate: Optional[str] = None
    scheduleEndDate: Optional[str] = None

class LocaleDTO(BaseModel):
    """LocaleDTO model"""
    country: str
    language: str

class GeoLocationDTO(BaseModel):
    """GeoLocationDTO model"""
    name: str
    urn: str
    facetUrn: str
    selectionType: str

class SelectedAttributeDTO(BaseModel):
    """SelectedAttributeDTO model"""
    urn: str
    name: str
    categoryName: str
    facet: str

class TargetAudienceDTO(BaseModel):
    """TargetAudienceDTO model"""
    include: Optional[List[List[Any]]] = None
    exclude: Optional[List[List[Any]]] = None

class AudienceDTO(BaseModel):
    """AudienceDTO model"""
    geoLocations: Optional[List[GeoLocationDTO]] = None
    targetAudience: Optional[Any] = None

class UnitCostDTO(BaseModel):
    """UnitCostDTO model"""
    amount: float

class LinkedInMediaDTO(BaseModel):
    """LinkedInMediaDTO model"""
    type: Optional[str] = None
    src: Optional[str] = None
    frames: Optional[List[str]] = None
    selectedPoster: Optional[float] = None
    thumbnailUrl: Optional[str] = None
    name: Optional[str] = None
    headline: Optional[str] = None
    destinationUrl: Optional[str] = None
    fileSizeBytes: Optional[float] = None

class LinkedInAdDTO(BaseModel):
    """LinkedInAdDTO model"""
    id: Optional[str] = None
    name: Optional[str] = None
    introductoryText: Optional[str] = None
    destinationUrl: Optional[str] = None
    callToActionLabel: Optional[str] = None
    destinationFormId: Optional[str] = None
    contentReferenceString: Optional[str] = None
    media: Optional[List[LinkedInMediaDTO]] = None
    adCampaignId: Optional[str] = None
    adId: Optional[str] = None
    headline: Optional[str] = None
    publishingStatus: Optional[str] = None
    adCampaignGroupId: Optional[str] = None
    description: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    linkedInError: Optional[str] = None

class AdCampaignDTO(BaseModel):
    """AdCampaignDTO model"""
    id: Optional[str] = None
    locale: Optional[Any] = None
    name: Optional[str] = None
    publishingStatus: Optional[str] = None
    mediaType: Optional[str] = None
    audience: Optional[Any] = None
    unitCost: Optional[Any] = None
    campaignType: Optional[str] = None
    adCampaignGroupId: Optional[str] = None
    adCampaignId: Optional[str] = None
    ads: Optional[List[LinkedInAdDTO]] = None
    linkedInError: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None

class AdCampaignGroupDataDTO(BaseModel):
    """AdCampaignGroupDataDTO model"""
    id: Optional[str] = None
    locationId: str
    budget: Optional[Any] = None
    adCampaigns: Optional[List[AdCampaignDTO]] = None
    adBudgetOptimization: Optional[str] = None
    objectiveType: Optional[str] = None
    name: Optional[str] = None
    adCampaignGroupId: Optional[str] = None
    publishingStatus: Optional[str] = None
    linkedInAdAccountId: Optional[str] = None
    unpublishedChanges: Optional[bool] = None
    meta: Optional[Dict[str, Any]] = None
    linkedInError: Optional[str] = None

class SponsoredAccountOwnerDTO(BaseModel):
    """SponsoredAccountOwnerDTO model"""
    sponsoredAccount: str

class CreationLocaleDTO(BaseModel):
    """CreationLocaleDTO model"""
    country: str
    language: str

class LocalizedStringDTO(BaseModel):
    """LocalizedStringDTO model"""
    localized: Dict[str, Any]

class MultipleChoiceOptionDTO(BaseModel):
    """MultipleChoiceOptionDTO model"""
    id: float
    text: Any

class MultipleChoiceQuestionDetailsDTO(BaseModel):
    """MultipleChoiceQuestionDetailsDTO model"""
    options: List[MultipleChoiceOptionDTO]

class QuestionDetailsDTO(BaseModel):
    """QuestionDetailsDTO model"""
    textQuestionDetails: Optional[Dict[str, Any]] = None
    multipleChoiceQuestionDetails: Optional[Any] = None

class LeadFormQuestionDTO(BaseModel):
    """LeadFormQuestionDTO model"""
    question: Any
    name: str
    questionDetails: Any
    predefinedField: Optional[str] = None

class PostSubmissionCallToActionTargetDTO(BaseModel):
    """PostSubmissionCallToActionTargetDTO model"""
    landingPageUrl: str

class PostSubmissionCallToActionDTO(BaseModel):
    """PostSubmissionCallToActionDTO model"""
    callToActionTarget: Any
    callToActionLabel: str

class PostSubmissionInfoDTO(BaseModel):
    """PostSubmissionInfoDTO model"""
    message: Any
    callToAction: Any

class ConsentDTO(BaseModel):
    """ConsentDTO model"""
    checkRequired: bool
    id: float
    consent: Any

class LegalInfoDTO(BaseModel):
    """LegalInfoDTO model"""
    consents: List[ConsentDTO]
    privacyPolicyUrl: str
    legalDisclaimer: Optional[Any] = None

class LeadFormContentDTO(BaseModel):
    """LeadFormContentDTO model"""
    questions: List[LeadFormQuestionDTO]
    description: Optional[Any] = None
    headline: Any
    postSubmissionInfo: Any
    legalInfo: Any

class HiddenFieldDTO(BaseModel):
    """HiddenFieldDTO model"""
    name: str
    value: str

class LinkedInCreateLeadFormBodyDTO(BaseModel):
    """LinkedInCreateLeadFormBodyDTO model"""
    owner: Any
    creationLocale: Any
    name: str
    state: str
    content: Any
    hiddenFields: Optional[List[HiddenFieldDTO]] = None

class LinkedInUpdateAdStatusBodyDTO(BaseModel):
    """LinkedInUpdateAdStatusBodyDTO model"""
    operationType: str
    type: str

