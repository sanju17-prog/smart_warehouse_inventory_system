# Generated by Django 5.1.6 on 2025-02-17 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_fleetmovement_fleet'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouse'),
        ),
    ]
