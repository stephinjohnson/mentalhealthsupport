# Generated by Django 4.1.4 on 2024-02-19 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_timeslot_session_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='therapist',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='user',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
