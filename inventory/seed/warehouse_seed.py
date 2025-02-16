from faker import Faker
faker = Faker("en_IN") # ensures Indian location
import random
from ..models.warehouse_models import Warehouse, WarehouseEmployee, WarehouseType
from ...users.models import CustomUser

WAREHOUSE_CHOICES = [
    'General Purpose Warehouse', # Industrial Goods & Equipments
    'Cold Storage Warehouse', # Perishables & Cold Chain Logistics
    'Bulk Storage & Distribution Center', # Bulk & Containerized Cargo
    'Fuel & Hazardous Material Warehouse' # Fuel & Energy Logistics, Pharmaceuticals & Vaccines
]

def seed_warehouse_types(n = 4):
    for _ in range(n):
        WarehouseType.objects.create(
            name = random.choice(WAREHOUSE_CHOICES)
        )

def seed_warehouse(n = 10):
    for _ in range(n):
        city = faker.city()
        state = faker.state()
        pincode = faker.postal_code()
        street = faker.street_address()
        address = f"{street}, {city}, {state}, {pincode}"
        warehouse_types = WarehouseType.objects.all()
        warehouse_type = random.choice(warehouse_types)
        warehouse = Warehouse.objects.create(
            warehouse_types = faker.random_element(elements=warehouse_types),
            name = f"{warehouse_type.name} - {city}",
            address = address,
            latitude = faker.latitude(),
            longitude = faker.longitude(),
            capacity = faker.random_int(min=2000, max=1000000)
        )
        warehouse.save()

def seed_warehouse_employees(n = 10000):
    users = CustomUser.objects.all()
    warehouses = Warehouse.objects.all()
    for _ in range(n):
        employee = random.choice(users)
        warehouse = random.choice(warehouses)
        employee_id = f"EMP-{faker.random_int(min=1000,max=99999)}"
        WarehouseEmployee.objects.create(
            emp_id = employee_id,
            employee = employee,
            warehouse = warehouse,
            assigned_at = faker.date_between(start_date="-24y", end_date="today")
        )