from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['employee_id','email','username','first_name','last_name','mobile_number','role']
    search_fields = ['email', 'username', 'first_name', 'last_name','role']
    ordering = ['employee_id','username','first_name','mobile_number','role']
    list_per_page = 20
