from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        MANAGER = "manager", "Manager"
        STAFF = "staff", "Staff"
    employee_id = models.CharField(max_length=10, unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STAFF)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    '''
    this is required because, we are using a custom user model, 
    AbstractUser inherits from PermissionsMixin, which includes the groups and user_permissions fields.
    Since you're using a custom user model, Django expects you to handle these fields properly.
    '''

    def __str__(self):
        return f"{self.username} ({self.employee_id})"
    
    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    def is_manager(self):
        return self.role == self.Role.MANAGER
    