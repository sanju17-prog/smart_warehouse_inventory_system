from django.contrib import admin
from .models import CustomUser
from import_export import resources
from import_export.admin import ImportExportMixin
# Register your models here.

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['employee_id','email','username','first_name','last_name','mobile_number','role','slug']
    search_fields = ['email', 'username', 'first_name', 'last_name','role']
    ordering_fields = ['employee_id','username','first_name','mobile_number','role']
    list_per_page = 20

