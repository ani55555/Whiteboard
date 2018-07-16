from django.forms import ModelForm
from polls.models import Patients


class PatientViewForm(ModelForm):
    class Meta:
        model = Patients
        fields = ['first_name', 'last_name']

class PatientAddForm(ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'


        #patient_fname = forms.CharField(label = 'First Name', max_length = 40)
        #patient_lname = forms.CharField(label = 'Last Name', max_length = 40)
