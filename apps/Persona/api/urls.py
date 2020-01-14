from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Persona.api import views

from apps.Persona.api.views import CurrentUserAPIView

router = DefaultRouter()
router.register(r"empresa", views.EmpresaViewSet)
router.register(r"escolaridad", views.EscolaridadViewSet)
router.register(r"persona", views.PersonaViewSet)
router.register(r"proyecto", views.ProyectoViewSet)
router.register(r"medio", views.MedioViewSet)
router.register(r"comportamiento", views.ComportamientoViewSet)
router.register(r"comportamiento-medio", views.ComportamientoMedioViewSet)
router.register(r"pregunta", views.PreguntaViewSet)
router.register(r"objetivo", views.ObjetivoViewSet)

urlpatterns = [
    path("usuario/", CurrentUserAPIView.as_view(), name="usuario-actual"),
    path("", include(router.urls)),
]