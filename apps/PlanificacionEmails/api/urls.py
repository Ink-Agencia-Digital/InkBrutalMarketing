from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.PlanificacionEmails.api import views

router = DefaultRouter()
router.register(r"tipo-campana", views.TipoCampanaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]