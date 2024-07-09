# Generated by Django 5.0.6 on 2024-07-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_booking_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('Checked-in,', 'Checked-in'), ('Cancelled', 'Cancelled'), ('Confirmed', 'Confirmed'), ('Checked-out', 'Checked-out'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
