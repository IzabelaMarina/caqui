# Generated by Django 4.1.1 on 2022-11-10 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_management', '0002_alter_flight_fk_flightstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='dt_est_arrival',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='dt_est_departure',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
