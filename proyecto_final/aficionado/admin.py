# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Perfil, Deporte
from .forms import PerfilAdminForm

# Register your models here.


class PerfilAdmin(admin.ModelAdmin):
    form = PerfilAdminForm

    # Añadimos los campos que queremos que aparezcan en la zona /admin
    list_display = (
        'id', 'owner', 'pais', 'ciudad', 'descripcion', 'fecha_nac', 'profesional')
    # Añadimos un filtrado (en este caso por pais)
    list_filter = ('pais',)		# Hay que poner la coma para que funcione
    # Añadimos un buscador # Hay que poner la coma para que funcione
    search_fields = ('owner',)

admin.site.register(Perfil, PerfilAdmin)


class DeporteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'icono', 'id')
    list_filter = ('nombre',)  # Hay que poner la coma para que funcione
    search_fields = ('nombre',)  # Hay que poner la coma para que funcione

admin.site.register(Deporte, DeporteAdmin)
