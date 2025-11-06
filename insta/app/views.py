from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *


def register(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        name=request.POST['name']
        username=request.POST['username']
        data=User.objects.create_user(email=email,password=password,first_name=name,username=username)
        data.save()
        return redirect(loginuser)
    return render(request,'register.html')

def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(index)
        else:
            return redirect(loginuser)
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect(loginuser)

def index(request):
    if request.user.is_authenticated:
        file=Post.objects.all()
        user=request.session['_auth_user_id']

        return render(request,'index.html',{'file':file})
    else:
        return redirect(loginuser)
    
    
def create(request):
    return render(request,'create.html')

def profile(request):
    

    return render(request,'profile.html')

def addfile(request):
    if request.method=='POST':
        files=request.FILES.get('doc')
        data=Profile.objects.create(file=files)
        data.save()
        return redirect(profile)
        
    
def editprofile(request):
    return render(request,'editprofile.html')



    
def addpost(request):
    if request.method=='POST':
        us=request.session['_auth_user_id']
        user=User.objects.get(pk=us)
        file=request.FILES.get('doc')
        data=Post.objects.create(doc=file,user=user)
        data.save()
        return redirect(index)  
    
def comment(request):
    if request.method=='POST':
        comment=request.POST['comment']
        print(comment)
        data=Comment.objects.create(comment=comment,user=request.user)
        data.save()
        return redirect(index)
















