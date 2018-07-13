# Generated by Django 2.0.6 on 2018-07-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('identification', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('status', models.BooleanField(default=True)),
                ('referrer', models.CharField(max_length=30)),
                ('facility', models.CharField(choices=[('TUS', 'Tuscaloosa'), ('WIN', 'Winfield'), ('JAS', 'Jasper'), ('DEM', 'Demopolis'), ('ANN', 'Anniston'), ('FTP', 'Fort Payne'), ('SYL', 'Sylacauga'), ('MON', 'Montgomery'), ('GAD', 'Gadsden')], max_length=3)),
                ('doctor', models.CharField(choices=[('BEA', 'Beatrous'), ('CAM', 'Campbell'), ('DRK', 'Drake'), ('HOB', 'Hobeika'), ('PNK', 'Pinkston'), ('SAN', 'Sanford')], max_length=30)),
                ('dosimetrist', models.CharField(choices=[('TAT', 'Tatum'), ('HUN', 'Hunter'), ('MAP', 'Maples')], max_length=30)),
                ('s_date', models.DateField()),
                ('e_date', models.DateField()),
                ('comments_other', models.TextField()),
            ],
        ),
    ]
