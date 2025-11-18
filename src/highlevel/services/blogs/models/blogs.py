from __future__ import annotations

# Blogs Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class UrlSlugCheckResponseDTO(BaseModel):
    """UrlSlugCheckResponseDTO model"""
    exists: bool

class UpdateBlogPostParams(BaseModel):
    """UpdateBlogPostParams model"""
    title: str
    locationId: str
    blogId: str
    imageUrl: str
    description: str
    rawHTML: str
    status: str
    imageAltText: str
    categories: List[str]
    tags: Optional[List[str]] = None
    author: str
    urlSlug: str
    canonicalLink: Optional[str] = None
    publishedAt: str

class BlogPostUpdateResponseWrapperDTO(BaseModel):
    """BlogPostUpdateResponseWrapperDTO model"""
    updatedBlogPost: BlogPostResponseDTO

class CreateBlogPostParams(BaseModel):
    """CreateBlogPostParams model"""
    title: str
    locationId: str
    blogId: str
    imageUrl: str
    description: str
    rawHTML: str
    status: str
    imageAltText: str
    categories: List[str]
    tags: Optional[List[str]] = None
    author: str
    urlSlug: str
    canonicalLink: Optional[str] = None
    publishedAt: str

class BlogPostCreateResponseWrapperDTO(BaseModel):
    """BlogPostCreateResponseWrapperDTO model"""
    data: BlogPostResponseDTO

class AuthorsResponseDTO(BaseModel):
    """AuthorsResponseDTO model"""
    authors: List[AuthorResponseDTO]

class AuthorResponseDTO(BaseModel):
    """AuthorResponseDTO model"""
    _id: str
    name: str
    locationId: str
    updatedAt: str
    canonicalLink: str

class CategoriesResponseDTO(BaseModel):
    """CategoriesResponseDTO model"""
    categories: List[CategoryResponseDTO]

class CategoryResponseDTO(BaseModel):
    """CategoryResponseDTO model"""
    _id: str
    label: Optional[str] = None
    locationId: str
    updatedAt: str
    canonicalLink: str
    urlSlug: str

class BlogGetResponseWrapperDTO(BaseModel):
    """BlogGetResponseWrapperDTO model"""
    data: List[BlogResponseDTO]

class BlogResponseDTO(BaseModel):
    """BlogResponseDTO model"""
    _id: str
    name: str

class BlogPostGetResponseWrapperDTO(BaseModel):
    """BlogPostGetResponseWrapperDTO model"""
    blogs: List[BlogPostResponseDTO]

class BlogPostResponseDTO(BaseModel):
    """BlogPostResponseDTO model"""
    categories: List[str]
    tags: Optional[List[str]] = None
    archived: bool
    _id: str
    title: str
    description: str
    imageUrl: str
    status: str
    imageAltText: str
    urlSlug: str
    canonicalLink: Optional[str] = None
    author: Optional[str] = None
    publishedAt: str
    updatedAt: str

