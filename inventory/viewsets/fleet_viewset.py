from rest_framework.viewsets import ModelViewSet
from inventory.models.fleet_models import Fleet, FleetMovement
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsAdminOrStaffOrManager, IsAdminOrManager
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from inventory.serializers.fleet_serializer import FleetSerializer, FleetMovementSerializer

class FleetViewSet(ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination

    def get_permissions(self):
        '''
        Assign permissions based on the action.
        '''
        if self.action in ["create", "update", "partial_update", "delete"]:
            #Only admin can modify the fleet data
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            # Admins and Managers can view fleet data
            permission_classes = [IsAuthenticated, IsAdminOrManager]

        return [permission() for permission in permission_classes]
    
class FleetMovementViewSet(ModelViewSet):
    queryset = FleetMovement.objects.all()
    serializer_class = FleetMovementSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = PageNumberPagination

    def get_permissions(self):
        '''
        Assign permissions based on the action.
        '''
        if self.action in ["create", "update", "partial_update", "delete"]:
            #Only admin can modify the fleet data
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            # Admins and Managers can view fleet data
            permission_classes = [IsAuthenticated, IsAdminOrManager]

        return [permission() for permission in permission_classes]