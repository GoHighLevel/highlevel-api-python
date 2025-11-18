from __future__ import annotations

# SocialMediaPosting Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

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
    location: Optional[Dict[str, Any]] = None
    account: Optional[Dict[str, Any]] = None
    companyId: Optional[str] = None

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
    type: Optional[str] = None
    thumbnail: Optional[str] = None
    defaultThumb: Optional[str] = None
    id: Optional[str] = None

class OgTagsSchema(BaseModel):
    """OgTagsSchema model"""
    metaImage: Optional[str] = None
    metaLink: Optional[str] = None

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
    approvalStatus: Optional[Dict[str, Any]] = None
    approverUser: Optional[Any] = None

class TiktokPostSchema(BaseModel):
    """TiktokPostSchema model"""
    privacyLevel: Optional[Dict[str, Any]] = None
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
    gmbEventType: Optional[str] = None
    title: Optional[str] = None
    offerTitle: Optional[str] = None
    startDate: Optional[Any] = None
    endDate: Optional[Any] = None
    termsConditions: Optional[str] = None
    url: Optional[str] = None
    couponCode: Optional[str] = None
    redeemOnlineUrl: Optional[str] = None
    actionType: Optional[Dict[str, Any]] = None

class GetPostFormattedSchema(BaseModel):
    """GetPostFormattedSchema model"""
    _id: Optional[str] = None
    source: Optional[str] = None
    locationId: str
    platform: Optional[str] = None
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
    user: Optional[Any] = None

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
    approvalStatus: Optional[Dict[str, Any]] = None

class CreatePostDTO(BaseModel):
    """CreatePostDTO model"""
    accountIds: List[str]
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
    userId: str

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
    type: Optional[Dict[str, Any]] = None
    originId: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    companyId: Optional[str] = None

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
    companyId: Optional[str] = None

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
    type: Optional[str] = None
    originId: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    urn: Optional[str] = None
    companyId: Optional[str] = None

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
    userId: Optional[str] = None

class SetAccountsResponseDTO(BaseModel):
    """SetAccountsResponseDTO model"""
    success: bool
    statusCode: float
    message: str

class CSVImportSchema(BaseModel):
    """CSVImportSchema model"""
    _id: str
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

class GetUploadStatusResponseSchema(BaseModel):
    """GetUploadStatusResponseSchema model"""
    csvs: Any
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
    type: Optional[Dict[str, Any]] = None
    tiktokPostDetails: Optional[Any] = None
    gmbPostDetails: Optional[Any] = None
    errorMessage: Optional[str] = None

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
    userId: Optional[str] = None

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
    status: Optional[Dict[str, Any]] = None
    count: Optional[float] = None
    createdBy: Optional[str] = None
    traceId: Optional[str] = None
    originId: Optional[str] = None
    approver: Optional[str] = None

class CSVResponseSchema(BaseModel):
    """CSVResponseSchema model"""
    csv: Optional[Any] = None

class DeleteCsvResponseDTO(BaseModel):
    """DeleteCsvResponseDTO model"""
    success: bool
    statusCode: float
    message: str
    results: Optional[Any] = None

class DeletePostResponseSchema(BaseModel):
    """DeletePostResponseSchema model"""
    postId: str

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
    type: Optional[str] = None
    originId: Optional[str] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    verified: Optional[bool] = None
    username: Optional[str] = None
    companyId: Optional[str] = None

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

class GetTiktokBusinessAccountSchema(BaseModel):
    """GetTiktokBusinessAccountSchema model"""
    profile: Optional[List[TiktokProfileSchema]] = None

class GetTiktokBusinessAccountResponseDTO(BaseModel):
    """GetTiktokBusinessAccountResponseDTO model"""
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

