# @generated
# File generated from our OpenAPI spec

from __future__ import annotations

# SocialPlanner Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class BaseOAuthAccountSchema(BaseModel):
    """BaseOAuthAccountSchema model"""
    name: str
    originId: str
    avatar: Optional[str] = None

class GoogleLocationSchema(BaseModel):
    """GoogleLocationSchema model"""
    name: Optional[str] = None
    storeCode: Optional[str] = None
    title: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    storefrontAddress: Optional[Dict[str, Any]] = None
    relationshipData: Optional[Dict[str, Any]] = None
    maxLocation: Optional[bool] = None
    isVerified: Optional[bool] = None
    isConnected: Optional[bool] = None

class GoogleAccountsSchema(BaseModel):
    """GoogleAccountsSchema model"""
    name: Optional[str] = None
    accountName: Optional[str] = None
    type: Optional[str] = None
    verificationState: Optional[str] = None
    vettedState: Optional[str] = None

class GetGoogleLocationSchema(BaseModel):
    """GetGoogleLocationSchema model"""
    location: Optional[Any] = None
    account: Optional[Any] = None

class GetGoogleLocationAccountSchema(BaseModel):
    """GetGoogleLocationAccountSchema model"""
    locations: Optional[Any] = None

class GetGoogleLocationResponseDTO(BaseModel):
    """GetGoogleLocationResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class AttachGMBLocationDTO(BaseModel):
    """AttachGMBLocationDTO model"""
    location: Dict[str, Any]
    account: Dict[str, Any]

class AttachGMBLocationLocationDTO(BaseModel):
    """AttachGMBLocationLocationDTO model"""
    name: str
    storeCode: Optional[str] = None
    title: str
    storefrontAddress: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    maxLocation: Optional[bool] = None
    isVerified: Optional[bool] = None
    isConnected: Optional[bool] = None

class AttachGMBLocationAccountDTO(BaseModel):
    """AttachGMBLocationAccountDTO model"""
    name: str
    accountName: str
    type: str
    verificationState: str
    vettedState: str

class SocialGoogleMediaAccountSchema(BaseModel):
    """SocialGoogleMediaAccountSchema model"""
    _id: Optional[str] = None
    oAuthId: Optional[str] = None
    oldId: Optional[str] = None
    locationId: Optional[str] = None
    originId: Optional[str] = None
    platform: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    active: Optional[bool] = None
    deleted: Optional[bool] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class SocialMediaGmbAccountResponseDTO(BaseModel):
    """SocialMediaGmbAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class SearchPostDTO(BaseModel):
    """SearchPostDTO model"""
    type: Optional[str] = None
    accounts: Optional[str] = None
    skip: str
    limit: str
    fromDate: str
    toDate: str
    includeUsers: str
    postType: Optional[Dict[str, Any]] = None

class PostMediaSchema(BaseModel):
    """PostMediaSchema model"""
    url: str
    caption: Optional[str] = None
    originalUrl: Optional[str] = None
    watermarkedUrl: Optional[str] = None
    type: str
    thumbnail: Optional[str] = None
    id: Optional[str] = None
    optimizedUrl: Optional[str] = None
    optimizedType: Optional[str] = None
    isModified: Optional[bool] = None
    altText: Optional[str] = None

class OgTagsSchema(BaseModel):
    """OgTagsSchema model"""
    metaImage: Optional[str] = None
    metaLink: Optional[str] = None
    ogTitle: Optional[str] = None
    ogDescription: Optional[str] = None

class PostUserSchema(BaseModel):
    """PostUserSchema model"""
    id: str
    title: str
    firstName: str
    lastName: str
    profilePhoto: str
    phone: str
    email: str

class FormatedApprovalDetails(BaseModel):
    """FormatedApprovalDetails model"""
    approver: Optional[str] = None
    requesterNote: Optional[str] = None
    approverNote: Optional[str] = None
    approvalStatus: Optional[str] = None
    approverUser: Optional[Any] = None

class TiktokPostSchema(BaseModel):
    """TiktokPostSchema model"""
    privacyLevel: str
    promoteOtherBrand: Optional[bool] = None
    enableComment: Optional[bool] = None
    enableDuet: Optional[bool] = None
    enableStitch: Optional[bool] = None
    videoDisclosure: Optional[bool] = None
    promoteYourBrand: Optional[bool] = None

class DateSchema(BaseModel):
    """DateSchema model"""
    year: float
    month: float
    day: float

class TimeSchema(BaseModel):
    """TimeSchema model"""
    hours: float
    minutes: float
    seconds: float

class StartDateSchema(BaseModel):
    """StartDateSchema model"""
    startDate: Optional[Any] = None
    startTime: Optional[Any] = None

class EndDateSchema(BaseModel):
    """EndDateSchema model"""
    endDate: Optional[Any] = None
    endTime: Optional[Any] = None

class GMBPostSchema(BaseModel):
    """GMBPostSchema model"""
    gmbEventType: str
    title: Optional[str] = None
    offerTitle: Optional[str] = None
    startDate: Optional[Any] = None
    endDate: Optional[Any] = None
    termsConditions: Optional[str] = None
    url: Optional[str] = None
    couponCode: Optional[str] = None
    redeemOnlineUrl: Optional[str] = None
    actionType: Optional[str] = None

class BlueskyPostSchema(BaseModel):
    """BlueskyPostSchema model"""
    shortenedLinks: Optional[List[str]] = None
    replyTo: Optional[str] = None
    quotePost: Optional[str] = None
    language: Optional[str] = None
    externalLink: Optional[str] = None
    externalLinkTitle: Optional[str] = None
    externalLinkDescription: Optional[str] = None

class LinkedinPollOptionDto(BaseModel):
    """LinkedinPollOptionDto model"""
    text: str

class LinkedinPollSettingsDto(BaseModel):
    """LinkedinPollSettingsDto model"""
    duration: str

class LinkedinPollDto(BaseModel):
    """LinkedinPollDto model"""
    question: str
    options: List[LinkedinPollOptionDto]
    settings: Any

class LinkedinPostSchema(BaseModel):
    """LinkedinPostSchema model"""
    pdfTitle: str
    postAsPdf: bool
    poll: Optional[Any] = None

class PinterestBoardSelection(BaseModel):
    """PinterestBoardSelection model"""
    accountId: str
    boards: List[str]

class PinterestPostSchema(BaseModel):
    """PinterestPostSchema model"""
    title: Optional[str] = None
    link: Optional[str] = None
    boardIds: Optional[Dict[str, Any]] = None
    pinterestBoards: Optional[List[PinterestBoardSelection]] = None
    shortenedLinks: Optional[List[str]] = None

class FacebookPostSchema(BaseModel):
    """FacebookPostSchema model"""
    type: str
    textFormatPresetId: Optional[str] = None

class InstagramPostSchema(BaseModel):
    """InstagramPostSchema model"""
    type: str
    collaborators: Optional[Dict[str, Any]] = None
    showOnFeed: Optional[bool] = None
    publishViaPushNotification: Optional[bool] = None
    publisherNote: Optional[str] = None

