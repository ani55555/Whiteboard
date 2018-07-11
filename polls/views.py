
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import *
from mysite.urls import *
from django import forms

def login_error_handle(request):
    return render(request, 'registration/login_error.html', {})

class signup_try(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def login_try(request):
    return render(request, 'registration/login.html', {})

def home_try(request):
    return render(request, 'polls/home.html', {})

#def pwd_reset_try(request):
#    return render(request, 'registration/password_reset_form.html', {})


@login_required(login_url = 'tryloginerror')
def search_try(request):
        return render(request, 'polls/search.html', {})

@login_required(login_url = 'tryloginerror')
def profile_try(request):
        return render(request, 'polls/profile.html', {})


@login_required(login_url = 'tryloginerror')
def information_try(request):
        return render(request, 'polls/information.html', {})

@login_required(login_url = 'tryloginerror')
def logout_try(request):
        logout(request, next_page='polls/home.html')
