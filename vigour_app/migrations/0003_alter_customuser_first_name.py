# Generated by Django 3.2.4 on 2021-06-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vigour_app', '0002_remove_patientappointment_speciality_pref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
