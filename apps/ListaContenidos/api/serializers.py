from rest_framework import serializers
from apps.ListaContenidos.models import Formato

class FormatoSerializer(serializers.ModelSerializer):
    FMT_Nombre_Formato = serializers.CharField(max_length=150)
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Formato
        exclude = ["updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

"""class ContenidoSerializer(serializers.ModelSerializer):
    CNT_Nombre_Contenido = serializers.CharField(max_length=150)
    CNT_Formato_Contenido = serializers.StringRelatedField(read_only=True)
    CNT_Embudo_Formato = serializers.StringRelatedField(read_only=True)
    CNT_Relevancia_Formato = serializers.StringRelatedField(read_only=True)
    CNT_Estado_Formato = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Formato
        exclude = ["updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")"""