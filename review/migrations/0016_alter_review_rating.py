# Generated by Django 5.0.6 on 2024-07-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0015_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐'), ('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐')], max_length=20),
        ),
    ]