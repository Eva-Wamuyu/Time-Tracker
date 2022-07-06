from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Userr(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cloudinary')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class Project(models.Model):
    user = models.ForeignKey(Userr, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    time_interval = models.IntegerField(default=None)
    break_interval = models.IntegerField(default=None)
    activity = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    play_hits = models.IntegerField(default=0)
    
class Reviews(models.Model):
    user = models.ForeignKey(Userr, on_delete=models.CASCADE)
    efficiency = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    productivity = models.IntegerField(default=0)




    

