from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.PlanificacionEmails.api.serializers import (TipoCampanaSerializer)
from apps.PlanificacionEmails.api.permissions import IsAuthorOrReadOnly
from apps.PlanificacionEmails.models import TipoCampana, Campana

class TipoCampanaViewSet(viewsets.ModelViewSet):
    queryset = TipoCampana.objects.all()
    serializer_class = TipoCampanaSerializer
    pemission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()