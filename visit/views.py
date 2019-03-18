from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from visit.models import *
from .forms import UserRegistrationForm, LoginForm
from django.urls import reverse

def Registration(request):
    if request.user.is_authenticated:
        return render(request, 'visit/registration/register.html')
    if request.method == 'POST':
        form  = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['username'],email = form.cleaned_data['email'] , password = form.cleaned_data['password'])
            user.save()

            return HttpResponseRedirect('/')
        else:
            return render(request, 'visit/registration/register.html', {'form': form},)

    else:
        form= UserRegistrationForm()
        context = {'form': form}
        return render(request, 'visit/registration/register.html', context )


@login_required
def Profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request,'visit/profile.html')

def LoginRequest(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.method == 'POST':
        form  = LoginRequest(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            UserProfile = authenticate(username=username, password=password)
            if UserProfile is not None:
                login(request, UserProfile)
                return HttpResponseRedirect('/home/')
            else:
                return render(request,'visit/registration/login.html',{'form':form})
        else:
            return render(request, 'visit/registration/login.html', {'form': form})

    else:
        form= LoginForm()
        context = {'form': form}
        return render(request, 'visit/registration/login.html', context, )


def logoutRequest(request):
    logout(request)
    return  render(request, 'visit/index.html')



def index(request):
    return render(request, 'visit/index.html', context = None)
