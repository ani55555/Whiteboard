# Generated by Django 2.0.6 on 2018-07-16 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180716_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='e_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='s_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
