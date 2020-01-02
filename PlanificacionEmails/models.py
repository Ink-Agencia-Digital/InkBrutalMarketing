from django.db import models
from ProcesoCompra.models import Estados
from ListaContenidos.models import Contenidos

# Create your models here.

# Modelo de la tabla de Tipos de Campañas
class TipoCampana(models.Model):
    TCM_Id_Tipo_Campana = models.BigAutoField(primary_key = True)
    TCM_Nombre_Tipo_Campana = models.CharField(max_length = 150)
    TCM_Descripcion_Campana = models.TextField()
    
    class Meta:
        db_table = 'TBL_Tipo_Campana'

# Modelo de la tabla de Campañas
class Campanas(models.Model):
    CMP_Id_Campana = models.BigAutoField(primary_key = True)
    CMP_Nombre_Campana = models.CharField(max_length = 150)
    CMP_Tipo_Campana = models.ForeignKey(TipoCampana, on_delete=models.CASCADE, related_name='FK_Campanas_Tipo_Campana_Id')
    CMP_Fecha_Campana = models.DateField()
    CMP_Horario_Campana = models.TimeField()
    CMP_Frecuencia_Campana = models.CharField(max_length = 50)
    CMP_Estado_Campana = models.ForeignKey(Estados, on_delete=models.CASCADE, related_name='FK_Campanas_Estado_Id')
    CMP_Archivo_Campana = models.TextField()
    CMP_Contenido_Campana = models.ForeignKey(Contenidos, on_delete=models.CASCADE, related_name='FK_Campanas_Contenido_Id')
    
    class Meta:
        db_table = 'TBL_Campanas'