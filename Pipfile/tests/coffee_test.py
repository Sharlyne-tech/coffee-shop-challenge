import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_name(self):
        coffee = Coffee("Americano")
        assert coffee.name == "Americano"
        
        with pytest.raises(TypeError):
            Coffee(123)
            
        with pytest.raises(ValueError):
            Coffee("A")
            
        with pytest.raises(AttributeError):
            coffee.name = "NewName"

    def test_orders(self):
        coffee = Coffee("Latte")
        customer = Customer("Eve")
        order = Order(customer, coffee, 5.0)
        assert order in coffee.orders()

    def test_customers(self):
        coffee = Coffee("Espresso")
        customer1 = Customer("Frank")
        customer2 = Customer("Grace")
        Order(customer1, coffee, 3.0)
        Order(customer2, coffee, 3.5)
        Order(customer1, coffee, 4.0)
        assert len(coffee.customers()) == 2
        assert customer1 in coffee.customers()
        assert customer2 in coffee.customers()

    def test_num_orders(self):
        coffee = Coffee("Cappuccino")
        assert coffee.num_orders() == 0
        customer = Customer("Henry")
        Order(customer, coffee, 4.5)
        Order(customer, coffee, 5.0)
        assert coffee.num_orders() == 2

    def test_average_price(self):
        coffee = Coffee("Mocha")
        customer = Customer("Ivy")
        Order(customer, coffee, 5.0)
        Order(customer, coffee, 7.0)
        assert coffee.average_price() == 6.0
        coffee2 = Coffee("Flat White")
        assert coffee2.average_price() == 0