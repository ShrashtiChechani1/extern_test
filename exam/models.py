from django.db import models
from django.contrib.auth.models import User
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Role1', 'Role1'),
        ('Role2', 'Role2'),
        ('Role3', 'Role3'),
    )
    user_role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    # Add any other fields specific to UserProfile

    def __str__(self):
        return self.email

class Permission(models.Model):
    permission_name  = models.TextField(null=True,unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    end_point = models.TextField(null=True,default=[])