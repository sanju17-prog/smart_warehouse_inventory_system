from django.db import models
from . import warehouse_models

class Fleet(models.Model):
    class Model(models.TextChoices):
        SHIP = "ship", "Ship"
        TRAIN = "train", "Train"
        TRUCK = "truck", "Truck"
        AIRCRAFT = "aircraft", "Aircraft"
    class Status(models.TextChoices):
        AVAILABLE = "available", "Available"
        IN_USE = "in_use", "In Use"
    fleet_code = models.CharField(max_length=255, unique=True)
    fleet_type = models.CharField(max_length=255, choices=Model.choices)
    capacity = models.IntegerField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.AVAILABLE)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.unique_slug_field()
        super(Fleet, self).save(*args, **kwargs)

    def unique_slug_field(self):
        self.slug = f"{self.fleet_code}-{self.fleet_type}"
        '''check if already exists'''
        num = 1
        while Fleet.objects.filter(slug = self.slug).exists():
            self.slug += str(num)
            num += 1
        return self.slug
    
    def __str__(self):
        return self.fleet_code
    
class FleetMovement(models.Model):
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    source = models.ForeignKey(warehouse_models.Warehouse, on_delete=models.CASCADE, related_name='source')
    destination = models.ForeignKey(warehouse_models.Warehouse, on_delete=models.CASCADE, related_name='destination')
    arrival_time = models.DateTimeField(auto_now=True)
    departure_time = models.DateTimeField(auto_now=True)
    current_location_checkpoint = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.unique_slug_field()
        super(FleetMovement, self).save(*args, **kwargs)

    def unique_slug_field(self):
        self.slug = f"{self.fleet.fleet_code[0]}-{self.source.name[0]}-{self.destination.name[0]}"
        '''check if already exists'''
        num = 1
        while FleetMovement.objects.filter(slug = self.slug).exists():
            self.slug += str(num)
            num += 1
        return self.slug
    
    def __str__(self):
        return f"{self.fleet.fleet_code} ({self.source.name} to {self.destination.name})"
    