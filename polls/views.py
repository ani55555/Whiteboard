
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView
from django.views import View
from django.http import *
from mysite.urls import *
from polls.forms import PatientAddForm, PatientSearchForm
from polls.models import Patients
from django import forms
import datetime




def login_error_handle(request):
    return render(request, 'registration/login_error.html', {})

class signup_try(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home_try(request):
    return render(request, 'polls/home.html', {})

def pwd_reset_try(request):
    return render(request, 'registration/password_reset_form.html', {})

# THE FOLLOWING REQUIRE LOGIN/AUTHENTICATION

@login_required(login_url = 'tryloginerror')
def profile_try(request):
        return render(request, 'polls/profile.html', {})


@login_required(login_url = 'tryloginerror')
def information_try(request):
        return render(request, 'polls/information.html', {})

@login_required(login_url = 'tryloginerror')
def logout_try(request):
        logout(request)
        return home_try(request)









@login_required(login_url = 'tryloginerror')
def addpatients(request):
    form = PatientAddForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form_add' : form}
    return render(request, 'polls/add.html', context)



@login_required(login_url = 'tryloginerror')
def table_try(request):
    tdata = list(Patients.objects.all())
    flist = [f.name for f in Patients._meta.get_fields()]
    vlist = [x for x in Patients.objects.values_list()]
    context = {
    'tdata' : tdata,
    'flist' : flist,
    'vlist' : vlist,
    }
    return render(request, 'polls/table_view.html', context)




@login_required(login_url = 'tryloginerror')
def searchpatients(request):
        form = PatientSearchForm(request.POST or None)
        if form.is_valid():
            request.session['fdata'] = form.cleaned_data['first_name']
            request.session['ldata'] = form.cleaned_data['last_name']
        context = {
        'form_search' : form,
        }
        return render(request, 'polls/search.html', context)


@login_required(login_url = 'tryloginerror')
def displayed_try(request):
        fdata = request.session['fdata']
        ldata = request.session['ldata']
        results = Patients.objects.filter(
        first_name__icontains = fdata
        ).filter(
        last_name__icontains = ldata
        ).values_list('first_name', 'last_name', 'phone_number', 'status')
        context = {
        'results' : results
        }
        return render(request, 'polls/displayed.html', context)


class EditPatient(UpdateView):
    model = Patients
    fields = '__all__'
    template_name_suffix = '_update_form'
