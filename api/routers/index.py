
from . import orders, order_details, payment_information, promotion, customer, ingredients, menu_items, review


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(payment_information.router)
    app.include_router(promotion.router)
    app.include_router(customer.router)
    app.include_router(ingredients.router)
    app.include_router(menu_items.router)
    app.include_router(review.router)
