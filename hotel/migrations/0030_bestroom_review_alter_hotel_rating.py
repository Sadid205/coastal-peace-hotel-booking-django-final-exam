# Generated by Django 5.1.1 on 2024-10-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0029_alter_hotel_rating'),
        ('review', '0030_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestroom',
            name='review',
            field=models.ManyToManyField(related_name='best_room', to='review.review'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.CharField(choices=[('🌟🌟', '🌟🌟'), ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟'), ('🌟🌟🌟🌟', '🌟🌟🌟🌟'), ('🌟', '🌟'), ('🌟🌟🌟', '🌟🌟🌟')], max_length=10),
        ),
    ]
