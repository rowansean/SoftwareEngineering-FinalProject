from sqlalchemy import Table, Column, Integer, ForeignKey
from ..dependencies.database import Base

association_table = Table(
    "menu_item_ingredient",
    Base.metadata,
    Column("menu_item_id", Integer, ForeignKey("MenuItems.id")),
    Column("ingredient_id", Integer, ForeignKey("ingredients.id")),
)