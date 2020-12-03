from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email

class Neighbourhood(models.Model):
    name = models.CharField(max_length=250)
    description = HTMLField()
    location = models.TextField(max_length=400)
    occupants_count = models.IntegerField(blank=True,default=0)
    healthcentre_no = models.IntegerField(blank=True)
    police_no = models.IntegerField(blank=True)
    admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save_hood(self):
        self.save()
    
    def delete_hood(self):
        self.delete()

class Business(models.Model):
    business_name = models.CharField(max_length=300)
    description = HTMLField()
    location = models.TextField(max_length=400)
    email_address = models.EmailField(max_length=400)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    hood = models.ForeignKey('Neighbourhood',on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name
    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()

