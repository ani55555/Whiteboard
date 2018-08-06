from django.db import models
from django import forms
from django.urls import reverse
import calendar




#django default name for this table is polls_patient (i think)
class Patients(models.Model):
    #choice options for field widgets
    STATUS_CHOICES = [
    ('A' , 'Active'),
    ('I' , 'Inactive')
    ]


    LOCATIONS_CHOICES = [
    ('Tuscaloosa', 'Tuscaloosa'),
    ('Winfield', 'Winfield'),
    ('Jasper', 'Jasper'),
    ('Demopolis', 'Demopolis'),
    ('Anniston', 'Anniston'),
    ('Fort Payne', 'Fort Payne'),
    ('Sylacauga', 'Sylacauga'),
    ('Montgomery', 'Montgomery'),
    ('Gadsden', 'Gadsden'),
    ]

    DOCTORS_CHOICES = [
    ('Beatrous', 'Beatrous'),
    ('Campbell', 'Campbell'),
    ('Drake', 'Drake'),
    ('Hobeika', 'Hobeika'),
    ('Pinkston', 'Pinkston'),
    ('Sanford', 'Sanford'),
    ]

    DOSIMETRIST_CHOICES = [
    ('Tatum', 'Tatum'),
    ('Hunter', 'Hunter'),
    ('Maples', 'Maples')
    ]





    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length = 30)

    identification = models.IntegerField(null = True, blank = True)
    phone_number = models.BigIntegerField(null = True, blank = True)
    email = models.EmailField(null = True, blank = True)

    area_under_treatment = []
    referrer = models.CharField(max_length = 30, blank = True)
    start_date = models.DateField(null = True, blank = True)
    end_date = models.DateField(null = True, blank = True)
    #Tuscaloosa, Winfield, Jasper, Demopolis, Anniston, Ft. Payne, Syl(coosa Valley regional), Montgomery, Gadsden

    status = models.CharField(max_length = 30, choices = STATUS_CHOICES, blank = True)
    facility = models.CharField(max_length = 30, choices = LOCATIONS_CHOICES, blank = True)
    doctor = models.CharField(max_length = 30, choices = DOCTORS_CHOICES, blank = True)
    dosimetrist = models.CharField(max_length = 30, choices = DOSIMETRIST_CHOICES, blank = True)
    comments_other = models.TextField(blank = True)





    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('patient-details', kwargs = {'id' : self.id})
