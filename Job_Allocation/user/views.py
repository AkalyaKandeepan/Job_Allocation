from django.contrib import messages
#from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.db import IntegrityError
#0.from mysql import connector
from . import forms
from .forms import CreateComment
from .models import Comment


def index(request):
    return render(request, 'user/index.html')
# Create your views here.
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("com")
        else:

            return redirect('register')
    else:
            return render(request,'user/login.html')
def register(request):
    if request.method=='POST':

        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.Info(request,'User Taken')
                return redirect('/register')

            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'pasword no match..')
            return redirect('register')

    else:
        return render(request,'user/register.html')
def logout(request):
    auth.logout(request)
    return redirect('login')


def com(request):
    saved = False
    if request.method=='POST':
        form=CreateComment(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.actor = request.user
            instance.save()
            saved = True
            messages.info(request,"data submitted successfully")

            return redirect('com')


    else:
        form=CreateComment()
    return render(request,'user/comment.html',{'form':form})


