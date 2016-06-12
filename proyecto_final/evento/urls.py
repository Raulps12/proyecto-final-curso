# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include
from macrosurl import url
from .views import crear_evento, editar_evento, eliminar_evento, ver_evento, busqueda_avanzada_eventos

urlpatterns = patterns('proyecto_final.evento.views',
                       # url(r'expresion regular', 'nombre de la función', name='nombre de la url' )
                       # la r al principio indica que lo siguiente es una
                       # expresión regular
                       url(r'^crear_evento/$', view=crear_evento, name='crear_evento'),
                       url(r'^editar_evento/:evento_pk/$', view=editar_evento, name='editar_evento'),
                       url(r'^eliminar_evento/:evento_pk/$', view=eliminar_evento, name='eliminar_evento'),
                       url(r'^ver_evento/:evento_pk/$', view=ver_evento, name='ver_evento'),
                       url(r'^busqueda_avanzada_eventos/$', view=busqueda_avanzada_eventos, name='busqueda_avanzada_eventos'),
                       )
