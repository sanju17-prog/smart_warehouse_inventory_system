from inventory.models.fleet_models import Fleet, FleetMovement
from rest_framework import serializers
from inventory.models.warehouse_models import Warehouse

class FleetSerializer(serializers.ModelSerializer):
    fleet_type = serializers.ChoiceField(choices=Fleet.Model.choices)
    status = serializers.ChoiceField(choices=Fleet.Status.choices)
    slug = serializers.ReadOnlyField()  # Ensure slug is included
    url = serializers.HyperlinkedIdentityField(
        view_name="fleet-detail", lookup_field="slug"
    )  # Generates the proper URL
    class Meta:
        model = Fleet
        fields = ['fleet_code','fleet_type','capacity','status', 'slug', 'url']

class FleetMovementSerializer(serializers.ModelSerializer):
    fleet = serializers.HyperlinkedRelatedField(
        queryset=Fleet.objects.all(),
        view_name='fleet-detail', 
        lookup_field = "slug" # The URL view name for Fleet detail (change this as needed)
    )
    source = serializers.HyperlinkedRelatedField(
        queryset=Warehouse.objects.all(),
        view_name='warehouse-detail',
        lookup_field = "slug"    # The URL view name for Warehouse detail (change this as needed)
    )
    destination = serializers.HyperlinkedRelatedField(
        queryset=Warehouse.objects.all(),
        view_name='warehouse-detail',
        lookup_field = "slug"  # The URL view name for Warehouse detail (change this as needed)
    )
    slug = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(
        view_name="fleet_movement-detail", lookup_field="slug"
    ) 
    class Meta:
        model = FleetMovement
        fields = [
            "fleet",
            "source",
            "destination",
            "arrival_time",
            "departure_time",
            "current_location_checkpoint",
            "latitude",
            "longitude",
            "slug",
            "url"
        ]
    def get_fleet(self, obj):
        return f"{obj.fleet.fleet_code} - {obj.fleet.fleet_type}"