class YoutubePostSchema(BaseModel):
    """YoutubePostSchema model"""
    title: Optional[str] = None
    privacyLevel: Optional[str] = None
    type: str

class GetPostFormattedSchema(BaseModel):
    """GetPostFormattedSchema model"""
    _id: Optional[str] = None
    source: Optional[str] = None
    locationId: str
    platform: Optional[str] = None
    thumbnail: Optional[str] = None
    displayDate: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    accountId: Optional[str] = None
    error: str
    postId: Optional[str] = None
    publishedAt: Optional[str] = None
    accountIds: Optional[List[str]] = None
    summary: Optional[str] = None
    media: Optional[List[PostMediaSchema]] = None
    status: Optional[Dict[str, Any]] = None
    createdBy: Optional[str] = None
    type: Dict[str, Any]
    tags: Optional[List[str]] = None
    ogTagsDetails: Optional[Any] = None
    postApprovalDetails: Optional[Any] = None
    tiktokPostDetails: Optional[Any] = None
    gmbPostDetails: Optional[Any] = None
    blueskyPostDetails: Optional[Any] = None
    user: Optional[Any] = None
    linkedinPostDetails: Optional[Any] = None
    pinterestPostDetails: Optional[Any] = None
    facebookPostDetails: Optional[Any] = None
    instagramPostDetails: Optional[Any] = None
    youtubePostDetails: Optional[Any] = None
    mediaOptimization: Optional[bool] = None
    insights: Optional[Any] = None

class PostInsightsSchema(BaseModel):
    """PostInsightsSchema model"""
    like: Optional[float] = None
    share: Optional[float] = None
    comment: Optional[float] = None

class PostSuccessfulResponseSchema(BaseModel):
    """PostSuccessfulResponseSchema model"""
    posts: Optional[List[GetPostFormattedSchema]] = None
    count: Optional[float] = None

class PostSuccessfulResponseDTO(BaseModel):
    """PostSuccessfulResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class PostApprovalSchema(BaseModel):
    """PostApprovalSchema model"""
    approver: Optional[str] = None
    requesterNote: Optional[str] = None
    approverNote: Optional[str] = None
    approvalStatus: Optional[str] = None

class CreatePostDTO(BaseModel):
    """CreatePostDTO model"""
    accountIds: List[str]
    summary: Optional[str] = None
    media: Optional[List[PostMediaSchema]] = None
    status: Optional[str] = None
    scheduleDate: Optional[str] = None
    selectedBestTime: Optional[str] = None
    createdBy: Optional[str] = None
    followUpComment: Optional[str] = None
    ogTagsDetails: Optional[Any] = None
    type: str
    postApprovalDetails: Optional[Any] = None
    scheduleTimeUpdated: Optional[bool] = None
    tags: Optional[List[str]] = None
    categoryId: Optional[str] = None
    applyWatermark: Optional[bool] = None
    tiktokPostDetails: Optional[Any] = None
    gmbPostDetails: Optional[Any] = None
    userId: str
    linkedinPostDetails: Optional[Any] = None
    pinterestPostDetails: Optional[Any] = None
    facebookPostDetails: Optional[Any] = None
    instagramPostDetails: Optional[Any] = None
    youtubePostDetails: Optional[Any] = None

class CreatePostSuccessfulResponseSchema(BaseModel):
    """CreatePostSuccessfulResponseSchema model"""
    post: Optional[Any] = None

class CreatePostSuccessfulResponseDTO(BaseModel):
    """CreatePostSuccessfulResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class GetPostSuccessfulResponseSchema(BaseModel):
    """GetPostSuccessfulResponseSchema model"""
    post: Optional[Any] = None

class GetPostSuccessfulResponseDTO(BaseModel):
    """GetPostSuccessfulResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class PostCreateRequest(BaseModel):
    """PostCreateRequest model"""
    accountIds: Optional[List[str]] = None
    summary: Optional[str] = None
    media: Optional[List[PostMediaSchema]] = None
    status: Optional[Dict[str, Any]] = None
    scheduleDate: Optional[str] = None
    createdBy: Optional[str] = None
    followUpComment: Optional[str] = None
    ogTagsDetails: Optional[Any] = None
    type: Dict[str, Any]
    postApprovalDetails: Optional[Any] = None
    scheduleTimeUpdated: Optional[bool] = None
    tags: Optional[List[str]] = None
    categoryId: Optional[str] = None
    tiktokPostDetails: Optional[Any] = None
    gmbPostDetails: Optional[Any] = None
    userId: Optional[str] = None

class UpdatePostSuccessfulResponseDTO(BaseModel):
    """UpdatePostSuccessfulResponseDTO model"""
    success: bool
    statusCode: float
    message: str

class DeletePostSuccessfulResponseSchema(BaseModel):
    """DeletePostSuccessfulResponseSchema model"""
    postId: Optional[str] = None

class DeletePostSuccessfulResponseDTO(BaseModel):
    """DeletePostSuccessfulResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class GetAccountSchema(BaseModel):
    """GetAccountSchema model"""
    id: Optional[str] = None
    oauthId: Optional[str] = None
    profileId: Optional[str] = None
    name: Optional[str] = None
    platform: Optional[str] = None
    type: Optional[str] = None
    expire: Optional[str] = None
    isExpired: Optional[bool] = None
    meta: Optional[Dict[str, Any]] = None

class GetGroupSchema(BaseModel):
    """GetGroupSchema model"""
    id: str
    name: str
    accountIds: List[str]

class AccountsListResponseSchema(BaseModel):
    """AccountsListResponseSchema model"""
    accounts: Optional[List[GetAccountSchema]] = None
    groups: Optional[List[GetGroupSchema]] = None

class AccountsListResponseDTO(BaseModel):
    """AccountsListResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class DeleteAccountResponseSchema(BaseModel):
    """DeleteAccountResponseSchema model"""
    locationId: Optional[str] = None
    id: Optional[str] = None

class LocationAndAccountDeleteResponseDTO(BaseModel):
    """LocationAndAccountDeleteResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class FacebookPageSchema(BaseModel):
    """FacebookPageSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    isOwned: Optional[bool] = None
    isConnected: Optional[bool] = None

class GetFacebookAccountsSchema(BaseModel):
    """GetFacebookAccountsSchema model"""
    pages: Optional[List[FacebookPageSchema]] = None

class GetFacebookAccountsResponseDTO(BaseModel):
    """GetFacebookAccountsResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class AttachFBAccountDTO(BaseModel):
    """AttachFBAccountDTO model"""
    type: str
    originId: str
    name: str
    avatar: str

class SocialMediaFacebookAccountSchema(BaseModel):
    """SocialMediaFacebookAccountSchema model"""
    _id: Optional[str] = None
    oAuthId: Optional[str] = None
    oldId: Optional[str] = None
    locationId: Optional[str] = None
    originId: Optional[str] = None
    platform: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    active: Optional[bool] = None
    deleted: Optional[bool] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class SocialMediaFBAccountResponseDTO(BaseModel):
    """SocialMediaFBAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class InstagramAccountSchema(BaseModel):
    """InstagramAccountSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    pageId: Optional[str] = None
    isConnected: Optional[bool] = None

