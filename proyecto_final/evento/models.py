# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from proyecto_final.aficionado.models import Deporte, Country, City
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from location_field.models.plain import PlainLocationField
# Create your models here.


@python_2_unicode_compatible
class Evento(models.Model):
    autor = models.ForeignKey(
        User, related_name="author_event", verbose_name=u'Autor')
    titulo = models.CharField(max_length=200, verbose_name=u'Título')
    imagen = models.ImageField(
        upload_to='imagenes_evento', verbose_name=u'Imagen')
    fecha_hora_creacion = models.DateTimeField(
        verbose_name=u'Fecha y Hora creación', default=now)
    fecha_hora = models.DateTimeField(verbose_name=u'Fecha y Hora')
    descripcion = models.TextField(
        max_length=250, verbose_name=u'Descripción')
    precio = models.IntegerField(verbose_name=u'Precio', blank=True, null=True)
    max_participantes = models.IntegerField(
        verbose_name=u'Máximo participantes', blank=True, null=True)
    pais = models.ForeignKey(Country, verbose_name=u'País', blank=True, null=True)
    ciudad = models.ForeignKey(City, verbose_name=u'Ciudad', blank=True, null=True)
    direccion = models.CharField(verbose_name=u'Dirección', max_length=255)
    localizacion = PlainLocationField(based_fields=['direccion'], zoom=7, verbose_name=u'Localización',)

    deportes = models.ManyToManyField(
        Deporte, related_name="deportes", verbose_name=u'Deportes')

    participantes = models.ManyToManyField(User, related_name="participantes", verbose_name=u'Participantes')

    class Meta:
        verbose_name = _('evento')
        verbose_name_plural = _('eventos')
