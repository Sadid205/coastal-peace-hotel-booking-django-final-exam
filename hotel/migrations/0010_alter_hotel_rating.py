# Generated by Django 5.1.1 on 2024-10-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_alter_hotel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.CharField(choices=[('🌟🌟🌟', '🌟🌟🌟'), ('🌟🌟', '🌟🌟'), ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟'), ('🌟🌟🌟🌟', '🌟🌟🌟🌟'), ('🌟', '🌟')], max_length=10),
        ),
    ]