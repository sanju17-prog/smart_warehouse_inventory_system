from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from rest_framework import serializers
class EmployeeSerializer(ModelSerializer):
    slug = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(
        view_name = "employees-detail",
        lookup_field = "slug"
    )
    class Meta:
        model = CustomUser
        fields = ['employee_id','email','username','first_name','last_name','mobile_number','role','slug','url']