# Generated by Django 5.1.4 on 2024-12-31 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0002_customer_phone_number_transaction_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='total',
            field=models.IntegerField(default=1),
        ),
    ]
