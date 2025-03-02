from django.db import models
from . import warehouse_models
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError

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
    

def default_departure_time():
    return timezone.now() + timedelta(hours=2)

class FleetMovement(models.Model):
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    '''
    here it shows, how many products are moved in or out.
    while in stock table, only current quantity of stock is stored.
    '''
    source = models.ForeignKey(warehouse_models.Warehouse, related_name="from_warehouse", on_delete=models.CASCADE, null=True, blank=True)
    destination = models.ForeignKey(warehouse_models.Warehouse, related_name="to_warehouse", on_delete=models.CASCADE, null=True, blank=True)
    arrival_time = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(default= default_departure_time) # by default product will reach to destination in 2 hours
    current_location_checkpoint = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.unique_slug_field()
        # Validate stock movement before saving
        try:
            self.update_warehouse_current_stock()
        except ValueError as e:
            raise ValidationError(str(e))
            # Raise a validation error to prevent saving

        # If validation passes, then update status and proceed with saving
        self.update_fleet_availability_status()
        super(FleetMovement, self).save(*args, **kwargs)

    def update_fleet_availability_status(self):
        latest_movement = FleetMovement.objects.filter(fleet=self.fleet).order_by('-arrival_time').first()
        if latest_movement < timezone.now():
            self.fleet.status = self.fleet.Status.AVAILABLE
        else:
            self.fleet.status = self.fleet.Status.IN_USE

    def update_warehouse_current_stock(self):
        '''
        Update given warehouse's current stock if stock movement is possible
        '''

        stock_product_qty = apps.get_model('inventory', 'StockProductQty')  # Lazy import

        # Get total stock available in source warehouse
        total_stock = stock_product_qty.objects.filter(stock__warehouse = self.source).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        
        if self.quantity > total_stock:
            raise ValidationError(f"Stock movement denied! {self.source} doesn't have enough stock.")

        # Check if source warehouse threshold is maintained
        if (self.source.current_stock - self.quantity) < self.source.threshold:
            raise ValidationError(
                f"Stock movement denied! Moving {self.quantity} units would drop {self.source}'s " + 
                f"stock below its threshold ({self.source.threshold})."
            )

        # Check if destination warehouse capacity is maintained
        if (self.destination.current_stock + self.quantity) > self.destination.capacity:
            raise ValidationError(
                f"Stock movement denied! Moving {self.quantity} units would exceed {self.destination}'s capacity"
            )

        # Check if fleet can carry the quantity
        if self.quantity > self.fleet.capacity:
            raise ValidationError(f"Stock movement denied! {self.fleet} cannot carry more than {self.fleet.capacity} units.")

        # Deduct stock in FIFO order
        remaining_qty = self.quantity
        stock_batches = stock_product_qty.objects.filter(stock__warehouse = self.source).order_by('manufacture_date')

        for batch in stock_batches:
            if remaining_qty <= 0:
                break

            if batch.quantity >= remaining_qty:
                batch.quantity -= remaining_qty
                batch.save()
                remaining_qty = 0
            else:
                remaining_qty -= batch.quantity
                batch.quantity = 0
                batch.save()
        
        self.source.current_stock -= self.quantity
        self.destination.current_stock += self.quantity
        self.source.save()
        self.destination.save()

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
    