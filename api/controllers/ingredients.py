from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.ingredients import Ingredient  

router = APIRouter()

@router.post("/ingredients/", response_model=Ingredient, status_code=status.HTTP_201_CREATED)
def create_ingredient(ingredient: Ingredient, db: Session = Depends(get_db)):
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient

@router.get("/ingredients/{ingredient_id}", response_model=Ingredient)
def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

@router.put("/ingredients/{ingredient_id}", response_model=Ingredient)
def update_ingredient(ingredient_id: int, updated_ingredient: Ingredient, db: Session = Depends(get_db)):
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    ingredient.name = updated_ingredient.name
    ingredient.amount = updated_ingredient.amount
    db.commit()
    return ingredient

@router.delete("/ingredients/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    db.delete(ingredient)
    db.commit()
    return {"ok": True}
