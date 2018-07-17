
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.http import *
from mysite.urls import *
from polls.forms import PatientAddForm, PatientViewForm
from polls.models import Patients
from django import forms
import datetime

#patients = Patients.objects.all()
#for patient in patients:
#    patient_list = [patient.first_name, patient.last_name, patient.identification, patient.phone_number, patient.comments_other, patient.start_date, patient.end_date, patient.status]


patient_list = list(Patients.objects.all())


def login_error_handle(request):
    return render(request, 'registration/login_error.html', {})

class signup_try(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#def login_try(request):
#    return render(request, 'registration/login.html', {})


def home_try(request):
    return render(request, 'polls/home.html', {})

def pwd_reset_try(request):
    return render(request, 'registration/password_reset_form.html', {})




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




#@login_required(login_url = 'tryloginerror')
class AddPatients(View):
    template_name = 'polls/add.html'
    def get(self, request):
        form_add = PatientAddForm()
        attr_list = PatientAddForm().fields
        return render(request, self.template_name, {
        'title' : "Add Patient",
        'patient_list' : patient_list,
        'form_add' : form_add,
        'attr_list' : attr_list
    })


#@login_required(login_url = 'tryloginerror')
class SearchPatients(View):
    template_name = 'polls/search.html'
    def get(self, request):
        form_view = PatientViewForm()
        return render(request, self.template_name, {
        'title' : "Retrieve Patient",
        'patient_list' : patient_list,
        'form_view' : form_view,
        })




@login_required(login_url = 'tryloginerror')
def search_try(request):
    return render(request, 'polls/search.html', {})


#------------------------------------------------------------------------------------------------------
#@login_required(login_url = 'tryloginerror')
#def PatientView(request):

    #if request.method == 'GET':
    #    f = PatientAddForm(request.GET)
    #    if f.is_valid():



    #context = {

    #}
    #return render(request, 'polls/search.html', context)
