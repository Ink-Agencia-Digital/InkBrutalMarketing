from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.ProcesoCompra.api.serializers import (EstadoSerializer, IdeaSerializer,
                                                EtapaSerializer, EmbudoSerializer)
from apps.ProcesoCompra.api.permissions import IsAuthorOrReadOnly
from apps.ProcesoCompra.models import Estado, Idea, Etapa, Embudo

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class EtapaViewSet(viewsets.ModelViewSet):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class EmbudoViewSet(viewsets.ModelViewSet):
    queryset = Embudo.objects.all()
    serializer_class = EmbudoSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()