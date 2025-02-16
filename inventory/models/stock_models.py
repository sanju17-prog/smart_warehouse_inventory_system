from django.db import models
from . import product_models
from . import warehouse_models
from users.models import CustomUser

class Stock(models.Model):
    product = models.ForeignKey(product_models.Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.product.sku_code}-{self.product.name}"
        super(Stock, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

class StockMovement(models.Model):
    class MovementType(models.TextChoices):
        IN = "in", "In"
        OUT = "out", "Out"
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
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
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.stock.product.sku_code}-{self.stock.product.name}-{self.movement_type}"
        super(StockMovement, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.stock.product.name} ({self.quantity})"