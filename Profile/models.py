from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class userprofile(models.Model):
    usrename=models.OneToOneField(User,related_name='userprofile',on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50,unique=True)
    lastname=models.CharField(max_length=50,unique=True)
    city = models.CharField(max_length = 150)
    email = models.EmailField(max_length=500,unique=True)
    userphoto=models.ImageField(upload_to='profile_photos/',default='')
    def __str__(self):
        return str(self.usrename)
    @receiver(post_save,sender=User)
    def save_profile(sender,instance,created,**kwargs):
        if created:
            userprofile.objects.create(usrename=instance)