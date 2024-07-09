# Generated by Django 5.0.6 on 2024-07-09 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_alter_booking_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('Checked-out', 'Checked-out'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Checked-in,', 'Checked-in'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]