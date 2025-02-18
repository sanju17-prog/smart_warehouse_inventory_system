from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.viewsets.warehouse_viewset import WarehouseViewset, WarehouseTypeViewset

route = DefaultRouter()

route.register(r"warehouse", WarehouseViewset, basename="warehouse")
route.register(r"warehouse-type", WarehouseTypeViewset, basename="warehouse_type")

urlpatterns = [
    path("warehouse/", include(route.urls))
]
