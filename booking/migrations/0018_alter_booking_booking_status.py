# Generated by Django 5.1.1 on 2024-10-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_alter_booking_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Checked-out', 'Checked-out'), ('Checked-in', 'Checked-in')], default='Pending', max_length=20),
        ),
    ]
