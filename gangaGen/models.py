# your_app_name/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    access_code = models.CharField(max_length=50, unique=True, blank=True, null=True)

    # Specify unique related_name for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username
