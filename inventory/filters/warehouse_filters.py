from django_filters import rest_framework as filters
import django_filters
import django_filters.widgets
from inventory.models.warehouse_models import Warehouse, WarehouseEmployee, WarehouseType
from users.models import CustomUser

class WarehouseTypeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = WarehouseType
        fields = ['name']

class WarehouseFilter(filters.FilterSet):
    warehouse_type = filters.ModelChoiceFilter(queryset = WarehouseType.objects.all())
    name = filters.CharFilter(lookup_expr='icontains')
    address = filters.CharFilter(lookup_expr='icontains')
    capacity = filters.NumberFilter(field_name='capacity',lookup_expr='range')
    is_active = filters.BooleanFilter(field_name='is_active', widget = django_filters.widgets.BooleanWidget)
    total_stock_value = filters.RangeFilter(field_name='total_stock_value')

    class Meta:
        model = Warehouse
        fields = ['warehouse_type','address','capacity','is_active','total_stock_value']

class WarehouseEmployeeFilter(filters.FilterSet):
    employee = filters.ModelChoiceFilter(queryset = CustomUser.objects.all())
    warehouse = filters.ModelChoiceFilter(queryset = Warehouse.objects.all())
    assigned_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = WarehouseEmployee
        fields = ['employee','warehouse','assigned_at']