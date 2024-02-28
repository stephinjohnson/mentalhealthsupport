# Generated by Django 4.1.4 on 2024-02-23 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_thread_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved')], default='PENDING', max_length=20)),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approved_appointments', to=settings.AUTH_USER_MODEL)),
                ('time_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.timeslot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]