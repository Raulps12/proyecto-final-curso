# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import Evento
from datetimewidget.widgets import DateWidget, TimeWidget, DateTimeWidget
from dal import autocomplete


class EventoForm(forms.ModelForm):

    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy hh:ii',
            'autoclose': True,
            'startView': 2,
            'showMeridian': True
        }
        model = Evento
        fields = ['titulo', 'imagen', 'fecha_hora', 'descripcion', 'deportes', 'pais', 'ciudad',
                  'precio', 'max_participantes', 'direccion', 'localizacion']
        widgets = {
            'fecha_hora': DateTimeWidget(usel10n=True, bootstrap_version=3, options=dateTimeOptions),
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true', 'id': 'ciudad'}),
        }


class EventoAdminForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ('__all__')
        widgets = {
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true', 'id': 'ciudad'}),
        }


class EventoEditarForm(forms.ModelForm):

    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy hh:ii',
            'autoclose': True,
            'startView': 2,
            'showMeridian': True
        }
        model = Evento
        fields = ['titulo', 'imagen', 'descripcion', 'fecha_hora', 'pais', 'ciudad',
                  'precio', 'max_participantes', 'direccion', 'localizacion']
        widgets = {
            'fecha_hora': DateTimeWidget(usel10n=True, bootstrap_version=3, options=dateTimeOptions),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true', 'id': 'ciudad'}),
        }


class EventoBusquedaAvanzadaForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ['pais', 'ciudad', 'deportes']
        widgets = {
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true'})
        }
