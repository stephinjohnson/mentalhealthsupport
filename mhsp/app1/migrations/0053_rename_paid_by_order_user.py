# Generated by Django 4.1.4 on 2024-03-22 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0052_order_paid_by_order_payment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid_by',
            new_name='user',
        ),
    ]