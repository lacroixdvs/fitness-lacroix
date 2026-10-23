from django.contrib import admin
from .models import *

@admin.register(PlanLacroix)
class PlanAdmin(admin.ModelAdmin):
    list_filter = ['nivel']
    search_fields = ['nombre']
    ordering = ['precio']
    list_display = ['nombre', 'precio', 'nivel']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['categoria']
    search_fields = ['titulo']
    ordering = ['-creado']
    list_display = ['titulo', 'categoria', 'autor']

admin.site.register([Usuario, CategoriaBlog, Comentario, EntrenadorLacroix, Rutina, Ejercicio, RutinaEjercicio, MetaLacroix, ProgresoDiario])