from django.contrib import admin
from apps.ProcesoCompra.models import Embudo, Estado, Etapa, Idea

# Register your models here.

admin.site.register(Embudo)
admin.site.register(Estado)
admin.site.register(Etapa)
admin.site.register(Idea)