# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import os

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.


        
        
class Post(models.Model):
   # user = models.ForeignKey(User, unique=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=4500)
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now= True)
   # user = models.OneToOneField(User, null=True)
    created_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
     )
     
    def __str__(self):
        return self.title

    

class Post_image(models.Model):
    image=models.ImageField(null=True, blank=True, default=None)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
   # Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=Post_image)
def Post_image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.image:
        instance.image.delete(False)
    else:
        pass