# Generated by Django 4.2.4 on 2023-09-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_alter_estadofuerza_latitud_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(choices=[('1', 'AGUASCALIENTES'), ('2', 'BAJA CALIFORNIA'), ('3', 'BAJA CALIFORNIA SUR'), ('4', 'CAMPECHE'), ('5', 'COAHUILA'), ('6', 'COLIMA'), ('7', 'CHIAPAS'), ('8', 'CHIHUAHUA'), ('9', 'CDMX'), ('10', 'DURANGO'), ('11', 'GUANAJUATO'), ('12', 'GUERRERO'), ('13', 'HIDALGO'), ('14', 'JALISCO'), ('15', 'EDOMEX'), ('16', 'MICHOACÁN'), ('17', 'MORELOS'), ('18', 'NAYARIT'), ('19', 'NUEVO LEÓN'), ('20', 'OAXACA'), ('21', 'PUEBLA'), ('22', 'QUERÉTARO'), ('23', 'QUINTANA ROO'), ('24', 'SAN LUIS POTOSÍ'), ('25', 'SINALOA'), ('26', 'SONORA'), ('27', 'TABASCO'), ('28', 'TAMAULIPAS'), ('29', 'TLAXCALA'), ('30', 'VERACRUZ'), ('31', 'YUCATÁN'), ('32', 'ZACATECAS')], default='9', max_length=2),
        ),
    ]
