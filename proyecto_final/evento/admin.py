# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Evento
from proyecto_final.aficionado.models import Deporte
from .forms import EventoAdminForm

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    form = EventoAdminForm

    # Añadimos los campos que queremos que aparezcan en la zona /admin
    list_display = ('autor', 'titulo', 'imagen', 'fecha_hora_creacion',
                    'fecha_hora', 'descripcion', 'precio', 'max_participantes', 'direccion', 'localizacion',)
    # Añadimos un filtrado (en este caso por pais)
    # Hay que poner la coma para que funcione
    list_filter = ('autor', 'fecha_hora_creacion',)
    # Añadimos un buscador # Hay que poner la coma para que funcione
    search_fields = ('autor',)

admin.site.register(Evento, EventoAdmin)
