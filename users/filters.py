from django_filters import rest_framework as filters
from users.models import CustomUser

class CustomUserFilter(filters.FilterSet):
    role = filters.ChoiceFilter(choices = CustomUser.Role.choices)
    employee_id = filters.CharFilter(lookup_expr='icontains')
    mobile_number = filters.CharFilter(lookup_expr='icontains')
    username = filters.CharFilter(lookup_expr='icontains')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CustomUser
        fields = ['role','employee_id','mobile_number','username','first_name','last_name']