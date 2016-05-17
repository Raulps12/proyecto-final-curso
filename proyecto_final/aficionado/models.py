# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.dispatch import receiver
from allauth.account.signals import user_signed_up

from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe

from cities_light.abstract_models import (
    AbstractCity, AbstractRegion, AbstractCountry)
from cities_light.receivers import connect_default_signals
# Create your models here.


class Country(AbstractCountry):
    pass
connect_default_signals(Country)


class Region(AbstractRegion):
    pass
connect_default_signals(Region)


@python_2_unicode_compatible
class City(AbstractCity):
    def __str__(self):
        return self.name

connect_default_signals(City)


@python_2_unicode_compatible
class Deporte(models.Model):
    nombre = models.CharField(max_length=200, verbose_name=u'Nombre')
    icono = models.ImageField(upload_to='icono_deportes')

    def __str__(self):
        return mark_safe('<img src ="' + self.icono.url + '" />')
        # return self.nombre


@python_2_unicode_compatible
class Perfil(models.Model):
    owner = models.OneToOneField(
        User, related_name="profile", verbose_name=u'Propietario')
    # related_name= es el nombre de la relación
    # pais = models.CharField(max_length=200, verbose_name=u'País', blank=True, null=True)
    # ciudad = models.CharField(max_length=100, verbose_name=u'Ciudad', blank=True, null=True)
    pais = models.ForeignKey(
        Country, verbose_name=u'País', blank=True, null=True)
    ciudad = models.ForeignKey(
        City, verbose_name=u'Ciudad', blank=True, null=True)
    descripcion = models.TextField(
        max_length=240, verbose_name=u'Descripción', blank=True, null=True)
    fecha_nac = models.DateField(
        verbose_name=u'Fecha de Nacimiento', blank=True, null=True)
    profesional = models.BooleanField(
        default=False, verbose_name=u'Profesional')

    deportes = models.ManyToManyField(
        Deporte, related_name="perfiles", verbose_name=u'Deportes')

    class Meta:
        verbose_name = _('perfil')
        verbose_name_plural = _('perfiles')


@receiver(user_signed_up)
def create_profile_on_signup(sender, request, user, **kwargs):
    perfil = Perfil(owner=user)
    perfil.save()