class GetInstagramAccountsSchema(BaseModel):
    """GetInstagramAccountsSchema model"""
    accounts: Optional[List[InstagramAccountSchema]] = None

class GetInstagramAccountsResponseDTO(BaseModel):
    """GetInstagramAccountsResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class AttachIGAccountDTO(BaseModel):
    """AttachIGAccountDTO model"""
    originId: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    pageId: str

class SocialMediaInstagramAccountSchema(BaseModel):
    """SocialMediaInstagramAccountSchema model"""
    _id: Optional[str] = None
    oAuthId: Optional[str] = None
    oldId: Optional[str] = None
    locationId: Optional[str] = None
    originId: Optional[str] = None
    platform: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    active: Optional[bool] = None
    deleted: Optional[bool] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class SocialMediaInstagramAccountResponseDTO(BaseModel):
    """SocialMediaInstagramAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class LinkedInPageSchema(BaseModel):
    """LinkedInPageSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    urn: Optional[str] = None
    isConnected: Optional[bool] = None

class LinkedInProfileSchema(BaseModel):
    """LinkedInProfileSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    urn: Optional[str] = None
    isConnected: Optional[bool] = None

class GetLinkedInAccountSchema(BaseModel):
    """GetLinkedInAccountSchema model"""
    pages: Optional[List[LinkedInPageSchema]] = None
    profile: Optional[List[LinkedInProfileSchema]] = None

class GetLinkedInAccountsResponseDTO(BaseModel):
    """GetLinkedInAccountsResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class AttachLinkedinAccountDTO(BaseModel):
    """AttachLinkedinAccountDTO model"""
    type: str
    originId: str
    name: str
    avatar: str
    urn: str

class SocialMediaLinkedInAccountSchema(BaseModel):
    """SocialMediaLinkedInAccountSchema model"""
    _id: Optional[str] = None
    oAuthId: Optional[str] = None
    oldId: Optional[str] = None
    locationId: Optional[str] = None
    originId: Optional[str] = None
    platform: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    active: Optional[bool] = None
    deleted: Optional[bool] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class SocialMediaLinkedInAccountResponseDTO(BaseModel):
    """SocialMediaLinkedInAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class TwitterProfileSchema(BaseModel):
    """TwitterProfileSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    username: Optional[str] = None
    avatar: Optional[str] = None
    protected: Optional[bool] = None
    verified: Optional[bool] = None
    isConnected: Optional[bool] = None

class GetTwitterAccountsSchema(BaseModel):
    """GetTwitterAccountsSchema model"""
    profile: Optional[List[TwitterProfileSchema]] = None

class GetTwitterAccountsResponseDTO(BaseModel):
    """GetTwitterAccountsResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class AttachTwitterAccountDTO(BaseModel):
    """AttachTwitterAccountDTO model"""
    originId: Optional[str] = None
    name: Optional[str] = None
    username: Optional[str] = None
    avatar: Optional[str] = None
    protected: Optional[bool] = None
    verified: Optional[bool] = None
    companyId: Optional[str] = None

class SocialMediaTwitterAccountSchema(BaseModel):
    """SocialMediaTwitterAccountSchema model"""
    _id: Optional[str] = None
    oAuthId: Optional[str] = None
    oldId: Optional[str] = None
    locationId: Optional[str] = None
    originId: Optional[str] = None
    platform: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    active: Optional[bool] = None
    deleted: Optional[bool] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class SocialMediaTwitterAccountResponseDTO(BaseModel):
    """SocialMediaTwitterAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class UploadCSVDTO(BaseModel):
    """UploadCSVDTO model"""
    file: Optional[str] = None

class UploadFileResponseSchema(BaseModel):
    """UploadFileResponseSchema model"""
    filePath: Optional[str] = None
    rowsCount: Optional[float] = None
    fileName: Optional[str] = None
    fileSize: Optional[float] = None
    csvFileType: Optional[str] = None

class UploadFileResponseDTO(BaseModel):
    """UploadFileResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class SetAccountsDTO(BaseModel):
    """SetAccountsDTO model"""
    accountIds: List[str]
    filePath: str
    rowsCount: float
    fileName: str
    approver: Optional[str] = None
    userId: str
    csvFileType: Optional[str] = None

class SetAccountsResultSchema(BaseModel):
    """SetAccountsResultSchema model"""
    csvId: str

class SetAccountsResponseDTO(BaseModel):
    """SetAccountsResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class SetAccountsUnprocessableDTO(BaseModel):
    """SetAccountsUnprocessableDTO model"""
    status: float
    options: Optional[Dict[str, Any]] = None
    message: List[str]
    name: str
    error: str
    statusCode: float
    traceId: Optional[str] = None

class CSVFileRequiredBadRequestDTO(BaseModel):
    """CSVFileRequiredBadRequestDTO model"""
    status: float
    options: Optional[Dict[str, Any]] = None
    message: str
    name: str
    error: str
    statusCode: float
    traceId: Optional[str] = None

class CSVErrorResponseDTO(BaseModel):
    """CSVErrorResponseDTO model"""
    code: str
    message: str
    fileType: Optional[str] = None
    csvFileType: Optional[str] = None
    missingHeaders: Optional[str] = None

class CSVImportSchema(BaseModel):
    """CSVImportSchema model"""
    id: Optional[str] = None
    locationId: Optional[str] = None
    fileName: Optional[str] = None
    accountIds: Optional[List[str]] = None
    file: Optional[str] = None
    status: Optional[str] = None
    count: Optional[float] = None
    createdBy: Optional[str] = None
    traceId: Optional[str] = None
    originId: Optional[str] = None
    approver: Optional[str] = None
    createdAt: Optional[str] = None
    csvFileType: Optional[str] = None
    mediaOptimization: Optional[bool] = None
    applyWatermark: Optional[bool] = None
    channel: Optional[str] = None
    updatedAt: Optional[str] = None

class GetUploadStatusResponseSchema(BaseModel):
    """GetUploadStatusResponseSchema model"""
    csvs: List[CSVImportSchema]
    count: float

class GetUploadStatusResponseDTO(BaseModel):
    """GetUploadStatusResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class OgImageSchema(BaseModel):
    """OgImageSchema model"""
    url: Optional[str] = None
    width: Optional[float] = None
    height: Optional[float] = None
    type: Optional[str] = None

class IOgTagsSchema(BaseModel):
    """IOgTagsSchema model"""
    url: Optional[str] = None
    ogDescription: Optional[str] = None
    ogImage: Optional[Any] = None
    ogTitle: Optional[str] = None
    ogUrl: Optional[str] = None
    ogSiteName: Optional[str] = None
    error: Optional[str] = None

