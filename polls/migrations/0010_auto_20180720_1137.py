# Generated by Django 2.0.6 on 2018-07-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20180720_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='identification',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
