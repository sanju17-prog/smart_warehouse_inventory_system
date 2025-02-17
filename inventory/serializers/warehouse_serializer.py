from inventory.models.warehouse_models import Warehouse, WarehouseEmployee, WarehouseType
from rest_framework import serializers
from inventory.models.warehouse_models import Warehouse

class WarehouseTypeSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    class Meta:
        model = WarehouseType
        fields = ['name','created_at']

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['name','address','latitude','longitude','capacity','is_active','total_stock_value']
    
    # def get_total_stock_value(self):
