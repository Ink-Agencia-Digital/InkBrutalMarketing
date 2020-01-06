# Generated by Django 3.0.1 on 2020-01-04 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comportamiento',
            fields=[
                ('CMP_Id_Comportamiento', models.BigAutoField(primary_key=True, serialize=False)),
                ('CMP_Descripcion_Comportamiento', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'TBL_Comportamientos',
            },
        ),
        migrations.CreateModel(
            name='Escolaridad',
            fields=[
                ('ESC_Id_Escolaridad', models.BigAutoField(primary_key=True, serialize=False)),
                ('ESC_Nombre_Escolaridad', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'TBL_Escolaridad',
            },
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('MDO_Id_Medio', models.BigAutoField(primary_key=True, serialize=False)),
                ('MDO_Nombre_Medio', models.CharField(max_length=150)),
                ('MDO_Descripcion_Medio', models.TextField()),
            ],
            options={
                'db_table': 'TBL_Medios',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('PRG_Id_Pregunta', models.BigAutoField(primary_key=True, serialize=False)),
                ('PRG_Nombre_Pregunta', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'TBL_Preguntas',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('PSN_Id_Persona', models.BigAutoField(primary_key=True, serialize=False)),
                ('PSN_Nombres_Persona', models.CharField(max_length=45)),
                ('PSN_Apellidos_Persona', models.CharField(max_length=45)),
                ('PSN_Edad_Persona', models.IntegerField()),
                ('PSN_Sexo_Persona', models.CharField(max_length=25)),
                ('PSN_Cargo_Persona', models.CharField(max_length=45)),
                ('PSN_Comportamiento_Persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Personas_Comportamiento_Id', to='Persona.Comportamiento')),
                ('PSN_Escoladidad_Persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Persona_Escolaridad_Escolaridad_Id', to='Persona.Escolaridad')),
            ],
            options={
                'db_table': 'TBL_Personas',
            },
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('OBJ_Id_Objetivo', models.BigAutoField(primary_key=True, serialize=False)),
                ('OBJ_Respuesta', models.TextField()),
                ('OBJ_Persona_Objetivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Objetivos_Persona_Id', to='Persona.Persona')),
                ('OBJ_Pregunta_Objetivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Objetivos_Pregunta_Id', to='Persona.Pregunta')),
            ],
            options={
                'db_table': 'TBL_Objetivos',
            },
        ),
        migrations.CreateModel(
            name='ComportamientoMedio',
            fields=[
                ('CMP_MDO_Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('CMP_MDO_Comportamiento_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Comportamientos_Medios_Comportamiento_Id', to='Persona.Comportamiento')),
                ('CMP_MDO_Medio_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Comportamientos_Medios_Medio_Id', to='Persona.Medio')),
            ],
            options={
                'db_table': 'TBL_Comportamientos_Medios',
            },
        ),
    ]