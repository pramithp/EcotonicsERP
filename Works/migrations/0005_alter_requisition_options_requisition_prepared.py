# Generated by Django 5.1.4 on 2024-12-17 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Technicians', '0007_department_info_designation_info'),
        ('Works', '0004_requisition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requisition',
            options={'ordering': ('-date_added',), 'verbose_name': 'Requisition', 'verbose_name_plural': 'Requisitions'},
        ),
        migrations.AddField(
            model_name='requisition',
            name='prepared',
            field=models.ForeignKey(default='b217550e-7766-4276-886c-6d4654297959', on_delete=django.db.models.deletion.CASCADE, to='Technicians.technician'),
            preserve_default=False,
        ),
    ]