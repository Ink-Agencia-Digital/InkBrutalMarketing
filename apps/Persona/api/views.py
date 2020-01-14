from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import get_object_or_404
from apps.Persona.api.serializers import (UserDisplaySerializer, EscolaridadSerializer,
                                          MedioSerializer, PreguntaSerializer, PersonaSerializer,
                                          ComportamientoSerializer, ComportamientoMedioSerializer,
                                          ObjetivoSerializer)
from apps.Persona.api.permissions import IsAuthorOrReadOnly
from apps.Persona.models import (Escolaridad, Medio, Pregunta, Persona, Comportamiento,
                                 ComportamientoMedio, Objetivo)

class CurrentUserAPIView(APIView):
    
    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)

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

class MedioViewSet(viewsets.ModelViewSet):
    queryset = Medio.objects.all()
    serializer_class = MedioSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class ComportamientoViewSet(viewsets.ModelViewSet):
    queryset = Comportamiento.objects.all()
    serializer_class = ComportamientoSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class ComportamientoMedioViewSet(viewsets.ModelViewSet):
    queryset = ComportamientoMedio.objects.all()
    serializer_class = ComportamientoMedioSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

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