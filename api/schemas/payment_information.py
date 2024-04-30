from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PaymentInformationBase(BaseModel):
    id: int

class PaymentInformationCreate(PaymentInformationBase):
    customer_id: Optional[int] = None
    card_information: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None

class PaymentInformationUpdate(BaseModel):
    customer_id: Optional[int] = None
    card_information: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None

class PaymentInformation(PaymentInformationBase):
    id: int
    class Config:
        from_attributes = True
