from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['employee_id','email','username','first_name','last_name','mobile_number','role']