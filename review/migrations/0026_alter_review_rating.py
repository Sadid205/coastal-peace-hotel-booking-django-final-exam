# Generated by Django 5.1.1 on 2024-10-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0025_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('4', '⭐⭐⭐⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('1', '⭐'), ('5', '⭐⭐⭐⭐⭐')], max_length=20),
        ),
    ]
