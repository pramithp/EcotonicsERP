# Generated by Django 4.2.7 on 2024-12-09 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0005_followup'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Customers.customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='type',
            field=models.CharField(choices=[('individual', 'individual'), ('industrial', 'industrial')], max_length=50),
        ),
    ]
