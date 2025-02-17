from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register("employees", EmployeeViewSet, basename="employees")

urlpatterns = [
    path('', include(router.urls)),path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]