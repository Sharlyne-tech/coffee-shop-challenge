from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create some coffees
espresso = Coffee("Espresso")
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")

# Create some orders
order1 = Order(alice, espresso, 3.0)
order2 = Order(alice, latte, 4.5)
order3 = Order(bob, espresso, 3.5)
order4 = Order(bob, cappuccino, 5.0)

# Test relationships
print(f"Alice's orders: {[o.coffee.name for o in alice.orders()]}")
print(f"Bob's coffees: {[c.name for c in bob.coffees()]}")
print(f"Espresso orders: {espresso.num_orders()}")
print(f"Latte average price: {latte.average_price()}")

# Test bonus
print(f"Biggest espresso fan: {Customer.most_aficionado(espresso).name}")