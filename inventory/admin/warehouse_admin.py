from django.contrib.admin import ModelAdmin
from users.models import CustomUser

class WarehouseAdmin(ModelAdmin):
    list_display = ['name', 'address', 'latitude', 'longitude', 'capacity', 'created_at', 'updated_at', 'warehouse_type', 'is_active', 'current_stock', 'threshold']
    ordering_fields = ['name', 'address', 'capacity', 'current_stock', 'threshold', 'created_at', 'updated_at', 'warehouse_type', 'is_active']
    search_fields = ['name', 'address', 'capacity', 'warehouse_type__name', 'current_stock', 'threshold']
    list_per_page = 20

    def formatted_warehouse_type(self, obj):
        return obj.warehouse_type.name
    formatted_warehouse_type.short_description = 'Warehouse Type'

class WarehouseTypeAdmin(ModelAdmin):
    list_display = ['name', 'created_at']
    ordering_fields =  ['name', 'created_at']
    search_fields = ['name']
    list_per_page = 20

class WarehouseEmployeeAdmin(ModelAdmin):
    list_display = ['employee', 'employee__role', 'warehouse', 'assigned_at']
    ordering_fields = ['employee', 'warehouse', 'assigned_at']
    search_fields = ['employee__name', 'employee__role', 'warehouse__name']
    list_filter = ['employee__role']
    list_per_page = 20
    

    def formatted_employee(self, obj):
        return obj.employee.name
    formatted_employee.short_description = 'Employee'

    def formatted_warehouse(self, obj):
        return obj.warehouse.name
    formatted_warehouse.short_description = 'Warehouse'