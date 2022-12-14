# Generated by Django 3.0 on 2022-08-10 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_low_battery', models.BooleanField(default=False)),
                ('is_network_error', models.BooleanField(default=False)),
                ('equipment_gps_tracker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.EquipmentGpsTracker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'db_table' : 'alert',
            },
        ),
    ]