class CSVMediaResponseSchema(BaseModel):
    """CSVMediaResponseSchema model"""
    url: Optional[str] = None
    type: Optional[str] = None
    size: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    aspectRatio: Optional[float] = None
    duration: Optional[float] = None
    format: Optional[str] = None
    videoCodecName: Optional[str] = None
    frameRate: Optional[float] = None
    audioCodecName: Optional[str] = None
    audioChannels: Optional[float] = None
    displayAspectRatio: Optional[str] = None
    frames: Optional[List[str]] = None
    selectedPoster: Optional[float] = None
    error: Optional[str] = None
    instagramError: Optional[str] = None
    gmbError: Optional[str] = None
    facebookError: Optional[str] = None
    linkedinError: Optional[str] = None
    twitterError: Optional[str] = None
    tiktokError: Optional[str] = None
    tiktokBusinessError: Optional[str] = None
    invalidError: Optional[str] = None

class CSVPostSchema(BaseModel):
    """CSVPostSchema model"""
    accountIds: Optional[List[str]] = None
    link: Optional[Any] = None
    medias: Optional[List[CSVMediaResponseSchema]] = None
    scheduleDate: Optional[str] = None
    summary: Optional[str] = None
    followUpComment: Optional[str] = None
    type: Optional[str] = None
    tiktokPostDetails: Optional[Any] = None
    gmbPostDetails: Optional[Any] = None
    errorMessage: Optional[str] = None
    csvFileType: Optional[str] = None
    mediaOptimization: Optional[bool] = None
    applyWatermark: Optional[bool] = None
    status: Optional[str] = None
    updatedAt: Optional[str] = None

class GetCsvPostResponseSchema(BaseModel):
    """GetCsvPostResponseSchema model"""
    csv: Optional[Any] = None
    count: Optional[float] = None
    posts: Optional[List[CSVPostSchema]] = None

class GetCsvPostResponseDTO(BaseModel):
    """GetCsvPostResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class CSVDefaultDTO(BaseModel):
    """CSVDefaultDTO model"""
    userId: str

class CsvPostStatusResponseDTO(BaseModel):
    """CsvPostStatusResponseDTO model"""
    success: bool
    statusCode: float
    message: str

class CsvResponse(BaseModel):
    """CsvResponse model"""
    locationId: Optional[str] = None
    fileName: Optional[str] = None
    accountIds: Optional[List[str]] = None
    file: Optional[str] = None
    status: Optional[str] = None
    count: Optional[float] = None
    createdBy: Optional[str] = None
    traceId: Optional[str] = None
    originId: Optional[str] = None
    approver: Optional[str] = None
    csvFileType: Optional[str] = None
    mediaOptimization: Optional[bool] = None
    applyWatermark: Optional[bool] = None
    updatedAt: Optional[str] = None

class CSVResponseSchema(BaseModel):
    """CSVResponseSchema model"""
    csv: Optional[Any] = None

class DeleteCsvResponseDTO(BaseModel):
    """DeleteCsvResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class DeletePostCsvSchema(BaseModel):
    """DeletePostCsvSchema model"""
    _id: Optional[str] = None
    csvFileType: Optional[str] = None
    mediaOptimization: Optional[bool] = None
    applyWatermark: Optional[bool] = None
    status: Optional[str] = None
    updatedAt: Optional[str] = None

class DeletePostResponseSchema(BaseModel):
    """DeletePostResponseSchema model"""
    postId: str
    csv: Optional[Any] = None

class DeletePostResponseDTO(BaseModel):
    """DeletePostResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class TiktokProfileSchema(BaseModel):
    """TiktokProfileSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    username: Optional[str] = None
    avatar: Optional[str] = None
    verified: Optional[bool] = None
    isConnected: Optional[bool] = None
    type: Optional[Dict[str, Any]] = None

class GetTiktokAccountSchema(BaseModel):
    """GetTiktokAccountSchema model"""
    profile: Optional[List[TiktokProfileSchema]] = None

class GetTiktokAccountResponseDTO(BaseModel):
    """GetTiktokAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class AttachTiktokAccountDTO(BaseModel):
    """AttachTiktokAccountDTO model"""
    type: str
    originId: str
    name: str
    avatar: str
    verified: Optional[bool] = None
    username: Optional[str] = None

class SocialMediaTiktokAccountSchema(BaseModel):
    """SocialMediaTiktokAccountSchema model"""
    _id: Optional[str] = None
    oAuthId: Optional[str] = None
    oldId: Optional[str] = None
    locationId: Optional[str] = None
    originId: Optional[str] = None
    platform: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    active: Optional[bool] = None
    deleted: Optional[bool] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class SocialMediaTiktokAccountResponseDTO(BaseModel):
    """SocialMediaTiktokAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class TikTokOAuthAccountSchema(BaseModel):
    """TikTokOAuthAccountSchema model"""

class GetTiktokBusinessAccountSchema(BaseModel):
    """GetTiktokBusinessAccountSchema model"""
    profile: Optional[List[TiktokProfileSchema]] = None

class GetTiktokBusinessAccountResponseDTO(BaseModel):
    """GetTiktokBusinessAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class YouTubeOAuthAccountSchema(BaseModel):
    """YouTubeOAuthAccountSchema model"""

class YoutubeProfileSchema(BaseModel):
    """YoutubeProfileSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    username: Optional[str] = None
    avatar: Optional[str] = None
    verified: Optional[bool] = None
    isConnected: Optional[bool] = None
    type: Optional[str] = None

class GetYoutubeAccountSchema(BaseModel):
    """GetYoutubeAccountSchema model"""
    profile: Optional[List[YoutubeProfileSchema]] = None

class GetYouTubeAccountsResponseDTO(BaseModel):
    """GetYouTubeAccountsResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class AttachYoutubeAccountResponseDTO(BaseModel):
    """AttachYoutubeAccountResponseDTO model"""
    type: str
    originId: str
    name: str
    avatar: str
    verified: Optional[bool] = None
    username: Optional[str] = None

class PinterestOAuthAccountSchema(BaseModel):
    """PinterestOAuthAccountSchema model"""

class SocialMediaThreadsAccountSchema(BaseModel):
    """SocialMediaThreadsAccountSchema model"""

class PinterestProfileSchema(BaseModel):
    """PinterestProfileSchema model"""
    id: Optional[str] = None
    name: Optional[str] = None
    username: Optional[str] = None
    avatar: Optional[str] = None
    isConnected: Optional[bool] = None
    type: Optional[str] = None
    websiteUrl: Optional[str] = None

class GetPinterestAccountSchema(BaseModel):
    """GetPinterestAccountSchema model"""
    profile: Optional[List[PinterestProfileSchema]] = None

class GetPinterestAccountsResponseDTO(BaseModel):
    """GetPinterestAccountsResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class AttachPinterestAccountDTO(BaseModel):
    """AttachPinterestAccountDTO model"""
    originId: str
    name: Optional[str] = None
    avatar: Optional[str] = None
    verified: Optional[bool] = None
    username: Optional[str] = None
    websiteUrl: Optional[str] = None
    companyId: Optional[str] = None
    type: Optional[str] = None
    originAccountType: Optional[str] = None

