from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int

    class ConfigDict:
        from_attributes = True