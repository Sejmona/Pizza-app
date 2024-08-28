class Sales:
    def __init__(self):
        self.sales = []

    def record_sale(self, order):
        self.sales.append(order)
        order.pizzas.clear()  # Vyprázdnění objednávky po zaplacení

    def get_sales_summary(self):
        summary = [str(order) for order in self.sales]
        return '\n'.join(summary)

