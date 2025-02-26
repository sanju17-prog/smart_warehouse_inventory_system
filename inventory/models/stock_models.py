from django.db import models
from . import product_models
from . import warehouse_models
from . import fleet_models
from users.models import CustomUser


class Stock(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    warehouse = models.ForeignKey(warehouse_models.Warehouse, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Stock, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        self.slug =  f"{self.warehouse.name}"
        ''' if already slug exists '''
        num = 1
        while Stock.objects.filter(slug = self.slug).exists():
            self.slug += str(num)
            num += 1
        return self.slug

    def __str__(self):
        return f"{self.warehouse.name})"
    
class StockProductQty(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    product = models.ForeignKey(product_models.Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(StockProductQty, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        self.slug =  f"{self.product.sku_code}-{self.product.name}"
        ''' if already slug exists '''
        num = 1
        while StockProductQty.objects.filter(slug = self.slug).exists():
            self.slug += str(num)
            num += 1
        return self.slug

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

class StockMovement(models.Model):
    class MovementType(models.TextChoices):
        IN = "in", "In"
        OUT = "out", "Out"
    stock = models.ForeignKey(StockProductQty, on_delete=models.CASCADE)
    batch_no = models.CharField(max_length=100, default='no_assign_0000')
    quantity = models.IntegerField()
    '''
    here it shows, how many products are moved in or out.
    while in stock table, only current quantity of stock is stored.
    '''
    warehouse = models.ForeignKey(warehouse_models.Warehouse, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MovementType.choices)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fleet = models.ForeignKey(fleet_models.Fleet, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(StockMovement, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        self.slug =  f"{self.stock.product.sku_code}-{self.stock.product.name}-{self.movement_type}"
        ''' if already slug exists '''
        num = 1
        while StockMovement.objects.filter(slug = self.slug).exists():
            self.slug += str(num)
            num += 1
        return self.slug

    def __str__(self):
        return f"{self.stock.product.name} ({self.quantity})"