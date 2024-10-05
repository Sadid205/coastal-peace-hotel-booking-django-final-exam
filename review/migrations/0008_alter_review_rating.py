# Generated by Django 5.1.1 on 2024-10-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1', '⭐'), ('3', '⭐⭐⭐'), ('2', '⭐⭐'), ('5', '⭐⭐⭐⭐⭐'), ('4', '⭐⭐⭐⭐')], max_length=20),
        ),
    ]