class Order:
    def __init__(self, items, total_amount):
        self.items = items
        self.total_price = total_amount

    def get_price(self):
        result = 0
        for item in self.items:
            result += item.price

        return result