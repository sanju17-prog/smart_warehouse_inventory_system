from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .permissions import IsAdmin, IsManager, IsStaff, IsAdminOrStaffOrManager
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
# Create your views here.

class EmployeeViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrStaffOrManager]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_admin():
            return CustomUser.objects.all()
        elif user.is_manager():
            return CustomUser.objects.filter(
                Q(role = CustomUser.Role.STAFF) | 
                Q(id = user.id)
            )
        else:
            return CustomUser.objects.filter(id = user.id)