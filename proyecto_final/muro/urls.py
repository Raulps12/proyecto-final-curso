# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include
from macrosurl import url
from .views import visita_muro, busqueda

urlpatterns = patterns('proyecto_final.muro.views',
                       # url(r'expresion regular', 'nombre de la función', name='nombre de la url' )
                       # la r al principio indica que lo siguiente es una
                       # expresión regular
                       # Esta será la página de inicio
                       url(r'^$', 'muro', name='muro'),
                       url(r'^muro/:usuario_pk/$', view=visita_muro, name='visita_muro'),
                       url(r'^buscar/$', view=busqueda, name='busqueda'),
                       # Urls de Django-avatar
                       url(r'^muro/avatar/', include('avatar.urls')),
                       # Resto de Urls
                       url(r'^crear_publicacion/$', 'crear_publicacion', name='crear_publicacion'),
                       )
