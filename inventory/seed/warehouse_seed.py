from faker import Faker
faker = Faker("en_IN") # ensures Indian location
import random
from inventory.models.warehouse_models import Warehouse, WarehouseEmployee, WarehouseType
from  users.models import CustomUser
from django.utils.timezone import make_aware
from datetime import datetime

WAREHOUSE_CHOICES = [
    'General Purpose Warehouse', # Industrial Goods & Equipments
    'Cold Storage Warehouse', # Perishables & Cold Chain Logistics
    'Bulk Storage & Distribution Center', # Bulk & Containerized Cargo
    'Fuel & Hazardous Material Warehouse' # Fuel & Energy Logistics, Pharmaceuticals & Vaccines
]

def seed_warehouse_types():
    for index in range(4):
        WarehouseType.objects.create(
            name = WAREHOUSE_CHOICES[index]
        )

def seed_warehouse(n = 10):
    for _ in range(n):
        location = faker.location_on_land()
        city = location[2]
        state = location[4]
        pincode = faker.postcode()
        street = faker.street_address()
        address = f"{street}, {city}, {state}, {pincode}"
        warehouse_types = WarehouseType.objects.all()
        warehouse_type = random.choice(warehouse_types)
        warehouse = Warehouse.objects.create(
            warehouse_type = faker.random_element(elements=warehouse_types),
            name = f"{warehouse_type.name} - {city}",
            address = address,
            latitude = location[0],
            longitude = location[1],
            capacity = faker.random_int(min=2000, max=1000000)
        )
        warehouse.save()

def seed_warehouse_employees(n = 10000):
    users = CustomUser.objects.all()
    warehouses = Warehouse.objects.all()
    for _ in range(n):
        employee = random.choice(users)
        warehouse = random.choice(warehouses)
        WarehouseEmployee.objects.create(
            employee = employee,
            warehouse = warehouse,
            assigned_at = faker.date_time_between(start_date="-24y", end_date=datetime.today())
        )