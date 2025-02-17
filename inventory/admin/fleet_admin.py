from django.contrib.admin import ModelAdmin
from ..models.fleet_models import Fleet, FleetMovement

class FleetAdmin(ModelAdmin):
    list_display = ['fleet_code', 'fleet_type', 'capacity', 'status']
    ordering = ['fleet_type','capacity','status']
    search_fields = ['fleet_type','capacity','status']
    list_per_page = 20

    def formatted_fleet_type(self, obj):
        return obj.fleet_type.name
    formatted_fleet_type.short_description = 'Fleet Type'

    def formatted_status(self, obj):
        return obj.status
    formatted_status.short_description = 'Status'

class FleetMovementAdmin(ModelAdmin):
    list_display = ['fleet', 'source', 'destination', 'current_location_checkpoint', 'latitude', 'longitude', 'arrival_time', 'departure_time']
    list_per_page = 20

    def formatted_source(self, obj):
        return obj.source.name
    formatted_source.short_description = 'Source'

    def formatted_destination(self, obj):
        return obj.destination.name
    formatted_destination.short_description = 'Destination'

    def formatted_current_location_checkpoint(self, obj):
        return obj.current_location_checkpoint.name
    formatted_current_location_checkpoint.short_description = 'Current Location Checkpoint'

    def formatted_latitude(self, obj):
        return obj.latitude
    formatted_latitude.short_description = 'Latitude'

    def formatted_longitude(self, obj):
        return obj.longitude
    formatted_longitude.short_description = 'Longitude'

    def formatted_arrival_time(self, obj):
        return obj.arrival_time
    formatted_arrival_time.short_description = 'Arrival Time'

    def formatted_departure_time(self, obj):
        return obj.departure_time
    formatted_departure_time.short_description = 'Departure Time'

