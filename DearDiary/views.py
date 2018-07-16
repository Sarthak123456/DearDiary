# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render, redirect
from models import Post,Post_image
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
    
    )
from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from .forms import UserLoginForm,UserRegisterForm
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.contrib import messages
from django.core.mail import send_mail
import datetime
# Create your views here.
   
def Upload(request):
    if request.method=="POST":
     dog = Post_image(
     image=request.FILES.get('image'))
     dog.save()
    return redirect('/index')
    

def index(request):
    #return HttpResponseRedirect("base.html")
    if request.user.is_authenticated(): #or request.session.get_expiry_age()> 10):
        request.session.set_expiry(600000)
        query=request.GET.get('q')
        if query:
            return redirect('/view?q=%s' %query)
        return render(request, "index.html")   
    else:
        return redirect("/login")
def landing(request):
    form=UserLoginForm(request.POST or None)
    title='Sign In'
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username, password=password)
        login(request,user)
       # print (request.user.is_authenticated())
        return redirect("/index")
    return render(request, "landing.html", {'form': form, 'title': title})  
          
def create(request):
  #  dogs.save()
    user = request.user
    #print (user)
    if request.method=="POST":
        post = Post(title=request.POST['title'],
        description=request.POST['description'],
        created_by_user=user,) 
        post.save()
        
        image=request.FILES.getlist('image')
        for x in image:
                 post_image = Post_image(
                 image=x,
                 post=post
                    )         
                 post_image.save()
        #import pdb;pdb.set_trace()
        
    return redirect("/")
        
def error(request):
    return render(request, '404.html')
    
def view(request):
    if request.user.is_authenticated(): #or request.session.get_expiry_age()> 10):
        request.session.set_expiry(600000)
        user = request.user
        today = datetime.datetime.now()
       # import pdb;pdb.set_trace()
        #dogs=Post.objects.all() #For seeing all entries 
        post= Post.objects.select_related().filter(created_by_user = user).order_by('-created_at')#[:4] #For seeing user specific entries
        # post_image=Post_image.objects.all()
        # posts=Post.objects.filter(created_by_user =user).count()
        # # print post_image[0]
        # # print posts
                 # import pdb; pdb.set_trace();
            # form=request.POST['multi_delete']
        checkbox = request.POST.getlist('checkbox')
        if request.method== 'POST':
                print checkbox
                for check in checkbox:
                    multi_delete= Post.objects.select_related().filter(Q(created_by_user = user) and Q(id = check)).delete()
                    print multi_delete
                
        context={'posts' : post, 'today' : today, 'checkbox' : checkbox }    
        return render(request, 'view.html', context)
    else:
        messages.info(request, 'Session Expired')
        return redirect("/login")
    
    
def final(request, id):
    dog=Post.objects.get(id=id)
    if dog.created_by_user==request.user:
        if request.user.is_authenticated():
            request.session.set_expiry(600)
            context={"dog": dog}
            return render(request, 'final.html', context)
        else:
            messages.info(request, 'Session Expired')
            return redirect("/login")
    else:
        pass
   
    
def edit(request, id):
    dog=Post.objects.get(id=id)
    if dog.created_by_user==request.user:
        
        if request.user.is_authenticated(): #or request.session.get_expiry_age()> 10):
            request.session.set_expiry(600000)
            query=request.GET.get('q')
            if query:
                return redirect('/view?q=%s' %query)
            context={"dog": dog}
            return render(request, 'edit.html', context)
        else:
            messages.info(request, 'Session Expired')
            return redirect("/login")
    else:
        pass
    
def update(request, id):
    dog=Post.objects.get(id=id)
    if dog.created_by_user==request.user:
        
        dog.title=request.POST['title']
        dog.description=request.POST['description']
        if dog.image == None:
            dog.image=request.FILES.get('image')
        elif dog.image != None:
            if request.FILES.get('image') != None:
                 dog.image=request.FILES.get('image')
            else:
                dog.image== dog.image
        #dog.image=request.FILES.get('image')
        dog.save()
        return redirect('/view')
    else:
        pass
    

def delete(request, id):
    
    dog=Post.objects.get(id=id)
    if dog.created_by_user==request.user:
     post = dog.post_image_set.all()
     post.delete()
     dog.delete()
     return redirect('/view')
     
    else:
        pass

def delete_image(request, id):
    post = Post_image.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(('/view'))
    

def login_view(request):
    #print (request.user.is_authenticated())
    title="Sign in"
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username, password=password)
        subject='Test registration'
        message='New user registered.\n Welcome to DD.'
        from_email=settings.EMAIL_HOST_USER
        to_list=[user.email, settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        login(request,user)
       # print (request.user.is_authenticated())
        return redirect("/index")
        
    return render(request, "form.html", {"form": form, "title" : title})

def register_view(request):
    title="Register"
    form=UserRegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        subject='Test registration'
        message='New user registered./n Welcome to DD.'
        from_email=settings.EMAIL_HOST_USER
        to_list=[user.email, settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=False)
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/index")
        
    context = {
        "form": form,
        'title': title
    }
    return render(request, "form.html", context)
    
def logout_view(request):
    
    logout(request)
    return redirect("/login")
    



    
