# Generated by Django 5.0.8 on 2024-11-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Works', '0002_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]