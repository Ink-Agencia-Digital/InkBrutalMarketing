from django.db import models
from Persona.models import Personas

# Create your models here.

# Modelo de la tabla de Ideas
class Ideas(models.Model):
    IDA_Id_Idea = models.BigAutoField(primary_key = True)
    IDA_Descripcion_Idea = models.TextField()
    
    class Meta:
        db_table = 'TBL_Ideas'

# Modelo de la tabla de Estados
class Estados(models.Model):
    EST_Id_Estado = models.BigAutoField(primary_key = True)
    EST_Nombre_Estado = models.CharField(max_length = 100)
    EST_Descripcion_Estado = models.TextField()
    
    class Meta:
        db_table = 'TBL_Estados'

# Modelo de la tabla de Etapas
class Etapas(models.Model):
    ETP_Id_Etapa = models.BigAutoField(primary_key = True)
    ETP_Descripcion_Etapa = models.TextField()
    ETP_Idea_Etapa = models.ForeignKey(Ideas, on_delete=models.CASCADE, related_name='FK_Etapas_Idea_Id')
    ETP_Estado_Etapa = models.ForeignKey(Estados, on_delete=models.CASCADE, related_name='FK_Etapas_Estado_Id')
    
    class Meta:
        db_table = 'TBL_Etapas'

# Modelo de la tabla de Embudo
class Embudo(models.Model):
    EBD_Id_Embudo = models.BigAutoField(primary_key = True)
    EBD_Persona_Embudo = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='FK_Embudo_Persona_Id')
    EBD_Etapa_Embudo = models.ForeignKey(Etapas, on_delete=models.CASCADE, related_name='FK_Embudo_Etapa_Id')
    
    class Meta:
        db_table = 'TBL_Embudo'