# Generated by Django 5.0.8 on 2024-10-21 14:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_lead_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]