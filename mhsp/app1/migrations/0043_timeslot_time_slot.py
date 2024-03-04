# Generated by Django 4.1.4 on 2024-03-04 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_timeslot_is_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='time_slot',
            field=models.CharField(choices=[('8-9', '8:00 AM - 9:00 AM'), ('9-10', '9:00 AM - 10:00 AM'), ('10-11', '10:00 AM - 11:00 AM'), ('12-1', '12:00 PM - 1:00 PM'), ('1-2', '1:00 PM - 2:00 PM'), ('2-3', '2:00 PM - 3:00 PM'), ('3-4', '3:00 PM - 4:00 PM')], max_length=5, null=True),
        ),
    ]
