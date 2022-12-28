# Generated by Django 4.1.3 on 2022-12-28 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0001_initial'),
        ('cars', '0002_car_dealership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='dealership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dealerships.dealership'),
            preserve_default=False,
        ),
    ]