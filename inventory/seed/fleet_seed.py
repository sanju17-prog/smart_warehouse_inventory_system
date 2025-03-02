from faker import Faker
import random
from geopy.geocoders import Nominatim
faker = Faker("en-IN") # ensures Indian location
from inventory.models import Fleet, Warehouse, FleetMovement

geolocator = Nominatim(user_agent="inventory")

def get_unique_plate_number():
    plate_number = faker.license_plate()
    num = 1
    while Fleet.objects.filter(plate_number=plate_number).exists():
        plate_number += str(num)
        num += 1
    return plate_number

def seed_fleet(n = 100):
    for _ in range(n):
        fleet = Fleet.objects.create(
            fleet_code = get_unique_plate_number(),
            fleet_type = faker.random_element(elements = [Fleet.Model.AIRCRAFT, Fleet.Model.SHIP, Fleet.Model.TRAIN, Fleet.Model.TRUCK]),
            capacity = faker.random_int(min = 100, max = 1000),    
        )

        fleet.save()
        print(f'Fleet {fleet.plate_number} created')

fleets = Fleet.objects.all()
index = 0

def get_unique_fleet():
    global index
    fleet = fleets[index]
    while FleetMovement.objects.filter(fleet = fleet).exists():
        index += 1
        fleet = fleets[index]
    return fleet

def seed_fleet_movement(n = 100):
    for _ in range(n):
        warehouses = Warehouse.objects.all()
        source = faker.random_element(elements = warehouses)
        source_latitude = source.latitude
        source_longitude = source.longitude
        destination = faker.random_element(elements= [warehouse for warehouse in warehouses if warehouse != source])
        destination_latitude = destination.latitude
        destination_longitude = destination.longitude
        arrival_time = faker.date_time_between(start_date = '-30d', end_date = 'now')
        departure_time = faker.date_time_between(start_date = arrival_time, end_date = 'now')
        latitude = random.uniform(float(min(source_latitude, destination_latitude)), 
                                 float(max(source_latitude, destination_latitude)))
        longitude = random.uniform(float(min(source_longitude, destination_longitude)), 
                                 float(max(source_longitude, destination_longitude)))
        current_location_checkpoint = geolocator.reverse((latitude, longitude), language='en')
        fleet = get_unique_fleet()
        if current_location_checkpoint is None:
            current_location_checkpoint = ' '
        fleet_movement = FleetMovement.objects.create(
            fleet = fleet,
            quantity = random.randint(1, fleet.capacity),
            source = source,
            destination = destination,
            arrival_time = arrival_time,
            departure_time = departure_time,
            current_location_checkpoint = current_location_checkpoint,
            latitude = latitude,
            longitude = longitude,
        )

        try:
            fleet_movement.save()
            print(f'Fleet Movement {fleet_movement.fleet.fleet_code} created')
        except Exception as e:
            print(str(e))