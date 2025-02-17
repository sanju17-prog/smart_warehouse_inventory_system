from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import CustomUser
# Create your views here.

class EmployeeViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()