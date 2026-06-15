#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.transactions = []

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.transactions.append(price)
            self.total += price

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        # match expected formatting behavior loosely
        if self.total.is_integer():
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.transactions:
            return

        last_price = self.transactions.pop()
        self.items.pop()

        self.total -= last_price

        if self.total < 0:
            self.total = 0.0