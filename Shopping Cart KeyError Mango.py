class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self, item_name, quantity, price):
        self.items[item_name] = quantity
        cost_of_the_added_item = quantity * price
        self.total += cost_of_the_added_item

    def remove_item(self, item_name, quantity, price):
        if quantity >= self.items[item_name]:
            num_items = self.items[item_name]
            self.total -= num_items * price
            del self.items[item_name]
        else:
            num_items = quantity
            self.total -= num_items * price
            self.items[item_name] -= quantity

    def checkout(self, cash_paid):
        if cash_paid < self.total:
            return "Cash paid not enough"
        else:
            balance = cash_paid - self.total
            return balance


class Shop(ShoppingCart):
    def __init__(self):
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1