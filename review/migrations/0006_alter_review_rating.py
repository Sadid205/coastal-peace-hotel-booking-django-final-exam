# Generated by Django 5.1.1 on 2024-10-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('2', '⭐⭐'), ('5', '⭐⭐⭐⭐⭐'), ('1', '⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐')], max_length=20),
        ),
    ]
