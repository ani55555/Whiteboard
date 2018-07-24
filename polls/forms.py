from django import forms

from django.forms import ModelForm, SelectDateWidget

from polls.models import Patients



YEARS_CHOICES = [i for i in range(1900, 2018)]


class PatientSearchForm(ModelForm):
    class Meta:
        model = Patients
        fields = ['first_name', 'last_name']



class PatientAddForm(ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        widgets = {
        'start_date' : SelectDateWidget(years = YEARS_CHOICES),
        'end_date' : SelectDateWidget(years = YEARS_CHOICES)
        }




class PatientEditForm(ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'

        #patient_fname = forms.CharField(label = 'First Name', max_length = 40)
        #patient_lname = forms.CharField(label = 'Last Name', max_length = 40)
