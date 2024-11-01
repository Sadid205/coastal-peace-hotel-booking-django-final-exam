# Generated by Django 5.1.1 on 2024-10-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0021_remove_review_hotel_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('5', '⭐⭐⭐⭐⭐'), ('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐')], max_length=20),
        ),
    ]
