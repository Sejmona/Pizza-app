class Pizza:
    def __init__(self, name, price, toppings=None):
        self.name = name
        self.price = price
        self.toppings = toppings if toppings else []

    def add_topping(self, topping):
        self.toppings.append(topping)
        self.price += topping.price

    def __str__(self):
        topping_names = ', '.join([topping.name for topping in self.toppings])
        return f"{self.name} - ${self.price:.2f} (Toppings: {topping_names})"
