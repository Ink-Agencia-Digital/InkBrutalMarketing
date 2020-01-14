from django.contrib import admin
from apps.Persona.models import (Comportamiento, ComportamientoMedio, Escolaridad,
                                 Medio, Objetivo, Persona, Pregunta, Empresa, Proyecto)

# Register your models here.

admin.site.register(Comportamiento)
admin.site.register(ComportamientoMedio)
admin.site.register(Escolaridad)
admin.site.register(Medio)
admin.site.register(Objetivo)
admin.site.register(Persona)
admin.site.register(Pregunta)
admin.site.register(Empresa)
admin.site.register(Proyecto)