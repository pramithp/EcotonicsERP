# Generated by Django 5.1.4 on 2025-01-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0004_alter_customer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
