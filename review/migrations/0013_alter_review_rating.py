# Generated by Django 5.0.6 on 2024-07-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0012_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐', '⭐')], max_length=20),
        ),
    ]