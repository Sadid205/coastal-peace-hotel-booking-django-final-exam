# Generated by Django 5.1.1 on 2024-10-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0024_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('3', '⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐'), ('1', '⭐'), ('2', '⭐⭐'), ('4', '⭐⭐⭐⭐')], max_length=20),
        ),
    ]
