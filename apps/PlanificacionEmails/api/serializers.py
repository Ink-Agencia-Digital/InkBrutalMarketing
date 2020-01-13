from rest_framework import serializers
from apps.PlanificacionEmails.models import TipoCampana, Campana

class TipoCampanaSerializer(serializers.ModelSerializer):
    TCM_Nombre_Tipo_Campana = serializers.CharField(max_length=150)
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = TipoCampana
        exclude = ["updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")