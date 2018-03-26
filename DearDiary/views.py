# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
        request.session.set_expiry(600)
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
     dog = Post(title=request.POST['title'],
     description=request.POST['description'],
     image=request.FILES.get('image'),
     created_by_user=user,)
     dog.save()
    return redirect("/")
        
def error(request):
    return render(request, '404.html')
    
def view(request):
    if request.user.is_authenticated(): #or request.session.get_expiry_age()> 10):
        request.session.set_expiry(600)
        user = request.user
    
        # dogs=Post.objects.all() #For seeing all entries 
        dogs= Post.objects.filter(created_by_user = user).order_by('-created_at')#[:4] #For seeing user specific entries
        query=request.GET.get('q')
        if query:
            dogs=dogs.filter(
                Q(title__icontains=query)|
                Q(description__icontains=query)|
                Q(created_at__icontains=query)
        
            ).distinct()
        context={ 'dogs': dogs}
        return render(request, 'view.html', context)
    else:
        messages.info(request, 'Session Expired')
        return redirect("/login")
    
    
def final(request, id):
    
    dog=Post.objects.get(id=id)
    context={"dog": dog}
    return render(request, 'final.html', context)
    
def edit(request, id):
    if request.user.is_authenticated(): #or request.session.get_expiry_age()> 10):
        request.session.set_expiry(600)
        query=request.GET.get('q')
        if query:
            return redirect('/view?q=%s' %query)
        dog=Post.objects.get(id=id)
        context={"dog": dog}
        return render(request, 'edit.html', context)
    else:
        messages.info(request, 'Session Expired')
        return redirect("/login")
    
def update(request, id):
    dog=Post.objects.get(id=id)
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
    

def delete(request, id):
    dog=Post.objects.get(id=id)
    dog.delete()
    return redirect('/view')

def delete_image(request, id):
    Post.objects.get(id=id).image.delete(save=True)
    return HttpResponseRedirect(('/view'))
    

def login_view(request):
    #print (request.user.is_authenticated())
    title="Sign in"
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username, password=password)
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
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/login")
        
    context = {
        "form": form,
        'title': title
    }
    return render(request, "form.html", context)
    
def logout_view(request):
    logout(request)
    return redirect("/login")
    

    
