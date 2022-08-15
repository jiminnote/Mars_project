# Generated by Django 4.0.6 on 2022-07-26 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment', '0001_initial'),
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairedCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'repaired_companies',
            },
        ),
        migrations.CreateModel(
            name='RepairedPurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'repaired_purposes',
            },
        ),
        migrations.CreateModel(
            name='RepairedSort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'repaired_sorts',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('identity', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('is_location_control', models.BooleanField(null=True)),
                ('is_equipment_control', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='RepairedManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('repaired_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.repairedcompany')),
            ],
            options={
                'db_table': 'repaired_managers',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField()),
                ('equipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment')),
                ('equipment_gps_tracker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.equipmentgpstracker')),
                ('repaired_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.repairedmanager')),
                ('repaired_purpose', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.repairedpurpose')),
                ('repaired_sort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.repairedsort')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'histories',
            },
        ),
    ]