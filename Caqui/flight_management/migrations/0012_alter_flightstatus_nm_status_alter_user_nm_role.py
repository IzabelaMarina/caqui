# Generated by Django 4.1.1 on 2022-11-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_management', '0011_alter_flight_nm_destination_alter_flight_nm_origin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightstatus',
            name='nm_status',
            field=models.CharField(choices=[('Previsto', 'Previsto'), ('Cancelado', 'Cancelado'), ('Embarcando', 'Embarcando'), ('Programado', 'Programado'), ('Taxiando', 'Taxiando Ida'), ('Pronto', 'Pronto'), ('Autorizado', 'Autorizado'), ('Em Voo', 'Em Voo'), ('Aterrissado', 'Aterrissado'), ('Desembarcando', 'Desembarcando')], default=0, max_length=13),
        ),
        migrations.AlterField(
            model_name='user',
            name='nm_role',
            field=models.IntegerField(choices=[('0', 'Piloto'), ('1', 'Operador De Voo'), ('2', 'Gerente De Operacoes'), ('3', 'Controlador de Voo')]),
        ),
    ]
