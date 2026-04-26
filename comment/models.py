from django.db import models
from django.conf import settings
from issue.models import Issue

# Create your models here.

User = settings.AUTH_USER_MODEL

class Comment(models.Model):
    # issue = models.foreign
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message