# Generated by Django 3.0 on 2022-08-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0004_auto_20220804_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='qr_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]