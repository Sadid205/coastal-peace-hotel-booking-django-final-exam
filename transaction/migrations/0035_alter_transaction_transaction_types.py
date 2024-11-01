# Generated by Django 5.1.1 on 2024-11-01 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0034_alter_transaction_transaction_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_types',
            field=models.CharField(choices=[('Deposit', 'Deposit'), ('Failed', 'Failed'), ('Booking', 'Booking'), ('Cancelled', 'Cancelled')], default='Deposit', max_length=20),
        ),
    ]
