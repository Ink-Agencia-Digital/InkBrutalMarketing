from rest_framework import serializers
from apps.ProcesoCompra.models import Idea, Estado, Etapa, Embudo

class IdeaSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Idea
        exclude = ["updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class EstadoSerializer(serializers.ModelSerializer):
    EST_Nombre_Estado = serializers.CharField(max_length=100)
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Estado
        exclude = ["updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")