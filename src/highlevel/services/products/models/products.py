from __future__ import annotations

# Products Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class BulkUpdateFilters(BaseModel):
    """BulkUpdateFilters model"""
    collectionIds: Optional[List[str]] = None
    productType: Optional[str] = None
    availableInStore: Optional[bool] = None
    search: Optional[str] = None

class PriceUpdateField(BaseModel):
    """PriceUpdateField model"""
    type: str
    value: float
    roundToWhole: Optional[bool] = None

class BulkUpdateDto(BaseModel):
    """BulkUpdateDto model"""
    altId: str
    altType: str
    type: str
    productIds: List[str]
    filters: Optional[Any] = None
    price: Optional[Any] = None
    compareAtPrice: Optional[Any] = None
    availability: Optional[bool] = None
    collectionIds: Optional[List[str]] = None
    currency: Optional[str] = None

class BulkUpdateResponseDto(BaseModel):
    """BulkUpdateResponseDto model"""
    status: bool
    message: Optional[str] = None

class WeightOptionsDto(BaseModel):
    """WeightOptionsDto model"""
    value: float
    unit: str

class PriceDimensionsDto(BaseModel):
    """PriceDimensionsDto model"""
    height: float
    width: float
    length: float
    unit: str

class ShippingOptionsDto(BaseModel):
    """ShippingOptionsDto model"""
    weight: Optional[Any] = None
    dimensions: Optional[Any] = None

class RecurringDto(BaseModel):
    """RecurringDto model"""
    interval: str
    intervalCount: float

class BulkEditPriceDto(BaseModel):
    """BulkEditPriceDto model"""
    _id: str
    name: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    compareAtPrice: Optional[float] = None
    availableQuantity: Optional[float] = None
    trackInventory: Optional[bool] = None
    allowOutOfStockPurchases: Optional[bool] = None
    sku: Optional[str] = None
    trialPeriod: Optional[float] = None
    totalCycles: Optional[float] = None
    setupFee: Optional[float] = None
    shippingOptions: Optional[Any] = None
    recurring: Optional[Any] = None

class ProductSEODto(BaseModel):
    """ProductSEODto model"""
    title: Optional[str] = None
    description: Optional[str] = None

class BulkEditProductDto(BaseModel):
    """BulkEditProductDto model"""
    _id: str
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    availableInStore: Optional[bool] = None
    prices: Optional[List[BulkEditPriceDto]] = None
    collectionIds: Optional[List[str]] = None
    isLabelEnabled: Optional[bool] = None
    isTaxesEnabled: Optional[bool] = None
    seo: Optional[Any] = None
    slug: Optional[str] = None
    automaticTaxCategoryId: Optional[str] = None
    taxInclusive: Optional[bool] = None
    taxes: Optional[List[Dict[str, Any]]] = None
    medias: Optional[List[Dict[str, Any]]] = None
    label: Optional[Dict[str, Any]] = None

class BulkEditRequestDto(BaseModel):
    """BulkEditRequestDto model"""
    altId: str
    altType: str
    products: List[BulkEditProductDto]

class BulkEditResponseDto(BaseModel):
    """BulkEditResponseDto model"""
    message: str
    status: bool
    updatedCount: float

class MembershipOfferDto(BaseModel):
    """MembershipOfferDto model"""
    label: str
    value: str
    _id: str

class PriceMetaDto(BaseModel):
    """PriceMetaDto model"""
    source: str
    sourceId: Optional[str] = None
    stripePriceId: str
    internalSource: str

class CreatePriceDto(BaseModel):
    """CreatePriceDto model"""
    name: str
    type: str
    currency: str
    amount: float
    recurring: Optional[Any] = None
    description: Optional[str] = None
    membershipOffers: Optional[List[MembershipOfferDto]] = None
    trialPeriod: Optional[float] = None
    totalCycles: Optional[float] = None
    setupFee: Optional[float] = None
    variantOptionIds: Optional[List[str]] = None
    compareAtPrice: Optional[float] = None
    locationId: str
    userId: Optional[str] = None
    meta: Optional[Any] = None
    trackInventory: Optional[bool] = None
    availableQuantity: Optional[float] = None
    allowOutOfStockPurchases: Optional[bool] = None
    sku: Optional[str] = None
    shippingOptions: Optional[Any] = None
    isDigitalProduct: Optional[bool] = None
    digitalDelivery: Optional[List[str]] = None

