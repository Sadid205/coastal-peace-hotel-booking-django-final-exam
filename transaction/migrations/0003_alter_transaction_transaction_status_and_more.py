# Generated by Django 5.0.6 on 2024-07-07 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_alter_transaction_transaction_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_status',
            field=models.CharField(choices=[('Failed', 'Failed'), ('Pending', 'Pending'), ('Completed', 'Completed')], max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_types',
            field=models.CharField(choices=[('Withdraw', 'Withdraw'), ('Deposit', 'Deposit')], max_length=20),
        ),
    ]