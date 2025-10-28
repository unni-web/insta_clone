from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
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

def index(request):
    if request.user.is_authenticated:

        return render(request,'index.html')
    else:
        return redirect(loginuser)