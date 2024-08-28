class Order:
    def __init__(self):
        self.items = []

    def add_item(self, pizza):
        self.items.append(pizza)

    def clear_order(self):
        self.items = []

    def get_summary(self):
        summary = "\n".join([str(item) for item in self.items])
        return summary if summary else "No items in the order."

    def is_empty(self):
        return len(self.items) == 0
