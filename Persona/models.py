from django.db import models

# Create your models here.

# Modelo de la tabla de Escolaridad
class Escolaridad(models.Model):
    ESC_Id_Escolaridad = models.BigAutoField(primary_key = True)
    ESC_Nombre_Escolaridad = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'TBL_Escolaridad'

# Modelo de la tabla de Medios
class Medios(models.Model):
    MDO_Id_Medio = models.BigAutoField(primary_key = True)
    MDO_Nombre_Medio = models.CharField(max_length = 150)
    MDO_Descripcion_Medio = models.TextField()
    
    class Meta:
        db_table = 'TBL_Medios'

# Modelo de la tabla de Comportamientos
class Comportamientos(models.Model):
    CMP_Id_Comportamiento = models.BigAutoField(primary_key = True)
    CMP_Descripcion_Comportamiento = models.CharField(max_length = 150)
    
    class Meta:
        db_table = 'TBL_Comportamientos'

# Modelo de la tabla de Relación Comportamiento-Medios
class ComportamientosMedios(models.Model):
    CMP_MDO_Id = models.BigAutoField(primary_key = True)
    CMP_MDO_Comportamiento_Id = models.ForeignKey(Comportamientos, on_delete=models.CASCADE, related_name='FK_Comportamientos_Medios_Comportamiento_Id')
    CMP_MDO_Medios_Id = models.ForeignKey(Medios, on_delete=models.CASCADE, related_name='FK_Comportamientos_Medios_Medio_Id')
    
    class Meta:
        db_table = 'TBL_Comportamientos_Medios'

# Modelo de la tabla de Personas
class Personas(models.Model):
    PSN_Nombres_Persona = models.CharField(max_length = 45)
    PSN_Apellidos_Persona = models.CharField(max_length = 45)
    PSN_Edad_Persona = models.IntegerField()
    PSN_Escoladidad_Persona = models.ForeignKey(Escolaridad, on_delete=models.CASCADE, related_name='FK_Persona_Escolaridad_Escolaridad_Id')
    PSN_Sexo_Persona = models.CharField(max_length = 25)
    PSN_Cargo_Persona = models.CharField(max_length = 45)
    PSN_Comportamiento_Persona = models.ForeignKey(Comportamientos, on_delete=models.CASCADE, related_name='FK_Personas_Comportamiento_Id')
    
    class Meta:
        db_table = 'TBL_Personas'

# Modelo de la tabla de Preguntas
class Preguntas(models.Model):
    PRG_Id_Pregunta = models.BigAutoField(primary_key = True)
    PRG_Nombre_Pregunta = models.CharField(max_length = 150)
    
    class Meta:
        db_table = 'TBL_Preguntas'

# Modelo de la tabla de Objetivos
class Objetivos(models.Model):
    OBJ_Id_Objetivo = models.BigAutoField(primary_key = True)
    OBJ_Persona_Objetivo = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='FK_Objetivos_Persona_Id')
    OBJ_Pregunta_Objetivo = models.ForeignKey(Preguntas, on_delete=models.CASCADE, related_name='FK_Objetivos_Pregunta_Id')
    OBJ_Respuesta = models.TextField()
    
    class Meta:
        db_table = 'TBL_Objetivos'