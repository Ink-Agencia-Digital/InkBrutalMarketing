from django.db import models
from ProcesoCompra.models import Embudo, Estados

# Create your models here.

# Modelo de la tabla de Formatos
class Formatos(models.Model):
    FMT_Id_Formato = models.BigAutoField(primary_key = True)
    FMT_Nombre_Formato = models.CharField(max_length = 150)
    FMT_Descripcion_Formato = models.TextField()
    
    class Meta:
        db_table = 'TBL_Formatos'

# Modelo de la tabla de Contenidos
class Contenidos(models.Model):
    CNT_Id_Contenido = models.BigAutoField(primary_key = True)
    CNT_Nombre_Contenido = models.CharField(max_length = 150)
    CNT_Formato_Contenido = models.ForeignKey(Formatos, on_delete=models.CASCADE, related_name='FK_Contenidos_Formato_Id')
    CNT_Embudo_Formato = models.ForeignKey(Embudo, on_delete=models.CASCADE, related_name='FK_Contenidos_Embudo_Id')
    CNT_Relevancia_Formato = models.CharField(max_length = 20)
    CNT_Estado_Formato = models.ForeignKey(Estados, on_delete=models.CASCADE, related_name='FK_Contenidos_Estado_Id')
    
    class Meta:
        db_table = 'TBL_Contenidos'