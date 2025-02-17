from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.viewsets.fleet_viewset import FleetViewSet, FleetMovementViewSet

route = DefaultRouter()

route.register("fleet", FleetViewSet, basename="fleet")
route.register("fleet_movement", FleetMovementViewSet, basename="fleet_movement")

urlpatterns = [
    path("", include(route.urls))
]
