
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic




def search_try(request):
    return render(request, "polls/search.html", {})
def home_try(request):
    return render(request, "polls/home.html", {})
def profile_try(request):
    return render(request, "polls/profile.html", {})
def information_try(request):
    return render(request, "polls/information.html", {})

class signup_try(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def login_determine(request):
    current_user = request.user
    if request.user.is_authenticated:
        print(current_user.id)
        return True
    else:
        print("Guest User")
        return False

















