from django.db import models

# Create your models here.

# Modelo de la tabla de Usuarios
class Usuario(models.Model):
    USR_Id_Usuario = models.BigAutoField(primary_key=True)
    USR_Tipo_Documento_Usuario = models.CharField(max_length=30)
    USR_Documento_Usuario = models.CharField(max_length=50)
    USR_Nombres_Usuario = models.CharField(max_length=50)
    USR_Apellidos_Usuario = models.CharField(max_length=50)
    USR_Direccion_Usuario = models.CharField(max_length=50)
    USR_Telenofo_Usuario = models.CharField(max_length=12)
    USR_Email_Usuario = models.EmailField()
    USR_Nombre_Usuario = models.CharField(max_length=15)
    USR_Contrasena_Usuario = models.TextField()
    
    class Meta:
        db_table = 'TBL_Usuarios'

# Modelo de la tabla de Roles
class Rol(models.Model):
    RLS_Id_Rol = models.BigAutoField(primary_key = True)
    RLS_Nombre_Rol = models.CharField(max_length = 30)
    RLS_Descripcion_Rol = models.TextField()
    
    class Meta:
        db_table = 'TBL_Roles'

# Modelo de la tabla de Relación Usuarios-Roles
class UsuarioRol(models.Model):
    USR_RLS_Id = models.BigAutoField(primary_key = True)
    USR_RLS_Usuario_Id = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name='FK_Usuarios_Roles_Usuario_Id')
    USR_RLS_Rol_Id = models.ForeignKey(Rol, on_delete = models.CASCADE, related_name='FK_Usuarios_Roles_Rol_Id')
    
    class Meta:
        db_table = 'TBL_Usuarios_Roles'

# Modelo de la tabla de Menús
class Menu(models.Model):
    MN_Id_Menu = models.BigAutoField(primary_key = True)
    MN_Nombre_Menu = models.CharField(max_length = 50)
    MN_Url_Menu = models.CharField(max_length = 30)
    MN_Icono_Menu = models.CharField(max_length = 15)
    
    class Meta:
        db_table = 'TBL_Menus'

# Modelo de la tabla de Relación Usuarios-Menús
class MenuUsuario(models.Model):
    MN_USR_Id = models.BigAutoField(primary_key = True)
    MN_USR_Menu_Id = models.ForeignKey(Menu, on_delete = models.CASCADE, related_name='FK_Menus_Usuarios_Menu_Id')
    MN_USR_Usuario_Id = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name='FK_Menus_Usuarios_Usuario_Id')
    
    class Meta:
        db_table = 'TBL_Menus_Usuarios'

# Modelo de la tabla de Permisos
class Permiso(models.Model):
    PRM_Id_Permiso = models.BigAutoField(primary_key = True)
    PRM_Nombre_Permiso = models.CharField(max_length = 50)
    PRM_Slug_Permiso = models.CharField(max_length = 100)
    
    class Meta:
        db_table = 'TBL_Permisos'

# Modelo de la tabla de Relación Usuarios-Permisos
class UsuarioPermiso(models.Model):
    USR_PRM_Id = models.BigAutoField(primary_key = True)
    USR_PRM_Usuario_Id = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name='FK_Usuarios_Permisos_Usuario_Id')
    USR_PRM_Permiso_Id = models.ForeignKey(Permiso, on_delete = models.CASCADE, related_name='FK_Usuarios_Permisos_Permiso_Id')
    
    class Meta:
        db_table = 'TBL_Usuarios_Permisos'