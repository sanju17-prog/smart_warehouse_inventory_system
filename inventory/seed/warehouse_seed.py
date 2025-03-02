from faker import Faker
faker = Faker()
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

def generate_address():
    # Dictionary of 20 Indian PIN codes mapped to city and state
    indian_locations = {
        "110001": ("New Delhi", "Delhi"),
        "400001": ("Mumbai", "Maharashtra"),
        "560001": ("Bangalore", "Karnataka"),
        "600001": ("Chennai", "Tamil Nadu"),
        "500001": ("Hyderabad", "Telangana"),
        "700001": ("Kolkata", "West Bengal"),
        "411001": ("Pune", "Maharashtra"),
        "380001": ("Ahmedabad", "Gujarat"),
        "302001": ("Jaipur", "Rajasthan"),
        "682001": ("Kochi", "Kerala"),
        "452001": ("Indore", "Madhya Pradesh"),
        "641001": ("Coimbatore", "Tamil Nadu"),
        "144001": ("Jalandhar", "Punjab"),
        "208001": ("Kanpur", "Uttar Pradesh"),
        "226001": ("Lucknow", "Uttar Pradesh"),
        "831001": ("Jamshedpur", "Jharkhand"),
        "492001": ("Raipur", "Chhattisgarh"),
        "180001": ("Jammu", "Jammu & Kashmir"),
        "248001": ("Dehradun", "Uttarakhand"),
        "795001": ("Imphal", "Manipur"),
    }

    attempts = 0
    while attempts < 20:
        pin_code, city_state = random.choice(list(indian_locations.items()))
        city, state = city_state
        address = f"{faker.building_number()}, {faker.street_name()}, {city}, {state}, {pin_code}"

        if not Warehouse.objects.filter(address=address).exists():
            return address
        
        attempts += 1
    
    raise ValueError("Max attempts reached! Unable to generate a unique address.")

def generate_unique_name():
    attempts  = 0
    while attempts < 20:
        name = faker.name()
        
        if not Warehouse.objects.filter(name=name).exists():
           return name
        attempts += 1

    raise ValueError("Max attempts reached! Unable to generate a unique name.")

def seed_warehouse(n = 10):
    for _ in range(n):
        warehouse_types = WarehouseType.objects.all()
        warehouse_type = random.choice(warehouse_types)
        
        warehouse = Warehouse.objects.create(
            warehouse_type = warehouse_type,
            name = generate_unique_name(),
            address = generate_address(),
            capacity = faker.random_int(min=2000, max=1000000),
            threshold = faker.random_int(min=2000, max=10000)
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