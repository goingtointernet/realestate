from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#User Model
class User(AbstractUser):
    is_admin= models.BooleanField('is admin', default=False)
    is_buyer= models.BooleanField('is buyer', default=False)
    is_seller= models.BooleanField('is seller', default=False)
    desc_text = 'Hello This is Default Description Of your Profile, Please Change it.'
    bio = models.CharField(default = desc_text, max_length=200, null=True)
    phone = models.IntegerField(default = 123456789)
    profile_img = models.ImageField(default = 'static/images/default_profile.png', upload_to = 'static/images', null = True, blank = True)


