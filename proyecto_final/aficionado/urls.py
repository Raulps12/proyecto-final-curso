# -*- encoding: utf-8 -*-
from django.conf.urls import patterns

from macrosurl import url
from .views import registro_perfil, editar_perfil

urlpatterns = patterns('proyecto_final.aficionado.views',
                       # url(r'expresion regular', 'nombre de la función', name='nombre de la url' )
                       # la r al principio indica que lo siguiente es una expresión regular
                       url(r'^registro_perfil/$', view=registro_perfil, name='registro_perfil'),
                       url(r'^editar_perfil/$', view=editar_perfil, name='editar_perfil'),
                       )
