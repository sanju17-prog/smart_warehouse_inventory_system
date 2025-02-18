from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.viewsets.fleet_viewset import FleetViewSet, FleetMovementViewSet

route = DefaultRouter()

route.register(r"fleet", FleetViewSet, basename="fleet")
route.register(r"fleet-movement", FleetMovementViewSet, basename="fleet_movement")

urlpatterns = [
    path("fleet/", include(route.urls))
]
