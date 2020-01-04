from django.contrib import admin
from apps.PlanificacionEmails.models import Campana, TipoCampana

# Register your models here.

admin.site.register(Campana)
admin.site.register(TipoCampana)