from django.db import models

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField()



class Task(models.Model):
    title = models.CharField(max_length=100)
    #category = models.ForeignKey(Category, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
