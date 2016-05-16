# -*- encoding: utf-8 -*-
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from proyecto_final.aficionado.forms import UserForm, PerfilForm
from .models import Perfil, Country, City

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from dal import autocomplete

# Create your views here.


@login_required
def registro_perfil(request):
    user_form = UserForm(instance=request.user)
    perfil_form = PerfilForm(instance=Perfil.objects.get(owner=request.user))
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(
            request.POST, instance=Perfil.objects.get(owner=request.user))
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
        # return HttpResponseRedirect('../../')
        # De esta manera en vez de que busque un directorio,
        # le decimos que busque una función determinada y nos lleva
        # a la página en la que se encuentra esa función
        # return HttpResponseRedirect(reverse('registro_perfil'))
    context = {'user_form': user_form, 'perfil_form': perfil_form, }
    return render(request, 'registro_perfil.html', context)
    # le pasamos un contexto, que tiene clave y valor el contexto sirve para
    # poder pasar la variable con su contenido a la plantilla


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return City.objects.none()

        qs = City.objects.all()
        pais = self.forwarded.get('pais', None)

        if pais:
            qs = qs.filter(country=pais)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
