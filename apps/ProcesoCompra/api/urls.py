from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.ProcesoCompra.api import views

router = DefaultRouter()
router.register(r"idea", views.IdeaViewSet)
router.register(r"estado", views.EstadoViewSet)
router.register(r"etapa", views.EtapaViewSet)
router.register(r"embudo", views.EmbudoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]