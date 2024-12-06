# Generated by Django 5.1.1 on 2024-10-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0026_alter_transaction_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_status',
            field=models.CharField(choices=[('Failed', 'Failed'), ('Success', 'Success'), ('Pending', 'Pending')], default='Success', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_types',
            field=models.CharField(choices=[('Withdraw', 'Withdraw'), ('Booking', 'Booking'), ('Deposit', 'Deposit')], default='Deposit', max_length=20),
        ),
    ]