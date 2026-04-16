from django.db import models

# Create your models here.

class Department(models.Model):
    dept = models.CharField(max_length=20)

    def __str__(self):
        return self.dept