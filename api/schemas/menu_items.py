from pydantic import BaseModel, Field

class MenuItemBase(BaseModel):
    name: str = Field(..., example="Burger")
    price: float = Field(..., example=9.99, description="Price of the menu item in USD")

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemRead(MenuItemBase):
    id: int

    class Config:
        orm_mode = True
