# Generated by Django 5.1.1 on 2024-10-22 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0011_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('4', '⭐⭐⭐⭐'), ('1', '⭐'), ('3', '⭐⭐⭐'), ('2', '⭐⭐'), ('5', '⭐⭐⭐⭐⭐')], max_length=20),
        ),
    ]
