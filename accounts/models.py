from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_maker = models.BooleanField(default=False)
    is_checker = models.BooleanField(default=False)

class Maker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    file = models.FileField()
    description= models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)                                                                                      
    modified_at = models.DateTimeField(auto_now=True)   

class Comment(models.Model):
    Post = models.ForeignKey(Maker, on_delete=models.CASCADE)
    comments = models.CharField(max_length=120)
    created_on = models.DateTimeField(auto_now_add=True)                                                                                      
    modified_at = models.DateTimeField(auto_now=True)   
    name= models.CharField(max_length=120, blank=True)