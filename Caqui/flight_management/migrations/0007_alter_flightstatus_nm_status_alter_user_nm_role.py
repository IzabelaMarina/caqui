# Generated by Django 4.1.1 on 2022-11-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_management', '0006_alter_flightstatus_nm_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightstatus',
            name='nm_status',
            field=models.IntegerField(choices=[(0, 'Previsto'), (1, 'Cancelado'), (2, 'Embarcando'), (3, 'Programado'), (4, 'Taxiando Ida'), (5, 'Pronto'), (6, 'Autorizado'), (7, 'Em Voo'), (8, 'Aterrissado'), (9, 'Desembarcando')], default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='nm_role',
            field=models.IntegerField(choices=[(0, 'Piloto'), (1, 'Operador De Voo'), (2, 'Gerente De Operacoes'), (3, 'Controlador De Voo')], default=0, max_length=24),
        ),
    ]