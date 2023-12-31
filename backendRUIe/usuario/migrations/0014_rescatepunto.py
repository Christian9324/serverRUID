# Generated by Django 4.2.4 on 2023-09-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_alter_usuario_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='RescatePunto',
            fields=[
                ('idRescate', models.AutoField(primary_key=True, serialize=False)),
                ('oficinaRepre', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=10)),
                ('hora', models.CharField(max_length=5)),
                ('aeropuerto', models.BooleanField(default=False)),
                ('carretero', models.BooleanField(default=False)),
                ('tipoVehic', models.CharField(max_length=30)),
                ('lineaAutobus', models.CharField(max_length=50)),
                ('numeroEcono', models.CharField(max_length=50)),
                ('placas', models.CharField(max_length=20)),
                ('vehiculoAseg', models.BooleanField(default=False)),
                ('casaSeguridad', models.BooleanField(default=False)),
                ('centralAutobus', models.BooleanField(default=False)),
                ('ferrocarril', models.BooleanField(default=False)),
                ('empresa', models.CharField(max_length=150)),
                ('hotel', models.BooleanField(default=False)),
                ('nombreHotel', models.CharField(max_length=100)),
                ('puestosADispo', models.BooleanField(default=False)),
                ('juezCalif', models.BooleanField(default=False)),
                ('reclusorio', models.BooleanField(default=False)),
                ('policiaFede', models.BooleanField(default=False)),
                ('dif', models.BooleanField(default=False)),
                ('policiaEsta', models.BooleanField(default=False)),
                ('policiaMuni', models.BooleanField(default=False)),
                ('guardiaNaci', models.BooleanField(default=False)),
                ('fiscalia', models.BooleanField(default=False)),
                ('otrasAuto', models.BooleanField(default=False)),
                ('voluntarios', models.BooleanField(default=False)),
                ('otro', models.BooleanField(default=False)),
                ('presuntosDelincuentes', models.BooleanField(default=False)),
                ('numPresuntosDelincuentes', models.IntegerField()),
                ('municipio', models.CharField(max_length=200)),
                ('puntoEstra', models.CharField(max_length=250)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('iso3', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=150)),
                ('noIdentidad', models.CharField(max_length=50)),
                ('parentesco', models.CharField(max_length=50)),
                ('fechaNacimiento', models.CharField(max_length=10)),
                ('sexo', models.BooleanField(default=False)),
                ('numFamilia', models.IntegerField()),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
