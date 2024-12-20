# Generated by Django 5.1.4 on 2024-12-19 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Technicians', '0008_alter_technician_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technician',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Technicians.department'),
        ),
        migrations.AlterField(
            model_name='technician',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Technicians.designation'),
        ),
    ]
