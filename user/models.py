from django.db import models
from django.contrib.auth.models import AbstractUser
from department.models import Department

# Create your models here.

roles = [("USER", "User"), ("STAFF", "Staff"), ("SUPERVISOR", "Supervisor")]


class CustomUser(AbstractUser):
    role = models.CharField(choices=roles, max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name="users")


    def __str__(self):
        return self.username