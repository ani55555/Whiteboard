from django.db import models






#django default name for this table is polls_patient (i think)
class Patients(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length = 30)
    identification = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(blank = True)
    status = models.BooleanField(default = True)
    area_under_treatment = []
    referrer = models.CharField(max_length = 30)
#Tuscaloosa, Winfield, Jasper, Demopolis, Anniston, Ft. Payne, Syl(coosa Valley regional), Montgomery, Gadsden
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

    facility = models.CharField(max_length = 3, choices = LOCATIONS_CHOICES)
    doctor = models.CharField(max_length = 30, choices = DOCTORS_CHOICES)
    dosimetrist = models.CharField(max_length = 30, choices = DOSIMETRIST_CHOICES)
    s_date = models.DateField()
    e_date = models.DateField()
    comments_other = models.TextField()
    #def __str__(self):
    #    return self.
    #total_fields = [First, Last, ID, Phone, Email, Status, Location, Doctor, Dosimetrist, Start, End]
