from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers.ingredients import create_ingredient, get_ingredient, update_ingredient, delete_ingredient
from ..schemas.ingredients import IngredientCreate, IngredientRead, IngredientUpdate

router = APIRouter()

@router.post("/ingredients/", response_model=IngredientRead, status_code=status.HTTP_201_CREATED)
def create_ingredient_route(ingredient: IngredientCreate, db: Session = Depends(get_db)):
    return create_ingredient(db, ingredient)

@router.get("/ingredients/{ingredient_id}", response_model=IngredientRead)
def read_ingredient_route(ingredient_id: int, db: Session = Depends(get_db)):
    return get_ingredient(db, ingredient_id)

@router.put("/ingredients/{ingredient_id}", response_model=IngredientRead)
def update_ingredient_route(ingredient_id: int, updated_ingredient: IngredientUpdate, db: Session = Depends(get_db)):
    return update_ingredient(db, ingredient_id, updated_ingredient)

@router.delete("/ingredients/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ingredient_route(ingredient_id: int, db: Session = Depends(get_db)):
    delete_ingredient(db, ingredient_id)
    return {"ok": True}
