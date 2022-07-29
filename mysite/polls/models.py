from email.policy import default
import profile
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class MyUser(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_related_name')
    email=models.EmailField()
    

class MediaPeofile(models.Model):
    image=models.ImageField(null=True,blank=True,default='',upload_to='profile/') 
    user=models.ForeignKey(User,related_name='media',on_delete=models.CASCADE)
    