class CreatePriceResponseDto(BaseModel):
    """CreatePriceResponseDto model"""
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

class ListPricesResponseDto(BaseModel):
    """ListPricesResponseDto model"""
    prices: List[DefaultPriceResponseDto]
    total: float

class InventoryItemDto(BaseModel):
    """InventoryItemDto model"""
    _id: str
    name: str
    availableQuantity: float
    sku: str
    allowOutOfStockPurchases: bool
    product: str
    updatedAt: str
    image: Optional[str] = None
    productName: Optional[str] = None

class GetInventoryResponseDto(BaseModel):
    """GetInventoryResponseDto model"""
    inventory: List[InventoryItemDto]
    total: Dict[str, Any]

class UpdateInventoryItemDto(BaseModel):
    """UpdateInventoryItemDto model"""
    priceId: str
    availableQuantity: Optional[float] = None
    allowOutOfStockPurchases: Optional[bool] = None

class UpdateInventoryDto(BaseModel):
    """UpdateInventoryDto model"""
    altId: str
    altType: str
    items: List[UpdateInventoryItemDto]

class UpdateInventoryResponseDto(BaseModel):
    """UpdateInventoryResponseDto model"""
    status: bool
    message: Optional[str] = None

class GetPriceResponseDto(BaseModel):
    """GetPriceResponseDto model"""
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

class UpdatePriceDto(BaseModel):
    """UpdatePriceDto model"""
    name: str
    type: str
    currency: str
    amount: float
    recurring: Optional[Any] = None
    description: Optional[str] = None
    membershipOffers: Optional[List[MembershipOfferDto]] = None
    trialPeriod: Optional[float] = None
    totalCycles: Optional[float] = None
    setupFee: Optional[float] = None
    variantOptionIds: Optional[List[str]] = None
    compareAtPrice: Optional[float] = None
    locationId: str
    userId: Optional[str] = None
    meta: Optional[Any] = None
    trackInventory: Optional[bool] = None
    availableQuantity: Optional[float] = None
    allowOutOfStockPurchases: Optional[bool] = None
    sku: Optional[str] = None
    shippingOptions: Optional[Any] = None
    isDigitalProduct: Optional[bool] = None
    digitalDelivery: Optional[List[str]] = None

class UpdatePriceResponseDto(BaseModel):
    """UpdatePriceResponseDto model"""
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

class DeletePriceResponseDto(BaseModel):
    """DeletePriceResponseDto model"""
    status: bool

class GetProductStatsResponseDto(BaseModel):
    """GetProductStatsResponseDto model"""
    totalProducts: float
    includedInStore: float
    excludedFromStore: float

class UpdateProductStoreDto(BaseModel):
    """UpdateProductStoreDto model"""
    altId: str
    altType: str
    action: str
    productIds: List[str]

class UpdateProductStoreResponseDto(BaseModel):
    """UpdateProductStoreResponseDto model"""
    status: bool
    message: Optional[str] = None

class UpdateDisplayPriorityBodyDto(BaseModel):
    """UpdateDisplayPriorityBodyDto model"""
    altId: str
    altType: str
    products: List[List[Any]]

class ListCollectionResponseDto(BaseModel):
    """ListCollectionResponseDto model"""
    data: List[List[Any]]
    total: float

class ProductCategories(BaseModel):
    """ProductCategories model"""

class DefaultCollectionResponseDto(BaseModel):
    """DefaultCollectionResponseDto model"""
    data: Any
    status: bool

class CollectionSEODto(BaseModel):
    """CollectionSEODto model"""
    title: Optional[str] = None
    description: Optional[str] = None

