# Generated by Django 4.2.4 on 2023-08-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_rename_apellido_usuario_apellido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('idPais', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pais', models.CharField(max_length=250)),
            ],
        ),
    ]
