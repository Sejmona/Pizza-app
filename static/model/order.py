class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total(self):
        return sum(pizza.price for pizza in self.pizzas)

    def __str__(self):
        return "\n".join([str(pizza) for pizza in self.pizzas])
