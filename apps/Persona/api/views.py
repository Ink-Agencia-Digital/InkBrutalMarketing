from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import get_object_or_404
from apps.Persona.api.serializers import (UserDisplaySerializer, EscolaridadSerializer,
                                          MedioSerializer, PreguntaSerializer, PersonaSerializer,
                                          ComportamientoSerializer, ComportamientoMedioSerializer,
                                          ObjetivoSerializer, EmpresaSerializer, ProyectoSerializer,
                                          PersonaJoinSerializer, ProyectoJoinSerializer,
                                          ComportamientoJoinSerializer)
from apps.Persona.api.permissions import IsAuthorOrReadOnly
from apps.Persona.models import (Escolaridad, Medio, Pregunta, Persona, Comportamiento,
                                 ComportamientoMedio, Objetivo, Empresa, Proyecto)

class CurrentUserAPIView(APIView):
    
    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class EscolaridadViewSet(viewsets.ModelViewSet):
    queryset = Escolaridad.objects.all()
    serializer_class = EscolaridadSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class PersonaJoinViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaJoinSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class PersonaFiltroView(generics.ListAPIView):
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def get_queryset(self):
        pk = int (self.kwargs.get("pk"))
        queryset = Persona.objects.all()
        queryset_j = Persona.objects.raw('''SELECT 
                                         TBL_Personas.PSN_Id_Persona, 
                                         TBL_Personas.PSN_Nombres_Persona, 
                                         TBL_Personas.PSN_Apellidos_Persona, 
                                         TBL_Personas.PSN_Edad_Persona, 
                                         TBL_Personas.PSN_Escoladidad_Persona_id, 
                                         TBL_Personas.PSN_Sexo_Persona, 
                                         TBL_Personas.PSN_Cargo_Persona, 
                                         TBL_Personas.created_at, 
                                         TBL_Personas.updated_at 
                                         FROM TBL_Personas 
                                         inner join TBL_Proyectos 
                                         on TBL_Proyectos.PRY_Persona_Proyecto_id = TBL_Personas.PSN_Id_Persona
                                         where TBL_Proyectos.PRY_Empresa_Proyecto_id = %s''', [pk])
        if queryset_j:
            filtro = []
            for psn in queryset:
                if psn not in queryset_j:
                    filtro.append(psn)
            return filtro
        else:
            return queryset

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class ProyectoJoinViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoJoinSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class MedioViewSet(viewsets.ModelViewSet):
    queryset = Medio.objects.all()
    serializer_class = MedioSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class MedioPersonaView(generics.ListAPIView):
    serializer_class = MedioSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def get_queryset(self):
        pk = (self.kwargs.get("pk"))
        queryset = Medio.objects.raw('''SELECT 
                                         TBL_Medios.MDO_Id_Medio, 
                                         TBL_Medios.MDO_Nombre_Medio, 
                                         TBL_Medios.MDO_Descripcion_Medio, 
                                         TBL_Medios.created_at, 
                                         TBL_Medios.updated_at 
                                         FROM TBL_Medios 
                                         inner join TBL_Comportamientos_Medios 
                                         on TBL_Comportamientos_Medios.CMP_MDO_Medio_Id_id = TBL_Medios.MDO_Id_Medio
                                         where TBL_Comportamientos_Medios.CMP_MDO_Comportamiento_Id_id = %s''', [pk])
        return queryset

class ComportamientoViewSet(viewsets.ModelViewSet):
    queryset = Comportamiento.objects.all()
    serializer_class = ComportamientoSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class ComportamientoJoinViewSet(viewsets.ModelViewSet):
    queryset = Comportamiento.objects.all()
    serializer_class = ComportamientoJoinSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class ComportamientoMedioViewSet(viewsets.ModelViewSet):
    queryset = ComportamientoMedio.objects.all()
    serializer_class = ComportamientoMedioSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class ComportamientoUltimoViewSet(viewsets.ModelViewSet):
    #queryset = Comportamiento.objects.raw("SELECT * FROM TBL_Comportamientos ORDER BY CMP_Id_Comportamiento DESC LIMIT 1")
    queryset = Comportamiento.objects.order_by('-created_at')
    serializer_class = ComportamientoSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class ObjetivoViewSet(viewsets.ModelViewSet):
    queryset = Objetivo.objects.all()
    serializer_class = ObjetivoSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()