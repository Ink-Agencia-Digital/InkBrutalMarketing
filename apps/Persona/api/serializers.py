from rest_framework import serializers
from apps.Administrador.models import CustomUser
from apps.Persona.models import Escolaridad, Medio, Comportamiento, Persona, Pregunta, Objetivo, ComportamientoMedio


class UserDisplaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ["username"]

class EscolaridadSerializer(serializers.ModelSerializer):
    ESC_Nombre_Escolaridad = serializers.CharField(max_length=50)
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Escolaridad
        exclude = ["updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class MedioSerializer(serializers.ModelSerializer):
    MDO_Nombre_Medio = serializers.CharField(max_length=150)
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Medio
        exclude = ["updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class PreguntaSerializer(serializers.ModelSerializer):
    PRG_Nombre_Pregunta = serializers.CharField(max_length=150)
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Pregunta
        exclude = ["updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")