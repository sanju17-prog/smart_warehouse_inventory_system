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

CATEGORY_WAREHOUSE_MAP = {
    "Bulk & Containerized Cargo": ["Bulk Storage & Distribution Center"],
    "Chemicals & Hazardous Materials": ["Hazardous Material Warehouse"],
    "Fuel & Energy Logistics": ["Fuel & Energy Material Warehouse"],
    "Perishables & Cold Chain Logistics": ["Cold Storage Warehouse"],
    "Industrial Goods & Equipment": ["General Purpose Warehouse"],
}

def seed_stock_product_qty(n = 1000):
    products_by_category = {
        category: list(Product.objects.filter(category__name=category))
        for category in CATEGORY_WAREHOUSE_MAP.keys()
    }
    
    stocks_by_warehouse = {
        warehouse: list(Stock.objects.filter(warehouse__warehouse_type__name=warehouse))
        for warehouses in CATEGORY_WAREHOUSE_MAP.values()
        for warehouse in warehouses
    }

    for _ in range(n):
        category = random.choice(list(CATEGORY_WAREHOUSE_MAP.keys()))
        warehouse_types = CATEGORY_WAREHOUSE_MAP[category]
        valid_stocks = sum([stocks_by_warehouse.get(w, []) for w in warehouse_types], [])
        valid_products = products_by_category.get(category, [])

        if not valid_stocks or not valid_products:
            continue  # Skip if no valid stock or product

        stock_product = StockProductQty.objects.create(
            stock=random.choice(valid_stocks),
            product=random.choice(valid_products),
            batch_no=None,  # Let model generate it
            quantity=random.randint(1000, 10000),
        )
        
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
