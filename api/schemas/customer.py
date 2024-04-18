from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, validator
from .order_details import OrderDetail  # Assuming OrderDetail is a Pydantic model

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    address: str

    @validator('phone_number')
    def validate_phone_number(cls, v):

        if len(v) < 10:
            raise ValueError("Phone number must be at least 10 digits")
        return v

class CustomerCreate(CustomerBase):
    pass  

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    id: int
    created_at: Optional[datetime] = None
    orders: Optional[List[OrderDetail]] = []  

    class Config:
        orm_mode = True

    @validator('created_at', pre=True, always=True)
    def set_created_at(cls, v):
        return v or datetime.now()
