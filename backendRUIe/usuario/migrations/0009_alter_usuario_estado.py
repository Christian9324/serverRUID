# Generated by Django 4.2.4 on 2023-09-01 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_alter_usuario_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.IntegerField(choices=[(1, 'AGUASCALIENTES'), (2, 'BAJA CALIFORNIA'), (3, 'BAJA CALIFORNIA SUR'), (4, 'CAMPECHE'), (5, 'CDMX'), (6, 'CHIAPAS'), (7, 'CHIHUAHUA'), (8, 'COAHUILA'), (9, 'COLIMA'), (10, 'DURANGO'), (11, 'EDOMEX'), (12, 'GUANAJUATO'), (13, 'GUERRERO'), (14, 'HIDALGO'), (15, 'JALISCO'), (16, 'MICHOACÁN'), (17, 'MORELOS'), (18, 'NAYARIT'), (19, 'NUEVO LEÓN'), (20, 'OAXACA'), (21, 'PUEBLA'), (22, 'QUERÉTARO'), (23, 'QUINTANA ROO'), (24, 'SAN LUIS POTOSÍ'), (25, 'SINALOA'), (26, 'SONORA'), (27, 'TABASCO'), (28, 'TAMAULIPAS'), (29, 'TLAXCALA'), (30, 'VERACRUZ'), (31, 'YUCATÁN'), (32, 'ZACATECAS')], default=1),
        ),
    ]