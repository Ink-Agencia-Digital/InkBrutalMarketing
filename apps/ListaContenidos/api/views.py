from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.ListaContenidos.api.serializers import (FormatoSerializer, ContenidoSerializer)
from apps.ListaContenidos.api.permissions import IsAuthorOrReadOnly
from apps.ListaContenidos.models import Formato, Contenido

class FormatoViewSet(viewsets.ModelViewSet):
    queryset = Formato.objects.all()
    serializer_class = FormatoSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class ContenidoViewSet(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()