class CreateProductCollectionsDto(BaseModel):
    """CreateProductCollectionsDto model"""
    altId: str
    altType: str
    collectionId: Optional[str] = None
    name: str
    slug: str
    image: Optional[str] = None
    seo: Optional[Any] = None

class CollectionSchema(BaseModel):
    """CollectionSchema model"""
    _id: str
    altId: str
    name: str
    slug: str
    image: str
    seo: Any
    createdAt: str

class CreateCollectionResponseDto(BaseModel):
    """CreateCollectionResponseDto model"""
    data: Any

class UpdateProductCollectionsDto(BaseModel):
    """UpdateProductCollectionsDto model"""
    altId: str
    altType: str
    name: Optional[str] = None
    slug: Optional[str] = None
    image: Optional[str] = None
    seo: Optional[Any] = None

class UpdateProductCollectionResponseDto(BaseModel):
    """UpdateProductCollectionResponseDto model"""
    status: bool
    message: Optional[str] = None

class DeleteProductCollectionResponseDto(BaseModel):
    """DeleteProductCollectionResponseDto model"""
    status: bool
    message: Optional[str] = None

class ListProductReviewsResponseDto(BaseModel):
    """ListProductReviewsResponseDto model"""
    data: List[List[Any]]
    total: float

class CountReviewsByStatusResponseDto(BaseModel):
    """CountReviewsByStatusResponseDto model"""
    data: List[List[Any]]

class UserDetailsDto(BaseModel):
    """UserDetailsDto model"""
    name: str
    email: str
    phone: Optional[str] = None
    isCustomer: Optional[bool] = None

class ProductReviewDto(BaseModel):
    """ProductReviewDto model"""
    headline: str
    comment: str
    user: Any

class UpdateProductReviewDto(BaseModel):
    """UpdateProductReviewDto model"""
    altId: str
    altType: str
    productId: str
    status: str
    reply: Optional[List[ProductReviewDto]] = None
    rating: Optional[float] = None
    headline: Optional[str] = None
    detail: Optional[str] = None

class UpdateProductReviewsResponseDto(BaseModel):
    """UpdateProductReviewsResponseDto model"""
    status: bool
    message: Optional[str] = None

class UpdateProductReviewObjectDto(BaseModel):
    """UpdateProductReviewObjectDto model"""
    reviewId: str
    productId: str
    storeId: str

class UpdateProductReviewsDto(BaseModel):
    """UpdateProductReviewsDto model"""
    altId: str
    altType: str
    reviews: List[UpdateProductReviewObjectDto]
    status: Dict[str, Any]

class DeleteProductReviewResponseDto(BaseModel):
    """DeleteProductReviewResponseDto model"""
    status: bool
    message: Optional[str] = None

class ProductVariantOptionDto(BaseModel):
    """ProductVariantOptionDto model"""
    id: str
    name: str

class ProductVariantDto(BaseModel):
    """ProductVariantDto model"""
    id: str
    name: str
    options: List[ProductVariantOptionDto]

class ProductLabelDto(BaseModel):
    """ProductLabelDto model"""
    title: str
    startDate: Optional[str] = None
    endDate: Optional[str] = None

class GetProductResponseDto(BaseModel):
    """GetProductResponseDto model"""
    _id: str
    description: Optional[str] = None
    variants: Optional[List[ProductVariantDto]] = None
    locationId: str
    name: str
    productType: str
    availableInStore: Optional[bool] = None
    createdAt: str
    updatedAt: str
    statementDescriptor: Optional[str] = None
    image: Optional[str] = None
    collectionIds: Optional[List[str]] = None
    isTaxesEnabled: Optional[bool] = None
    taxes: Optional[List[str]] = None
    automaticTaxCategoryId: Optional[str] = None
    label: Optional[Any] = None
    slug: Optional[str] = None

class DeleteProductResponseDto(BaseModel):
    """DeleteProductResponseDto model"""
    status: bool

