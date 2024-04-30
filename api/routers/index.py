from . import orders, order_details, payment_information, promotion


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(payment_information.router)
    app.include_router(promotion.router)
