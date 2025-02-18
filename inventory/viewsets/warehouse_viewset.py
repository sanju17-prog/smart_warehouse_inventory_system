from rest_framework.viewsets import ModelViewSet
from inventory.models.warehouse_models import Warehouse, WarehouseType, WarehouseEmployee
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsAdminOrManager
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from inventory.serializers.warehouse_serializer import WarehouseSerializer, WarehouseTypeSerializer, WarehouseEmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from inventory.filters.warehouse_filters import WarehouseFilter, WarehouseTypeFilter, WarehouseEmployeeFilter
from inventory.permissions import GeneralPermission

class WarehouseTypeViewset(ModelViewSet):
    queryset = WarehouseType.objects.all()
    serializer_class = WarehouseTypeSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = WarehouseTypeFilter
    ordering_fields = ['name']

    def get_permissions(self):
        if self.action in ["create","update","partial_update","delete"]:
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            permission_classes = [IsAuthenticated, IsAdminOrManager]
        return [permission() for permission in permission_classes]
    
class WarehouseViewset(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = WarehouseFilter
    ordering_fields = ['warehouse_type', 'name', 'address', 'capacity', 'is_active']
    permission_classes = [GeneralPermission]
    
class WarehouseEmployeeViewset(ModelViewSet):
    queryset = WarehouseEmployee.objects.all()
    serializer_class = WarehouseEmployeeSerializer
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = WarehouseEmployeeFilter
    ordering_fields = ['employee','warehouse','assigned_at']
    permission_classes = [GeneralPermission]
    

