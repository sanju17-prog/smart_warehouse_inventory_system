from ..models.warehouse_models import Warehouse, WarehouseEmployee, WarehouseType
from django.contrib.admin import ModelAdmin

class WarehouseAdmin(ModelAdmin):
    list_display = ['name', 'address', 'latitude', 'longitude', 'capacity', 'created_at', 'updated_at', 'warehouse_type', 'is_active', 'total_stock_value']

    def formatted_warehouse_type(self, obj):
        return obj.warehouse_type.name
    formatted_warehouse_type.short_description = 'Warehouse Type'

class WarehouseTypeAdmin(ModelAdmin):
    list_display = ['name', 'created_at']

class WarehouseEmployeeAdmin(ModelAdmin):
    list_display = ['employee', 'warehouse', 'assigned_at']

    def formatted_employee(self, obj):
        return obj.employee.name
    formatted_employee.short_description = 'Employee'

    def formatted_warehouse(self, obj):
        return obj.warehouse.name
    formatted_warehouse.short_description = 'Warehouse'