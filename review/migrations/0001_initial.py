# Generated by Django 5.0.6 on 2024-07-07 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest', '0001_initial'),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.TextField()),
                ('rating', models.CharField(choices=[('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐', '⭐⭐'), ('⭐', '⭐')], max_length=20)),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ManyToManyField(to='hotel.hotel')),
                ('reviewer', models.ManyToManyField(to='guest.guest')),
            ],
        ),
    ]