class AttachThreadsAccountDTO(BaseModel):
    """AttachThreadsAccountDTO model"""
    type: str
    originId: str
    name: str
    avatar: str

class SocialMediaTiktokBusinessAccountResponseDTO(BaseModel):
    """SocialMediaTiktokBusinessAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class SocialMediaYouTubeAccountResponseDTO(BaseModel):
    """SocialMediaYouTubeAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class SocialMediaPinterestAccountResponseDTO(BaseModel):
    """SocialMediaPinterestAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class SocialMediaThreadsAccountResponseDTO(BaseModel):
    """SocialMediaThreadsAccountResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class CategorySchema(BaseModel):
    """CategorySchema model"""
    name: Optional[str] = None
    primaryColor: Optional[str] = None
    secondaryColor: Optional[str] = None
    locationId: Optional[str] = None
    _id: Optional[str] = None
    createdBy: Optional[str] = None
    deleted: bool
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class GetByLocationIdResponseSchema(BaseModel):
    """GetByLocationIdResponseSchema model"""
    count: float
    categories: List[CategorySchema]

class GetByLocationIdResponseDTO(BaseModel):
    """GetByLocationIdResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class GetByIdResponseSchema(BaseModel):
    """GetByIdResponseSchema model"""
    name: Optional[str] = None
    primaryColor: Optional[str] = None
    secondaryColor: Optional[str] = None
    locationId: Optional[str] = None
    _id: Optional[str] = None
    createdBy: Optional[str] = None
    deleted: bool
    message: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class GetCategorySchema(BaseModel):
    """GetCategorySchema model"""
    category: Optional[Any] = None

class GetByIdResponseDTO(BaseModel):
    """GetByIdResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class SocialMediaTagSchema(BaseModel):
    """SocialMediaTagSchema model"""
    tag: Optional[str] = None
    locationId: Optional[str] = None
    _id: Optional[str] = None
    createdBy: Optional[str] = None
    deleted: Optional[bool] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class GetTagsByLocationIdResponseSchema(BaseModel):
    """GetTagsByLocationIdResponseSchema model"""
    tags: Optional[List[SocialMediaTagSchema]] = None
    count: Optional[float] = None

class GetTagsByLocationIdResponseDTO(BaseModel):
    """GetTagsByLocationIdResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class UpdateTagDTO(BaseModel):
    """UpdateTagDTO model"""
    tagIds: List[str]

class GetTagsByIdResponseSchema(BaseModel):
    """GetTagsByIdResponseSchema model"""
    tags: List[SocialMediaTagSchema]
    count: Optional[float] = None

class GetTagsByIdResponseDTO(BaseModel):
    """GetTagsByIdResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class DeletePostsDto(BaseModel):
    """DeletePostsDto model"""
    postIds: Optional[List[str]] = None

class BulkDeletePostSuccessfulResponseSchema(BaseModel):
    """BulkDeletePostSuccessfulResponseSchema model"""
    deletedCount: Optional[float] = None

class BulkDeleteResponseDto(BaseModel):
    """BulkDeleteResponseDto model"""
    success: bool
    statusCode: float
    message: str
    results: Any

class AvailableCategoryQueueDetailsDTO(BaseModel):
    """AvailableCategoryQueueDetailsDTO model"""
    queueId: Optional[str] = None
    prioritizeNewContent: Optional[bool] = None
    enableFuturePosts: Optional[bool] = None

class AvailableCategoryDTO(BaseModel):
    """AvailableCategoryDTO model"""
    deleted: Optional[bool] = None
    _id: Optional[str] = None
    name: Optional[str] = None
    locationId: Optional[str] = None
    primaryColor: Optional[str] = None
    secondaryColor: Optional[str] = None
    createdBy: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    publishedPostsCount: Optional[float] = None
    status: Optional[str] = None
    queueDetails: Optional[Any] = None

class MetaDTO(BaseModel):
    """MetaDTO model"""
    count: Optional[str] = None

class FetchAvailableCategoriesResponseDTO(BaseModel):
    """FetchAvailableCategoriesResponseDTO model"""
    message: Optional[str] = None
    categories: Optional[List[AvailableCategoryDTO]] = None
    meta: Optional[MetaDTO] = None

class WrappedFetchAvailableCategoriesResponseDTO(BaseModel):
    """WrappedFetchAvailableCategoriesResponseDTO model"""
    success: bool
    statusCode: float
    results: FetchAvailableCategoriesResponseDTO
    traceId: Optional[str] = None

class TimeSlotDTO(BaseModel):
    """TimeSlotDTO model"""
    dayOfWeek: float
    time: str

class CreateCategoryQueueDTO(BaseModel):
    """CreateCategoryQueueDTO model"""
    locationId: str
    categoryId: str
    timeSlots: List[TimeSlotDTO]
    enableFuturePosts: Optional[bool] = None
    prioritizeNewContent: Optional[bool] = None
    userId: str

class CreatedTimeSlotDTO(BaseModel):
    """CreatedTimeSlotDTO model"""
    _id: Optional[str] = None
    dayOfWeek: Optional[float] = None
    time: Optional[str] = None

class CreatedCategoryQueueDTO(BaseModel):
    """CreatedCategoryQueueDTO model"""
    _id: Optional[str] = None
    locationId: Optional[str] = None
    categoryId: Optional[str] = None
    timeSlots: Optional[List[CreatedTimeSlotDTO]] = None
    enableFuturePosts: Optional[bool] = None
    prioritizeNewContent: Optional[bool] = None
    status: Optional[str] = None
    startDate: Optional[str] = None
    skipDateTime: Optional[List[str]] = None
    totalPosts: Optional[float] = None
    lastScheduledTime: Optional[str] = None
    createdBy: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class CreateCategoryQueueResponseDTO(BaseModel):
    """CreateCategoryQueueResponseDTO model"""
    message: Optional[str] = None
    queue: Optional[Any] = None

class WrappedCreateCategoryQueueResponseDTO(BaseModel):
    """WrappedCreateCategoryQueueResponseDTO model"""
    success: bool
    statusCode: float
    results: CreateCategoryQueueResponseDTO
    traceId: Optional[str] = None

class FetchCategoryQueuesDTO(BaseModel):
    """FetchCategoryQueuesDTO model"""
    locationId: str
    skip: Optional[float] = None
    limit: Optional[float] = None

class CategoryInfoDTO(BaseModel):
    """CategoryInfoDTO model"""
    _id: Optional[str] = None
    name: Optional[str] = None
    primaryColor: Optional[str] = None
    secondaryColor: Optional[str] = None
    deleted: Optional[bool] = None
    locationId: Optional[str] = None
    createdBy: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class CategoryQueueWithCategoryDTO(BaseModel):
    """CategoryQueueWithCategoryDTO model"""
    _id: Optional[str] = None
    locationId: Optional[str] = None
    categoryId: Optional[str] = None
    timeSlots: Optional[List[TimeSlotDTO]] = None
    enableFuturePosts: Optional[bool] = None
    prioritizeNewContent: Optional[bool] = None
    currentOrder: Optional[float] = None
    status: Optional[str] = None
    startDate: Optional[str] = None
    skipDateTime: Optional[List[str]] = None
    currentPostId: Optional[str] = None
    totalPosts: Optional[float] = None
    lastScheduledTime: Optional[str] = None
    createdBy: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    category: Optional[Any] = None

