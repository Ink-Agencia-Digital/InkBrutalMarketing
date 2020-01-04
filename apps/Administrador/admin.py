from django.contrib import admin
from apps.Administrador.models import Usuario, Rol, UsuarioRol, Menu, MenuUsuario, Permiso, UsuarioPermiso

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(UsuarioRol)
admin.site.register(Menu)
admin.site.register(MenuUsuario)
admin.site.register(Permiso)
admin.site.register(UsuarioPermiso)