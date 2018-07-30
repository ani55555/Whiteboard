
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.core import serializers
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.list import ListView
from django.views import View
from django.http import *
from mysite.urls import *
from polls.forms import PatientAddForm, PatientSearchForm
from polls.models import Patients
from django import forms
import datetime




def login_error_handle(request):
    return render(request, 'registration/login_error.html', {})

class signup_try(CreateView):
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

# THESE VIEWS ARE STILL IN PROGRESS PLS BE PATIENT HAHA GET IT? 'PATIENT' HAHAHAHAHAAAAAAAAA



class searchpatients(FormView):
        template_name = 'polls/search.html'
        form_class = PatientSearchForm
        success_url = '../table_view'
        def runthisshit(self, request):
            if self.form.is_valid:
                return render(request, 'polls/home.html')









def addpatients(request):
    form = PatientAddForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form_add' : form}
    return render(request, 'polls/add.html', context)


class listdisplay(ListView):
    model = Patients
    template_name = 'polls/listedpatients.html'
    queryset = Patients.objects.all()
    context_object_name = "patients"


class EditPatientView(UpdateView):
    model = Patients
    template_name = 'polls/edit.html'
    fields = '__all__'
    success_url = '../table_view'


class SeePatientInfo(DetailView):
    model = Patients
    template_name = 'polls/see.html'
    def get_context_data(self, **kwargs):
        vlist = [x for x in Patients.objects.values_list()]
        flist = [f.name for f in Patients._meta.get_fields()]
        truelist = vlist[self.kwargs['pk'] - 1]
        zippedupshit = zip(flist, truelist)
        context = super(SeePatientInfo, self).get_context_data(**kwargs)
        context['zippedupshit'] = zippedupshit
        return context
