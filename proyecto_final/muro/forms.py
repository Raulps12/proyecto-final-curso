# -*- encoding: utf-8 -*-
from django import forms
from .models import Publicacion, Comentario
from proyecto_final.aficionado.models import Perfil
from dal import autocomplete


class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ['titulo', 'video', 'imagen', 'texto']


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        # fields = ['autor', 'texto', 'fecha_hora', 'publicacion']
        fields = ['texto']


class PerfilBusquedaAvanzadaForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ['pais', 'ciudad', 'deportes']
        widgets = {
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true'})
        }


class PerfilBusquedaAvanzadaAdminForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('__all__')
        widgets = {
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete'),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'])
        }