class FetchCategoryQueuesResponseDTO(BaseModel):
    """FetchCategoryQueuesResponseDTO model"""
    message: Optional[str] = None
    queues: Optional[List[CategoryQueueWithCategoryDTO]] = None
    meta: Optional[MetaDTO] = None

class WrappedFetchCategoryQueuesResponseDTO(BaseModel):
    """WrappedFetchCategoryQueuesResponseDTO model"""
    success: bool
    statusCode: float
    results: FetchCategoryQueuesResponseDTO
    traceId: Optional[str] = None

class FetchQueueByIdResponseDTO(BaseModel):
    """FetchQueueByIdResponseDTO model"""
    message: Optional[str] = None
    queue: Optional[Any] = None

class WrappedFetchQueueByIdResponseDTO(BaseModel):
    """WrappedFetchQueueByIdResponseDTO model"""
    success: bool
    statusCode: float
    results: FetchQueueByIdResponseDTO
    traceId: Optional[str] = None

class FetchQueueItemsDTO(BaseModel):
    """FetchQueueItemsDTO model"""
    locationId: str
    sessionId: Optional[str] = None
    skip: Optional[float] = None
    limit: Optional[float] = None
    errorFilter: Optional[bool] = None
    itemId: Optional[str] = None

class OgTagsDTO(BaseModel):
    """OgTagsDTO model"""
    metaLink: Optional[Dict[str, Any]] = None
    metaImage: Optional[Dict[str, Any]] = None
    ogTitle: Optional[Dict[str, Any]] = None

class VariationDTO(BaseModel):
    """VariationDTO model"""
    _id: Optional[str] = None
    content: Optional[str] = None
    mentions: Optional[List[Dict[str, Any]]] = None
    ogTags: Optional[Any] = None

class QueueItemDTO(BaseModel):
    """QueueItemDTO model"""
    _id: Optional[str] = None
    order: Optional[float] = None
    variations: Optional[List[VariationDTO]] = None
    primaryImage: Optional[str] = None
    postId: Optional[str] = None
    post: Optional[Any] = None
    errors: Optional[List[str]] = None
    scheduledDateTime: Optional[str] = None
    scheduledVariationIndex: Optional[float] = None
    isSkipped: Optional[bool] = None

class FetchQueueItemsMetaDTO(BaseModel):
    """FetchQueueItemsMetaDTO model"""
    count: Optional[str] = None
    skip: Optional[float] = None
    limit: Optional[float] = None

class FetchQueueItemsResponseDTO(BaseModel):
    """FetchQueueItemsResponseDTO model"""
    message: Optional[str] = None
    items: Optional[List[QueueItemDTO]] = None
    meta: Optional[FetchQueueItemsMetaDTO] = None

class WrappedFetchQueueItemsResponseDTO(BaseModel):
    """WrappedFetchQueueItemsResponseDTO model"""
    success: bool
    statusCode: float
    results: FetchQueueItemsResponseDTO
    traceId: Optional[str] = None

class StartEditSessionDTO(BaseModel):
    """StartEditSessionDTO model"""
    locationId: str

class StartEditSessionResponseDTO(BaseModel):
    """StartEditSessionResponseDTO model"""
    message: Optional[str] = None
    sessionId: Optional[str] = None
    itemCount: Optional[float] = None

class WrappedStartEditSessionResponseDTO(BaseModel):
    """WrappedStartEditSessionResponseDTO model"""
    success: bool
    statusCode: float
    results: StartEditSessionResponseDTO
    traceId: Optional[str] = None

class SaveEditSessionDTO(BaseModel):
    """SaveEditSessionDTO model"""
    locationId: str
    sessionId: str
    keepInDraft: Optional[bool] = None

class UpdatedSlotInfoDTO(BaseModel):
    """UpdatedSlotInfoDTO model"""
    itemId: Optional[str] = None
    scheduledDateTime: Optional[str] = None
    isSkipped: Optional[bool] = None

class SaveEditSessionResponseDTO(BaseModel):
    """SaveEditSessionResponseDTO model"""
    message: Optional[str] = None
    updatedSlots: Optional[List[UpdatedSlotInfoDTO]] = None
    totalPostsChanged: Optional[float] = None

class WrappedSaveEditSessionResponseDTO(BaseModel):
    """WrappedSaveEditSessionResponseDTO model"""
    success: bool
    statusCode: float
    results: SaveEditSessionResponseDTO
    traceId: Optional[str] = None

class DiscardEditSessionDTO(BaseModel):
    """DiscardEditSessionDTO model"""
    locationId: str
    sessionId: str
    keepInDraft: Optional[bool] = None

class DiscardEditSessionResponseDTO(BaseModel):
    """DiscardEditSessionResponseDTO model"""
    message: Optional[str] = None

class WrappedDiscardEditSessionResponseDTO(BaseModel):
    """WrappedDiscardEditSessionResponseDTO model"""
    success: bool
    statusCode: float
    results: DiscardEditSessionResponseDTO
    traceId: Optional[str] = None

class EditSessionCalendarDTO(BaseModel):
    """EditSessionCalendarDTO model"""
    locationId: str
    sessionId: str
    startDate: str
    endDate: str
    accountIds: Optional[List[str]] = None

class EditSessionScheduledPostDTO(BaseModel):
    """EditSessionScheduledPostDTO model"""
    scheduledDateTime: Optional[str] = None
    post: Optional[Any] = None
    queueItemId: Optional[str] = None
    queueId: Optional[str] = None
    order: Optional[float] = None
    variations: Optional[List[VariationDTO]] = None
    primaryImage: Optional[str] = None
    errors: Optional[List[str]] = None
    category: Optional[Any] = None
    currentVariation: Optional[float] = None
    timezone: Optional[str] = None
    isDraft: Optional[bool] = None
    originalItemId: Optional[str] = None

class EditSessionCalendarResponseDTO(BaseModel):
    """EditSessionCalendarResponseDTO model"""
    message: Optional[str] = None
    scheduledPosts: Optional[List[EditSessionScheduledPostDTO]] = None
    total: Optional[float] = None
    timezone: Optional[str] = None

class WrappedEditSessionCalendarResponseDTO(BaseModel):
    """WrappedEditSessionCalendarResponseDTO model"""
    success: bool
    statusCode: float
    results: EditSessionCalendarResponseDTO
    traceId: Optional[str] = None

class FetchSlotsDTO(BaseModel):
    """FetchSlotsDTO model"""
    locationId: str
    sessionId: Optional[str] = None
    skip: Optional[float] = None
    limit: Optional[float] = None

