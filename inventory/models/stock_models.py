from django.db import models
from django.utils import timezone
from datetime import timedelta
from users.models import CustomUser
from . import product_models
from . import warehouse_models
from . import fleet_models


class Stock(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=1000, unique=True, null=True, blank=True)
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
    batch_no = models.CharField(max_length=100, default='no_assign_0000')
    manufacture_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    quantity = models.IntegerField()
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        
        # set expiry for perishables default to 1.5 years
        if self.product.category.name == "Perishables & Cold Chain Logistics" and not self.expiry_date:
            self.expiry_date = timezone.now() + timedelta(days=547) # 1.5 years
        
        # generate batch no
        if self.batch_no is None or self.batch_no == 'no_assign_0000':
            self.batch_no = self.generate_batch_no()
        
        # update warehouse's current stock
        self.stock.warehouse.current_stock += self.quantity
        self.stock.warehouse.save()

        super(StockProductQty, self).save(*args, **kwargs)

    def generate_batch_no(self):
        category_code = self.product.category.name[:3].upper() # First 3 letters of category
        year_month = timezone.now().strftime("%Y-%m") # YYYY-MM format
        unique_id = StockProductQty.objects.filter(product=self.product).count() + 1 # Id = current product counts + 1
        return f"{category_code}-{year_month}-{unique_id}"

    def generate_unique_slug(self):
        self.slug =  f"{self.product.sku_code}-{self.product.name}"
        ''' if already slug exists '''
        num = 1
        while StockProductQty.objects.filter(slug = self.slug).exists():
            self.slug += str(num)
            num += 1
        return self.slug

    def __str__(self):
        return f"{self.product.name} - Batch {self.batch_no} ({self.quantity})"

class StockMovement(models.Model):
    stock = models.ForeignKey(StockProductQty, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reason = models.TextField(blank=True)
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