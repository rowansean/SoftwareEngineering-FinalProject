from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PromotionBase(BaseModel):
    id: int

class PromotionCreate(PromotionBase):
    promotion_code: Optional[int] = None
    expiration_date: Optional[int] = None

class PromotionUpdate(BaseModel):
    promotion_code: Optional[int] = None
    expiration_date: Optional[int] = None 

class Promotion(PromotionBase):
    id: int
    class Config:
        from_attributes = True
