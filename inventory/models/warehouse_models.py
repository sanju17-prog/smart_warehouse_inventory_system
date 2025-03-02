from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
import time
from geopy.geocoders import Nominatim
# Create your models here.

geolocator = Nominatim(user_agent="geoapi")

class WarehouseType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True,null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        super(WarehouseType, self).save(*args, **kwargs)

    def get_unique_slug(self):
        self.slug = slugify(self.name)
        num = 1
        while WarehouseType.objects.filter(slug = self.slug).exists():
            self.slug += str(num)
            num += 1
        return self.slug
    
    def __str__(self):
        return self.name

class Warehouse(models.Model):
    warehouse_type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, default="abc")
    address = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    capacity = models.PositiveIntegerField(default=0) # maximum number of products that can be stored
    current_stock = models.PositiveIntegerField(default=0) # current number of products available in warehouse
    threshold = models.PositiveIntegerField(default=0) # current number of products available in warehouse
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    '''
    warehouses might shut down or be under maintenance, so temporarily inactive.
    instead of deleting the warehouse, we can set this field to False.
    '''
    total_stock_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    '''
    we are storing it, instead of calculating it every time, to reduce the load on the database.
    as for large data, or let say frequent requests, it can be a bottleneck.
    '''
    slug = models.SlugField(max_length=200,unique=True,null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        self.latitude, self.longitude = self.get_lat_lon(self.address)
        super(Warehouse, self).save(*args, **kwargs)

    def get_lat_lon(self, address):
        time.sleep(1) # Ensures 1 request per second, so not to exceed its rate limit
        modified_address = f"{self.address}, India"
        location = geolocator.geocode(modified_address)
        if location:
            return location.latitude, location.longitude

        # If location is None, try again with just city and India
        address_parts = self.address.split(",")
        if len(address_parts) > 1:
            city = address_parts[-2].strip()
            location = geolocator.geocode(f"{city}, India")
            if location:
                return location.latitude, location.longitude
        
        # Final fallback: use a default location (e.g., New Delhi)
        return 28.6139, 77.2090  # Coordinates for New Delhi, India

    def get_unique_slug(self):
        self.slug = slugify(self.name)
        num = 1
        while Warehouse.objects.filter(slug = self.slug).exists():
            self.slug += str(num)
            num += 1
        return self.slug
    
    def __str__(self):
        return self.name
    
class WarehouseEmployee(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True,null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        super(WarehouseEmployee, self).save(*args, **kwargs)

    def get_unique_slug(self):
        self.slug = f"{self.employee.username}-{self.warehouse.name}"
        num = 1
        while WarehouseEmployee.objects.filter(slug = self.slug).exists():
            self.slug += str(num)
            num += 1
        return self.slug

    class Meta:
        unique_together = ('employee', 'warehouse')
    
    def __str__(self):
        return f"{self.employee.username} ({self.employee.employee_id})"