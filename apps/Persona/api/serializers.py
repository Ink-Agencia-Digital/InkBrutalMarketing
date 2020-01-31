from rest_framework import serializers
from apps.Administrador.models import CustomUser
from apps.Persona.models import (Escolaridad, Medio, Comportamiento, Persona,
                                 Pregunta, Objetivo, ComportamientoMedio, Empresa,
                                 Proyecto)


class UserDisplaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ["username"]

class EmpresaSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Empresa
        fields = ["EMP_Id_Empresa", "EMP_Nombre_Empresa", "EMP_NIT_Empresa", "EMP_Telefono_Empresa", "EMP_Direccion_Empresa", "EMP_Correo_Empresa", "EMP_Tamano_Empresa", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class EscolaridadSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Escolaridad
        fields = ["ESC_Id_Escolaridad", "ESC_Nombre_Escolaridad", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class PersonaSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Persona
        fields = ["PSN_Id_Persona", "PSN_Nombres_Persona", "PSN_Apellidos_Persona", "PSN_Edad_Persona", "PSN_Escoladidad_Persona", "PSN_Sexo_Persona", "PSN_Cargo_Persona", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class PersonaJoinSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    PSN_Escoladidad_Persona = EscolaridadSerializer(many = False)
    
    class Meta:
        model = Persona
        fields = ["PSN_Id_Persona", "PSN_Nombres_Persona", "PSN_Apellidos_Persona", "PSN_Edad_Persona", "PSN_Escoladidad_Persona", "PSN_Sexo_Persona", "PSN_Cargo_Persona", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class ProyectoSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Proyecto
        fields = ["PRY_Id_Proyecto", "PRY_Nombre_Proyecto", "PRY_Empresa_Proyecto", "PRY_Persona_Proyecto", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class ProyectoJoinSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    PRY_Empresa_Proyecto = EmpresaSerializer(many = False)
    PRY_Persona_Proyecto = PersonaSerializer(many = False)
    
    class Meta:
        model = Proyecto
        fields = ["PRY_Id_Proyecto", "PRY_Nombre_Proyecto", "PRY_Empresa_Proyecto", "PRY_Persona_Proyecto", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class MedioSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Medio
        fields = ["MDO_Id_Medio", "MDO_Nombre_Medio", "MDO_Descripcion_Medio", "MDO_Icono_Medio", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class ComportamientoSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Comportamiento
        fields = ["CMP_Id_Comportamiento", "CMP_Descripcion_Comportamiento", "CMP_Persona_Comportamiento", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class ComportamientoJoinSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    CMP_Persona_Comportamiento = PersonaSerializer(many = False)
    
    class Meta:
        model = Comportamiento
        fields = ["CMP_Id_Comportamiento", "CMP_Descripcion_Comportamiento", "CMP_Persona_Comportamiento", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class ComportamientoMedioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComportamientoMedio
        fields = ["CMP_MDO_Id", "CMP_MDO_Comportamiento_Id", "CMP_MDO_Medio_Id"]

class PreguntaSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Pregunta
        fields = ["PRG_Id_Pregunta", "PRG_Nombre_Pregunta", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class ObjetivoSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Objetivo
        fields = ["OBJ_Id_Objetivo", "OBJ_Persona_Objetivo", "OBJ_Pregunta_Objetivo", "OBJ_Respuesta_Objetivo", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class ObjetivoJoinSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    OBJ_Persona_Objetivo = PersonaSerializer(many = False)
    OBJ_Pregunta_Objetivo = PreguntaSerializer(many = False)
    
    class Meta:
        model = Objetivo
        fields = ["OBJ_Id_Objetivo", "OBJ_Persona_Objetivo", "OBJ_Pregunta_Objetivo", "OBJ_Respuesta_Objetivo", "created_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")