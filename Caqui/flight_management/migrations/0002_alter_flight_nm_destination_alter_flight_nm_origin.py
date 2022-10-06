# Generated by Django 4.1.1 on 2022-10-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='nm_destination',
            field=models.CharField(choices=[(0, 'Bsb'), (1, 'Cgh'), (2, 'Gig'), (3, 'Ssa'), (4, 'Fln'), (5, 'Poa'), (6, 'Vcp'), (7, 'Rec'), (8, 'Cwb'), (9, 'Bel'), (10, 'Vix'), (11, 'Sdu'), (12, 'Cgb'), (13, 'Cgr'), (14, 'For'), (15, 'Mcp'), (16, 'Mgf'), (17, 'Gyn'), (18, 'Nvt'), (19, 'Mao'), (20, 'Nat'), (21, 'Bps'), (22, 'Mcz'), (23, 'Pmw'), (24, 'Slz'), (25, 'Gru'), (26, 'Ldb'), (27, 'Pvh'), (28, 'Rbr'), (29, 'Joi'), (30, 'Udi'), (31, 'Cxj'), (32, 'Igu'), (33, 'The'), (34, 'Aju'), (35, 'Jpa'), (36, 'Pnz'), (37, 'Cnf'), (38, 'Bvb'), (39, 'Cpv'), (40, 'Stm'), (41, 'Ios'), (42, 'Jdo'), (43, 'Imp'), (44, 'Xap'), (45, 'Mab'), (46, 'Czs'), (47, 'Ppb'), (48, 'Cfb'), (49, 'Fen'), (50, 'Jtc'), (51, 'Moc')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flight',
            name='nm_origin',
            field=models.CharField(choices=[(0, 'Bsb'), (1, 'Cgh'), (2, 'Gig'), (3, 'Ssa'), (4, 'Fln'), (5, 'Poa'), (6, 'Vcp'), (7, 'Rec'), (8, 'Cwb'), (9, 'Bel'), (10, 'Vix'), (11, 'Sdu'), (12, 'Cgb'), (13, 'Cgr'), (14, 'For'), (15, 'Mcp'), (16, 'Mgf'), (17, 'Gyn'), (18, 'Nvt'), (19, 'Mao'), (20, 'Nat'), (21, 'Bps'), (22, 'Mcz'), (23, 'Pmw'), (24, 'Slz'), (25, 'Gru'), (26, 'Ldb'), (27, 'Pvh'), (28, 'Rbr'), (29, 'Joi'), (30, 'Udi'), (31, 'Cxj'), (32, 'Igu'), (33, 'The'), (34, 'Aju'), (35, 'Jpa'), (36, 'Pnz'), (37, 'Cnf'), (38, 'Bvb'), (39, 'Cpv'), (40, 'Stm'), (41, 'Ios'), (42, 'Jdo'), (43, 'Imp'), (44, 'Xap'), (45, 'Mab'), (46, 'Czs'), (47, 'Ppb'), (48, 'Cfb'), (49, 'Fen'), (50, 'Jtc'), (51, 'Moc')], max_length=3),
        ),
    ]
