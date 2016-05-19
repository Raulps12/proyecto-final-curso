# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url, include

urlpatterns = patterns('proyecto_final.muro.views',
                       # url(r'expresion regular', 'nombre de la función', name='nombre de la url' )
                       # la r al principio indica que lo siguiente es una
                       # expresión regular
                       # Esta será la página de inicio
                       url(r'^$', 'muro', name='muro'),
                       # Urls de Django-avatar
                       url(r'^muro/avatar/', include('avatar.urls')),
                       # Resto de Urls
                       url(r'^crear_publicacion/$', 'crear_publicacion', name='crear_publicacion'),
                       )
