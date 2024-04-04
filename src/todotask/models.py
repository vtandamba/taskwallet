from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
