# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



# Create your models here.


class Post_image(models.Model):
    image=models.FileField(null=True, blank=True, default=None)
    created_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
     )
     
    
    
    def __str__(self):
        return str(self.image)

        
class Post(models.Model):
   # user = models.ForeignKey(User, unique=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=4500)
    image =models.FileField(null=True, blank=True, default=None)#models.ForeignKey(Post_image,null=True,on_delete=models.CASCADE ) #
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now= True)
   # user = models.OneToOneField(User, null=True)
    created_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
     )
     
    def __str__(self):
        return self.title

    
