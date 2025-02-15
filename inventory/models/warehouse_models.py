from django.db import models
from users.models import CustomUser
# Create your models here.

class WarehouseType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    capacity = models.PositiveIntegerField() # maximum number of products that can be stored
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    warehouse_type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE)
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
    
    def __str__(self):
        return self.name
    
class WarehouseEmployee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee_id', 'warehouse')
    
    def __str__(self):
        return f"{self.user.username} ({self.employee_id})"