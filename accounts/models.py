from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_images')
    
    def __str__(self):
        return self.email
