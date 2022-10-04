from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from . models import *
from accounts.forms import RegistrationForm,ListForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User


def home(request):
    return render(request,"accounts/home.html")

def registeruser(request):
    form = RegistrationForm()
    if request.method =="POST":
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            profile_pic = form.cleaned_data['profile_pic']   
            try:
               user = CustomUser.objects.create_user(fullname=fullname,phone=phone,password=password,email=email,username =username,profile_pic=profile_pic)
               user.save()
               messages.success(request,"you have registered sussesfully")
               return redirect('/')
            except:
               messages.success(request,"you are not registered sussesfully")
               return redirect('/')
        else:
            return redirect('register')
        
    context={"form":form}
    return render(request,"accounts/register.html",context)
def loginuser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email,password=password)
       
        if user !=None :
            login(request,user)
            redirect_url = request.GET.get('next','/')
            return redirect(redirect_url)
        else:
            messages.error(request,"user not authenticated")
    return render(request, 'accounts/registration/login.html')
        
def logoutuser(request):
    logout(request)
    return redirect('/')


def edituser(request,pk):
    user = CustomUser.objects.get(id=pk)
    form = ListForm(instance=user)
    if request.method == "POST":
        form = ListForm(request.POST,request.FILES,instance= user)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    context={"form":form}
    return render(request,"accounts/edit.html",context)
    


