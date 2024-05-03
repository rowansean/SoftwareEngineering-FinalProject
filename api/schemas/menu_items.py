from pydantic import BaseModel, Field

class MenuItemBase(BaseModel):
    name: str = Field(..., example="Burger")
    price: float = Field(..., example=9.99, description="Price of the menu item in USD")
    calories: int = Field(..., example=500, description="Calories of the menu item")
    category: str = Field(..., example="Entree", description="Category of the menu item")
      
class MenuItemCreate(MenuItemBase):
    pass

class MenuItemRead(MenuItemBase):
    id: int

    class Config:
        orm_mode = True