# Generated by Django 4.2.4 on 2023-09-07 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_puntosinternacion_alter_usuario_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='paises',
            name='iso3',
            field=models.CharField(max_length=3, null=True),
        ),
    ]