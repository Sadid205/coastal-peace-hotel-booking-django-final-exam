# Generated by Django 5.1.1 on 2024-10-02 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1', '⭐'), ('4', '⭐⭐⭐⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')], max_length=20),
        ),
    ]