class ProductMediaDto(BaseModel):
    """ProductMediaDto model"""
    id: str
    title: Optional[str] = None
    url: str
    type: str
    isFeatured: Optional[bool] = None
    priceIds: Optional[List[List[Any]]] = None

class CreateProductDto(BaseModel):
    """CreateProductDto model"""
    name: str
    locationId: str
    description: Optional[str] = None
    productType: str
    image: Optional[str] = None
    statementDescriptor: Optional[str] = None
    availableInStore: Optional[bool] = None
    medias: Optional[List[ProductMediaDto]] = None
    variants: Optional[List[ProductVariantDto]] = None
    collectionIds: Optional[List[str]] = None
    isTaxesEnabled: Optional[bool] = None
    taxes: Optional[List[str]] = None
    automaticTaxCategoryId: Optional[str] = None
    isLabelEnabled: Optional[bool] = None
    label: Optional[Any] = None
    slug: Optional[str] = None
    seo: Optional[Any] = None
    taxInclusive: Optional[bool] = None

class CreateProductResponseDto(BaseModel):
    """CreateProductResponseDto model"""
    _id: str
    description: Optional[str] = None
    variants: Optional[List[ProductVariantDto]] = None
    locationId: str
    name: str
    productType: str
    availableInStore: Optional[bool] = None
    createdAt: str
    updatedAt: str
    statementDescriptor: Optional[str] = None
    image: Optional[str] = None
    collectionIds: Optional[List[str]] = None
    isTaxesEnabled: Optional[bool] = None
    taxes: Optional[List[str]] = None
    automaticTaxCategoryId: Optional[str] = None
    label: Optional[Any] = None
    slug: Optional[str] = None

class UpdateProductDto(BaseModel):
    """UpdateProductDto model"""
    name: str
    locationId: str
    description: Optional[str] = None
    productType: str
    image: Optional[str] = None
    statementDescriptor: Optional[str] = None
    availableInStore: Optional[bool] = None
    medias: Optional[List[ProductMediaDto]] = None
    variants: Optional[List[ProductVariantDto]] = None
    collectionIds: Optional[List[str]] = None
    isTaxesEnabled: Optional[bool] = None
    taxes: Optional[List[str]] = None
    automaticTaxCategoryId: Optional[str] = None
    isLabelEnabled: Optional[bool] = None
    label: Optional[Any] = None
    slug: Optional[str] = None
    seo: Optional[Any] = None
    taxInclusive: Optional[bool] = None
    prices: Optional[List[str]] = None

class UpdateProductResponseDto(BaseModel):
    """UpdateProductResponseDto model"""
    _id: str
    description: Optional[str] = None
    variants: Optional[List[ProductVariantDto]] = None
    locationId: str
    name: str
    productType: str
    availableInStore: Optional[bool] = None
    createdAt: str
    updatedAt: str
    statementDescriptor: Optional[str] = None
    image: Optional[str] = None
    collectionIds: Optional[List[str]] = None
    isTaxesEnabled: Optional[bool] = None
    taxes: Optional[List[str]] = None
    automaticTaxCategoryId: Optional[str] = None
    label: Optional[Any] = None
    slug: Optional[str] = None

class DefaultProductResponseDto(BaseModel):
    """DefaultProductResponseDto model"""
    _id: str
    description: Optional[str] = None
    variants: Optional[List[ProductVariantDto]] = None
    locationId: str
    name: str
    productType: str
    availableInStore: Optional[bool] = None
    createdAt: str
    updatedAt: str
    statementDescriptor: Optional[str] = None
    image: Optional[str] = None
    collectionIds: Optional[List[str]] = None
    isTaxesEnabled: Optional[bool] = None
    taxes: Optional[List[str]] = None
    automaticTaxCategoryId: Optional[str] = None
    label: Optional[Any] = None
    slug: Optional[str] = None

class ListProductsStats(BaseModel):
    """ListProductsStats model"""
    total: float

class ListProductsResponseDto(BaseModel):
    """ListProductsResponseDto model"""
    products: List[DefaultProductResponseDto]
    total: List[ListProductsStats]

