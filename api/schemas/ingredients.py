from pydantic import BaseModel, Field

class IngredientBase(BaseModel):
    name: str = Field(..., example="Sugar")
    amount: int = Field(..., example=100, description="Amount of the ingredient in grams")

class IngredientCreate(IngredientBase):
    pass

class IngredientRead(IngredientBase):
    id: int

    class Config:
        orm_mode = True
