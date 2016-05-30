# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from embed_video.fields import EmbedVideoField
# Create your models here.


@python_2_unicode_compatible
class Publicacion(models.Model):
    autor = models.ForeignKey(
        User, related_name="author", verbose_name=u'Autor')
    titulo = models.CharField(max_length=200, verbose_name=u'Título')
    fecha_hora = models.DateTimeField(
        verbose_name=u'Fecha y Hora', default=now)
    video = EmbedVideoField(verbose_name=u'Video', blank=True, null=True)
    imagen = models.ImageField(
        upload_to='imagenes_publicacion', verbose_name=u'Imagen', blank=True, null=True)
    texto = models.TextField(
        max_length=250, verbose_name=u'Text', blank=True, null=True)

    class Meta:
        verbose_name = _('publicacion')
        verbose_name_plural = _('publicaciones')

    def __str__(self):
        return str(self.id) + " - " + self.titulo


@python_2_unicode_compatible
class Comentario(models.Model):
    autor = models.ForeignKey(
        User, related_name="author_comments", verbose_name=u'Autor')
    texto = models.TextField(max_length=250, verbose_name=u'Texto')
    fecha_hora = models.DateTimeField(
        verbose_name=u'Fecha y Hora', default=now)
    publicacion = models.ForeignKey(
        Publicacion, related_name="comments", verbose_name=u'Publicación')

    class Meta:
        verbose_name = _('comentario')
        verbose_name_plural = _('comentarios')
