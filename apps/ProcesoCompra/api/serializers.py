from rest_framework import serializers
from apps.ProcesoCompra.models import Idea, Estado, Etapa, Embudo

class EstadoSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Estado
        fields = ["EST_Id_Estado", "EST_Nombre_Estado", "EST_Descripcion_Estado", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class EtapaSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Etapa
        fields = ["ETP_Id_Etapa", "ETP_Descripcion_Etapa", "ETP_Estado_Etapa", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class IdeaSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Idea
        fields = ["IDA_Id_Idea", "IDA_Descripcion_Idea", "IDA_Etapa_Idea", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class EmbudoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Embudo
        fields = ["EBD_Id_Embudo", "EBD_Persona_Embudo", "EBD_Etapa_Embudo"]