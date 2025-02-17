from rest_framework.viewsets import ModelViewSet
from users.models import CustomUser
from users.permissions import IsAdmin, IsAdminOrStaffOrManager, IsManager, IsStaff
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination