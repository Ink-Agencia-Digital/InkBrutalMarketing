from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Persona.api import views

from apps.Persona.api.views import CurrentUserAPIView

router = DefaultRouter()
router.register(r"empresa", views.EmpresaViewSet)
router.register(r"escolaridad", views.EscolaridadViewSet)
router.register(r"persona", views.PersonaViewSet)
router.register(r"persona-join", views.PersonaJoinViewSet)
router.register(r"proyecto", views.ProyectoViewSet)
router.register(r"proyecto-join", views.ProyectoJoinViewSet)
router.register(r"comportamiento", views.ComportamientoViewSet)
router.register(r"comportamiento-join", views.ComportamientoJoinViewSet)
router.register(r"comportamiento-ultimo", views.ComportamientoUltimoViewSet)
router.register(r"medio", views.MedioViewSet)
router.register(r"comportamiento-medio", views.ComportamientoMedioViewSet)
router.register(r"pregunta", views.PreguntaViewSet)
router.register(r"objetivo", views.ObjetivoViewSet)

urlpatterns = [
    path("usuario/", CurrentUserAPIView.as_view(), name="usuario-actual"),
    path("persona/<int:pk>/filtro/", views.PersonaFiltroView.as_view(), name="filtro-personas"),
    path("persona/<int:pk>/medio/", views.MedioPersonaView.as_view(), name="medios-persona"),
    path("persona/<int:idpersona>/objetivo/", views.ObjetivoPersonaViewSet.as_view(), name="objetivos-persona"),
    path("", include(router.urls)),
]