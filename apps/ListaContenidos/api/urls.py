from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.ListaContenidos.api import views

router = DefaultRouter()
router.register(r"formato", views.FormatoViewSet)
router.register(r"contenido", views.ContenidoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]