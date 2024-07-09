# Generated by Django 5.0.6 on 2024-07-08 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0004_alter_guest_user'),
        ('hotel', '0014_alter_hotel_rating'),
        ('review', '0013_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='hotel',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('5', '⭐⭐⭐⭐⭐'), ('2', '⭐⭐'), ('1', '⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐')], max_length=20),
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewer',
        ),
        migrations.AddField(
            model_name='review',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guest.guest'),
        ),
    ]