# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('proyecto_final.muro.views',
                       # url(r'expresion regular', 'nombre de la función', name='nombre de la url' )
                       # la r al principio indica que lo siguiente es una expresión regular
                       url(r'^$', 'muro', name='muro'),		# Esta será la página de inicio
                       )
