from inventory.models.stock_models import Stock, StockMovement, StockProductQty
from faker import Faker
import random
from inventory.models.product_models import Product
from inventory.models.warehouse_models import Warehouse
from users.models import CustomUser
from inventory.models.fleet_models import Fleet
faker = Faker()

def seed_stocks(n = 1000):
    warehouses = Warehouse.objects.all()
    for _ in range(n):
        stock = Stock.objects.create(
            warehouse = faker.random_element(elements = warehouses)
        )
        stock.save()
        print(f'Stock {stock} created')
    
def seed_stock_product_qty(n = 1000):
    stocks = Stock.objects.all()
    products = Product.objects.all()

    for _ in range(n):
        stock_product = StockProductQty.objects.create(
            stock = random.choice(stocks),
            product = random.choice(products),
            batch_no = None, # Let model generate it
            quantity = random.randint(1000, 10000)
        )

        stock_product.save()
        print(f"{stock_product.batch_no} created!!")

def seed_stock_movements(n = 1000):
    stocks = Stock.objects.all()
    users = CustomUser.objects.all()
    fleets = Fleet.objects.all()
    for _ in range(n):
        stock_movement = StockMovement.objects.create(
            stock = faker.random_element(elements = stocks),
            user = faker.random_element(elements = users),
            reason = faker.sentences(),
            fleet = faker.random_element(fleets)
        )
        stock_movement.save()
        print(f'Stock Movement {stock_movement.stock.product.name} created')
