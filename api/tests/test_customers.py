from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import customer as model
from ..controllers import customer as controller
from unittest.mock import MagicMock

def test_update_customer(db_session: Session):
    # Create a sample customer
    customer_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone_number": "1234567890",
        "address": "123 Main St"
    }
    customer_object = model.Customer(**customer_data)

    # Add the customer to the database
    db_session.add(customer_object)
    db_session.commit()

    # Update the customer
    update_data = {
        "name": "Jane Smith",
        "email": "janesmith@example.com"
    }
    request = MagicMock(dict=MagicMock(return_value=update_data))
    updated_customer = controller.update_customer(db_session, customer_object.id, request)

    # Assertions
    assert updated_customer is not None
    assert updated_customer.name == "Jane Smith"
    assert updated_customer.email == "janesmith@example.com"