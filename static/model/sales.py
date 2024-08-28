class Sales:
    def __init__(self):
        self.sales_data = []

    def record_sale(self, order):
        self.sales_data.append(order)

    def get_sales_summary(self):
        summary = {}
        for order in self.sales_data:
            for pizza in order.pizzas:
                summary[pizza.name] = summary.get(pizza.name, 0) + 1
        return summary
