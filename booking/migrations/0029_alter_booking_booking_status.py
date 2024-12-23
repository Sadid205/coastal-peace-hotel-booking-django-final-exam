# Generated by Django 5.1.1 on 2024-10-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0028_alter_booking_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('Checked-in', 'Checked-in'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Checked-out', 'Checked-out'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
