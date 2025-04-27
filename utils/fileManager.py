import json
from models.order import Order
from models.pizza import Pizza
from models.topping import Topping

class FileManager:
    @staticmethod
    def save_order(order: Order, filename="orders.json"):
        try:
            orders = FileManager.load_orders(filename)
        except FileNotFoundError:
            orders = []

        orders.append(FileManager.order_to_dict(order))

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(orders, file, ensure_ascii=False, indent=4)

    @staticmethod
    def load_orders(filename="orders.json"):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def order_to_dict(order: Order):
        return {
            "id": order.id,
            "customer_name": order.customer_name,
            "created_at": order.created_at.isoformat(),
            "pizzas": [
                {
                    "name": pizza.name,
                    "base_price": pizza.base_price,
                    "toppings": [
                        {"name": t.name, "price": t.price}
                        for t in pizza.toppings
                    ]
                } for pizza in order.pizzas
            ]
        }
