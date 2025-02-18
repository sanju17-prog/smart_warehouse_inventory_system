from inventory.models.fleet_models import Fleet, FleetMovement
from inventory.models.warehouse_models import Warehouse
from django_filters import rest_framework as filters

class FleetFilter(filters.FilterSet):
    fleet_code = filters.CharFilter(lookup_expr='icontains')
    fleet_type = filters.ChoiceFilter(choices = Fleet.Model)
    capacity_range = filters.BaseRangeFilter(field_name='capacity')
    status = filters.ChoiceFilter(choices = Fleet.Status)

    class Meta:
        model = Fleet
        fields = ['fleet_code','fleet_type','capacity_range','status']

class FleetMovementFilter(filters.FilterSet):
    fleet = filters.ModelChoiceFilter(queryset = Fleet.objects.all())
    source = filters.ModelChoiceFilter(queryset = Warehouse.objects.all())
    destination = filters.ModelChoiceFilter(queryset = Warehouse.objects.all())
    current_location_checkpoint = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FleetMovement
        fields = ['fleet__fleet_code','source__name','destination__name','current_location_checkpoint']