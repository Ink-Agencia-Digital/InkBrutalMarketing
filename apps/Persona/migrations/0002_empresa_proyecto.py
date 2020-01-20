# Generated by Django 2.1.7 on 2020-01-14 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('EMP_Id_Empresa', models.BigAutoField(primary_key=True, serialize=False)),
                ('EMP_Nombre_Empresa', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'TBL_Empresas',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('PRY_Id_Proyecto', models.BigAutoField(primary_key=True, serialize=False)),
                ('PRY_Nombre_Proyecto', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('PRY_Empresa_Proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Proyecto_Empresa_Empresa_Id', to='Persona.Empresa')),
                ('PRY_Persona_Proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Proyecto_Persona_Persona_Id', to='Persona.Persona')),
            ],
            options={
                'db_table': 'TBL_Proyectos',
            },
        ),
    ]