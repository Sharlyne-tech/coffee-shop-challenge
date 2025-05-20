import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def test_init(self):
        customer = Customer("Jack")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 4.0)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 4.0
        
        with pytest.raises(TypeError):
            Order("not a customer", coffee, 4.0)
            
        with pytest.raises(TypeError):
            Order(customer, "not a coffee", 4.0)
            
        with pytest.raises(TypeError):
            Order(customer, coffee, "4.0")
            
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
            
        with pytest.raises(ValueError):
            Order(customer, coffee, 10.5)

    def test_price_immutability(self):
        customer = Customer("Karen")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        with pytest.raises(AttributeError):
            order.price = 6.0