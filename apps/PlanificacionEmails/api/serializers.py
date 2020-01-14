from rest_framework import serializers
from apps.PlanificacionEmails.models import TipoCampana, Campana

class TipoCampanaSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = TipoCampana
        fields = ["TCM_Id_Tipo_Campana", "TCM_Nombre_Tipo_Campana", "TCM_Descripcion_Campana", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class CampanaSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Campana
        fields = ["CMP_Id_Campana", "CMP_Nombre_Campana", "CMP_Tipo_Campana", "CMP_Fecha_Campana", "CMP_Horario_Campana", "CMP_Frecuencia_Campana", "CMP_Estado_Campana", "CMP_Archivo_Campana", "CMP_Contenido_Campana", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")