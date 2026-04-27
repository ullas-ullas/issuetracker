from django.db import models
from user.models import CustomUser
from department.models import Department
from django.conf import settings

# Create your models here.

user = settings.AUTH_USER_MODEL

class Issue(models.Model):

    status_choices = [("OPEN", "Open"), ("IN_PROGRESS", "In progress"), ("CLOSED", "Closed")]
    priority_choices = [("LOW", "Low"), ("MEDIUM", "Medium"), ("HIGH", "High")]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices=status_choices, max_length=20)
    priority = models.CharField(choices=priority_choices, max_length=10, default="MEDIUM")
    created_by = models.ForeignKey(user, on_delete=models.CASCADE, related_name="created_issues")
    assigned_to = models.ForeignKey(user, on_delete=models.SET_NULL, blank=True, null=True, related_name="assigned_issues")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="issues")
    is_escalated = models.BooleanField(default=False)
    due_time = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title