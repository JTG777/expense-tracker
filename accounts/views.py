from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if not user.exists():
            messages.error(request,"User doesn't exists")
            return redirect('login')
        
        else:
            user=authenticate(username=username,password=password)
            if not user:
                messages.error(request,"password or username incorrect")
                return redirect('login')

            else:
                login(request,user)
                messages.success(request,"You have successfully login")
                return redirect('index')
        

    return render(request,'registration/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.info(request, "This username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        messages.success(request, "You have successfully registered")
        return redirect('login')

    return render(request,'registration/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')