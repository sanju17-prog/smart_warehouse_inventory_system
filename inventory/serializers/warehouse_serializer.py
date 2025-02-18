from inventory.models.warehouse_models import Warehouse, WarehouseEmployee, WarehouseType
from rest_framework import serializers
from inventory.models.warehouse_models import Warehouse
from users.models import CustomUser

class WarehouseTypeSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(
        view_name = "warehouse-detail",
        lookup_field = "slug"
    )
    class Meta:
        model = WarehouseType
        fields = ['name','created_at','slug','url']

class WarehouseSerializer(serializers.ModelSerializer):
    warehouse_type = serializers.HyperlinkedRelatedField(
        queryset = WarehouseType.objects.all(),
        view_name = 'warehouse_type-detail',
        lookup_field = 'slug'
    )
    slug = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(
        view_name = "warehouse-detail",
        lookup_field = "slug"
    )
    total_stock_value = serializers.ReadOnlyField()
    latitude = serializers.ReadOnlyField()
    longitude = serializers.ReadOnlyField()
    class Meta:
        model = Warehouse
        fields = ['warehouse_type','name','address','latitude','longitude','capacity','is_active','total_stock_value','slug','url']
    
class WarehouseEmployeeSerializer(serializers.ModelSerializer):
    employee = serializers.HyperlinkedRelatedField(
        queryset = CustomUser.objects.all(),
        view_name = 'employees-detail',
        lookup_field = 'slug'
    )
    warehouse = serializers.HyperlinkedRelatedField(
        queryset = Warehouse.objects.all(),
        view_name = 'warehouse-details',
        lookup_field = 'slug'
    )
    slug = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(
        view_name="warehouse_employee-detail", lookup_field="slug"
    ) 
    class Meta:
        model = WarehouseEmployee
        fields = ['employee__first_name','warehouse__name','assigned_at','slug','url']