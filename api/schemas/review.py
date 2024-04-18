from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator

class ReviewBase(BaseModel):
    note: str
    score: str  

    @validator('score')
    def validate_score(cls, v):
       
        if v not in ['A', 'B', 'C', 'D', 'E', 'F']:
            raise ValueError("Score must be a single letter from A to F")
        return v

class ReviewCreate(ReviewBase):
    order_id: int  # Must be provided when creating a review

class ReviewUpdate(BaseModel):
    note: Optional[str] = None
    score: Optional[str] = None

class ReviewOut(ReviewBase):
    id: int
    order_id: int
    created_at: datetime

    class Config:
        orm_mode = True
