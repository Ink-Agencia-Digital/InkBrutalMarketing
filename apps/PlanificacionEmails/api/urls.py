from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.PlanificacionEmails.api import views

router = DefaultRouter()
router.register(r"tipo-campana", views.TipoCampanaViewSet)
router.register(r"campana", views.CampanaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]