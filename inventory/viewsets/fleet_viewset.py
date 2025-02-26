from rest_framework.viewsets import ModelViewSet
from inventory.models.fleet_models import Fleet, FleetMovement
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from inventory.serializers.fleet_serializer import FleetSerializer, FleetMovementSerializer
from django_filters.rest_framework import DjangoFilterBackend
from inventory.filters.fleet_filters import FleetFilter, FleetMovementFilter
from rest_framework.filters import OrderingFilter
from inventory.permissions import StockFleetPermission

class FleetViewSet(ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = FleetFilter
    ordering_fields = ['fleet_code','fleet_type','capacity','status']
    permission_classes = [StockFleetPermission]
    
class FleetMovementViewSet(ModelViewSet):
    queryset = FleetMovement.objects.all()
    serializer_class = FleetMovementSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = FleetMovementFilter
    ordering_fields = ['fleet','source','destination','current_location_checkpoint']
    lookup_field = "slug"
    permission_classes = [StockFleetPermission]