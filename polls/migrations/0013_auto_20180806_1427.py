# Generated by Django 2.0.6 on 2018-08-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20180806_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='facility',
            field=models.CharField(blank=True, choices=[('Tuscaloosa', 'Tuscaloosa'), ('Winfield', 'Winfield'), ('Jasper', 'Jasper'), ('Demopolis', 'Demopolis'), ('Anniston', 'Anniston'), ('Fort Payne', 'Fort Payne'), ('Sylacauga', 'Sylacauga'), ('Montgomery', 'Montgomery'), ('Gadsden', 'Gadsden')], max_length=30),
        ),
        migrations.AlterField(
            model_name='patients',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive')], max_length=30),
        ),
    ]