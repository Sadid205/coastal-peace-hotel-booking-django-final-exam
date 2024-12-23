# Generated by Django 5.1.1 on 2024-10-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_alter_hotel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.CharField(choices=[('🌟', '🌟'), ('🌟🌟🌟', '🌟🌟🌟'), ('🌟🌟🌟🌟', '🌟🌟🌟🌟'), ('🌟🌟', '🌟🌟'), ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟')], max_length=10),
        ),
        migrations.CreateModel(
            name='HotelsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ManyToManyField(related_name='best_hotel', to='hotel.hotel')),
            ],
        ),
    ]
