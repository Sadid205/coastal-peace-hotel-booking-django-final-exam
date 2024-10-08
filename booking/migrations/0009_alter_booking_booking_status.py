# Generated by Django 5.1.1 on 2024-10-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_booking_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Checked-in', 'Checked-in'), ('Checked-out', 'Checked-out'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20),
        ),
    ]
