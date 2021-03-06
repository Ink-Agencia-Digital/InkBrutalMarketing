# Generated by Django 2.1.7 on 2020-01-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0002_empresa_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='EMP_Correo_Empresa',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='EMP_Direccion_Empresa',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='EMP_NIT_Empresa',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='EMP_Telefono_Empresa',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
