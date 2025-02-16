from inventory.models.stock_models import Stock, StockMovement
from faker import Faker
import random
from inventory.models.product_models import Product
from inventory.models.warehouse_models import Warehouse
from users.models import CustomUser
from inventory.models.fleet_models import Fleet
faker = Faker()

def seed_stocks(n = 1000):
    for _ in range(n):
        products = Product.objects.all()
        stock = Stock.objects.create(
            product = faker.random_element(elements = products),
            quantity = random.randint(1,100000)
        )
        stock.save()
        print(f'Stock {stock.product.name} created')

def seed_stock_movements(n = 1000):
    for _ in range(n):
        stocks = Stock.objects.all()
        warehouses = Warehouse.objects.all()
        users = CustomUser.objects.all()
        fleet = Fleet.objects.all()
        stock_movement = StockMovement.objects.create(
            stock = faker.random_element(elements = stocks),
            quantity = random.randint(1, 100000),
            warehouse = faker.random_element(elements = warehouses),
            movement_type = faker.random_element(elements = ['in', 'out']),
            user = faker.random_element(elements = users),
            vehicle = faker.random_element(elements = fleet)
        )
        stock_movement.save()
        print(f'Stock Movement {stock_movement.stock.product.name} created')
