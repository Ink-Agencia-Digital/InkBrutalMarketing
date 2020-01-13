from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.ListaContenidos.api import views

router = DefaultRouter()
router.register(r"formato", views.FormatoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]