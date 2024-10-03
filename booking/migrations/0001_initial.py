# Generated by Django 5.1.1 on 2024-09-30 14:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest_or_admin', '0001_initial'),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.CharField(choices=[('Cancelled', 'Cancelled'), ('Checked-in', 'Checked-in'), ('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Checked-out', 'Checked-out')], default='Pending', max_length=20)),
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('check_in_date', models.DateTimeField(blank=True, null=True)),
                ('check_out_date', models.DateTimeField(blank=True, null=True)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('number_of_guests', models.IntegerField(default=0, null=True)),
                ('room_type', models.CharField(max_length=20, null=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest_or_admin.guestoradmin')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
        ),
    ]
