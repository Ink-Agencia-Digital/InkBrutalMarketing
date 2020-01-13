from django.db import models
from apps.ProcesoCompra.models import Embudo, Estado

# Create your models here.

# Modelo de la tabla de Formatos
class Formato(models.Model):
    FMT_Id_Formato = models.BigAutoField(primary_key = True)
    FMT_Nombre_Formato = models.CharField(max_length = 150)
    FMT_Descripcion_Formato = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Formatos'

# Modelo de la tabla de Contenidos
class Contenido(models.Model):
    CNT_Id_Contenido = models.BigAutoField(primary_key = True)
    CNT_Nombre_Contenido = models.CharField(max_length = 150)
    CNT_Formato_Contenido = models.ForeignKey(Formato, on_delete=models.CASCADE, related_name='FK_Contenidos_Formato_Id')
    CNT_Embudo_Formato = models.OneToOneField(Embudo, on_delete=models.CASCADE, related_name='FK_Contenidos_Embudo_Id')
    CNT_Relevancia_Formato = models.CharField(max_length = 20)
    CNT_Estado_Formato = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='FK_Contenidos_Estado_Id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'TBL_Contenidos'