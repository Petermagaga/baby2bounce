from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    health_conditions = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    job_type = models.CharField(max_length=255, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_groups',  # Change this name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_permissions',  # Change this name
        blank=True
    )

    def __str__(self):
        return self.username
