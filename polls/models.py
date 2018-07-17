from django.db import models
from django import forms
import calendar




#django default name for this table is polls_patient (i think)
class Patients(models.Model):
    #choice options for field widgets
    STATUS_CHOICES = [
    ('A' , 'Active'),
    ('I' , 'Inactive')
    ]


    LOCATIONS_CHOICES = [
    ('TUS', 'Tuscaloosa'),
    ('WIN', 'Winfield'),
    ('JAS', 'Jasper'),
    ('DEM', 'Demopolis'),
    ('ANN', 'Anniston'),
    ('FTP', 'Fort Payne'),
    ('SYL', 'Sylacauga'),
    ('MON', 'Montgomery'),
    ('GAD', 'Gadsden'),
    ]

    DOCTORS_CHOICES = [
    ('BEA', 'Beatrous'),
    ('CAM', 'Campbell'),
    ('DRK', 'Drake'),
    ('HOB', 'Hobeika'),
    ('PNK', 'Pinkston'),
    ('SAN', 'Sanford'),
    ]

    DOSIMETRIST_CHOICES = [
    ('TAT', 'Tatum'),
    ('HUN', 'Hunter'),
    ('MAP', 'Maples')
    ]





    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length = 30)
    identification = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(blank = True)

    area_under_treatment = []
    referrer = models.CharField(max_length = 30)
    start_date = models.DateField()
    end_date = models.DateField()
#Tuscaloosa, Winfield, Jasper, Demopolis, Anniston, Ft. Payne, Syl(coosa Valley regional), Montgomery, Gadsden

    status = models.CharField(max_length = 15, choices = STATUS_CHOICES)
    facility = models.CharField(max_length = 3, choices = LOCATIONS_CHOICES)
    doctor = models.CharField(max_length = 30, choices = DOCTORS_CHOICES)
    dosimetrist = models.CharField(max_length = 30, choices = DOSIMETRIST_CHOICES)

    comments_other = models.TextField()
    #def __str__(self):
    #    return self.
    #total_fields = [First, Last, ID, Phone, Email, Status, Location, Doctor, Dosimetrist, Start, End]