class FetchSlotsResponseDTO(BaseModel):
    """FetchSlotsResponseDTO model"""
    message: Optional[str] = None
    slots: Optional[List[UpdatedSlotInfoDTO]] = None
    total: Optional[float] = None
    skip: Optional[float] = None
    limit: Optional[float] = None
    timezone: Optional[str] = None

class WrappedFetchSlotsResponseDTO(BaseModel):
    """WrappedFetchSlotsResponseDTO model"""
    success: bool
    statusCode: float
    results: FetchSlotsResponseDTO
    traceId: Optional[str] = None

class UpdateCategoryQueueDTO(BaseModel):
    """UpdateCategoryQueueDTO model"""
    locationId: str
    skipLegacyWatermark: Optional[bool] = None
    status: Optional[Dict[str, Any]] = None
    skipDateTime: Optional[str] = None
    timeSlots: Optional[List[TimeSlotDTO]] = None
    enableFuturePosts: Optional[bool] = None
    prioritizeNewContent: Optional[bool] = None

class CategoryQueueDTO(BaseModel):
    """CategoryQueueDTO model"""
    _id: Optional[str] = None
    locationId: Optional[str] = None
    categoryId: Optional[str] = None
    timeSlots: Optional[List[TimeSlotDTO]] = None
    enableFuturePosts: Optional[bool] = None
    prioritizeNewContent: Optional[bool] = None
    currentOrder: Optional[float] = None
    status: Optional[str] = None
    startDate: Optional[str] = None
    skipDateTime: Optional[List[str]] = None
    currentPostId: Optional[str] = None
    totalPosts: Optional[float] = None
    lastScheduledTime: Optional[str] = None
    createdBy: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class UpdateCategoryQueueResponseDTO(BaseModel):
    """UpdateCategoryQueueResponseDTO model"""
    message: Optional[str] = None
    queue: Optional[Any] = None

class WrappedUpdateCategoryQueueResponseDTO(BaseModel):
    """WrappedUpdateCategoryQueueResponseDTO model"""
    success: bool
    statusCode: float
    results: UpdateCategoryQueueResponseDTO
    traceId: Optional[str] = None

class GeneralSuccessResponseDTO(BaseModel):
    """GeneralSuccessResponseDTO model"""
    message: Optional[str] = None
    updatedSlots: Optional[List[UpdatedSlotInfoDTO]] = None
    totalPostsChanged: Optional[float] = None

class WrappedGeneralSuccessResponseDTO(BaseModel):
    """WrappedGeneralSuccessResponseDTO model"""
    success: bool
    statusCode: float
    results: GeneralSuccessResponseDTO
    traceId: Optional[str] = None

class QueueModifiedPostDTO(BaseModel):
    """QueueModifiedPostDTO model"""
    accountIds: Optional[List[str]] = None
    summary: Optional[str] = None
    media: Optional[List[PostMediaSchema]] = None
    status: Optional[Dict[str, Any]] = None
    scheduleDate: Optional[str] = None
    selectedBestTime: Optional[str] = None
    createdBy: Optional[str] = None
    followUpComment: Optional[str] = None
    ogTagsDetails: Optional[Any] = None
    type: Optional[Dict[str, Any]] = None
    postApprovalDetails: Optional[Any] = None
    scheduleTimeUpdated: Optional[bool] = None
    tags: Optional[List[str]] = None
    categoryId: Optional[str] = None
    applyWatermark: Optional[bool] = None
    tiktokPostDetails: Optional[Any] = None
    gmbPostDetails: Optional[Any] = None
    userId: Optional[str] = None
    linkedinPostDetails: Optional[Any] = None
    pinterestPostDetails: Optional[Any] = None
    facebookPostDetails: Optional[Any] = None
    instagramPostDetails: Optional[Any] = None
    youtubePostDetails: Optional[Any] = None
    locationId: Optional[str] = None

class OgTagsInputDTO(BaseModel):
    """OgTagsInputDTO model"""
    metaLink: Optional[Dict[str, Any]] = None
    metaImage: Optional[Dict[str, Any]] = None
    ogTitle: Optional[Dict[str, Any]] = None

class VariationInputDTO(BaseModel):
    """VariationInputDTO model"""
    content: Optional[str] = None
    mentions: Optional[List[Dict[str, Any]]] = None
    ogTags: Optional[Any] = None

class UpdateQueueItemDTO(BaseModel):
    """UpdateQueueItemDTO model"""
    locationId: str
    sessionId: Optional[str] = None
    modifiedPostPayload: Optional[Any] = None
    newOrder: Optional[Any] = None
    variations: Optional[List[VariationInputDTO]] = None
    primaryImage: Optional[str] = None

class GetModifiedPayloadFormattedSchema(BaseModel):
    """GetModifiedPayloadFormattedSchema model"""
    _id: Optional[str] = None
    source: Optional[str] = None
    locationId: str
    displayDate: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    accountId: Optional[str] = None
    error: str
    postId: Optional[str] = None
    publishedAt: Optional[str] = None
    thumbnail: Optional[str] = None
    accountIds: Optional[List[str]] = None
    summary: Optional[str] = None
    media: Optional[List[PostMediaSchema]] = None
    status: Optional[Dict[str, Any]] = None
    createdBy: Optional[str] = None
    type: Dict[str, Any]
    tags: Optional[List[str]] = None
    ogTagsDetails: Optional[Any] = None
    postApprovalDetails: Optional[Any] = None
    tiktokPostDetails: Optional[Any] = None
    gmbPostDetails: Optional[Any] = None
    user: Optional[Any] = None
    linkedinPostDetails: Optional[Any] = None
    pinterestPostDetails: Optional[Any] = None
    facebookPostDetails: Optional[Any] = None
    instagramPostDetails: Optional[Any] = None
    youtubePostDetails: Optional[Any] = None
    mediaOptimization: Optional[bool] = None

class CreatedQueueItemWithVariationsDTO(BaseModel):
    """CreatedQueueItemWithVariationsDTO model"""
    _id: Optional[str] = None
    order: Optional[float] = None
    variations: Optional[List[VariationDTO]] = None
    primaryImage: Optional[str] = None
    lastScheduledTime: Optional[str] = None
    queueId: Optional[str] = None
    postId: Optional[str] = None
    modifiedPostPayload: Optional[Any] = None
    parentPostId: Optional[str] = None
    errors: Optional[List[str]] = None
    currentVariation: Optional[float] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    deleted: Optional[bool] = None
    locationId: Optional[str] = None

class UpdateQueueItemResponseDTO(BaseModel):
    """UpdateQueueItemResponseDTO model"""
    message: Optional[str] = None
    queueItem: Optional[Any] = None
    updatedSlots: Optional[List[UpdatedSlotInfoDTO]] = None
    totalPostsChanged: Optional[float] = None

class WrappedUpdateQueueItemResponseDTO(BaseModel):
    """WrappedUpdateQueueItemResponseDTO model"""
    success: bool
    statusCode: float
    results: UpdateQueueItemResponseDTO
    traceId: Optional[str] = None

