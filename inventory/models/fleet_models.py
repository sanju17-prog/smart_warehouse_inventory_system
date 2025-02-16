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
    plate_number = models.CharField(max_length=255, unique=True)
    fleet_type = models.CharField(max_length=255, choices=Model.choices)
    capacity = models.IntegerField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.AVAILABLE)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.plate_number}-{self.model}"
        super(Fleet, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.plate_number
    
class FleetMovement(models.Model):
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    source = models.ForeignKey(warehouse_models.Warehouse, on_delete=models.CASCADE, related_name='source')
    destination = models.ForeignKey(warehouse_models.Warehouse, on_delete=models.CASCADE, related_name='destination')
    arrival_time = models.DateTimeField(auto_now=True)
    departure_time = models.DateTimeField(auto_now=True)
    current_location_checkpoint = models.ForeignKey(warehouse_models.Warehouse, on_delete=models.CASCADE, related_name='current_location')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.fleet.plate_number}-{self.source.name}-{self.destination.name}"
        super(FleetMovement, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.fleet.plate_number} ({self.source.name} to {self.destination.name})"