# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.contrib import admin

# Register your models here.
from .models import Post,Post_image

class PostAdmins(admin.ModelAdmin):
   model = Post_image

class PostImageInline(admin.TabularInline):
    model = Post
    extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [ PostImageInline, ]
    
admin.site.register(Post, PostAdmins,)
