# Generated by Django 4.0.6 on 2022-07-29 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_equipmentdevice_is_matched_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='equipment_gps_tracker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.equipmentgpstracker'),
        ),
      
    ]