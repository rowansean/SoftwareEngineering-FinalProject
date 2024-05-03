
from . import orders, order_details, menu_items, ingredients, customer, review, promotion, payment_information

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    payment_information.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    ingredients.Base.metadata.create_all(engine)

