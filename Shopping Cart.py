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
            self.total -= (self.items[item_name]) * price
            del self.items[item_name]
        else:
            self.items[item_name] -= quantity
            cost_of_the_removed_item = quantity * price
            self.total -= cost_of_the_removed_item

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




