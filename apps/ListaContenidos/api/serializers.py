from rest_framework import serializers
from apps.ListaContenidos.models import Formato, Contenido

class FormatoSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Formato
        fields = ["FMT_Id_Formato", "FMT_Nombre_Formato", "FMT_Descripcion_Formato", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class ContenidoSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Contenido
        fields = ["CNT_Id_Contenido", "CNT_Nombre_Contenido", "CNT_Formato_Contenido", "CNT_Embudo_Formato", "CNT_Relevancia_Formato", "CNT_Estado_Formato", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")