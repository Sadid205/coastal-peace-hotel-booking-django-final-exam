# Generated by Django 5.1.1 on 2024-10-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0018_hotel_included_category_alter_hotel_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='included_category',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.CharField(choices=[('🌟🌟🌟🌟', '🌟🌟🌟🌟'), ('🌟', '🌟'), ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟'), ('🌟🌟', '🌟🌟'), ('🌟🌟🌟', '🌟🌟🌟')], max_length=10),
        ),
    ]
