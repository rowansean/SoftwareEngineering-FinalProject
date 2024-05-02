
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.ingredients import Ingredient
from ..schemas.ingredients import IngredientCreate, IngredientRead, IngredientUpdate
from sqlalchemy.exc import SQLAlchemyError

def create_ingredient(db: Session, ingredient_data: IngredientCreate) -> IngredientRead:
    new_ingredient = Ingredient(name=ingredient_data.name, amount=ingredient_data.amount)
    try:
        db.add(new_ingredient)
        db.commit()
        db.refresh(new_ingredient)
        return new_ingredient
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

def get_ingredient(db: Session, ingredient_id: int) -> IngredientRead:
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

def update_ingredient(db: Session, ingredient_id: int, ingredient_data: IngredientUpdate) -> IngredientRead:
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    ingredient.name = ingredient_data.name
    ingredient.amount = ingredient_data.amount
    db.commit()
    return ingredient

def delete_ingredient(db: Session, ingredient_id: int):
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    db.delete(ingredient)
    db.commit()
    return True