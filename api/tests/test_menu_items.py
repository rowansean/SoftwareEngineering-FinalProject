from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import menu_items as model
from ..controllers import customer as controller
from unittest.mock import MagicMock


def test_update_menu_item(db_session):
    # Create a sample menu item
    menu_item_data = {
        "name": "Burger",
        "price": 9.99,
        "calories": 500,
        "category": "Main"
    }

    menu_item_object = model.MenuItem(**menu_item_data)

    # Add the menu item to the database
    db_session.add(menu_item_object)
    db_session.commit()

    # Update the menu item
    update_data = {
        "price": 10.99,
        "calories": 550
    }
    updated_menu_item = controller.update(db_session, menu_item_object.id, update_data)

    # Assertions
    assert updated_menu_item is not None
    assert updated_menu_item.price == 10.99
    assert updated_menu_item.calories == 550