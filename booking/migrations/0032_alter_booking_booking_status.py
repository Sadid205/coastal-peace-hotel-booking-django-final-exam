# Generated by Django 5.1.1 on 2024-10-31 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0031_alter_booking_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Pending', 'Pending'), ('Checked-in', 'Checked-in'), ('Cancelled', 'Cancelled'), ('Checked-out', 'Checked-out')], default='Pending', max_length=20),
        ),
    ]
