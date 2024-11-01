# Generated by Django 5.1.1 on 2024-10-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0022_service_alter_hotel_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_name', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.CharField(choices=[('🌟🌟🌟', '🌟🌟🌟'), ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟'), ('🌟🌟🌟🌟', '🌟🌟🌟🌟'), ('🌟🌟', '🌟🌟'), ('🌟', '🌟')], max_length=10),
        ),
    ]
