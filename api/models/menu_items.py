from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "MenuItems"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    calories = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)

    ingredients = relationship("Ingredient", secondary="Ingredient", back_populates="menu_items")