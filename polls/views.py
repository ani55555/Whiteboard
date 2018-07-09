
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic




def search_try(request):
    return render(request, "polls/search.html", {})
def home_try(request):
    return render(request, "polls/home.html", {})
def upgrade_try(request):
    return render(request, "polls/upgrade.html", {})
def information_try(request):
    return render(request, "polls/information.html", {})

class signup_try(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'














