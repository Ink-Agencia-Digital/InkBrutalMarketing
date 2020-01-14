from django.db import models

# Create your models here.

# Modelo de la tabla Empresa
class Empresa(models.Model):
    EMP_Id_Empresa = models.BigAutoField(primary_key = True)
    EMP_Nombre_Empresa = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Empresas'

# Modelo de la tabla de Escolaridad
class Escolaridad(models.Model):
    ESC_Id_Escolaridad = models.BigAutoField(primary_key = True)
    ESC_Nombre_Escolaridad = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Escolaridad'

# Modelo de la tabla de Personas
class Persona(models.Model):
    PSN_Id_Persona = models.BigAutoField(primary_key = True)
    PSN_Nombres_Persona = models.CharField(max_length = 45)
    PSN_Apellidos_Persona = models.CharField(max_length = 45)
    PSN_Edad_Persona = models.IntegerField()
    PSN_Escoladidad_Persona = models.ForeignKey(Escolaridad, on_delete=models.CASCADE, related_name='FK_Persona_Escolaridad_Escolaridad_Id')
    PSN_Sexo_Persona = models.CharField(max_length = 25)
    PSN_Cargo_Persona = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Personas'

# Modelo de la tabla Proyecto
class Proyecto(models.Model):
    PRY_Id_Proyecto = models.BigAutoField(primary_key = True)
    PRY_Nombre_Proyecto = models.CharField(max_length = 150)
    PRY_Empresa_Proyecto = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='FK_Proyecto_Empresa_Empresa_Id')
    PRY_Persona_Proyecto = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='FK_Proyecto_Persona_Persona_Id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Proyectos'

# Modelo de la tabla de Medios
class Medio(models.Model):
    MDO_Id_Medio = models.BigAutoField(primary_key = True)
    MDO_Nombre_Medio = models.CharField(max_length = 150)
    MDO_Descripcion_Medio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Medios'

# Modelo de la tabla de Comportamientos
class Comportamiento(models.Model):
    CMP_Id_Comportamiento = models.BigAutoField(primary_key = True)
    CMP_Descripcion_Comportamiento = models.CharField(max_length = 150)
    CMP_Persona_Comportamiento = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='FK_Comportamiento_Personas_Id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Comportamientos'

# Modelo de la tabla de Relación Comportamiento-Medios
class ComportamientoMedio(models.Model):
    CMP_MDO_Id = models.BigAutoField(primary_key = True)
    CMP_MDO_Comportamiento_Id = models.ForeignKey(Comportamiento, on_delete=models.CASCADE, related_name='FK_Comportamientos_Medios_Comportamiento_Id')
    CMP_MDO_Medio_Id = models.ForeignKey(Medio, on_delete=models.CASCADE, related_name='FK_Comportamientos_Medios_Medio_Id')
    
    class Meta:
        db_table = 'TBL_Comportamientos_Medios'

# Modelo de la tabla de Preguntas
class Pregunta(models.Model):
    PRG_Id_Pregunta = models.BigAutoField(primary_key = True)
    PRG_Nombre_Pregunta = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Preguntas'

# Modelo de la tabla de Objetivos
class Objetivo(models.Model):
    OBJ_Id_Objetivo = models.BigAutoField(primary_key = True)
    OBJ_Persona_Objetivo = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='FK_Objetivos_Persona_Id')
    OBJ_Pregunta_Objetivo = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='FK_Objetivos_Pregunta_Id')
    OBJ_Respuesta_Objetivo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Objetivos'