class Pizza:
    def __init__(self, name, price, size, topping):
        self.name = name
        self.price = price
        self.size = size
        self.topping = topping

    def add_topping(self, topping):
        self.topping.append(topping)

