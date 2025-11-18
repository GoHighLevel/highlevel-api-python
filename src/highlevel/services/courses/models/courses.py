from __future__ import annotations

# Courses Models

from typing import Optional, Any, List, Dict
from pydantic import BaseModel

class visibility(BaseModel):
    """visibility model"""

class contentType(BaseModel):
    """contentType model"""

class type(BaseModel):
    """type model"""

class PostMaterialInterface(BaseModel):
    """PostMaterialInterface model"""
    title: str
    type: type
    url: str

class PostInterface(BaseModel):
    """PostInterface model"""
    title: str
    visibility: visibility
    thumbnailUrl: Optional[str] = None
    contentType: contentType
    description: str
    bucketVideoUrl: Optional[str] = None
    postMaterials: Optional[List[PostMaterialInterface]] = None

class SubCategoryInterface(BaseModel):
    """SubCategoryInterface model"""
    title: str
    visibility: visibility
    thumbnailUrl: Optional[str] = None
    posts: Optional[List[PostInterface]] = None

class CategoryInterface(BaseModel):
    """CategoryInterface model"""
    title: str
    visibility: visibility
    thumbnailUrl: Optional[str] = None
    posts: Optional[List[PostInterface]] = None
    subCategories: Optional[List[SubCategoryInterface]] = None

class InstructorDetails(BaseModel):
    """InstructorDetails model"""
    name: str
    description: str

class ProductInterface(BaseModel):
    """ProductInterface model"""
    title: str
    description: str
    imageUrl: Optional[str] = None
    categories: List[CategoryInterface]
    instructorDetails: Optional[InstructorDetails] = None

class PublicExporterPayload(BaseModel):
    """PublicExporterPayload model"""
    locationId: str
    userId: Optional[str] = None
    products: List[ProductInterface]

