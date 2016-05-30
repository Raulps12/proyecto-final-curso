# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Publicacion, Comentario

# Register your models here.


class PublicacionAdmin(admin.ModelAdmin):

    # Añadimos los campos que queremos que aparezcan en la zona /admin
    list_display = ('autor', 'titulo', 'fecha_hora',
                    'video', 'imagen', 'texto',)
    # Añadimos un filtrado (en este caso por pais)
    # Hay que poner la coma para que funcione
    list_filter = ('autor', 'fecha_hora',)
    # Añadimos un buscador # Hay que poner la coma para que funcione
    search_fields = ('autor',)

admin.site.register(Publicacion, PublicacionAdmin)


class ComentarioAdmin(admin.ModelAdmin):

    list_display = ('autor', 'texto', 'fecha_hora', 'publicacion',)
    list_filter = ('autor', 'fecha_hora',)
    # Añadimos un buscador # Hay que poner la coma para que funcione
    search_fields = ('autor',)

admin.site.register(Comentario, ComentarioAdmin)
