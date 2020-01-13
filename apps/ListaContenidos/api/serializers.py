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