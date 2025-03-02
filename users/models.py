from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.utils.text import slugify
import random

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        if not username:
            raise ValueError("The Username field must be set")
        
        email = self.normalize_email(email)
        extra_fields.setdefault("role", CustomUser.Role.STAFF)  # Default role is 'staff'
        extra_fields.setdefault("employee_id", self.generate_unique_employee_id()) # Ensure unique ID

        user = self.model(username = username, email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("role", CustomUser.Role.ADMIN)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("employee_id", self.generate_unique_employee_id())

        return self.create_user(username, email, password, **extra_fields)

    def generate_unique_employee_id(self):
        while True:
            emp_id = f"EMP-{random.randint(1000, 99999)}"
            if not CustomUser.objects.filter(employee_id=emp_id).exists():
                return emp_id

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        MANAGER = "manager", "Manager"
        STAFF = "staff", "Staff"
    employee_id = models.CharField(max_length=10, unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STAFF)
    slug = models.SlugField(unique=True, blank=True,null=True)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    '''
    this is required because, we are using a custom user model, 
    AbstractUser inherits from PermissionsMixin, which includes the groups and user_permissions fields.
    Since you're using a custom user model, Django expects you to handle these fields properly.
    '''

    objects = CustomUserManager()  # Assign custom manager


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        if not self.employee_id:
            self.employee_id = CustomUser.objects.generate_unique_employee_id()
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.employee_id})"
    
    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    def is_manager(self):
        return self.role == self.Role.MANAGER
    