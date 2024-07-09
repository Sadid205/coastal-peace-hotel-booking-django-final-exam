# Generated by Django 5.0.6 on 2024-07-07 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_user'),
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
    ]