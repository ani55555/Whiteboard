# Generated by Django 2.0.6 on 2018-08-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20180806_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='doctor',
            field=models.CharField(blank=True, choices=[('Beatrous', 'Beatrous'), ('Campbell', 'Campbell'), ('Drake', 'Drake'), ('Hobeika', 'Hobeika'), ('Pinkston', 'Pinkston'), ('Sanford', 'Sanford')], max_length=30),
        ),
        migrations.AlterField(
            model_name='patients',
            name='dosimetrist',
            field=models.CharField(blank=True, choices=[('Tatum', 'Tatum'), ('Hunter', 'Hunter'), ('Maples', 'Maples')], max_length=30),
        ),
        migrations.AlterField(
            model_name='patients',
            name='facility',
            field=models.CharField(blank=True, choices=[('Tuscaloosa', 'Tuscaloosa'), ('Winfield', 'Winfield'), ('Jasper', 'Jasper'), ('Demopolis', 'Demopolis'), ('Anniston', 'Anniston'), ('Fort Payne', 'Fort Payne'), ('Sylacauga', 'Sylacauga'), ('Montgomery', 'Montgomery'), ('Gadsden', 'Gadsden')], max_length=3),
        ),
    ]
