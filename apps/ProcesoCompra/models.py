from django.db import models
from apps.Persona.models import Persona

# Create your models here.

# Modelo de la tabla de Ideas
class Idea(models.Model):
    IDA_Id_Idea = models.BigAutoField(primary_key = True)
    IDA_Descripcion_Idea = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Ideas'

# Modelo de la tabla de Estados
class Estado(models.Model):
    EST_Id_Estado = models.BigAutoField(primary_key = True)
    EST_Nombre_Estado = models.CharField(max_length = 100)
    EST_Descripcion_Estado = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Estados'

# Modelo de la tabla de Etapas
class Etapa(models.Model):
    ETP_Id_Etapa = models.BigAutoField(primary_key = True)
    ETP_Descripcion_Etapa = models.TextField()
    ETP_Idea_Etapa = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='FK_Etapas_Idea_Id')
    ETP_Estado_Etapa = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='FK_Etapas_Estado_Id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Etapas'

# Modelo de la tabla de Embudo
class Embudo(models.Model):
    EBD_Id_Embudo = models.BigAutoField(primary_key = True)
    EBD_Persona_Embudo = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='FK_Embudo_Persona_Id')
    EBD_Etapa_Embudo = models.ForeignKey(Etapa, on_delete=models.CASCADE, related_name='FK_Embudo_Etapa_Id')
    
    class Meta:
        db_table = 'TBL_Embudo'