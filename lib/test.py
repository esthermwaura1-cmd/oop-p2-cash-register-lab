from cash_register import CashRegister

register = CashRegister(20)

register.add_item("Laptop", 50000, 1)
register.add_item("Mouse", 3000, 2)

print(register.total)

register.apply_discount()

print(register.total)

register.void_last_transaction()

print(register.total)
print(register.items)