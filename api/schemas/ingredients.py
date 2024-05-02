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

class IngredientUpdate(IngredientBase):
    name: str = Field(None, example="Sugar", description="Name of the ingredient")
    amount: int = Field(None, example=100, description="Amount of the ingredient in grams")
