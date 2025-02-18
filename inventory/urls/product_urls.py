from django.urls import path, include
from rest_framework.routers import DefaultRouter

route = DefaultRouter()

urlpatterns = [
    path("product/", include(route.urls))
]
