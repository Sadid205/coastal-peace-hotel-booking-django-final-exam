# Generated by Django 5.1.1 on 2024-10-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0025_alter_bestroom_location_alter_hotel_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestroom',
            old_name='amenity',
            new_name='amenities',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.CharField(choices=[('🌟🌟', '🌟🌟'), ('🌟', '🌟'), ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟'), ('🌟🌟🌟', '🌟🌟🌟'), ('🌟🌟🌟🌟', '🌟🌟🌟🌟')], max_length=10),
        ),
    ]
