from django.db import models
from django.contrib.auth.models import AbstractUser,User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(max_length=400)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    status = HTMLField(blank=True,null=True)
    neighbourhood = models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,related_name='hood_user',null=True)

    
    def __str__(self):
        return self.email

class Neighbourhood(models.Model):
    name = models.CharField(max_length=250)
    description = HTMLField()
    location = models.TextField(max_length=400)
    occupants_count = models.IntegerField(blank=True,default=0)
    healthcentre_no = models.IntegerField(blank=True)
    police_no = models.IntegerField(blank=True)
    admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='hood_hood')
    business = models.ManyToManyField('Business',blank=True,related_name='hood_business')
    

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
    hood = models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,related_name='business_in_hood')

    def __str__(self):
        return self.business_name
    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()

class Post(models.Model):
    subject = models.TextField(max_length=400)
    description = HTMLField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='hood_post_user')
    hood_post = models.ForeignKey('Neighbourhood',on_delete=models.CASCADE,related_name='hood_posts')

    def __str__(self):
        return self.subject
    
    def save_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()




class Join(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='hood_join_user')
    hood_name = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,related_name='hood_join')
    location = models.ForeignKey(Neighbourhood , on_delete=models.CASCADE, related_name="hood_location_user",default='')

    def __str__(self):
        return self.description

    def save_join(self):
        self.save

    def delete_join(self):
        self.delete




class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    hood_name = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, related_name='profile_name')
    avatar = CloudinaryField('image')

    def __str__(self):
        return self.user.username
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()

    @classmethod
    def update(cls, id, value):
        cls.objects.filter(id=id).update(avatar=value)
        
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
