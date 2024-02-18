# Generated by Django 4.1.4 on 2024-02-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='session_type',
            field=models.CharField(choices=[('MORNING', 'Morning Session'), ('AFTERNOON', 'Afternoon Session')], max_length=50, null=True),
        ),
    ]
