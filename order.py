from material import Material
from process import AssemblyProcess
from product import Product


class Order:
    ORDER_STATES = {
        "ORDER_RECEIVED": "Order received",
        "ORDER_STARTED": "Order in production",
        "ORDER_STALLED": "Order is on hold",
        "ORDER_FINISHED": "Order ready in production",
        "ORDER_IN_STORE": "Order ready for delivery",
        "ORDER_DELIVERED": "Order is confirmed delivered",
    }

    def __init__(self, order_id, delivery_date, customer_id, customer_name, *products):
        self.order_id = order_id
        self.delivery_date = delivery_date
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.products = products
        self.order_status = "Default state"
        self.product_finished = []

    def set_order_state(self, state):
        if state in self.ORDER_STATES:
            self.order_status = self.ORDER_STATES[state]

    def add_products_finished(self, product):
        if product not in self.products and product in self.products:
            self.product_finished.append(product)
