from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.Administrador.models import Usuario, Rol, UsuarioRol, Menu, MenuUsuario, Permiso, UsuarioPermiso, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "is_staff"]

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(UsuarioRol)
admin.site.register(Menu)
admin.site.register(MenuUsuario)
admin.site.register(Permiso)
admin.site.register(UsuarioPermiso)
admin.site.register(CustomUser, CustomUserAdmin)