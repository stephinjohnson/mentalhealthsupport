# Generated by Django 4.1.4 on 2023-11-26 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_therapist_therapistfeedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='therapistfeedback',
            name='therapist',
        ),
        migrations.RemoveField(
            model_name='therapistfeedback',
            name='user',
        ),
        migrations.DeleteModel(
            name='Therapist',
        ),
        migrations.DeleteModel(
            name='TherapistFeedback',
        ),
    ]
