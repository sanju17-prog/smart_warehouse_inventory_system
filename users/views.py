from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .permissions import IsAdminOrStaffOrManager
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination
from .filters import CustomUserFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db.models import Q, Case, When, IntegerField
# Create your views here.

class EmployeeViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrStaffOrManager]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CustomUserFilter
    ordering_fields = ['employee_id','first_name','last_name','username','mobile_number','role','email']
    lookup_field = 'slug'

    def get_queryset(self):
        user = self.request.user
        base_queryset = CustomUser.objects.all()

        if user.is_admin():
            queryset = base_queryset
        elif user.is_manager():
            queryset = base_queryset.filter(
                Q(role = CustomUser.Role.STAFF) | 
                Q(id = user.id)
            )
        else:
            queryset = base_queryset.filter(id = user.id)

        return queryset.order_by(
            Case(
                When(id = user.id, then=0),
                default=1,
                output_field=IntegerField(),
            ),
        )