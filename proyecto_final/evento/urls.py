# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include
from macrosurl import url
from .views import crear_evento

urlpatterns = patterns('proyecto_final.evento.views',
                       # url(r'expresion regular', 'nombre de la función', name='nombre de la url' )
                       # la r al principio indica que lo siguiente es una
                       # expresión regular
                       url(r'^crear_evento/$', view=crear_evento, name='crear_evento'),
                       )
