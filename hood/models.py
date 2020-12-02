from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
# Create your models here.

class User(AbstractUser):
    pass

