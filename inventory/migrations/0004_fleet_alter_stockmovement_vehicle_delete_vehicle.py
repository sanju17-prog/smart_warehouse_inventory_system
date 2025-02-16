# Generated by Django 5.1.6 on 2025-02-16 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_vehicle_stockmovement_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=255, unique=True)),
                ('fleet_type', models.CharField(choices=[('ship', 'Ship'), ('train', 'Train'), ('truck', 'Truck'), ('aircraft', 'Aircraft')], max_length=255)),
                ('capacity', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('in_use', 'In Use')], default='available', max_length=10)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('arrival_time', models.DateTimeField(auto_now=True)),
                ('departure_time', models.DateTimeField(auto_now=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('current_location_checkpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='inventory.warehouse')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='inventory.warehouse')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='inventory.warehouse')),
            ],
        ),
        migrations.AlterField(
            model_name='stockmovement',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.fleet'),
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
