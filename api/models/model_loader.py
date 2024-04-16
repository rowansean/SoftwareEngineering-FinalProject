from . import orders, order_details, recipes, sandwiches, resources, customer, review

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)
