from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
# Create your models here.

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
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    capacity = models.PositiveIntegerField() # maximum number of products that can be stored
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
        super(Warehouse, self).save(*args, **kwargs)

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