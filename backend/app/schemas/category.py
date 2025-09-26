from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):

    name: str = Field(..., min_length=3, max_length=100)
    slug: str = Field(..., min_length=3, max_length=100)
    sort_order: int = Field(0, ge=0)
    is_active: bool = Field(True)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):

    name: Optional[str] = Field(None, min_length=1, max_length=100)
    slug: Optional[str] = Field(None, min_length=1, max_length=100)
    sort_order: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool] = None

class CategoryOut(CategoryBase):
    category_id: int

    class Config: 
        from_attributes = True