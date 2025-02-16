from .models import CustomUser
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db.models.signals import post_save

@receiver(post_save, sender = CustomUser)
def assign_user_group(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'admin':
            group, _ = Group.objects.get_or_create(name = "Admin")
        elif instance.role == 'manager':
            group, _ = Group.objects.get_or_create(name = "Manager")
        else:
            group, _ = Group.objects.get_or_create(name = "Staff")
        instance.groups.add(group)