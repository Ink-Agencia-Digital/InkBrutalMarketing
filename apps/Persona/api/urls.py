from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Persona.api import views

from apps.Persona.api.views import CurrentUserAPIView

router = DefaultRouter()
router.register(r"escolaridad", views.EscolaridadViewSet)
router.register(r"medio", views.MedioViewSet)
router.register(r"pregunta", views.PreguntaViewSet)

urlpatterns = [
    path("usuario/", CurrentUserAPIView.as_view(), name="usuario-actual"),
    path("", include(router.urls)),
]