class CalendarListDTO(BaseModel):
    """CalendarListDTO model"""
    locationId: str
    startDate: str
    endDate: str
    categoryIds: Optional[List[str]] = None
    accountIds: Optional[List[str]] = None

class ScheduledPostDTO(BaseModel):
    """ScheduledPostDTO model"""
    scheduledDateTime: Optional[str] = None
    post: Optional[Any] = None
    queueItemId: Optional[str] = None
    queueId: Optional[str] = None
    order: Optional[float] = None
    variations: Optional[List[VariationDTO]] = None
    primaryImage: Optional[str] = None
    errors: Optional[List[str]] = None
    category: Optional[Any] = None
    currentVariation: Optional[float] = None
    timezone: Optional[str] = None

class FetchCalendarListResponseDTO(BaseModel):
    """FetchCalendarListResponseDTO model"""
    message: Optional[str] = None
    scheduledPosts: Optional[List[ScheduledPostDTO]] = None
    total: Optional[float] = None
    timezone: Optional[str] = None

class WrappedFetchCalendarListResponseDTO(BaseModel):
    """WrappedFetchCalendarListResponseDTO model"""
    success: bool
    statusCode: float
    results: FetchCalendarListResponseDTO
    traceId: Optional[str] = None

class DeleteActivePostResponseDTO(BaseModel):
    """DeleteActivePostResponseDTO model"""
    message: Optional[str] = None

class WrappedDeleteActivePostResponseDTO(BaseModel):
    """WrappedDeleteActivePostResponseDTO model"""
    success: bool
    statusCode: float
    results: DeleteActivePostResponseDTO
    traceId: Optional[str] = None

class ResetQueueItemDTO(BaseModel):
    """ResetQueueItemDTO model"""
    locationId: str
    sessionId: Optional[str] = None

class QueueItemWithVariationsDTO(BaseModel):
    """QueueItemWithVariationsDTO model"""
    _id: Optional[str] = None
    order: Optional[float] = None
    variations: Optional[List[VariationDTO]] = None
    primaryImage: Optional[str] = None
    postId: Optional[str] = None
    post: Optional[Any] = None
    errors: Optional[List[str]] = None
    scheduledDateTime: Optional[str] = None
    scheduledVariationIndex: Optional[float] = None
    isSkipped: Optional[bool] = None
    currentVariation: Optional[float] = None

class ResetQueueItemResponseDTO(BaseModel):
    """ResetQueueItemResponseDTO model"""
    message: Optional[str] = None
    queueItem: Optional[Any] = None

class WrappedResetQueueItemResponseDTO(BaseModel):
    """WrappedResetQueueItemResponseDTO model"""
    success: bool
    statusCode: float
    results: ResetQueueItemResponseDTO
    traceId: Optional[str] = None

class CloneQueueItemDTO(BaseModel):
    """CloneQueueItemDTO model"""
    locationId: str
    sessionId: str
    order: float

class CloneQueueItemResponseDTO(BaseModel):
    """CloneQueueItemResponseDTO model"""
    message: Optional[str] = None
    queueItem: Optional[Any] = None

class WrappedCloneQueueItemResponseDTO(BaseModel):
    """WrappedCloneQueueItemResponseDTO model"""
    success: bool
    statusCode: float
    results: CloneQueueItemResponseDTO
    traceId: Optional[str] = None

class CreateQueueItemDTO(BaseModel):
    """CreateQueueItemDTO model"""
    locationId: str
    sessionId: Optional[str] = None
    modifiedPostPayload: Optional[Any] = None
    order: Optional[Any] = None
    variations: Optional[List[VariationInputDTO]] = None
    primaryImage: Optional[str] = None
    directToQueue: Optional[bool] = None

class CreateQueueItemResponseDTO(BaseModel):
    """CreateQueueItemResponseDTO model"""
    message: Optional[str] = None
    queueItem: Optional[Any] = None

class WrappedCreateQueueItemResponseDTO(BaseModel):
    """WrappedCreateQueueItemResponseDTO model"""
    success: bool
    statusCode: float
    results: CreateQueueItemResponseDTO
    traceId: Optional[str] = None

class CommentsCreateBodyDTO(BaseModel):
    """CommentsCreateBodyDTO model"""
    parentId: str
    isParentThread: bool
    content: str
    attachments: Optional[List[AttachmentDTO]] = None
    mentions: Optional[List[MentionsDTO]] = None
    notifyAllGroupMembers: Optional[bool] = None

class CommentsCreateResponseDTO(BaseModel):
    """CommentsCreateResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Any

class CommentsLikeResponseDTO(BaseModel):
    """CommentsLikeResponseDTO model"""
    success: bool
    statusCode: float
    message: str

class DeleteLikeResponseDTO(BaseModel):
    """DeleteLikeResponseDTO model"""
    success: bool
    statusCode: float
    message: str

class CommentsGetListBodyDTO(BaseModel):
    """CommentsGetListBodyDTO model"""
    fromDate: Optional[str] = None
    toDate: Optional[str] = None
    originIds: List[str]
    sortBy: Optional[str] = None
    search: Optional[str] = None
    skip: Optional[float] = None
    limit: Optional[float] = None
    parentId: Optional[str] = None

class CommentsGetListResponseDTO(BaseModel):
    """CommentsGetListResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Any

class AttachmentDTO(BaseModel):
    """AttachmentDTO model"""
    url: str
    type: str

class MentionsDTO(BaseModel):
    """MentionsDTO model"""
    name: str
    id: str
    offset: float
    length: float
    slug: Optional[str] = None

class CommentsGetListResultsDTO(BaseModel):
    """CommentsGetListResultsDTO model"""
    comments: List[CommentItemDTO]
    meta: Any

class CommentItemDTO(BaseModel):
    """CommentItemDTO model"""
    _id: str
    platform: str
    platformCommentId: Optional[str] = None
    platformParentId: Optional[str] = None
    platformPostId: Optional[str] = None
    postId: str
    originId: str
    isParentThread: Optional[bool] = None
    isPost: bool
    content: Optional[str] = None
    attachments: Optional[List[CommentAttachmentDTO]] = None
    author: Optional[Any] = None
    level: Optional[float] = None
    likeCount: float
    reactionCount: float
    replyCount: float
    shareCount: float
    repostCount: float
    quoteCount: float
    previewLink: Optional[str] = None
    isRead: bool
    isDeleted: bool
    isEdited: bool
    publishedAt: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

class CommentsListMetaDTO(BaseModel):
    """CommentsListMetaDTO model"""
    total: float
    totalUnread: Optional[float] = None
    skip: float
    limit: float
    hasMore: bool

class CommentAuthorDTO(BaseModel):
    """CommentAuthorDTO model"""
    id: Optional[str] = None
    name: Optional[str] = None
    profilePic: Optional[str] = None

class CommentAttachmentDTO(BaseModel):
    """CommentAttachmentDTO model"""
    type: Optional[str] = None
    url: Optional[str] = None
    thumbnail: Optional[str] = None
    videoUrl: Optional[str] = None

