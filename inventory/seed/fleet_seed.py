from faker import Faker
faker = Faker("en-IN") # ensures Indian location
from ..models import Fleet, Warehouse, FleetMovement

def seed_fleet(n = 100):
    for _ in range(n):
        fleet = Fleet.objects.create(
            plate_number = faker.license_plate(),
            fleet_type = faker.random_element(elements = ['Ship', 'Train', 'Truck', 'Aircraft']),
            capacity = faker.random_int(min = 100, max = 1000),    
        )

        fleet.save()
        print(f'Fleet {fleet.plate_number} created')

def seed_fleet_movement(n = 100):
    for _ in range(n):
        fleets = Fleet.objects.all()
        warehouses = Warehouse.objects.all()
        fleet_movement = FleetMovement.objects.create(
            fleet = faker.random_element(elements = fleets),
            source = faker.random_element(elements = warehouses),
            destination = faker.random_element(elements= [warehouse for warehouse in warehouses if warehouse != fleet_movement.source]),
            arrival_time = faker.date_time_between(start_date = '-30d', end_date = 'now'),
            departure_time = faker.date_time_between(start_date = fleet_movement.arrival_time + 1, end_date = 'now'),
            current_location_checkpoint = faker.random_element(elements= [warehouse for warehouse in warehouses if warehouse != fleet_movement.source and warehouse != fleet_movement.destination]),
            latitude = faker.latitude(),
            longitude = faker.longitude(),
        )

        fleet_movement.save()
        print(f'Fleet Movement {fleet_movement.fleet.plate_number} created')