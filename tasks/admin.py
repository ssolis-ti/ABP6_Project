from django.contrib import admin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'fecha_inicio')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_inicio', 'usuario')

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'proyecto', 'estado', 'prioridad', 'creado_por')
    list_filter = ('estado', 'prioridad', 'proyecto')
    search_fields = ('titulo', 'descripcion')
