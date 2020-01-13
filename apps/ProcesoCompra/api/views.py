from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.ProcesoCompra.api.serializers import (EstadoSerializer, IdeaSerializer)
from apps.ProcesoCompra.api.permissions import IsAuthorOrReadOnly
from apps.ProcesoCompra.models import Estado, Idea

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