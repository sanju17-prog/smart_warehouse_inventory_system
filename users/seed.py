from faker import Faker
faker = Faker("en_IN")
from django.utils.timezone import make_aware
from datetime import datetime
import random
from django.contrib.auth import authenticate
from .models import CustomUser
from inventory.models.warehouse_models import Warehouse

EMAIL_EXTENSIONS = [
    "yahoo.com",
    "hotmail.com",
    "email.com",
    "gmail.com",
    "googlemail.com",
    "outlook.com",
    "icloud.com"
]


def generate_unique_email(first_name, last_name):
    '''Ensures unique email related to user's first name'''
    while True:
        email = f"{first_name.lower()}.{last_name.lower()}{faker.random_int(1000,9999999)}@{random.choice(EMAIL_EXTENSIONS)}"
        if not CustomUser.objects.filter(email=email).exists():
            return email
        
def generate_unique_username(first_name, last_name):
    '''Ensures unique username related to user's first name'''
    while True:
        username = f"{first_name.lower()}{last_name.lower()}{faker.random_int(min=1000,max=999999)}"
        if not CustomUser.objects.filter(username=username).exists():
            return username

def generate_unique_mobile():
    '''Ensures unique mobile num'''
    while True:
        mobile = faker.msisdn()[:10]  # Generate a 10-digit mobile number
        if not CustomUser.objects.filter(mobile_number=mobile).exists():
            return mobile
        
def generate_unique_employee_id():
    '''Ensures unique employee id'''
    while True:
        emp_id = f"EMP-{faker.random_int(1000,99999)}"
        if not CustomUser.objects.filter(employee_id = emp_id).exists():
            return emp_id

def seed_custom_user(n = 1000, batch_size = 5000):
    users = []
    for _ in range(n):
        first_name = faker.first_name()
        last_name = faker.last_name()
        random_date = faker.date_between(start_date="-30y", end_date="-10d")
        date_joined = make_aware(datetime.combine(random_date, datetime.min.time()))
        role = random.choice([role.value for role in CustomUser.Role])
        users.append(CustomUser(
            username=generate_unique_username(first_name, last_name),
            first_name=first_name,
            last_name=last_name,
            email=generate_unique_email(first_name, last_name),
            date_joined=date_joined,
            employee_id=generate_unique_employee_id(),
            mobile_number=generate_unique_mobile(),
            role=role
        ))

        if(len(users) >= batch_size):
            CustomUser.objects.bulk_create(users)
            users = []

    CustomUser.objects.bulk_create(users)

def remove_excess_admin():
    total_warehouses = Warehouse.objects.all().count()
    total_admins = CustomUser.objects.filter(role = CustomUser.Role.ADMIN)

    for user, excess_user in enumerate(total_admins):
        if user >= total_warehouses:
            excess_user.role = CustomUser.Role.STAFF
            excess_user.save()

def set_password_users():
    users = CustomUser.objects.all().exclude(username='admin')

    for user in users:
        print("Setting for " + user.first_name)
        new_password = user.last_name + "@" + user.first_name
        print(f"New password for {user.username}: {new_password}")
        print("Is user active: ",user.is_active)
        user.set_password(new_password)
        user.save()

    print("All users password set successfully!!")

def check_valid_password():
    users = CustomUser.objects.all().exclude(username='admin')
    for user in users:
        username = user.username
        password = user.last_name + "@" + user.first_name
        print(f"Trying to authenticate {username} with password: {password}")
        print("Is user active: ",user.is_active)
        user = authenticate(username=username, password=password)
        if user is not None:
            print("Successful!!")
        else:
            print("not done!!")