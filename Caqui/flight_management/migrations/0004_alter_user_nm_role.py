# Generated by Django 4.1.1 on 2022-11-10 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_management', '0003_alter_flight_dt_est_arrival_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nm_role',
            field=models.CharField(choices=[('Piloto', 'Piloto'), ('Operador de voo', 'Operador De Voo'), ('Gerente de operações', 'Gerente De Operacoes'), ('Controlador de Voo', 'Controlador De Voo'), ('Companhia', 'Companhia')], max_length=24),
        ),
    ]
