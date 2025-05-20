import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_name(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"
        
        with pytest.raises(TypeError):
            customer.name = 123
            
        with pytest.raises(ValueError):
            customer.name = ""
            
        with pytest.raises(ValueError):
            customer.name = "ThisNameIsWayTooLong"

    def test_orders(self):
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert order in customer.orders()

    def test_coffees(self):
        customer = Customer("Charlie")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Cappuccino")
        Order(customer, coffee1, 4.0)
        Order(customer, coffee2, 5.0)
        Order(customer, coffee1, 4.5)
        assert len(customer.coffees()) == 2
        assert coffee1 in customer.coffees()
        assert coffee2 in customer.coffees()

    def test_create_order(self):
        customer = Customer("Dave")
        coffee = Coffee("Mocha")
        order = customer.create_order(coffee, 6.0)
        assert order in customer.orders()
        assert order.coffee == coffee
        assert order.price == 6.0